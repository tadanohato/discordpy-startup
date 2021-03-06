from discord.ext import commands
import os
import traceback

import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def tdnht(ctx):
    await ctx.send('hato')
@bot.command()
async def tintin(ctx):
    unko = random.randint(1,8)
    await ctx.send(str(unko) + 'です')
    
bot.run(token)
