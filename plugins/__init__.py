from bot.plugins import welcomer, embed_ctrl, plugin_ctrl

plugins = (
    welcomer.Welcomer,
    embed_ctrl.EmbedController,
    plugin_ctrl.PluginController,
)

__all__ = ("plugins",)
