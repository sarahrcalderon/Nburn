class WeatherData:
    def __init__(self, city, description, temperature, humidity, wind_speed):
        self.city = city
        self.description = description
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def to_dict(self):
        return {
            "city": self.city,
            "description": self.description,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
        }
