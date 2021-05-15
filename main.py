import os
import platform

import discord
from discord.ext import commands

from colorama import Fore, Style

from config import prefix, status_str, token


bot = commands.AutoShardedBot(commands.when_mentioned_or(prefix), intents=discord.Intents.all())


loaded_cogs = 0

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        bot.load_extension(f"cogs.{cog[:-3]}")
        loaded_cogs += 1
        print(Fore.YELLOW + f"Loaded {cog}")
print(Style.RESET_ALL)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Game(status_str))
    print(Fore.GREEN + f"Logged in as {bot.user.name}")
    print(f"ID: {bot.user.id}")
    print(f"Running Discord.py version {discord.__version__}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print(f"Loaded *{loaded_cogs}* cogs in total", Style.RESET_ALL)
    print("-" * 15)

bot.run(token)