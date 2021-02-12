import discord

from discord.ext import commands #i wanna die inside
import lists
import nekos
import random



class Random(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meow(self, ctx):
        await ctx.send(nekos.cat())
 
    @commands.command()
    async def woof(self, ctx):
        await ctx.send(nekos.img('woof'))

    
    @commands.command()
    async def waifu(self, ctx):
        await ctx.send(nekos.img('waifu'))

    
    @commands.command()
    async def neko(self, ctx):
        await ctx.send(nekos.img('neko'))

    @commands.command()
    async def femboy(self, ctx):

        itsuki_is_gay = random.choice(lists.femboys)
        
        #Build Embed
        embed = discord.Embed(description='Heres your Femboy', color=0x33DAFF)
        embed.set_image(url=itsuki_is_gay)
        await ctx.send(embed=embed)
    
    @commands.command(brief="Keegans Command")
    async def mirai(self, ctx):

        miraipic = random.choice(lists.mirai)

        embed = discord.Embed(color=0xffe5b4)
        embed.set_image(url=miraipic)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Random(bot))