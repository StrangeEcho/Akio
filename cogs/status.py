import asyncio

import config
import discord
from discord.ext import commands, tasks


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.status_change.start()

    @tasks.loop()
    async def status_change(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="your love"))
        await asyncio.sleep(60)
        await self.bot.change_presence(activity=discord.Game("with Tylerr"))
        await asyncio.sleep(60)
        await self.bot.change_presence(activity=discord.Game("with Jay/wi1dloli"))
        await asyncio.sleep(60) 
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"you do {config.prefix}help"))
        await asyncio.sleep(60)
        await self.bot.change_presence(activity=discord.Streaming(name="『　　』| Anime & Gaming", url="https://discord.gg/mfsvxkehuT"))
        await asyncio.sleep(60)

        

def setup(bot):
    bot.add_cog(Status(bot))
