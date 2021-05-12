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
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user) # ratelimit is 100 per 1 hour so rip 
    async def animequote(self, ctx: commands.Context):
        """Get a sick ass anime quote"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://animechan.vercel.app/api/random") as resp:
                #vars
                char = (await resp.json())["character"]
                quote = (await resp.json())["quote"]
                anime = (await resp.json())["anime"]
                await ctx.send(embed=discord.Embed(description=f"{quote}\n~{char}", color=0xFFB6C1).set_footer(text=f"Quote From: {anime}"))

def setup(bot):
    bot.add_cog(Waifus(bot))