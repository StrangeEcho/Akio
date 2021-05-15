from discord.ext import commands


def setup(bot: commands.Bot):
    bot.load_extension("jishaku")