from models.weather_model import WeatherData
from repositories.weather_repository import WeatherRepository

class WeatherService:
    @staticmethod
    def fetch_weather(city):
        data = WeatherRepository.get_weather_data(city)
        
        # Processa os dados e cria o modelo
        return WeatherData(
            city=data.get("name"),
            description=data["weather"][0]["description"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
        )
