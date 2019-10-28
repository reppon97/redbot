import pymorphy2
from redbot.botdb.data import BOTDB_DATA
from redbot.botdb.tree import Tree


class BotDB:
    def __init__(self):
        self.tree = Tree()
        self.tree.populate(BOTDB_DATA)

    def search(self, message):
        split_message = message.split()

        current_node = self.tree.root

        to_replace = ''

        for part in split_message:
            temp = current_node.has_child(part)

            if temp is not None:
                to_replace += ' {}'.format(temp.value)
                current_node = temp

        if current_node.handler:
            message = message.replace(to_replace.strip(), '').strip()

            if current_node.morph:
                message = self.normalize_message(message)

            return {
                "handler": current_node.handler,
                "object": message
            }
        else:
            return None

    @staticmethod
    def normalize_message(message):
        result = ''
        morph = pymorphy2.MorphAnalyzer()

        parts = message.split(' ')
        for part in parts:
            if part.endswith('ой'):
                part = part.replace('ой', 'а')
                result += "{} ".format(part)
            else:
                morphed = morph.parse(part)[0]
                result += "{} ".format(morphed.normal_form)

        return result.strip()
