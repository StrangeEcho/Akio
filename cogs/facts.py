import discord

from discord.ext import commands
import aiohttp

class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def catfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/cat') as r:
                
                cf = (await r.json())['fact']

                await ctx.send(cf)

def setup(bot):
    bot.add_cog(Facts(bot))