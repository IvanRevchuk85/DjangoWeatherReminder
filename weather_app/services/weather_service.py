import requests
from django.conf import settings


#  Функция для получения данных о погоде по названию города
def get_weather_by_city(city_name):
    api_key = settings.OPENWEATHER_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Параметры запроса
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    # делаем GET-запрос
    response = requests.get(base_url, params=params)

    # если все ок, возвращаем данные
    if  response.status_code == 200:
        return response.json()
    else:
        return None
