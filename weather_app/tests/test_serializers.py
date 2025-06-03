import pytest
from weather_app.serializers import ReminderSerializer, SubscriptionSerializer, WeatherDataSerializer
from weather_app.models import Reminder, Subscription, WeatherData
from datetime import time


@pytest.mark.django_db
def test_reminder_serializer(test_user):
    """
    🔄 Тест сериализации напоминания
    """
    reminder = Reminder.objects.create(
        user=test_user,
        location="Kyiv",
        reminder_time=time(8, 0),
        is_active=True
    )
    serializer = ReminderSerializer(instance=reminder)
    data = serializer.data
    assert data["location"] == "Kyiv"
    assert data["is_active"] is True


@pytest.mark.django_db
def test_subscription_serializer(test_user):
    """
    🔄 Тест сериализации подписки
    """
    sub = Subscription.objects.create(
        user=test_user,
        city="Lviv",
        period=7
    )
    serializer = SubscriptionSerializer(instance=sub)
    data = serializer.data
    assert data["city"] == "Lviv"
    assert data["period"] == 7


@pytest.mark.django_db
def test_weatherdata_serializer():
    """
    🔄 Тест сериализации погодных данных
    """
    weather = WeatherData.objects.create(
        city="Odesa",
        temperature=23.1,
        humidity=55,
        description="солнечно"
    )
    serializer = WeatherDataSerializer(instance=weather)
    data = serializer.data
    assert data["city"] == "Odesa"
    assert data["temperature"] == 23.1
    assert data["description"] == "солнечно"
