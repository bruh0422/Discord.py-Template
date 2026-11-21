import discord
from discord.ext import commands

import os, importlib

from core.classes import Cog_Extension
import core.classes as c

class Dev(Cog_Extension):
    @commands.command(description='讀取分類')
    @commands.is_owner()
    async def load(self, ctx: commands.Context | discord.Interaction, extension: str):
        if extension == '*':
            item = []
            for x in os.listdir('./cmds'):
                if x.endswith('.py'):
                    await self.bot.load_extension(f'cmds.{x[:-3]}')
                    item.append(f'`{x}`')

            embed = discord.Embed(title='✅讀取成功', color=discord.Color.green())
            embed.add_field(name='📥｜以下分類已被讀取', value=' '.join(item))
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await self.bot.load_extension(f'cmds.{extension}')
            embed = discord.Embed(title='✅讀取成功', color=discord.Color.green())
            embed.add_field(name='📥｜以下分類已被讀取', value=f'`{extension}.py`')
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(description='卸載分類')
    @commands.is_owner()
    async def unload(self, ctx: commands.Context | discord.Interaction, extension: str):
        if extension == '*':
            item = []
            for x in os.listdir('./cmds'):
                if x.endswith('.py'):
                    await self.bot.unload_extension(f'cmds.{x[:-3]}')
                    item.append(f'`{x}`')
            embed = discord.Embed(title='✅卸載成功', color=discord.Color.green())
            embed.add_field(name='📤｜以下分類已被卸載', value=' '.join(item))
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await self.bot.unload_extension(f'cmds.{extension}')
            embed = discord.Embed(title='✅卸載成功', color=discord.Color.green())
            embed.add_field(name='📤｜以下分類已被卸載', value=f'`{extension}.py`')
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(description='重新讀取分類')
    @commands.is_owner()
    async def reload(self, ctx: commands.Context | discord.Interaction, extension: str):
        importlib.reload(c)

        if extension == '*':
            item = []
            for x in os.listdir('./cmds'):
                if x.endswith('.py'):
                    try:
                        await self.bot.reload_extension(f'cmds.{x[:-3]}')
                    except commands.errors.ExtensionNotLoaded:
                        pass
                    else:
                        item.append(f'`{x}`')
            embed = discord.Embed(title='✅重新讀取成功', color=discord.Color.green())
            embed.add_field(name='♻️｜以下分類已被重新讀取', value=' '.join(item))
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await self.bot.reload_extension(f'cmds.{extension}')
            embed = discord.Embed(title='✅重新讀取成功', color=discord.Color.green())
            embed.add_field(name='♻️｜以下分類已被重新讀取', value=f'`{extension}.py`')
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(description='同步 app_commands')
    @commands.is_owner()
    async def sync(self, ctx: commands.Context | discord.Interaction):
        cmds = await self.bot.tree.sync()
        embed = discord.Embed(title='✅同步成功', description=f'已同步 `{len(cmds)}` 個指令', color=discord.Color.green())
        await ctx.reply(embed=embed, mention_author=False)

async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))