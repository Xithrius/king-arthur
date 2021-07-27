"""The zones cog helps with managing Cloudflare zones."""
from typing import Optional

from discord.ext import commands

from arthur.apis.cloudflare import zones
from arthur.bot import KingArthur
from arthur.utils import generate_error_message


class Zones(commands.Cog):
    """Commands for working with Cloudflare zones."""

    def __init__(self, bot: KingArthur) -> None:
        self.bot = bot

    @commands.group(name="zones", invoke_without_command=True)
    async def zones(self, ctx: commands.Context) -> None:
        """Commands for working with Cloudflare zones."""
        await ctx.send_help(ctx.command)

    @zones.command(name="purge")
    async def purge(
        self, ctx: commands.Context, zone_name: Optional[str] = "pythondiscord.com"
    ) -> None:
        """Command to clear the Cloudflare cache of the specified zone."""
        pydis_zones = await zones.list_zones(zone_name)
        required_id = pydis_zones[zone_name]
        purge_attempt_response = await zones.purge_zone(required_id)

        if purge_attempt_response["success"]:
            message = ":white_check_mark:"
            message += f" **Cache cleared!** The Cloudflare cache for `{zone_name}` was cleared."
        else:
            description_content = f"The cache for `{zone_name}` couldn't be cleared.\n"
            if errors := purge_attempt_response["errors"]:
                for error in errors:
                    description_content += f"`{error['code']}`: {error['message']}\n"
            message = generate_error_message(description=description_content, emote=":x:")

        await ctx.send(message)


def setup(bot: KingArthur) -> None:
    """Add the extension to the bot."""
    bot.add_cog(Zones(bot))