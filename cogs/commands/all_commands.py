from disnake.ext import commands
from disnake import Embed
from disnake.utils import get

class About(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def anonim(self, ctx):
        pass

    @anonim.sub_command(name="report", description="отправьте анонимное сообщение о нарушении")
    async def report(self, ctx, message):
        #нарушители
        channel_to_send = self.bot.get_channel(1012046671963750411)                
        channel_log = self.bot.get_channel(1012044889690738698)
        role_mod = get(ctx.guild.roles, name="Модератор")
        embed_message = Embed(title="Замечено нарушение",description=f"анонимное сообщение:\n\n{message}\n",color=0x000000) 
        try:
            await ctx.response.send_message("Ваш репорт создан, позже с вами свяжется модератор через лс для дальнейшего обсуждения нарушения.", ephemeral=True)
            await channel_to_send.send(f"{role_mod.mention}")
            await channel_to_send.send(embed=embed_message)
            embed = Embed(title="**была использована команда `echo`**", 
                description=f"Использовал {ctx.user.mention}\n"
                            f"В канале {ctx.channel.mention}\n"
                            f"Текст:\n{message}\n\n",  
                            color=0x000000)
            await channel_log.send(embed=embed)
        except Exception as e:
            print(f"ERROR: echo, {e}")


    @anonim.sub_command(name="about", description="информация о боте")
    async def about(self, ctx):
        channel_log = self.bot.get_channel(874524444457066557)
        channel_nar = self.bot.get_channel(1012046671963750411)
        creator     = self.bot.get_user(    1006203420635582464)
        try:
            embed = Embed(
                title="**Обо мне:**",
                description=
                f"Нужен я для отправки аннонимных сообщений о нарушителях в канал\n{channel_nar.mention}\n"
                f"Но предупреждаю, если вы будете спамить, мой создатель все увидит и выдаст соответствующее наказание.\n"
                f"Если вы хотите отправить жалобу на кого-либо, испольуйте команду `/echo`, расскажите о проблеме,"
                f"позже модераторы рассмотрят вашу заявку\n\n"
                f"Создан: {creator.mention}, специально для discord сервера 'name'"
            )
            await ctx.response.send_message(embed=embed, ephemeral=True)

            embed_log = Embed(title="**была использована команда `about`**", 
                              description=f"использовал {ctx.user.mention}\nв канале {ctx.channel.mention}",  
                              color=0x000000)
            await channel_log.send(embed=embed_log)

        except Exception as e:
            print(f"ERROR: echo, {e}")


def setup(bot: commands.Bot):
    bot.add_cog(About(bot))
