```python
import random
from ai_components import AIComponentSchema

class WeatherSystem:
    def __init__(self):
        self.weatherData = AIComponentSchema({
            "current_weather": None,
            "forecast": []
        })

    def generate_weather(self):
        weather_types = ["Sunny", "Rainy", "Windy", "Snowy", "Cloudy"]
        return random.choice(weather_types)

    def update_weather(self):
        self.weatherData["current_weather"] = self.generate_weather()
        self.weatherData["forecast"] = [self.generate_weather() for _ in range(5)]
        return self.weatherData

    def get_current_weather(self):
        return self.weatherData["current_weather"]

    def get_forecast(self):
        return self.weatherData["forecast"]

weather_system = WeatherSystem()

def updateWeather():
    global weather_system
    weatherData = weather_system.update_weather()
    return weatherData
```