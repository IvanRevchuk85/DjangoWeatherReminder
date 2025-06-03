import pytest
from weather_app.models import Reminder, Subscription, WeatherData
import os


# Testing the Reminder model
def test_reminder_str(test_reminder):
    expected = f"Reminder for {test_reminder.user.username} at {test_reminder.reminder_time} in {test_reminder.location}"
    assert str(test_reminder) == expected


def test_reminder_fields(test_reminder):
    assert test_reminder.user.username == "ivan"
    assert test_reminder.location == "Kyiv"
    assert str(test_reminder.reminder_time) == "08:00:00"
    assert test_reminder.is_active is True
    assert test_reminder.create_at is not None

# Testing the Subscription Model


def test_subscription_str(test_subscription):
    expected = f"{test_subscription.user.username} - {test_subscription.city} ({test_subscription.period} дн.)"
    assert str(test_subscription) == expected


def test_subscription_fields(test_subscription):
    assert test_subscription.user.username == "ivan"
    assert test_subscription.city == "Lviv"
    assert test_subscription.period == 6
    assert test_subscription.created_at is not None
    assert test_subscription.updated_at is not None


# Testing the WeatherData Model
def test_weatherdata_str(test_weather):
    expected = f"{test_weather.city} - {test_weather.temperature}°C, {test_weather.description}"
    assert str(test_weather) == expected


def test_weatherdata_fields(test_weather):
    assert test_weather.city == "Odesa"
    assert test_weather.temperature == 20.5
    assert test_weather.humidity == 60
    assert test_weather.description == "Солнечно"
    assert test_weather.timestamp is not None


print(os.environ.get('DJANGO_SETTINGS_MODULE'))
