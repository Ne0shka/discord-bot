from discord.ext import commands
from discord import ClientException


class PluginController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def enable_plugin(self, plugin_name):
        try:
            await self.bot.add_cog(self.bot.available_plugins[plugin_name](self.bot))
            return f'{plugin_name} успешно перезагружен!'
        except TypeError:
            print(f'{plugin_name} не является Cog\'ом')
            return f'Произошла ошибка! Проверьте консоль!'
        except commands.CommandError as e:
            print(f'[{plugin_name}] CommandError: {e}')
            return f'Произошла ошибка! Проверьте консоль!'
        except ClientException:
            return f'{plugin_name} был загружен ранее!'

    async def disable_plugin(self, plugin_name):
        return await self.bot.remove_cog(plugin_name)

    @commands.command()
    async def enable(self, ctx, *, plugin_name):
        if plugin_name in self.bot.available_plugins:
            await ctx.send(await self.enable_plugin(plugin_name))
        else:
            await ctx.send('Неверно указано имя плагина!')

    @commands.command()
    async def disable(self, ctx, *, plugin_name):
        if plugin_name in self.bot.available_plugins:
            if await self.disable_plugin(plugin_name):
                await ctx.send(f'{plugin_name} успешно выгружен!')
            else:
                await ctx.send(f'{plugin_name} был выгружен ранее!')
        else:
            await ctx.send('Неверно указано имя плагина!')

    @commands.command()
    async def reload(self, ctx, *, plugin_name):
        if plugin_name in self.bot.available_plugins:
            if await self.disable_plugin(plugin_name):
                await ctx.send(await self.enable_plugin(plugin_name))
            else:
                await ctx.send(f'{plugin_name} был выгружен ранее!')
        else:
            await ctx.send('Неверно указано имя плагина!')
