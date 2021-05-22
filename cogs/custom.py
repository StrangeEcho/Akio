import random

import discord
from discord.ext import commands
from utils import lists



class Custom(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def mirai(self, ctx : commands.Context):
        await ctx.send(random.choice(lists.mirai))
    
    @commands.command()
    async def femboy(self, ctx : commands.Context):
        await ctx.send(random.choice(lists.femboys))
    
    @commands.command()
    async def trap(self, ctx : commands.Context):
        await ctx.send(random.choice(lists.traps))
    

    @commands.command()
    async def boost(self, ctx: commands.Context):
        await ctx.send("https://media1.tenor.com/images/68b7eca6ad0720a64a7e14d6bca83942/tenor.gif?itemid=11979611")
        

def setup(bot: commands.Bot):
    bot.add_cog(Custom(bot))