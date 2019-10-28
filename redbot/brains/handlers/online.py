from redbot.brains.handlers.handler import AbstractHandler


class OnlineHandler(AbstractHandler):
    def __init__(self, input_, online):
        super().__init__(input_)
        self.online = online

    def handle(self):
        response = ''

        for user in self.online:
            response = '{}\n'.format(user.get_full_name())

        return response
