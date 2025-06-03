from rest_framework import serializers
from .models import Reminder, Subscription, WeatherData


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        # Защищаем поле user от ручного ввода
        extra_kwargs = {'user': {'read_only': True}}


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        # Поле user автоматически добавляется в view — руками не шлём
        extra_kwargs = {'user': {'read_only': True}}


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
