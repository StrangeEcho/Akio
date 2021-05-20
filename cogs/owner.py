import io
import textwrap
import traceback
from contextlib import redirect_stdout
from typing import Optional

import discord
from discord.ext import commands


class OwnerOnly(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self._last_result = None

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')


    @commands.command(name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        """Evaluates python code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'reply': ctx.message.reference.resolved,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

    @commands.command(aliases= ["echo", "repeat", "send"])
    @commands.is_owner()
    async def say(self, ctx : commands.Context, chan : Optional[discord.TextChannel] = None, *, msg : str):
        """Make the bot say something ig"""
        chan = chan or ctx.channel
        try:
            await chan.send(msg)
        except discord.Forbidden as e:
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx : commands.Context, cog):
        """Load a cog or an extension."""
        try:
            self.bot.load_extension(cog)
            await ctx.send(":ok_hand: Cog Reloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")
    
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx : commands.Context, cog):
        """Unload a cog or an extension."""
        try:
            self.bot.unload_extension(cog)
            await ctx.send(":ok_hand: Cog Reloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog):
        """Reload a cog or an extension."""
        try:
            self.bot.reload_extension(cog)
            await ctx.send(":ok_hand: Cog Reloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")


def setup(bot: commands.Bot):
    bot.add_cog(OwnerOnly(bot))
