from attr import field
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Hello, I am online now')

@bot.command()
async def proxies(ctx):

    proxies = discord.Embed(title='Prime Proxy Companies', description='Footlocker is a Footsite. You can visit at https://www.footlocker.com/. ', color=0x070d53)
    proxies.set_thumbnail(url='https://imgur.com/1Nl5Lc3.png')
    proxies.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=proxies)

bot.run('MTAyODg3MjU4NDI5NDU4MDI0NQ.GkYlPA.9smFe6HPPIbhj3KcJYM68PsuqiYtcjiWnP9yUE')