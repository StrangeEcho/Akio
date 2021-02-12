import asyncio

import discord
from discord.ext import commands


class OnEdit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.timeout = 60

    async def edit_process_commands(self, message: discord.Message):
        if not message.author.bot:
            ctx = await self.bot.get_context(message)
            await self.bot.invoke(ctx)
            

    @commands.command(hidden=True)
    @commands.is_owner()
    async def edittime(self, ctx, *, timeout: float):
        if timeout < 0:
            timeout = 0
        await self.config.timeout.set(timeout)
        self.timeout = timeout
        await ctx.message.add_reaction("<a:ticky:739397443325526056>")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.edited_at:
            return
        if before.content == after.content:
            return
        if self.timeout is None:
            self.timeout = await self.config.timeout()
        if (after.edited_at - after.created_at).total_seconds() > self.timeout:
            return
        await self.edit_process_commands(after)


def setup(bot):
    bot.add_cog(OnEdit(bot))