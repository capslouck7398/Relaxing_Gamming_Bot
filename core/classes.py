import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = False
intents.members = True
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 