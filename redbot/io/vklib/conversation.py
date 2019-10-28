from redbot.config import CONF


class Conversation:

    def __init__(self, vk_api):
        self.members = []
        self.vk_api = vk_api
        self.parse_members_from_vk()

    def parse_members_from_vk(self):
        members = self.get_conversation_members()
        result = []
        for member in members['profiles']:
            result.append(User(member))

            self.members = result

    def get_online_members(self):
        result = []

        members = self.get_conversation_members()
        for member in members['profiles']:
            if member['online']:
                result.append(User(member))

        return result

    def get_conversation_members(self):
        return self.vk_api.method('messages.getConversationMembers', {'peer_id': CONF['vklib']['peer_id']})


class User:
    def __init__(self, member):
        self.id = member['id']
        self.first_name = member['first_name']
        self.last_name = member['last_name']
        self.sex = member['sex']

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
