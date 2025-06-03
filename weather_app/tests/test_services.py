import pytest
from unittest.mock import patch
from weather_app.services.weather_service import get_weather_by_city


@patch("weather_app.services.weather_service.requests.get")
def test_get_weather_by_city_success(mock_get):
    """
    ✅ Testing a successful response from the OpenWeather API
    """
    #  Fake API response
    mock_response = {
        "main": {"temp": 15.5, "humidity": 55},
        "weather": [{"description": "ясно"}],
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_weather_by_city("Kyiv")

    assert result == mock_response
    mock_get.assert_called_once()
    assert "main" in result
    assert result["main"]["temp"] == 15.5


@patch("weather_app.services.weather_service.requests.get")
def test_get_weather_by_city_fail(mock_get):
    """
     Tests the case where the API returns an error (e.g. 404)
    """
    mock_get.return_value.status_code = 404

    result = get_weather_by_city("InvalidCity")
    assert result is None
