import wikipedia
from wikidata.client import Client
import urllib.request, json
from urllib.parse import quote
from datetime import date
from redbot.brains.handlers.handler import AbstractHandler


class WikiParser:
    def __init__(self):
        host = 'https://ru.wikipedia.org/w/api.php'
        parameters = '?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&format=json&titles='

        self.url = "{}{}".format(host, parameters)
        self.page_title = None

    def get_id_by_title(self, title):
        wikipedia.set_lang('ru')
        full_title = wikipedia.search(title)[0]
        self.page_title = full_title

        with urllib.request.urlopen("{}{}".format(self.url, quote(full_title))) as url:
            data = json.loads(url.read().decode())
            print(data)
            pages = data['query']['pages']
            page_id = next(iter(pages))

            return pages[page_id]['pageprops']['wikibase_item']

    def get_property(self, entity_id, property_id):
        wiki_client = Client()
        print(entity_id)
        entity = wiki_client.get(entity_id, True)
        print(entity)
        property = wiki_client.get(property_id)
        print(property)

        return entity[property]


class AgeHandler(AbstractHandler):
    def __init__(self, input_):
        super().__init__(input_)
        self.wiki = WikiParser()
        self.title = self._input
        self.birth_date = None
        self.age = None

    def lookup_age_of(self):
        entity_id = self.wiki.get_id_by_title(self.title)
        self.birth_date = self.wiki.get_property(entity_id, 'P569')

        return self.calculate_age()

    def handle(self):
        self.lookup_age_of()

        return self.decorate_message()

    def decorate_message(self):
        extension = 'лет'

        age = str(self.age)

        if age[-1] == '1':
            extension = 'год'
        elif 1 < int(age[-1]) <= 4:
            extension = 'года'

        return "{}: {} {}".format(self.wiki.page_title, self.age, extension)

    def calculate_age(self):
        today = date.today()
        born = self.birth_date

        self.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        return self.age
