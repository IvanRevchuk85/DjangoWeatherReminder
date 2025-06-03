import os
import django
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Устанавливаем модуль настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_weather_reminder.settings')

# Запускаем Django до любых импортов моделей или ORM
django.setup()

# Теперь можно импортировать всё, что зависит от Django
import pytest
from django.contrib.auth.models import User
from weather_app.models import Reminder, Subscription, WeatherData
from rest_framework.test import APIClient
from datetime import time

# ✅ Базовый пользователь
@pytest.fixture()
def test_user(db):
    return User.objects.create_user(username="ivan", password="73501505")

# ✅ Напоминание
@pytest.fixture()
def test_reminder(test_user):
    return Reminder.objects.create(
        user=test_user,
        location="Kyiv",
        reminder_time=time(hour=8, minute=0),
        is_active=True,
    )

# ✅ Подписка
@pytest.fixture()
def test_subscription(test_user):
    return Subscription.objects.create(
        user=test_user,
        city="Lviv",
        period=6,
    )

# ✅ Погода
@pytest.fixture()
def test_weather(db):
    return WeatherData.objects.create(
        city="Odesa",
        temperature=20.5,
        humidity=60,
        description="Солнечно"
    )

# ✅ API клиент без авторизации
@pytest.fixture()
def api_client():
    return APIClient()

# ✅ API клиент с авторизацией
@pytest.fixture()
def authenticated_client(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    return api_client

# ✅ Валидные данные для подписки
@pytest.fixture()
def valid_subscription_data():
    return {"city": "Kyiv", "period": 6}

# ✅ Мок ответа погоды
@pytest.fixture()
def mocked_weather_response():
    return {
        "main": {"temp": 22.5, "humidity": 45},
        "weather": [{"description": "солнечно"}]
    }
