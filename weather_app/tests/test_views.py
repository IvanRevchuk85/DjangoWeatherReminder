import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from weather_app.models import Reminder, Subscription, WeatherData
from unittest.mock import patch


@pytest.mark.django_db
def test_reminder_viewset_list_create(test_user):
    """
    ✅ Проверка списка и создания напоминаний
    """
    client = APIClient()
    client.force_authenticate(user=test_user)

    # 📋 Проверка GET списка
    response = client.get("/api/reminders/")
    assert response.status_code == 200

    # ➕ Создание нового напоминания
    data = {"location": "Dnipro", "reminder_time": "09:00:00", "is_active": True}
    response = client.post("/api/reminders/", data)
    assert response.status_code == 201
    assert Reminder.objects.filter(location="Dnipro").exists()


@pytest.mark.django_db
def test_subscription_viewset_list_create(test_user):
    """
    ✅ Проверка списка и создания подписок
    """
    client = APIClient()
    client.force_authenticate(user=test_user)

    response = client.get("/api/subscriptions/")
    assert response.status_code == 200

    data = {"city": "Kharkiv", "period": 6}
    response = client.post("/api/subscriptions/", data)
    assert response.status_code == 201
    assert Subscription.objects.filter(city="Kharkiv").exists()


@patch("weather_app.views.get_weather_by_city")
@pytest.mark.django_db
def test_weather_data_view(mock_weather, test_user):
    """
    🌤 Проверка получения и сохранения погоды
    """
    client = APIClient()
    client.force_authenticate(user=test_user)

    # 🎭 Мокаем API
    mock_weather.return_value = {
        "main": {"temp": 21.5, "humidity": 48},
        "weather": [{"description": "облачно"}],
    }

    response = client.get("/api/weather/?city=Odesa")
    assert response.status_code == 200
    assert WeatherData.objects.filter(city="Odesa").exists()
    assert response.data[0]["description"] == "облачно"
