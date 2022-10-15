import json
from discord.ext import commands
from discord import Embed, File


class EmbedController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, data):
        await ctx.message.delete()
        embed = None
        content = None
        try:
            json_obj = json.loads(data)
            embed = await self.get_embed_from_json(json_data=json_obj)
        except json.JSONDecodeError:
            content = data
        finally:
            await self.send_from_bot(ctx.channel, embed, content)

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
    async def send_from_bot(channel, embed=None, text=None, image=None):
        file = None
        if image:
            file = File(fp=image, filename="welcome.png")
            embed.set_image(url="attachment://welcome.png")
        await channel.send(content=text, file=file, embed=embed)
