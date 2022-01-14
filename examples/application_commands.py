from pincer.ext import commands
from pincer.objects import Message

bot = commands.Bot(token="token")


@bot.slash_command(guild="id")  # limits the guild with this command.
async def ping(inter: commands.Interaction):
    await inter.send("Pong :ping_pong:")


@bot.user_command(guild="id")  # limits the guild with this command.
async def say_hi(inter: commands.Interaction):
    await inter.send(f"{inter.author.user.mention} hi!")


@bot.message_command(guild="id")  # limits the guild with this command.
async def message_content(inter: commands.Interaction, msg: Message):
    await inter.send()


bot.run()
