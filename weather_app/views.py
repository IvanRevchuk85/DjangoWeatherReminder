from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Reminder, Subscription, WeatherData
from .serializers import ReminderSerializer, SubscriptionSerializer, WeatherDataSerializer
from .services.weather_service import get_weather_by_city


# Reminder
class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Subscription
class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
       Override create to show more informative errors when 400 Bad Request occurs.
        """
        serializer = self.get_serializer(data=request.data)
        # if something is wrong, it will give a detailed description
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Weather
class WeatherDataView(APIView):
    # Access only for authorized persons
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the city parameter from the URL
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "The city parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        # We receive weather data from the service
        weather = get_weather_by_city(city)

        if weather:
            # Saving weather data to the database
            WeatherData.objects.create(
                city=city,
                temperature=weather['main']['temp'],
                humidity=weather['main']['humidity'],
                description=weather['weather'][0]['description']
            )
        else:
            return Response({"error": "Failed to get weather"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the last 10 weather records
        queryset = WeatherData.objects.all().order_by('-timestamp')[:10]
        serializer = WeatherDataSerializer(queryset, many=True)
        return Response(serializer.data)
