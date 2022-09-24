import json
from io import BytesIO

from discord import File, Embed
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

from bot.config import WELCOME_CHANNEL_ID


class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open(self.bot.path / "templates" / "welcome_embed.json") as file:
            channel = await member.guild.fetch_channel(WELCOME_CHANNEL_ID)
            embed = Embed.from_dict(json.load(file))
            file = await self.get_welcome_image(member)

            embed.set_image(url="attachment://welcome.png")
            await channel.send(file=file, embed=embed)

    async def get_welcome_image(self, member):
        with BytesIO() as file:
            font = ImageFont.truetype("arial.ttf", 120)
            text = "Добро пожаловать,\n{}#{}".format(member.name[:20], member.discriminator)
            welcome_path = self.bot.path / "templates" / "welcome.png"

            image = Image.open(welcome_path)
            draw = ImageDraw.Draw(image)

            x, y = image.size
            draw.text((x/2+x/4-x/16, y/2), text=text, fill="white", font=font, anchor="mm", align="center")

            image.save(file, format='PNG', optimize=True)
            file.seek(0)
            return File(fp=file, filename="welcome.png")
