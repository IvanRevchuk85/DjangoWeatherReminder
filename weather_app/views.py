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
        Переопределяем create, чтобы показать более информативные ошибки при 400 Bad Request.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # если что-то не так — выдаст подробное описание
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Weather
class WeatherDataView(APIView):
    permission_classes = [IsAuthenticated]  # Доступ только авторизованным

    def get(self, request):
        city = request.query_params.get('city')  # Получаем параметр city из URL

        if not city:
            return Response({"error": "Параметр city обязателен"}, status=status.HTTP_400_BAD_REQUEST)

        weather = get_weather_by_city(city)  # Получаем данные погоды из сервиса

        if weather:
            # Сохраняем данные о погоде в БД
            WeatherData.objects.create(
                city=city,
                temperature=weather['main']['temp'],
                humidity=weather['main']['humidity'],
                description=weather['weather'][0]['description']
            )
        else:
            return Response({"error": "Не удалось получить погоду"}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем последние 10 записей о погоде
        queryset = WeatherData.objects.all().order_by('-timestamp')[:10]
        serializer = WeatherDataSerializer(queryset, many=True)
        return Response(serializer.data)
