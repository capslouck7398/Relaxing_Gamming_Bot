from datetime import datetime
from random import Random, random
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
import random,re

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):                                       #指令一定要有ctx，"context"上下文，
        await ctx.send(f'{int(self.bot.latency*1000)} (ms)')        #A:嗨 (上文) (使用者,id,所在伺服器,所在頻道)
                                                                    #B:安安 (下文)
    # @commands.command()
    # async def 特別週(self, ctx):
    #     embed=discord.Embed(title="特別週", url="https://zh.wikipedia.org/zh-tw/%E7%89%B9%E5%88%A5%E9%80%B1", description="小特、特別肥", color=0x00ffff, timestamp= datetime.utcnow())
    #     embed.set_author(name="賽馬娘Pretty Derby", url="https://zh.wikipedia.org/zh-tw/%E8%B3%BD%E9%A6%AC%E5%A8%98_Pretty_Derby", icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
    #     embed.set_thumbnail(url="https://static.komoejoy.com/uma/gw/pc/imgs/character/matchSuit/%E7%89%B9%E5%88%A5%E9%80%B1.png")
    #     embed.add_field(name="CV：                   ", value="和氣杏未              ", inline=True)
    #     embed.add_field(name="身高：", value="158cm", inline=True)
    #     embed.add_field(name="體重：", value="微減（起跑前些微緊張）", inline=True)
    #     embed.add_field(name="三圍：", value="B79/W57/H81", inline=True)
    #     embed.add_field(name="生日：", value="5月2日                         ", inline=True)
    #     embed.add_field(name="初始星數：", value="三星", inline=True)
    #     embed.add_field(name="場地資質：", value="草地:A 沙地:G", inline=True)
    #     embed.add_field(name="距離資質：", value="短距離:F 一哩:C 中距離:A 長距離:A", inline=True)
    #     embed.add_field(name="腳質資質：", value="領頭:G 前列:A 居中:A 後追:C", inline=True)
    #     embed.add_field(name="成長率：", value="持久力+20% 智力+10%", inline=True)
    #     await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, * ,msg):
        #刪除我所說的訊息
        await ctx.message.delete()
        #ctx.message > msg 代表自己所說的訊息
        #複誦我所說的訊息
        await ctx.send(msg)
    
    @commands.command()
    async def clear(self, ctx, num:int):
        #清除num筆訊息，purge訊息刪除
        await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def cmdA(self,ctx,num:float):
        await ctx.send(num)

    @commands.command()
    async def cmdB(self,ctx,num):
        await ctx.send(num)
        
    @commands.command()
    async def random_squad(self,ctx):
        online = []
        #我 所在的伺服器 = ctx.guild
        #列出伺服器所有成員 = ctx.guild.members 出來的是array
        for member in ctx.guild.member:
            print(member.status)
        #判斷每個成員的在線狀態
        #if 成員狀態 == 在線:
            #就把該成員加到online list
            if str(member.status) == 'online' and member.bot == False:
                online.append(member.name)
        
        #選出不重複的5人
        ramdom_online = random.sample(online, k=20)
        for squad in range(4):
            x = random.sample(ramdom_online, k=5)
            await ctx.send(f'第{squad+1}小隊：' + str(x))
            #移除已取完的人
            for name in x:
                ramdom_online.remove(name)
    
    @commands.command()
    async def group(self, ctx, msg, num1:int, num:int):
        msg1 = str(msg)
        box = msg1.split(",")
        for a in range(num):
            x = random.sample(box, k=num1)
            x1 = str(x)
            x2 = re.sub("\'|\[|\]","",x1)
            await ctx.send(f'第{a+1}組為：' + x2)
            for name in x:
                box.remove(name)
    
    @commands.command()
    async def jack(self, ctx, msg, num:int, award): 
        #num總獎項數 award各獎項人數
        #總人數
        msg1 = str(msg)
        box = msg1.split(",")
        #各獎項人數
        award1 = str(award)
        award2 = award1.split(",")
        if len(award2) > 1 :
            for a in range(num):
                num1 = int(award2[a])
                x = random.sample(box, k=num1)
                x1 = str(x)
                x2 = re.sub("\'|\[|\]","",x1)
                await ctx.send(f'{a+1}獎：' + x2)
                for name in x:
                    box.remove(name)
        elif len(award2) == 1 :
            for a in range(num):
                award3 = int(award)
                x = random.sample(box, k=award3)
                x1 = str(x)
                x2 = re.sub("\'|\[|\]","",x1)
                await ctx.send(f'{a+1}獎：' + x2)
                for name in x:
                    box.remove(name)    

    @commands.command()
    async def ch_group(self,ctx,num:int,num1:int):
        online = []
        for member in ctx.channel.members:
            #abc = member + member.status
            if member.bot == False:
                online.append(member.name)
        for squad in range(num1):
            rd_group = random.sample(online, k=num)
            await ctx.send(f'第{squad+1}組：' + str(rd_group))
    


    # @commands.group()
    # async def codetest(self,ctx):
    #     pass

    # @codetest.command()
    # async def python(self,ctx):
    #     await ctx.send("Python") 
    # @codetest.command()
    # async def javascript(self,ctx):
    #     await ctx.send("javascript")     
    # @codetest.command()
    # async def cpp(self,ctx):
    #     await ctx.send("C++") 
    




def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(Main(bot))