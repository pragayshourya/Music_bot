import discord
from discord.ext import commands

#import os

#import all of the cogs

from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot

bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run("ODg5NDQwNDE0NDQ3MzMzMzc2.YUhR7w.Kv7Do_5TGbgH3is_VVy0I1VZUuQ")


