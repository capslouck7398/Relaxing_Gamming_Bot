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
import json,random,re

with open('gacha.json', 'r',encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class Gacha(Cog_Extension):

    @commands.command()
    async def gapcr(self,ctx):
        #ga = [random.choices(jdata['pcr-pick-up']),random.choices(jdata['pcr-3']),random.choices(jdata['pcr-2']),random.choices(jdata['pcr-1'])]
        gap = ["ap","a3","a2","a1"]
        gap10 = ["ap","a3","a2"]
        ga = []
        result = random.choices(gap,weights=[0.7,2.3,18,79],k=9)
        result_10 = random.choices(gap10,weights=[0.7,2.3,97],k=1)
        stone = jdata['pcr-stone']
        stone1 = str(stone)
        stone2 = re.sub("\[|\]|\'","",stone1)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['pcr-1'])
                ga.append(a)
            elif i == "a2":
                b = random.choices(jdata['pcr-2'])
                ga.append(b)
            elif i == "a3":
                c = random.choices(jdata['pcr-3'])
                ga.append(c)
            elif i == "ap":
                d = random.choices(jdata['pcr-pick-up'])
                ga.append(d)
                await ctx.send("恭喜抽到本期加倍角色！美咲(舞台)！")
            else:
                pass
        for i in result_10:
            if i == "a2":
                b = random.choices(jdata['pcr-2'])
                ga.append(b)
            elif i == "a3":
                c = random.choices(jdata['pcr-3'])
                ga.append(c)
            elif i == "ap":
                d = random.choices(jdata['pcr-pick-up'])
                ga.append(d)
                await ctx.send("恭喜抽到本期加倍角色！美咲(舞台)！")
            else:
                pass
        result1_1 = str(ga[0:5])
        result1_2 = str(ga[5:10])
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        result2_2 = re.sub("\[|\]|\'|\ |\,","",result1_2)
        count = 0
        for i in ga:
            a = str(i)
            if a[4:5] == "3":
                count = count + 50
            elif a[4:5] == "2":
                count = count + 10
            elif a[4:5] == "1":
                count = count + 1
            else:
                pass
        if count == 19:
            await ctx.send("恭喜獲得"+str(count)+"顆"+stone2+"女神的秘石，你是非洲來的吧？")
        elif count >= 200:
            await ctx.send("恭喜超級歐洲人獲得"+str(count)+"顆"+stone2+"女神的秘石")
        elif count >= 150:
            await ctx.send("恭喜歐洲人獲得"+str(count)+"顆"+stone2+"女神的秘石")
        else:
            await ctx.send("恭喜獲得"+str(count)+"顆"+stone2+"女神的秘石！")
        await ctx.send(result2_1 + "\n" + result2_2)

    @commands.command()
    async def gapcrt(self,ctx,num:int):
        gap = ["ap","a3","a2","a1"]
        ga = []
        pcr1 = []
        pcr2 = []
        pcr3 = []
        result = random.choices(gap,weights=[0.7,2.3,18,79],k=num)
        stone = jdata['pcr-stone']
        stone1 = str(stone)
        stone2 = re.sub("\[|\]|\'","",stone1)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['pcr-1'])
                pcr1.append(a)
            elif i == "a2":
                b = random.choices(jdata['pcr-2'])
                pcr2.append(b)
            elif i == "a3":
                c = random.choices(jdata['pcr-3'])
                pcr3.append(c)
                ga.append(c)
            elif i == "ap":
                d = random.choices(jdata['pcr-pick-up'])
                pcr3.append(d)
                ga.append(d)
                await ctx.send("恭喜抽到本期加倍角色！美咲(舞台)！")
            else:
                pass
        result1_1 = str(ga)
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        count = 0
        for i in ga:
            a = str(i)
            if a[4:5] == "3":
                count = count + 50
            elif a[4:5] == "2":
                count = count + 10
            elif a[4:5] == "1":
                count = count + 1
            else:
                pass
        lpcr1 = str(len(pcr1))
        lpcr2 = str(len(pcr2))
        lpcr3 = str(len(pcr3))
        if count == 19:
            await ctx.send("恭喜獲得"+str(count)+"顆"+stone2+"女神的秘石，你是非洲來的吧？")
        elif count >= 200:
            await ctx.send("恭喜超級歐洲人獲得"+str(count)+"顆"+stone2+"女神的秘石")
        elif count >= 150:
            await ctx.send("恭喜歐洲人獲得"+str(count)+"顆"+stone2+"女神的秘石")
        else:
            await ctx.send("恭喜獲得"+str(count)+"顆"+stone2+"女神的秘石！")
        if lpcr3 == "0":
            await ctx.send("你是超級非洲人吧？")
            await ctx.send("恭喜共獲得" + "\n" + "★★★ " + lpcr3 + "張！"+ "\n" + "★★    " + lpcr2 + "張！"+ "\n"+ "★        " + lpcr1 + "張！")
        else:
            await ctx.send("恭喜共獲得" + "\n" + "★★★ " + lpcr3 + "張！"+ "\n" + "★★    " + lpcr2 + "張！"+ "\n"+ "★        " + lpcr1 + "張！")
            await ctx.send(result2_1)

    @commands.command()
    async def gauma(self,ctx):
        gap = ["ap3","ap2","a3","a2","a1"]
        gap10 = ["ap3","ap2","a3","a2"]
        ga = []
        uma1 = []
        uma2 = []
        uma3 = []
        result = random.choices(gap,weights=[1,0,2,18,79],k=9)
        result_10 = random.choices(gap10,weights=[1,0,2,97],k=1)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['uma-1'])
                ga.append(a)
                uma1.append(a)
            elif i == "a2":
                b = random.choices(jdata['uma-2'])
                ga.append(b)
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['uma-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['uma-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['uma-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        for i in result_10:
            if i == "a2":
                b = random.choices(jdata['uma-2'])
                ga.append(b)
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['uma-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['uma-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['uma-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        luma1 = str(len(uma1))
        luma2 = str(len(uma2))
        luma3 = str(len(uma3))
        result1_1 = str(ga[0:5])
        result1_2 = str(ga[5:10])
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        result2_2 = re.sub("\[|\]|\'|\ |\,","",result1_2)
        await ctx.send("恭喜獲得" + "\n" + "★★★ " + luma3 + "張！"+ "\n" + "★★    " + luma2 + "張！"+ "\n"+ "★        " + luma1 + "張！")
        await ctx.send(result2_1 + "\n" + result2_2)
        if luma1 == "9" and luma2 == "1":
            await ctx.send("你是非洲人吧？")

    @commands.command()
    async def gaumat(self,ctx,num:int):
        gap = ["ap3","ap2","a3","a2","a1"]
        ga = []
        uma1 = []
        uma2 = []
        uma3 = []
        result = random.choices(gap,weights=[1,0,2,18,79],k=num)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['uma-1'])
                uma1.append(a)
            elif i == "a2":
                b = random.choices(jdata['uma-2'])
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['uma-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['uma-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['uma-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        luma1 = str(len(uma1))
        luma2 = str(len(uma2))
        luma3 = str(len(uma3))
        result1_1 = str(ga)
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        if luma3 == "0":
            await ctx.send("你是超級非洲人吧？")
            await ctx.send("恭喜共獲得" + "\n" + "★★★ " + luma3 + "張！"+ "\n" + "★★    " + luma2 + "張！"+ "\n"+ "★        " + luma1 + "張！")
        else:
            await ctx.send("恭喜共獲得" + "\n" + "★★★ " + luma3 + "張！"+ "\n" + "★★    " + luma2 + "張！"+ "\n"+ "★        " + luma1 + "張！")
            await ctx.send(result2_1)


    @commands.command()
    async def gaumas(self,ctx):
        gap = ["ap3","ap2","a3","a2","a1"]
        gap10 = ["ap3","ap2","a3","a2"]
        ga = []
        uma1 = []
        uma2 = []
        uma3 = []
        result = random.choices(gap,weights=[1,0,2,18,79],k=9)
        result_10 = random.choices(gap10,weights=[1,0,2,97],k=1)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['umas-1'])
                ga.append(a)
                uma1.append(a)
            elif i == "a2":
                b = random.choices(jdata['umas-2'])
                ga.append(b)
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['umas-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['umas-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['umas-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        for i in result_10:
            if i == "a2":
                b = random.choices(jdata['umas-2'])
                ga.append(b)
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['umas-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['umas-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['umas-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        luma1 = str(len(uma1))
        luma2 = str(len(uma2))
        luma3 = str(len(uma3))
        result1_1 = str(ga[0:5])
        result1_2 = str(ga[5:10])
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        result2_2 = re.sub("\[|\]|\'|\ |\,","",result1_2)
        await ctx.send("恭喜獲得" + "\n" + "SSR " + luma3 + "張！"+ "\n" + "SR  " + luma2 + "張！"+ "\n"+ "R    " + luma1 + "張！")
        await ctx.send(result2_1 + "\n" + result2_2)
        if luma1 == "9" and luma2 == "1":
            await ctx.send("你是非洲人吧？")

    @commands.command()
    async def gaumast(self,ctx,num:int):
        gap = ["ap3","ap2","a3","a2","a1"]
        ga = []
        uma1 = []
        uma2 = []
        uma3 = []
        result = random.choices(gap,weights=[1,0,2,18,79],k=num)
        for i in result:
            if i == "a1":
                a = random.choices(jdata['umas-1'])
                uma1.append(a)
            elif i == "a2":
                b = random.choices(jdata['umas-2'])
                uma2.append(b)
            elif i == "a3":
                c = random.choices(jdata['umas-3'])
                ga.append(c)
                uma3.append(c)
            elif i == "ap2":
                d = random.choices(jdata['umas-2-pick-up'])
                ga.append(d)
                uma2.append(d)
            elif i == "ap3":
                e = random.choices(jdata['umas-3-pick-up'])
                ga.append(e)
                uma3.append(e)
                await ctx.send("恭喜抽到本期加倍角色！")
            else:
                pass
        luma1 = str(len(uma1))
        luma2 = str(len(uma2))
        luma3 = str(len(uma3))
        result1_1 = str(ga)
        result2_1 = re.sub("\[|\]|\'|\ |\,","",result1_1)
        if luma3 == "0":
            await ctx.send("你是超級非洲人吧？")
            await ctx.send("恭喜共獲得" + "\n" + "SSR " + luma3 + "張！"+ "\n" + "SR  " + luma2 + "張！"+ "\n"+ "R    " + luma1 + "張！")
        else:
            await ctx.send("恭喜共獲得" + "\n" + "SSR " + luma3 + "張！"+ "\n" + "SR  " + luma2 + "張！"+ "\n"+ "R    " + luma1 + "張！")
            await ctx.send(result2_1)




def setup(bot):
    bot.add_cog(Gacha(bot))