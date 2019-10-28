from redbot.brains.handlers.handler import AbstractHandler
import pyowm
from redbot.config import CONF


class WeatherHandler(AbstractHandler):
    def __init__(self, input_):
        super().__init__(input_)
        self.city = self._input
        self.owm_client = OWMWeatherClient(self.city)

    def handle(self):
        return self.decorate_message()

    def decorate_message(self):
        return "It's {} in {}. Temperature: {}°C. Wind speed = {} m/s. Humidity: {}%".format(
            self.owm_client.get_detailed(),
            self.city,
            self.owm_client.get_temperature('celsius'),
            self.owm_client.get_wind(),
            self.owm_client.get_humidity(),
        )


class OWMWeatherClient():
    def __init__(self, city):
        owm = pyowm.OWM(CONF['handlers']['weather']['token'])
        observation = owm.weather_at_place("{}".format(city))
        self.w = observation.get_weather()

    def get_detailed(self):
        return self.w.get_detailed_status()

    def get_temperature(self, format):
        return self.w.get_temperature(format)['temp']

    def get_wind(self):
        return self.w.get_wind()['speed']

    def get_humidity(self):
        return self.w.get_humidity()
