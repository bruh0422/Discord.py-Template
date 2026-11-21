import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot import MyBot

class Cog_Extension(commands.Cog):
    def __init__(self, bot: "MyBot"):
        self.bot = bot