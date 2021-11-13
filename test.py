import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def 발탄(ctx):
    await ctx.send('https://youtu.be/YNf2my7id-A https://youtu.be/LakcTJ7lmgw')
@client.command()
async def 비아(ctx):
    await ctx.send('https://youtu.be/RRxHRHWyp-Q https://youtu.be/lLgvOOt3DSA https://youtu.be/GtVyd7N9M2Q')
@client.command()
async def 쿠크(ctx):
    await ctx.send('https://youtu.be/Y1I19YwJuIY https://youtu.be/pS81SiezMcc https://youtu.be/YHiJToAhGZ0 ')
@client.command()
async def 아르고스(ctx):
    await ctx.send('https://youtu.be/EwAUycmaZVs https://youtu.be/FG9F6on4LAY https://youtu.be/hCncYVwjlDY ')
@client.command()
async def 아브데자뷰(ctx):
    await ctx.send('https://youtu.be/6bg4xYvbF2o https://youtu.be/Ql6jzAQWmak https://youtu.be/G5jKLI7gCoU https://youtu.be/mwP40-E3ELE')


access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
