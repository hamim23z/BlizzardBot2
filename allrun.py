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

import subprocess

process1 = subprocess.Popen(["python", "channel.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "shoesize.py"])
process3 = subprocess.Popen(["python", "website.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()