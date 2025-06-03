import pytest
from unittest.mock import patch, MagicMock
from weather_app.tasks import send_weather_notifications


@pytest.mark.django_db
@patch("weather_app.tasks.notify_subscriber")
@patch("weather_app.tasks.fetch_weather_by_city")
def test_send_weather_notifications(mock_fetch, mock_notify, test_user, test_subscription):
    """
    Checks that the task calls fetch_weather and notify_subscriber
    """
    # Customizing the OpenWeather API Response
    mock_fetch.return_value = {
        "main": {"temp": 12, "humidity": 70},
        "weather": [{"description": "ясно"}],
    }

    # Calling the task
    send_weather_notifications()

    # Checking that the weather has been received
    mock_fetch.assert_called_once_with(test_subscription.city)

    # Checking that the notification was sent
    mock_notify.assert_called_once()
    args, kwargs = mock_notify.call_args

    assert kwargs["user"] == test_user
    assert kwargs["weather_data"]["temperature"] == 12
    assert kwargs["weather_data"]["humidity"] == 70
    assert kwargs["weather_data"]["description"] == "ясно"
