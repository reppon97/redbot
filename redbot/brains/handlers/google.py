from redbot.brains.handlers.handler import AbstractHandler
import urllib.request
from bs4 import BeautifulSoup


class GoogleHandler(AbstractHandler):
    def __init__(self, input_):
        super().__init__(input_)
    #     self.google_phrase = ''
    #     self.parse_message()
    # #
    # # def handle(self):
    #     google_url = 'https://google.com/#q={}'.format(self.google_phrase)
    #     gp = GoogleParser(google_url)
    #
    #     return gp.get_answer_box()
    #
    # def parse_message(self):
    #     message = self.message.replace('search ', '')
    #     self.google_phrase = message.replace(' ', '+')
    #

# class GoogleParser:
#     def __init__(self, url):
#         self.dom = ''
#         self.url = url
#
#     def get_data(self):
#         self.dom = urllib.request.urlopen(self.url)
#
#     def get_answer_box(self):
#         self.get_data()
#         soup = BeautifulSoup(self.dom)
#
#         res = soup.find('div', {'id': 'res'})
#         div = res.find('div', {'class: Z0LcW'})
#
#         return str(div)

