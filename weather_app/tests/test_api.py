import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from weather_app.models import Reminder, Subscription


@pytest.mark.django_db
def test_get_reminders(test_user, test_reminder):
    client = APIClient()
    client.force_authenticate(user=test_user)
    response = client.get("/api/reminders/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["location"] == "Kyiv"


@pytest.mark.django_db
def test_create_subscription(test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)
    data = {"city": "Kyiv", "period": 6}
    response = client.post("/api/subscriptions/", data, format="json")
    print("❗ response.data:", response.data)

    assert response.status_code == 201
    assert Subscription.objects.filter(city="Kyiv").exists()


@pytest.mark.django_db
def test_subscription_invalid_period(test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)
    data = {"city": "Lviv", "period": 0}
    response = client.post("/api/subscriptions/", data, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_jwt_token_auth(test_user):
    client = APIClient()
    response = client.post("/api/token/", {
        "username": "ivan",
        "password": "73501505"
    })
    assert response.status_code == 200
    assert "access" in response.data
    access_token = response.data["access"]

    # Проверяем доступ с токеном
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/api/reminders/")
    assert response.status_code == 200


def test_unauthorized_access():
    client = APIClient()
    response = client.get("/api/reminders/")
    assert response.status_code == 401
