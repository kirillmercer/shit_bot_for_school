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


    print(">>> TOKEN | is ready  |", "―――――――――――――――――――――――――――――――――――――――――",
          ">>> BOT   | starting  |", sep="\n")


def load_token():
    token = "MTA2ODE0MDA3NjY3ODI1ODczOQ.GHmOF0.zG1vrX-dYCBzrHL9F37tQadEfRqabk_2-d-ads"
    return token


def load_bot():
    bot = commands.InteractionBot(intents=Intents.all())
    return bot
