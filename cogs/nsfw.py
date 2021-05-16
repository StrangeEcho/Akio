import discord
import nekos
from discord.ext import commands


class NSFW(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_nsfw()
    async def nsfwtrap(self, ctx : commands.Context):
        await ctx.send(nekos.img('trap'))    

    @commands.command()
    @commands.is_nsfw()
    async def feet(self, ctx : commands.Context):
        await ctx.send(nekos.img('feet'))

    @commands.command()
    @commands.is_nsfw()
    async def yuri(self, ctx : commands.Context):
        await ctx.send(nekos.img('yuri'))

    @commands.command()
    @commands.is_nsfw()
    async def futanari(self, ctx : commands.Context):
        await ctx.send(nekos.img('futanari'))

    @commands.command()
    @commands.is_nsfw()
    async def hololewd(self, ctx : commands.Context):
        await ctx.send(nekos.img('hololewd'))

    @commands.command()
    @commands.is_nsfw()
    async def lewdkemo(self, ctx : commands.Context):
        await ctx.send(nekos.img('lewdkemo'))

    @commands.command()
    @commands.is_nsfw()
    async def solo(self, ctx : commands.Context):
        await ctx.send(nekos.img('solog'))  

    @commands.command()
    @commands.is_nsfw()
    async def feetg(self, ctx : commands.Context):
        await ctx.send(nekos.img('feetg'))

    @commands.command()
    @commands.is_nsfw()
    async def cum(self, ctx : commands.Context):
        await ctx.send(nekos.img('cum'))

    @commands.command()
    @commands.is_nsfw()
    async def erokemo(self, ctx : commands.Context):
        await ctx.send(nekos.img('erokemo'))
    
    @commands.command()
    @commands.is_nsfw()
    async def lewd(self, ctx : commands.Context):
        await ctx.send(nekos.img('lewd'))
    
    @commands.command()
    @commands.is_nsfw()
    async def nsfw_neko(self, ctx : commands.Context):
        await ctx.send(nekos.img('nsfw_neko_gif'))

    @commands.command()
    @commands.is_nsfw()
    async def solo(self, ctx : commands.Context):
        await ctx.send(nekos.img('solo'))

    
    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx : commands.Context):
        await ctx.send(nekos.img('hentai'))

    @commands.command()
    @commands.is_nsfw()
    async def pussy(self, ctx : commands.Context):
        await ctx.send(nekos.img('pussy'))
    
    @commands.command()
    @commands.is_nsfw()
    async def tits(self, ctx : commands.Context):
        await ctx.send(nekos.img('tits'))
    
    @commands.command()
    @commands.is_nsfw()
    async def petanko(self, ctx : commands.Context):
        await ctx.send(nekos.img('smallboobs'))

    @commands.command()
    @commands.is_nsfw()
    async def boobies(self, ctx : commands.Context):
        await ctx.send(nekos.img('boobs'))
    
    
def setup(bot):
    bot.add_cog(NSFW(bot))
