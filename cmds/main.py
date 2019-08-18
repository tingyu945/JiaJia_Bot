import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency * 1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('Hello discord user.')

def setup(bot):
    bot.add_cog(Main(bot))