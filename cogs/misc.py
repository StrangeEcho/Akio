import aiohttp
import discord
from discord.ext import commands
from config import client_id

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Wacky Ping Command"""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://animechan.vercel.app/api/random") as resp:
                await ctx.send(
                    embed=discord.Embed(
                        title="**Pong!**",
                        color=discord.Color.purple(),
                        description=f"Websocket: {round(self.bot.latency * 1000)}ms",
                    )
                    .set_thumbnail(url=self.bot.user.avatar.url)
                    .set_footer(text=(await resp.json())["quote"])
                )
    
    @commands.command()
    async def invite(self, ctx: commands.Context):
        try:
            await ctx.author.send(f"Invite me using this link below!\nhttps://discord.com/api/oauth2/authorize?client_id={client_id}&permissions=0&scope=bot")
            await ctx.send("You have mail!")
        except discord.Forbidden:
            await ctx.send("Can't Dm you, sorry. Check your privacy settings.")

def setup(bot: commands.Bot):
    bot.add_cog(Miscellaneous(bot))
