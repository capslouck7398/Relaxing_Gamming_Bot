from datetime import datetime
from click import command
import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = False
intents.members = True
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
from datetime import datetime,timezone,timedelta
import json, asyncio, datetime, random, time, re

class Draw(Cog_Extension):
    def __init__(self, *args, **kwargs):  #*args, **kwargs 可變參數
        super().__init__(*args, **kwargs)

        self.counter = 0

    @commands.command()
    async def drawset(self,ctx,name,num:int):
        all = []
        self.counter = 0
        with open('draw.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        if self.counter == 0:
            for i in range(num):
                all.append(i+1)
            print(all)
        name1 = str(name)
        box = name1.split(",")
        # box = list
        if len(box) == len(all):
            jdata['draw_name'] = box
            jdata['draw'] = all
            with open('draw.json', 'w', encoding='utf8') as jfile:
                json.dump(jdata, jfile, indent=4)

            self.counter = 1

            print(jdata['draw'])
            await ctx.send(f"抽籤筒準備完成！請從1~{num}開始抽籤")
            # await ctx.send("*註：30分鐘後抽籤筒將淨空")
            # time.sleep(1800)
            # all = []
            # jdata['draw'] = all
            # with open('draw.json', 'w', encoding='utf8') as jfile:
            #     json.dump(jdata, jfile, indent=4)
            # self.counter = 1
        else:
            await ctx.send("人數與號碼數不符合！請重新輸入！")
    
    @commands.command()
    async def draw(self,ctx):
        print(self.counter)
        if self.counter == 1 :
            with open('draw.json', 'r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            box = jdata['draw']
            for i,a in enumerate(range(len(box))):
                name1 = jdata['draw_name'][i]
                draw_num = random.sample(box, k=1)
                draw_num1 = str(draw_num)
                draw_num2 = re.sub("\'|\[|\]","",draw_num1)
                await ctx.send(f"恭喜{name1}抽到{draw_num2}號！")
                for name in draw_num:
                    box.remove(name)
                if len(box) != 0:
                    pass
                else:
                    await ctx.send("抽籤筒已抽取完畢！")
                    jdata = { "draw_name":[],"draw":[]}
                    box = jdata
                    with open('draw.json', 'w', encoding='utf8') as jfile:
                        json.dump(box,jfile,indent=4)
                    self.counter = 0
                    
                    return
        else:
            await ctx.send("請先設定抽籤筒！")
            return





def setup(bot):
    bot.add_cog(Draw(bot))