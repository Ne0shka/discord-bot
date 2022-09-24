import os
from pathlib import Path

from discord import Intents
from discord.ext import commands

from bot.plugins import plugins
from bot.config import COMMAND_PREFIXES


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=COMMAND_PREFIXES, intents=self.setup_intents())
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))

    def setup_intents(self):
        intents = Intents.default()
        intents.members = True
        intents.message_content = True
        return intents

    async def setup_hook(self):
        await self.register_plugins()

    async def register_plugins(self):
        for Plugin in plugins:
            await self.add_cog(Plugin(self))
