from datetime import datetime
from click import command
import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = True
intents.members = True
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
from datetime import datetime,timezone,timedelta
import json,random

class Search(Cog_Extension):
    @commands.command()
    async def spc(self,ctx,*,input):
        def rep(input):
            li = []
            for i in input:
                li.append(i)
            for i in range(len(li)):
                if li[i] == ' ':
                    li[i] = '%20'
            return ''.join(li)
        input = rep(input)
        result = "https://ecshweb.pchome.com.tw/search/v3.3/?q=" + input
        await ctx.send(result)
    
    @commands.command()
    async def ssp(self,ctx,*,input):
        def rep(input):
            li = []
            for i in input:
                li.append(i)
            for i in range(len(li)):
                if li[i] == ' ':
                    li[i] = '%20'
            return ''.join(li)
        input = rep(input)
        result = "https://shopee.tw/search?keyword=" + input
        await ctx.send(result)   

def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(Search(bot))