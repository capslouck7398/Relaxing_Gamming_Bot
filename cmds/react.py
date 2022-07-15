import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = False
intents.members = True
from discord.ext import commands
from core.classes import Cog_Extension
import random, json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def rdpic(self, ctx):
        random_url_pic = random.choice(jdata['url_pic'])
        #pic = discord.File(random_pic)  #傳送指定位置圖片
        await ctx.send(random_url_pic)

    @commands.command()
    async def rdbl(self, ctx):
        random_bl_pic = random.choice(jdata['bl_pic'])
        #pic = discord.File(random_pic)  #傳送指定位置圖片
        await ctx.send(random_bl_pic)

    # @commands.command()
    # async def rdtest(self, ctx):
    #     random_test_pic = random.choice(jdata['uma_pic_1'])
    #     #pic = discord.File(random_pic)  #傳送指定位置圖片
    #     await ctx.send(random_test_pic)

    # @commands.command()
    # async def rdazur(self,ctx):
    #     await ctx.send("..s azur 吸血鬼")


def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(React(bot))