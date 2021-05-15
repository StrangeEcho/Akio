import discord

from discord.ext import commands

import aiohttp

class Miscellaneous(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx : commands.Context):
        """Wacky Ping Command"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://animechan.vercel.app/api/random") as resp:
                await ctx.send(embed=discord.Embed(
                    title="**Pong!**",
                    color=discord.Color.purple(),
                    description=f"Websocket: {round(self.bot.latency * 1000)}ms"
                )
                .set_thumbnail(url=self.bot.user.avatar_url)
                .set_footer(text=(await resp.json())["quote"])
                )

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))

