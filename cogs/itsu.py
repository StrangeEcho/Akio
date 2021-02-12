import contextlib
import jishaku.paginators
import jishaku.exception_handling
import discord
import re
from discord.ext.commands.context import Context
from discord.http import Route, HTTPClient
from typing import Union
from collections import namedtuple

EmojiSettings = namedtuple('EmojiSettings', 'start back forward end close')

class FakeEmote(discord.PartialEmoji):
    @classmethod
    def from_name(cls, name):
        emoji_name = re.sub("|<|>", "", name)
        a, name, id = emoji_name.split(":")
        return cls(name=name, id=int(id), animated=bool(a))


emote = EmojiSettings(
    start=FakeEmote.from_name("<:before_fast:779669326348156959>"),
    back=FakeEmote.from_name("<:before_check:779669831623770132>"),
    forward=FakeEmote.from_name("<:next_check:779669444699881472>"),
    end=FakeEmote.from_name("<:next_fast:779669510943932416>"),
    close=FakeEmote.from_name("<:stop_check:779669563696611348>")
)
jishaku.paginators.EMOJI_DEFAULT = emote  # Overrides jishaku emojis


async def attempt_add_reaction(msg: discord.Message, reaction: Union[str, discord.Emoji]):
    reacts = {
        "\N{WHITE HEAVY CHECK MARK}": "<:checkmark:779670688114016256>",
        "\N{BLACK RIGHT-POINTING TRIANGLE}": emote.forward,
        "\N{HEAVY EXCLAMATION MARK SYMBOL}": "<:information:779670754764652546>",
        "\N{DOUBLE EXCLAMATION MARK}": "<:crossmark:779670792749056000>",
        "\N{ALARM CLOCK}": emote.end
    }
    with contextlib.suppress(discord.HTTPException):
        return await msg.add_reaction(reacts[reaction])


jishaku.exception_handling.attempt_add_reaction = attempt_add_reaction               

def setup(bot):
    pass