import pytest
from unittest.mock import patch
from weather_app.services.notification_service import notify_subscriber

@pytest.mark.django_db
@patch("weather_app.services.notification_service.send_mail")
@patch("weather_app.services.notification_service.requests.post")
def test_notifi_subscriber_sends_email_and_webhook(mock_post, mock_send_mail, test_user):
    weather_data = {
        "city": "Lviv",
        "temperature": 16,
        "humidity": 60,
        "description": "солнечно",
    }
    webhook_url = "https://webhook.site/test_url"

    notify_subscriber(
        user=test_user,
        weather_data=weather_data,
        send_email=True,
        send_webhook=True,
        webhook_url=webhook_url,
    )

    # Проверка email
    mock_send_mail.assert_called_once()
    subject, message, from_mail, recipient_list = mock_send_mail.call_args[0]
    assert "Lviv" in subject
    assert str(weather_data["temperature"]) in message
    assert test_user.email in recipient_list

    # Проверка webhook
    expected_payload = {
        "user": test_user.username,
        **weather_data,
    }
    mock_post.assert_called_once_with(webhook_url, json=expected_payload, timeout=5)
