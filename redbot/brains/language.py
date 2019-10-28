import sympy
from redbot.brains.handlers import time, weather, google, currency, online, wiki
from redbot.brains.helpers import translate
from redbot.botdb.db import BotDB


class LanguageProcessor:

    def __init__(self, message, conversation):
        self._db = BotDB()
        self._message = message
        self.result = ''
        self._conversation = conversation

    def process(self) -> bool:
        db_result = self._db.search(self._message)
        print(db_result)
        print(self._message)
        if db_result:
            try:
                handler_name = "{0}('{1}')".format(db_result['handler'], db_result['object'])
                handler = eval(handler_name)

                self.result = handler.handle()
            except Exception as e:
                print(e)
                return False

        return True
