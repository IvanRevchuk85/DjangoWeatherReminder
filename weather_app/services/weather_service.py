import requests
from django.conf import settings


#  Function to get weather data by city name
def get_weather_by_city(city_name):
    api_key = settings.OPENWEATHER_API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Request parameters
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    # GET request
    response = requests.get(base_url, params=params)

    # if everything is ok, we return the data
    if response.status_code == 200:
        return response.json()
    else:
        return None
