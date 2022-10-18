import os
from pathlib import Path

from discord import Intents
from discord.ext import commands
from discord import Object as DiscordObject

from bot.plugins import plugins
from bot.config import COMMAND_PREFIXES, GUILD_ID


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=COMMAND_PREFIXES, intents=self.setup_intents())
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.available_plugins = {}

    @staticmethod
    def setup_intents():
        intents = Intents.default()
        intents.members = True
        intents.message_content = True
        return intents

    async def setup_hook(self):
        await self.register_plugins()
        await self.register_app_commands()

    async def register_plugins(self):
        for Plugin in plugins:
            self.available_plugins[Plugin(self).qualified_name] = Plugin
            await self.add_cog(Plugin(self))

    async def register_app_commands(self):
        guild = DiscordObject(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
