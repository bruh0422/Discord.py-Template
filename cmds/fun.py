import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Fun(Cog_Extension):
    @commands.command()
    async def say(self, ctx: commands.Context, *, message: str):
        await ctx.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))