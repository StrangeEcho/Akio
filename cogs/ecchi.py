import discord

from discord.ext import commands

import nekos

class Ecchi(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_nsfw()
    async def trap(self, ctx):
        await ctx.send(nekos.img('trap'))    

    @commands.command()
    @commands.is_nsfw()
    async def feet(self, ctx):
        await ctx.send(nekos.img('feet'))
#
    @commands.command()
    @commands.is_nsfw()
    async def yuri(self, ctx):
        await ctx.send(nekos.img('yuri'))
#
    @commands.command()
    @commands.is_nsfw()
    async def futanari(self, ctx):
        await ctx.send(nekos.img('futanari'))

    @commands.command()
    @commands.is_nsfw()
    async def hololewd(self, ctx):
        await ctx.send(nekos.img('hololewd'))

    @commands.command()
    @commands.is_nsfw()
    async def lewdkemo(self, ctx):
        await ctx.send(nekos.img('lewdkemo'))

    @commands.command()
    @commands.is_nsfw()
    async def solo(self, ctx):
        await ctx.send(nekos.img('solog'))  

    @commands.command()
    @commands.is_nsfw()
    async def feetg(self, ctx):
        await ctx.send(nekos.img('feetg'))

    @commands.command()
    @commands.is_nsfw()
    async def cum(self, ctx):
        await ctx.send(nekos.img('cum'))

    @commands.command()
    @commands.is_nsfw()
    async def erokemo(self, ctx):
        await ctx.send(nekos.img('erokemo'))
    
    @commands.command()
    @commands.is_nsfw()
    async def lewd(self, ctx):
        await ctx.send(nekos.img('lewd'))
    
    @commands.command()
    @commands.is_nsfw()
    async def nsfw_neko(self, ctx):
        await ctx.send(nekos.img('nsfw_neko_gif'))

    @commands.command()
    @commands.is_nsfw()
    async def solo(self, ctx):
        await ctx.send(nekos.img('solo'))

    
    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        await ctx.send(nekos.img('hentai'))

    @commands.command()
    @commands.is_nsfw()
    async def pussy(self, ctx):
        await ctx.send(nekos.img('pussy'))
    
    @commands.command()
    @commands.is_nsfw()
    async def tits(self, ctx):
        await ctx.send(nekos.img('tits'))
    
    @commands.command()
    @commands.is_nsfw()
    async def petanko(self, ctx):
        await ctx.send(nekos.img('smallboobs'))

    @commands.command()
    @commands.is_nsfw()
    async def boobies(self, ctx):
        await ctx.send(nekos.img('boobs'))
    
    
def setup(bot):
    bot.add_cog(Ecchi(bot))