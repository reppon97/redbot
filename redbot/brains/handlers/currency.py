from redbot.brains.handlers.handler import AbstractHandler
from redbot.config import CONF
import re
import requests


class CurrencyConverter(AbstractHandler):
    def __init__(self, input_):
        super().__init__(input_)
        API_KEY = CONF['handlers']['currency']['token']
        url = CONF['handlers']['currency']['url'] + API_KEY
        ans = requests.get(url).json()
        self.unit = ''
        self.usd = ans['rates']['USD']

    def handle(self):
        return self.parse_message()

    def parse_message(self):
        print(self.unit)
        match = re.search('convert (\w+)', self._input, re.IGNORECASE)
        self.unit = match.group(1)
        self.result = float(self.unit) * float(self.usd)
        self.roundedresult = round(float(self.result), 2)

        return self.decorate_message()

    def decorate_message(self):
        return '{:,} USD'.format(float(self.roundedresult))
