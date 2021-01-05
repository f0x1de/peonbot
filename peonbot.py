#!/usr/bin/env python3

import discord
from discord.ext import commands

from lib.config import config

bot = commands.Bot(command_prefix=config.bot.prefix)


@bot.event
async def on_ready():
    print("Logged in as {} ({}).".format(bot.user.name, bot.user.id))


def main():
    for cog in config.bot.cogs.autoload:
        bot.load_extension(f"cogs.{cog}")

    bot.run(config.discord.api.token)


if __name__ == "__main__":
    main()