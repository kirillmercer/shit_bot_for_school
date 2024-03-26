from os import listdir, getenv
from disnake import Intents
from disnake.ext import commands


def load_cogs(bot):
    for filename in listdir('./cogs/event'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.event.{filename[:-3]}')
    for filename in listdir('./cogs/commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.commands.{filename[:-3]}')
    print('any print')


def load_token():
    token = '' #my token from .ini
    return token


def load_bot():
    bot = commands.InteractionBot(intents=Intents.all())
    return bot
