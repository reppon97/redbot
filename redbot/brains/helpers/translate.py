from googletrans import Translator


class GoogleTranslate():
    def __init__(self, translation):
        self.message = self.parse_message()
        self.translated = ''

    def handle(self):
        return self.parse_message()

    def parse_message(self):
        tr = Translator()
        raw = self.message.replace('translate ', '', 1)
        self.translated = tr.translate(raw, dest='en').text

        return self.translated
