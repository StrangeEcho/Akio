import discord
import config
from copy import copy
from discord.ext import commands
   
class NoPrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot      
   


    @commands.command(hidden=True)
    async def pp(self, ctx):
        await ctx.send("pp")

    @commands.Cog.listener()
    async def on_message(self, message):
        gays = [682849186227552266, 661067997003251722, 284102119408140289]
        if not message.author.id in gays:
            return   
        msg = copy(message)
        msg.content = f">:{msg.content}"
        await self.bot.process_commands(msg)

def setup(bot):
    n = NoPrefix(bot)
    bot.add_cog(n)