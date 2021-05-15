import discord
from discord.ext import commands

from typing import Optional 
class Owner_Only(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command(aliases= ["echo", "repeat", "send"])
    @commands.is_owner()
    async def say(self, ctx : commands.Context, chan : Optional[discord.TextChannel] = None, *, msg : str):
        chan = chan or ctx.channel
        try:
            await chan.send(msg)
        except discord.Forbidden as e:
            await ctx.send(e)

    @commands.command()
    async def load(self, ctx, cog):
        try:
            await self.bot.load_extension(cog)
        except commands.ExtensionError as e:
            await ctx.send(e)
    
    @commands.command()
    async def unload(self, ctx, cog):
        try:
            await self.bot.unload_extension(name)(cog)
        except commands.ExtensionError as e:
            await ctx.send(e)

    @commands.command()
    async def reload(self, ctx, cog):
        try:
            await self.bot.reload_extension(cog)
        except commands.ExtensionError as e:
            await ctx.send(e)


def setup(bot: commands.Bot):
    bot.add_cog(Owner_Only(bot))