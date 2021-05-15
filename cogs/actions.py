import discord
from discord.ext import commands

import aiohttp

default = " " #empty string for when no one is passed to hug

class Actions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx: commands.Context, *, person = default):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://waifu.pics/api/sfw/hug") as resp:
                await ctx.send(embed=discord.Embed(
                    color=ctx.author.color,
                    description=f"{ctx.author.mention} hugs {person}"
                )
                .set_image(url=(resp.json())["url"])
                )

def setup(bot : commands.Bot):
    bot.add_cog(Actions(bot))
