# THIS COG IS COMPLETELY WROTE BY ITSUKI


from copy import copy

import discord
from config import prefix
from discord.ext import commands


class NoPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def pp(self, ctx: commands.Context):
        """Tylerr While Rewriting: 'Why'"""
        await ctx.send("pp")

    @commands.Cog.listener()
    async def on_message(self, message):
        da_people = [682849186227552266, 661067997003251722, 284102119408140289]
        if not message.author.id in da_people:
            return
        msg = copy(message)
        msg.content = f"{prefix}{msg.content}"
        await self.bot.process_commands(msg)


def setup(bot: commands.Bot):
    bot.add_cog(NoPrefix(bot))
