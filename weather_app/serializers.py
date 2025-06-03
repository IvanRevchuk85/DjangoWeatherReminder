from rest_framework import serializers
from .models import Reminder, Subscription, WeatherData


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        # Protecting the user field from manual input
        extra_kwargs = {'user': {'read_only': True}}


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        # The user field is automatically added to the view - do not send it manually
        extra_kwargs = {'user': {'read_only': True}}


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
