import json
from discord.ext import commands
from discord import Embed, File


class EmbedController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def say(self, ctx, *, json_data):
        await ctx.message.delete()
        json_obj = None
        try:
            json_obj = json.loads(json_data)
        except json.JSONDecodeError:
            pass
        finally:
            embed = await self.get_embed_from_json(json_data=json_obj)
            await self.send_from_bot(ctx.channel, embed)

    @staticmethod
    async def get_embed_from_json(json_data=None, fp=None):
        if json_data:
            return Embed.from_dict(json_data)
        elif fp:
            with open(fp) as file:
                return Embed.from_dict(json.load(file))
        else:
            pass

    @staticmethod
    async def send_from_bot(channel, embed, image=None):
        file = None
        if image:
            file = File(fp=image, filename="welcome.png")
            embed.set_image(url="attachment://welcome.png")
        await channel.send(file=file, embed=embed)

