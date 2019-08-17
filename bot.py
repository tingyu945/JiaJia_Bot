import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(612336888694571180)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(612336911347875841)
    await channel.send(F'{member} leave!')

bot.run("NjEyMzE1MDkzNjM1NDMyNTgw.XVg2Pg.QO4JDqDCJ7GIEAZwlD5cAHpPrEQ")