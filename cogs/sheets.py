import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# https://developers.google.com/sheets/api/guides/concepts
# https://docs.google.com/spreadsheets/d/1y7MaMeZb-XkrvsGVlCYdAfKKdCRJ50TdyU6Tdry6e-o/edit#gid=0
#TODO: Create skeleton directing flow of application by an user wanting to rent, add, delete items.

key_file = 'secret_key.json'
scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(key_file, scope)
client = gspread.authorize(creds)

class Storage(commands.Cog):

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
    async def Equipment_List(self, ctx):
        sheet1 = client.open('Inventory').get_worksheet(0)
        equipment = sheet1.get_all_records()

        sheet2 = client.open('Inventory').get_worksheet(1)
        snacks = sheet2.get_all_records()
        await ctx.send(equipment)

def setup(bot):
    bot.add_cog(Storage(bot))





