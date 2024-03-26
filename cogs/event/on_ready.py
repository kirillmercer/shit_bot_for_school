from disnake.ext import commands


class Events_bot(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>>READY\n>>> LOGS:")
        i = 0
        if self.bot.guilds is not None:
            for guild in self.bot.guilds:
                i += 1
                print(f"#{i}: {guild} | {guild.id}")


def setup(bot: commands.Bot):
    bot.add_cog(Events_bot(bot))
    print(f">>> {__name__} loaded ")
