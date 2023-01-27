from core.loads import load_bot, load_token, load_cogs

if __name__ == '__main__':
    bot = load_bot()
    load_cogs(bot)
    bot.run(load_token())
