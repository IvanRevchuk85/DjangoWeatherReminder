import requests
from django.conf import settings


# Получение погоды по имени города
def fetch_weather_by_city(city_name):
    """
    Отпровляет запрос в OpenWeather API и возвращает JSON с  погодой
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
        print(f"❌ Ошибка при запросе погоды для {city_name}: {e}")
        return None