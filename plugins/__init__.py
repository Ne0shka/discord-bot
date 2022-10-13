from bot.plugins import welcomer, embed_ctrl

plugins = (
    welcomer.Welcomer,
    embed_ctrl.EmbedController,
)

__all__ = ("plugins",)
