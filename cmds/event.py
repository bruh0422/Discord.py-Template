import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot: return

        if message.content == 'ping':
            await message.reply('pong', mention_author=False)

async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))