from datetime import time
from rest_framework.test import APIClient
from weather_app.models import Reminder, Subscription, WeatherData
from django.contrib.auth.models import User
import pytest
import os
import django
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Installing the Django Settings Module
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_weather_reminder.settings')

# Run Django before any model or ORM imports
django.setup()

# Now you can import everything that depends on Django

# ✅ Basic user


@pytest.fixture()
def test_user(db):
    return User.objects.create_user(username="ivan", password="73501505")

# ✅ Reminder


@pytest.fixture()
def test_reminder(test_user):
    return Reminder.objects.create(
        user=test_user,
        location="Kyiv",
        reminder_time=time(hour=8, minute=0),
        is_active=True,
    )

# ✅ Subscription


@pytest.fixture()
def test_subscription(test_user):
    return Subscription.objects.create(
        user=test_user,
        city="Lviv",
        period=6,
    )

# ✅ Weather


@pytest.fixture()
def test_weather(db):
    return WeatherData.objects.create(
        city="Odesa",
        temperature=20.5,
        humidity=60,
        description="Солнечно"
    )

# ✅ API client without authorization


@pytest.fixture()
def api_client():
    return APIClient()

# ✅ API client with authorization


@pytest.fixture()
def authenticated_client(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    return api_client

# ✅ Valid data for subscription


@pytest.fixture()
def valid_subscription_data():
    return {"city": "Kyiv", "period": 6}

# ✅ Weather response mockup


@pytest.fixture()
def mocked_weather_response():
    return {
        "main": {"temp": 22.5, "humidity": 45},
        "weather": [{"description": "солнечно"}]
    }
