```python
import unittest
from AI_Farmtopia.weather_system import WeatherSystem

class TestWeatherSystem(unittest.TestCase):

    def setUp(self):
        self.weather_system = WeatherSystem()

    def test_initial_conditions(self):
        self.assertEqual(self.weather_system.current_weather, None)
        self.assertEqual(self.weather_system.forecast, [])

    def test_generate_weather(self):
        self.weather_system.generate_weather()
        self.assertIsNotNone(self.weather_system.current_weather)
        self.assertTrue(len(self.weather_system.forecast) > 0)

    def test_change_weather(self):
        initial_weather = self.weather_system.current_weather
        self.weather_system.change_weather()
        self.assertNotEqual(self.weather_system.current_weather, initial_weather)

    def test_update_weather(self):
        initial_weather = self.weather_system.current_weather
        self.weather_system.update_weather()
        self.assertNotEqual(self.weather_system.current_weather, initial_weather)

if __name__ == '__main__':
    unittest.main()
```