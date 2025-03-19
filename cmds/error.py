import discord
from discord.ext import commands

from core.classes import Cog_Extension

class Error(Cog_Extension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context | discord.Interaction, error: commands.CommandError):
        if hasattr(ctx.command, 'on_error'): return

        embed=discord.Embed(title='❌錯誤', description=f'```\n{str(error)}\n```', color=0xff0000)
        try:
            await ctx.reply(embed=embed, mention_author=False)
        except discord.NotFound:
            await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Error(bot))