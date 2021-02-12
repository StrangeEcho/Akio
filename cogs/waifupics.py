import discord

from discord.ext import commands

import aiohttp
																				
class Waifus(commands.Cog): 

    def __init__(self, bot):
        self.bot = bot


    @commands.command(help='Just a megumin command', aliases=['Megumin'])
    async def megumin(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://waifu.pics/api/sfw/megumin') as r:
                
                megumin = (await r.json())['url']

                embed = discord.Embed(color=0x33DAFF)
                embed.set_image(url=megumin)
                embed.set_footer(text='say hello to bb')
                await ctx.send(embed=embed)

    @commands.command(help='Just a Shinobu command', aliases=['Shinobu'])
    async def shinobu(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://waifu.pics/api/sfw/shinobu') as r:
                
                shinobu = (await r.json())['url']

                embed = discord.Embed(color=0x33DAFF)
                embed.set_image(url=shinobu)
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Waifus(bot))