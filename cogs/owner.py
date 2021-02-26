import discord

from typing import Optional

from discord.ext import commands

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(aliases = ['echo']) 
    @commands.is_owner()
    async def say(self, ctx, chan : Optional[discord.TextChannel] = None, *, message):
        """Say something with the bot."""
        await ctx.message.delete()
        if chan is None:
            await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
        else:
            await chan.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
    
    @commands.is_owner()
    @commands.command(name='frick', aliases=['sho'], hidden=True)
    async def frick(self, ctx: commands.Context, limit: int = 50) -> None:
        """
        Cleans up the bots messages.
        `limit`: The amount of messages to check back through. Defaults to 50.
        """

        prefix = ">:"

        if ctx.channel.permissions_for(ctx.me).manage_messages:
            messages = await ctx.channel.purge(check=lambda message: message.author == ctx.me or message.content.startswith(prefix), bulk=True, limit=limit)
        else:
            messages = await ctx.channel.purge(check=lambda message: message.author == ctx.me, bulk=False, limit=limit)

        await ctx.send(f'Found and deleted `{len(messages)}` of my message(s) out of the last `{limit}` message(s).', delete_after=3)
        
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """Reload a cog or an extension."""
        try:
            self.bot.reload_extension(cog)
            await ctx.send(":ok_hand: Cog Reloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
    
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """Unload a cog or an extension."""
        try:
            self.bot.unload_extension(cog)
            await ctx.send(":ok_hand: Cog Unloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        """
        Load a cog or an extension.
        """
        try:
            self.bot.load_extension(cog)
            await ctx.send(":ok_hand: Cog Loaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
    
    @commands.command(help='Shutsdown Bot', aliases=['Shutdown', 'logout', 'Logout'])
    @commands.is_owner()
    async def shutdown(self, context):
        embed = discord.Embed(
            description="Logging Out. Bye! :woman_walking:",
            color=0x33DAFF
        )
        await context.send('shutting down')
        await self.bot.logout()
        await self.bot.close()

def setup(bot):
    bot.add_cog(Owner(bot))

        