import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(F'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['apple', 'pen', 'pie', 'abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')
        if msg.content == '清' and msg.author != self.bot.user:
            await msg.channel.send('周')
        if msg.content == '小' and msg.author != self.bot.user:
            await msg.channel.send('蔡')
        if msg.content == '周' and msg.author != self.bot.user:
            await msg.channel.send('宇博')
        if msg.content == '蔡' and msg.author != self.bot.user:
            await msg.channel.send('政詰')

def setup(bot):
    bot.add_cog(Event(bot))