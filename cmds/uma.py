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
import json,random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Uma(Cog_Extension):

    @commands.command()
    async def set_pic(self, ctx , url:str):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['url_pic_1'].append(url)
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f'success!')

    @commands.command()
    async def 特別週(self, ctx):
        random_image_1_1 = random.choice(jdata['image_1_1'])
        embed=discord.Embed(title="特別週", url="https://zh.wikipedia.org/zh-tw/%E7%89%B9%E5%88%A5%E9%80%B1", description="小特、特別肥、スペシャルウィーク", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_1_0'])
        embed.set_image(url=random_image_1_1)
        embed.add_field(name="CV：", value="和氣杏未", inline=True)
        embed.add_field(name="身高：", value="158cm", inline=True)
        embed.add_field(name="體重：", value="微減（競賽前略顯緊張）", inline=True)
        embed.add_field(name="三圍：", value="B79/W57/H81", inline=True)
        embed.add_field(name="生日：", value="5月2日                         ", inline=True)
        # embed.add_field(name="初始星數：", value="三星", inline=True)
        # embed.add_field(name="場地資質：", value="草地:A 沙地:G", inline=True)
        # embed.add_field(name="距離資質：", value="短距離:F 一哩:C 中距離:A 長距離:A", inline=True)
        # embed.add_field(name="腳質資質：", value="領頭:G 前列:A 居中:A 後追:C", inline=True)
        # embed.add_field(name="成長率：", value="持久力+20% 智力+10%", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def 無聲鈴鹿(self, ctx):
        random_image_1_2 = random.choice(jdata['image_1_2'])
        embed=discord.Embed(title="無聲鈴鹿", url="https://ja.wikipedia.org/wiki/%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%B3%E3%82%B9%E3%82%B9%E3%82%BA%E3%82%AB", description="サイレンススズカ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_2_0'])
        embed.set_image(url=random_image_1_2)
        embed.add_field(name="CV：", value="高野麻里佳", inline=True)
        embed.add_field(name="身高：", value="161cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B70/W53/H79", inline=True)
        embed.add_field(name="生日：", value="5月1日", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 東海帝皇(self, ctx):
        random_image_1_3 = random.choice(jdata['image_1_3'])
        embed=discord.Embed(title="東海帝皇", url="https://zh.wikipedia.org/zh-tw/%E6%9D%B1%E6%B5%B7%E5%B8%9D%E7%8E%8B", description="東海帝王、トウカイテイオー", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_3_0'])
        embed.set_image(url=random_image_1_3)
        embed.add_field(name="CV：", value="Machico", inline=True)
        embed.add_field(name="身高：", value="150cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B77/W54/H76", inline=True)
        embed.add_field(name="生日：", value="4月20日", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 丸善斯基(self, ctx):
        random_image_1_4 = random.choice(jdata['image_1_4'])
        embed=discord.Embed(title="丸善斯基", url="https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%AB%E3%82%BC%E3%83%B3%E3%82%B9%E3%82%AD%E3%83%BC", description="阿姨、丸善阿姨、マルゼンスキー", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_4_0'])
        embed.set_image(url=random_image_1_4)
        embed.add_field(name="CV：", value="Lynn", inline=True)
        embed.add_field(name="身高：", value="164cm", inline=True)
        embed.add_field(name="體重：", value="調整狀態相當理想", inline=True)
        embed.add_field(name="三圍：", value="B92/W58/H88", inline=True)
        embed.add_field(name="生日：", value="5月19日", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 富士奇石(self, ctx):
        random_image_1_5 = random.choice(jdata['image_1_5'])
        embed=discord.Embed(title="富士奇石", url="https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%B8%E3%82%AD%E3%82%BB%E3%82%AD", description="富士奇蹟、フジキセキ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_5_0'])
        embed.set_image(url=random_image_1_5)
        embed.add_field(name="CV：", value="松井惠理子", inline=True)
        embed.add_field(name="身高：", value="168cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B84/W58/H82", inline=True)
        embed.add_field(name="生日：", value="4月15日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 小栗帽(self, ctx):
        random_image_1_6 = random.choice(jdata['image_1_6'])
        embed=discord.Embed(title="小栗帽", url="https://zh.wikipedia.org/zh-tw/%E5%B0%8F%E6%A0%97%E5%B8%BD", description="オグリキャップ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_1_6_0'])
        embed.set_image(url=random_image_1_6)
        embed.add_field(name="CV：", value="高柳知葉", inline=True)
        embed.add_field(name="身高：", value="167cm", inline=True)
        embed.add_field(name="體重：", value="微增（吃太多）", inline=True)
        embed.add_field(name="三圍：", value="B82/W57/H82", inline=True)
        embed.add_field(name="生日：", value="3月27日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 黃金船(self, ctx):
        random_image_2_1 = random.choice(jdata['image_2_1'])
        embed=discord.Embed(title="黃金船", url="https://ja.wikipedia.org/wiki/%E3%82%B4%E3%83%BC%E3%83%AB%E3%83%89%E3%82%B7%E3%83%83%E3%83%97", description="ゴールドシップ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_1_0'])
        embed.set_image(url=random_image_2_1)
        embed.add_field(name="CV：", value="上田瞳", inline=True)
        embed.add_field(name="身高：", value="170cm", inline=True)
        embed.add_field(name="體重：", value="無法測定", inline=True)
        embed.add_field(name="三圍：", value="B88/W55/H88", inline=True)
        embed.add_field(name="生日：", value="3月6日                         ", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def 伏特加(self, ctx):
        random_image_2_2 = random.choice(jdata['image_2_2'])
        embed=discord.Embed(title="伏特加", url="https://zh.wikipedia.org/zh-tw/%E4%BC%8F%E7%89%B9%E5%8A%A0_(%E9%A6%AC)", description="Vodka", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_2_0'])
        embed.set_image(url=random_image_2_2)
        embed.add_field(name="CV：", value="大橋彩香", inline=True)
        embed.add_field(name="身高：", value="165cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B76/W55/H78", inline=True)
        embed.add_field(name="生日：", value="4月4日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 大和赤驥(self, ctx):
        random_image_2_3 = random.choice(jdata['image_2_3'])
        embed=discord.Embed(title="大和赤驥", url="https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%83%AF%E3%82%B9%E3%82%AB%E3%83%BC%E3%83%AC%E3%83%83%E3%83%88", description="ダイワスカーレット", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_3_0'])
        embed.set_image(url=random_image_2_3)
        embed.add_field(name="CV：", value="木村千咲", inline=True)
        embed.add_field(name="身高：", value="163cm", inline=True)
        embed.add_field(name="體重：", value="不明（拒絕測量）", inline=True)
        embed.add_field(name="三圍：", value="B90/W56/H82", inline=True)
        embed.add_field(name="生日：", value="5月13日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 大樹快車(self, ctx):
        random_image_2_4 = random.choice(jdata['image_2_4'])
        embed=discord.Embed(title="大樹快車", url="https://ja.wikipedia.org/wiki/%E3%82%BF%E3%82%A4%E3%82%AD%E3%82%B7%E3%83%A3%E3%83%88%E3%83%AB", description="タイキシャトル", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_4_0'])
        embed.set_image(url=random_image_2_4)
        embed.add_field(name="CV：", value="大坪由佳", inline=True)
        embed.add_field(name="身高：", value="172cm", inline=True)
        embed.add_field(name="體重：", value="微增（不過no problem!）", inline=True)
        embed.add_field(name="三圍：", value="B94/W59/H90", inline=True)
        embed.add_field(name="生日：", value="3月23日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 草上飛(self, ctx):
        random_image_2_5 = random.choice(jdata['image_2_5'])
        embed=discord.Embed(title="草上飛", url="https://ja.wikipedia.org/wiki/%E3%82%B0%E3%83%A9%E3%82%B9%E3%83%AF%E3%83%B3%E3%83%80%E3%83%BC", description="阿草、グラスワンダー", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_5_0'])
        embed.set_image(url=random_image_2_5)
        embed.add_field(name="CV：", value="前田玲奈", inline=True)
        embed.add_field(name="身高：", value="152cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B77/W53/H84", inline=True)
        embed.add_field(name="生日：", value="2月18日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 菱亞馬遜(self, ctx):
        random_image_2_6 = random.choice(jdata['image_2_6'])
        embed=discord.Embed(title="菱亞馬遜", url="https://ja.wikipedia.org/wiki/%E3%83%92%E3%82%B7%E3%82%A2%E3%83%9E%E3%82%BE%E3%83%B3", description="ヒシアマゾン", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_2_6_0'])
        embed.set_image(url=random_image_2_6)
        embed.add_field(name="CV：", value="巽悠衣子", inline=True)
        embed.add_field(name="身高：", value="160cm", inline=True)
        embed.add_field(name="體重：", value="微增（不予置評）", inline=True)
        embed.add_field(name="三圍：", value="B92/W59/H89", inline=True)
        embed.add_field(name="生日：", value="3月26日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 目白麥昆(self, ctx):
        random_image_3_1 = random.choice(jdata['image_3_1'])
        embed=discord.Embed(title="目白麥昆", url="https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%B8%E3%83%AD%E3%83%9E%E3%83%83%E3%82%AF%E3%82%A4%E3%83%BC%E3%83%B3", description="メジロマックイーン", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_1_0'])
        embed.set_image(url=random_image_3_1)
        embed.add_field(name="CV：", value="大西沙織", inline=True)
        embed.add_field(name="身高：", value="159cm", inline=True)
        embed.add_field(name="體重：", value="微增（目前拼命調整中！）", inline=True)
        embed.add_field(name="三圍：", value="B71/W54/H76", inline=True)
        embed.add_field(name="生日：", value="4月3日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 神鷹(self, ctx):
        random_image_3_2 = random.choice(jdata['image_3_2'])
        embed=discord.Embed(title="神鷹", url="https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%AB%E3%82%B3%E3%83%B3%E3%83%89%E3%83%AB%E3%83%91%E3%82%B5%E3%83%BC", description="エルコンドルパサー", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_2_0'])
        embed.set_image(url=random_image_3_2)
        embed.add_field(name="CV：", value="高橋未奈美", inline=True)
        embed.add_field(name="身高：", value="163cm", inline=True)
        embed.add_field(name="體重：", value="微增（重訓效果）", inline=True)
        embed.add_field(name="三圍：", value="B89/W58/H86", inline=True)
        embed.add_field(name="生日：", value="3月17日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 好歌劇(self, ctx):
        random_image_3_3 = random.choice(jdata['image_3_3'])
        embed=discord.Embed(title="好歌劇", url="https://ja.wikipedia.org/wiki/%E3%83%86%E3%82%A4%E3%82%A8%E3%83%A0%E3%82%AA%E3%83%9A%E3%83%A9%E3%82%AA%E3%83%BC", description="テイエムオペラオー", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_3_0'])
        embed.set_image(url=random_image_3_3)
        embed.add_field(name="CV：", value="德井青空", inline=True)
        embed.add_field(name="身高：", value="156cm", inline=True)
        embed.add_field(name="體重：", value="總是完美（自稱）", inline=True)
        embed.add_field(name="三圍：", value="B76/W55/H80", inline=True)
        embed.add_field(name="生日：", value="3月13日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 魯道夫象徵(self, ctx):
        random_image_3_4 = random.choice(jdata['image_3_4'])
        embed=discord.Embed(title="魯道夫象徵", url="https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%B3%E3%83%9C%E3%83%AA%E3%83%AB%E3%83%89%E3%83%AB%E3%83%95", description="皇帝、シンボリルドルフ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_4_0'])
        embed.set_image(url=random_image_3_4)
        embed.add_field(name="CV：", value="田所梓", inline=True)
        embed.add_field(name="身高：", value="165cm", inline=True)
        embed.add_field(name="體重：", value="相當理想", inline=True)
        embed.add_field(name="三圍：", value="B86/W59/H85", inline=True)
        embed.add_field(name="生日：", value="3月13日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 氣槽(self, ctx):
        random_image_3_5 = random.choice(jdata['image_3_5'])
        embed=discord.Embed(title="氣槽", url="https://ja.wikipedia.org/wiki/%E3%82%A8%E3%82%A2%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%B4", description="エアグルーヴ", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_5_0'])
        embed.set_image(url=random_image_3_5)
        embed.add_field(name="CV：", value="青木瑠璃子", inline=True)
        embed.add_field(name="身高：", value="165cm", inline=True)
        embed.add_field(name="體重：", value="調整狀態相當理想", inline=True)
        embed.add_field(name="三圍：", value="B90/W57/H86", inline=True)
        embed.add_field(name="生日：", value="4月6日                         ", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def 愛麗數碼(self, ctx):
        random_image_3_6 = random.choice(jdata['image_3_6'])
        embed=discord.Embed(title="愛麗數碼", url="https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%B0%E3%83%8D%E3%82%B9%E3%82%BF%E3%82%AD%E3%82%AA%E3%83%B3", description="愛麗數子、アグネスタキオン", color=0x00ffff, timestamp= datetime.utcnow())
        embed.set_author(name="賽馬娘Pretty Derby", url=jdata['uma_wiki_url'], icon_url="https://upload.wikimedia.org/wikipedia/zh/e/ed/Umamusume_logo.png")
        embed.set_thumbnail(url=jdata['image_3_6_0'])
        embed.set_image(url=random_image_3_6)
        embed.add_field(name="CV：", value="上坂菫", inline=True)
        embed.add_field(name="身高：", value="143cm", inline=True)
        embed.add_field(name="體重：", value="無增減", inline=True)
        embed.add_field(name="三圍：", value="B74/W51/H75", inline=True)
        embed.add_field(name="生日：", value="5月15日", inline=True)

        await ctx.send(embed=embed)
    
    
    
    

    







def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(Uma(bot))