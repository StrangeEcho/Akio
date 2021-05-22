import random
from typing import Optional

import aiohttp
import discord
import nekos
from discord.ext import commands

from utils.lists import compliments

default = " "  # empty string for when no one is passed to hug


class Actions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def compliment(self, ctx: commands.Context, person: Optional[discord.Member] = None):
        person = person or ctx.author
        await ctx.send(
            embed=discord.Embed(
                description=f"{person.mention} {random.choice(compliments)}",
                color=ctx.author.color,
            ).set_footer(text=f"Compliment from {ctx.author}")
        )

    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx: commands.Context, *, person=default):
        """Make someones day with a hug"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/hug") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} hugs {person}"
                    ).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx: commands.Context, *, person=default):
        """Pat someone. Pats are very gud"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/pat") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} pats {person}"
                    ).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx: commands.Context, *, person=default):
        """Give that special someone a lil smooch smooch"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/kiss") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} kisses {person}"
                    )
                    .set_image(url=(await resp.json())["url"])
                    .set_footer(text="ooooooooo 💘")
                )

    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx: commands.Context, *, person=default):
        """Ever wanted to lick someone? Here you go."""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/lick") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} licks {person}"
                    ).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx: commands.Context, *, person=default):
        """You a big bad bulli"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/bully") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color,
                        description=f"{ctx.author.mention} bullies {person}",
                    )
                    .set_image(url=(await resp.json())["url"])
                    .set_footer(text="oof")
                )

    @commands.command()
    @commands.guild_only()
    async def poke(self, ctx: commands.Context, *, person=default):
        """Annoy someone with a lil poke"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/poke") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} pokes {person}"
                    ).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx: commands.Context, *, person=default):
        """Express your anger with a slap"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/slap") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color, description=f"{ctx.author.mention} slaps {person}"
                    )
                    .set_image(url=(await resp.json())["url"])
                    .set_footer(text="Ouchie")
                )

    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx: commands.Context):
        """You feeling smug? :face_with_raised_eyebrow:"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.waifu.pics/sfw/smug") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        color=ctx.author.color,
                        description=f"{ctx.author.mention} has a smug look on their face",
                    ).set_image(url=(await resp.json())["url"])
                )

    @commands.command()
    @commands.guild_only()
    async def tickle(self, ctx, *, person=default):
        """Tickle Tickle Tickle :)"""

        tickle = nekos.img("tickle")

        embed = discord.Embed(color=0xFFB6C1)
        embed.description = f"{ctx.author.mention} tickles {person}"
        embed.set_image(url=tickle)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def baka(self, ctx, *, person=default):
        """Onii-san anata BAKA!"""

        baka = nekos.img("baka")

        embed = discord.Embed(color=0xFFB6C1)
        embed.description = f"{ctx.author.mention} calls {person} a baka"
        embed.set_image(url=baka)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def feed(self, ctx, *, person=default):
        """Give our lil friend sum to eat"""

        feed = nekos.img("feed")

        embed = discord.Embed(color=0xFFB6C1)
        embed.description = f"{ctx.author.mention} feeds {person}"
        embed.set_image(url=feed)
        embed.set_footer(text="Eat Up!")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Actions(bot))
