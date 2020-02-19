import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
secret_key = os.getenv("BOT_KEY")

command_prefix = '!!'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    
    print(f'Bot is Online~\n{bot.user.name}, (ID: {bot.user.id})\n')
    
    #Loads cogs
    print('Loading cogs:')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'- {(filename[:-3]).title()} commands loaded')
            
@bot.event
async def on_disconnect():
    print('Bot Disconnected...')

@bot.command()
async def reload(ctx, extension = 'Utility'):
    bot.load_extension(f'cogs.{extension}')
    bot.unload_extension(f'cogs.{extension}')

if __name__ == "__main__":   
    bot.run(secret_key)