import discord
from discord.ext import commands
from utils import helpstrings
class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['I cant afford nitro'], hidden=True)
    @commands.is_owner()
    async def www(self, ctx):
        await ctx.send("<a:joy:795290854872973332>")
        
    @commands.command(aliases=['bird raving'], hidden=True)
    async def birb(self, ctx):
        await ctx.send("<a:BirdRave:770062487718461470>")
        
    @commands.command( aliases=['anime girl cry'], hidden=True)
    @commands.is_owner()
    async def tvt(self, ctx):
        await ctx.send("<:acry:661081550527528962>")
        
    @commands.command(aliases=['sad catto'], hidden=True)
    async def oh(self, ctx):
        await ctx.send("<:oh:717649162316939295>") 
        await ctx.message.delete()
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def sudo(self, ctx, member: discord.Member, *, msg):
        """
       Send webhooks which look like a user is saying something.
        """

        webhook = await ctx.channel.create_webhook(name="su")
        await webhook.send(content=msg, username=member.name, avatar_url=member.avatar_url)
        await webhook.delete()

        message = ctx.message
        message.author = member
        message.content = msg
        await self.bot.process_commands(message)
        await ctx.message.delete()
        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def hi(self, ctx, member: discord.Member, *, hi):
        """
       Send webhooks which look like a user is saying something.
        """
	
        webhook = await ctx.channel.create_webhook(name="su")
        await webhook.send(content=hi, username=member.name, avatar_url=member.avatar_url)
        await webhook.delete()
	
        message = ctx.message
        message.author = member
        message.content = hi
        await self.bot.process_commands(message)
        await ctx.message.delete()
        
    
    #===========
    @commands.command(hidden=True)
    @commands.is_owner()
    async def animecrytest(self, ctx):
        webhook = await ctx.channel.create_webhook(name="act")
        await ctx.message.delete()
        await webhook.send(content="<a:animecry12:808741594106822687>", username=ctx.author.display_name, avatar_url=ctx.author.avatar_url)
    
     
        
        
        
def setup(bot):
    bot.add_cog(Owner(bot))

        