import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

class Cog_Extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot