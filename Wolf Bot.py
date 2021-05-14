import discord
import os
import time
import discord.ext
from discord.ext.commands.core import bot_has_permissions
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

bot = commands.Bot(command_prefix='=')
@bot.command()
async def creator(ctx):
    await ctx.send('I was created by **TYPEX**')
@bot.command()
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('TYPEX.GG'))
@bot.command(pass_context=True)
async def id(ctx):
    await ctx.send("{} is your name".format(ctx.message.author.mention))
    await ctx.send("{} is your id".format(ctx.message.author.id))
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))@commands.command()
@bot.command()
@bot_has_permissions()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")
bot.run('ODMwODA4NDAwMDcyODAyMzA0.YHMEng.BMZH2Hsr0PUCn2Bns9B6XohmZOw')