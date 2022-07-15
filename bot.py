import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = True
intents.members = True
from discord.ext import commands
import json
import random  #隨機模組
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='..s ', intents=intents)  #prefix指呼叫機器人需要的指令

@bot.event
async def on_ready():
    print(">> Bot is online. <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done. ')  

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done. ')  

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done. ')  

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')    #從第0個字開始，到倒數第三個字

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
