import requests
from django.conf import settings


# Get weather by city name
def fetch_weather_by_city(city_name):
    """
    Sends a request to the OpenWeather API and returns JSON with the weather
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": settings.OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "ru",
    }

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error while requesting weather for {city_name}: {e}")
        return None
