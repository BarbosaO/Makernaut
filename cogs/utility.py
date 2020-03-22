import discord
from discord.ext import commands

class Utilities(commands.Cog):

    '''
    Administrative tools to scan integrity of the bot
    '''

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def function():
        pass
        
    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'--Pong! That took {round(self.bot.latency * 1000)}ms')

    #@commands.command()
    #async def clear(self, ctx, amount):

def setup(bot):
    bot.add_cog(Utilities(bot)) 