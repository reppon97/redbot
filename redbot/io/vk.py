import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from redbot.config import CONF
from redbot.redbot import RedBot
from redbot.io.vklib.conversation import Conversation


class VK:
    def __init__(self):
        self.vk_api = vk_api.VkApi(token=CONF['vklib']['token'])
        self.session_api = self.vk_api.get_api()

    def longpoll(self):
        longpoll = VkBotLongPoll(self.vk_api, CONF['vklib']['group_id'])

        conversation = Conversation(self.vk_api)

        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:  # New message received
                message = event.obj.text.lower()
                response = RedBot.input(message)

                if response:
                    self.send_message(response)

    def send_message(self, message):
        return self.vk_api.method('messages.send',
                                  {'peer_id': CONF['vklib']['peer_id'], 'message': message,
                                   'random_id': random.randint(-21473848, 21473848)}
                                  )
