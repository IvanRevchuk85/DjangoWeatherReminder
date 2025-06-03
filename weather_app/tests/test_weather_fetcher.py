import pytest
from unittest.mock import patch, Mock

import requests

from weather_app.services.weather_fetcher import fetch_weather_by_city

# Successful response


@patch("weather_app.services.weather_fetcher.requests.get")
def test_fetch_weather_success(mock_get):
    # Mocking response
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"city": "Lviv", "temperature": 15}
    mock_get.return_value = mock_response

    city = "Lviv"
    result = fetch_weather_by_city(city)

    mock_get.assert_called_once()
    assert result == {"city": "Lviv", "temperature": 15}

# Request error


@patch("weather_app.services.weather_fetcher.requests.get", side_effect=requests.RequestException("Ошибка"))
def test_fetch_weather_failure(mock_get):
    result = fetch_weather_by_city("InvalidCity")
    assert result is None
