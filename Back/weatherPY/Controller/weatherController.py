from services.weather_service import WeatherService
import json

class WeatherController:
    @staticmethod
    def get_weather(city):
        try:
            weather_data = WeatherService.fetch_weather(city)
            return {
                "status": 200,
                "data": weather_data.to_dict(),
            }
        except Exception as e:
            return {
                "status": 500,
                "error": str(e),
            }
