import random

import discord
from discord.ext import commands

from utils import lists


class Custom(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def mirai(self, ctx: commands.Context):
        await ctx.send(random.choice(lists.mirai))

    @commands.command()
    async def femboy(self, ctx: commands.Context):
        await ctx.send(random.choice(lists.femboys))

    @commands.command()
    async def trap(self, ctx: commands.Context):
        await ctx.send(random.choice(lists.traps))


def setup(bot: commands.Bot):
    bot.add_cog(Custom(bot))
