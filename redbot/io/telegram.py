import telebot
from redbot.config import CONF
from redbot.brains import language


class TELEGRAM:
    def __init__(self):
        TOKEN = CONF['telegram']['token']
        self.tb = telebot.TeleBot(TOKEN)

    def longpoll(self, messages):
        self.tb.set_update_listener(self.longpoll)  # register listener
        self.tb.polling()
        self.tb.polling(none_stop=True)
        self.tb.polling(interval=3)
        for m in messages:
            chatid = m.chat.id
            if m.content_type == 'text':
                message = m.text.lower()
                processor = language.LanguageProcessor(message)
                processor.process()
                if processor.result:
                    self.tb.send_message(chatid, processor.result)

        while True:  # Don't let the main Thread end.
            pass
