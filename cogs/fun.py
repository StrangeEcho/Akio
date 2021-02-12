import discord

from discord.ext import commands

import lists
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eightball(self, ctx, *, question):
        embed = discord.Embed(
            title='🎱The Magic 8ball🎱',
            description=f'**Question:** {question}\n**Answer:** {random.choice(lists.eightball)}',
            color=0xffc2ff 
        )
        embed.set_footer(text=f'Question Asked By {ctx.message.author}')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def compliment(self, ctx):
        embed = discord.Embed(
            description=f'{ctx.message.author.mention} {random.choice(lists.compliments)}',
            color=0xffc2ff
        )
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Fun(bot))