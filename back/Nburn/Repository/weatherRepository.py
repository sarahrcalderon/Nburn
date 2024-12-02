import requests
from utils.api_key import API_KEY

class WeatherRepository:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather_data(city):
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "pt_br",
        }
        response = requests.get(WeatherRepository.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao buscar dados: {response.status_code} - {response.text}")
