import discord 
from discord.ext import commands

import platform
import config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(brief = 'Ping Command')
    async def ping(self, ctx):
        embed = discord.Embed(
            title='🏓Pong!',
            description=f'{round(self.bot.latency * 1000)} Milliseconds',
            color=0x33DAFF
        )
        await ctx.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, ctx):
        await ctx.send("I sent you a private message!")
        embed = discord.Embed(
            title='Here you go! \:D',
            description=f'Click [Here](https://discordapp.com/oauth2/authorize?&client_id=785248905679863868&scope=bot&permissions=8) To Invite Me',
            color=0xffc2ff
        )
        await ctx.author.send(embed=embed)

    @commands.command(hidden=True)
    async def boost(self, ctx):
        embed = discord.Embed(
            color=0xffc2ff
        )
        embed.set_image(url='https://media1.tenor.com/images/68b7eca6ad0720a64a7e14d6bca83942/tenor.gif?itemid=11979611')
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Misc(bot))