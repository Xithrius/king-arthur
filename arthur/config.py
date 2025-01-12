"""Utilities for interacting with the config for King Arthur."""
from typing import Optional

from pydantic import BaseSettings


class Config(BaseSettings):
    """Configuration for King Arthur."""

    # Discord bot token
    token: str

    # Discord bot prefix
    prefixes: list[str] = ["arthur ", "M-x "]

    # Authorised role ID for usage
    devops_role: int = 409416496733880320

    # Token for authorising with the Cloudflare API
    cloudflare_token: str

    # Guild id
    guild_id: int = 267624335836053506

    # Token for authorising with the Notion API
    notion_api_token: Optional[str] = None

    class Config:  # noqa: D106
        env_file = ".env"
        env_prefix = "KING_ARTHUR_"


CONFIG = Config()
