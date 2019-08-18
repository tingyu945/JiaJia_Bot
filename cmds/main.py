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
        await ctx.send('Hi there.')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit = num+1)
def setup(bot):
    bot.add_cog(Main(bot))