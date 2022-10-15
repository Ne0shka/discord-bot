from envparse import Env

env = Env()
env.read_envfile()

GUILD_ID = env.int("GUILD_ID")
BOT_TOKEN = env.str("BOT_TOKEN")
COMMAND_PREFIXES = env.list("COMMAND_PREFIXES")
WELCOME_CHANNEL_ID = env.int("WELCOME_CHANNEL_ID")
