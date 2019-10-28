from redbot.brains.handlers.handler import AbstractHandler
from datetime import datetime


class TimeHandler(AbstractHandler):
    def __init__(self, input_):
        super().__init__(input_)
        self.time = ''

    def handle(self):
        self.time = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        return self.decorate_message()

    def decorate_message(self):
        return 'Current time: {}'.format(self.time)
