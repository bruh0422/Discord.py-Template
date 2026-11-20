import discord
from discord.ext import commands

import os

from dotenv import load_dotenv
load_dotenv()

class MyBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents.all())

    async def setup_hook(self):
        for filename in os.listdir('./cmds'):
            if filename.endswith('.py'):
                await self.load_extension(f'cmds.{filename[:-3]}')

    async def on_ready(self):
        print(f'Logged in as｜{str(self.user)}')

if __name__ == '__main__':
    MyBot().run(os.getenv('TOKEN'))