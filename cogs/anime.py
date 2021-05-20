import aiohttp
import discord
from discord.ext import commands


class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def megumin(self, ctx: commands.Context):
        """Legendary Waifu"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/megumin") as resp:
                await ctx.send(
                    embed=discord.Embed(color=0x654321)
                    .set_image(url=(await resp.json())["url"])
                    .set_footer(text="say hello to bb")
                )

    @commands.command()
    async def shinobu(self, ctx: commands.Context):
        """Monogatari girl """
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/shinobu") as resp:
                await ctx.send(
                    embed=discord.Embed(color=0xFAF0BE).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)  # ratelimit is 100 per 1 hour so rip
    async def animequote(self, ctx: commands.Context):
        """Get a sick ass anime quote"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://animechan.vercel.app/api/random") as resp:
                char = (await resp.json())["character"]
                quote = (await resp.json())["quote"]
                anime = (await resp.json())["anime"]
                await ctx.send(
                    embed=discord.Embed(
                        description=f"{quote}\n~{char}", color=0xFFB6C1
                    ).set_footer(text=f"Quote From: {anime}")
                )


def setup(bot):
    bot.add_cog(Anime(bot))
