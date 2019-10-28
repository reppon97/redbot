import os
import discord
from dotenv import load_dotenv
from redbot.redbot import RedBot

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = RedBot.input(message.content)

    if response:
        await message.channel.send(response)

client.run(token)
