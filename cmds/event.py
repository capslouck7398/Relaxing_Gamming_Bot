import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = False
intents.members = True
from discord.ext import commands
from core.classes import Cog_Extension
import json,random,re
from cmds.main import Main

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['welcome_channel']))
        await channel.send(f'歡迎 {member} 加入"雲端工程師養成班"大家庭！！')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['leave_channel']))
        await channel.send(f'成員 {member} 已經依依不捨的離開伺服器了')

    @commands.Cog.listener()
    async def on_message(self, msg):
        a = ['你是誰']
        b = ['講個笑話']
        #if msg.content.endswith('apple'):
        if msg.content in a and msg.author != self.bot.user:
            await msg.channel.send('最可愛的Bot ٩(◦`꒳´◦)۶')
        elif msg.content in b and msg.author != self.bot.user:
            b1 = random.sample(jdata['laugh'],k=1)
            b2 = str(b1)
            b3 = re.sub("\'|\[|\]","",b2)
            await msg.channel.send(b3)
    
    # 處理"指令"發生的錯誤 Error Handler
    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     # 上文: ... 指令 觸發了 ___ 錯誤 server channel msg
    #     #await ctx.send(ctx.command)
    #     #檢查指令是否有自己的error handler: 如果有就跳過
    #     if hasattr(ctx.command, 'on_error'):
    #         return
    #     if isinstance(error, commands.errors.MissingRequiredArgment):
    #         await ctx.send("遺失參數") #cmdA
    #     elif isinstance(error,commands.errors.CommandNotFound):
    #         await ctx.send("沒這指令啦！")
    #     else:
    #         await ctx.send("發生錯誤")

    # # 指令個別專用的錯誤處理
    # @Main.cmdB.error
    # async def cmdB_error(self,ctx,error):
    #     if isinstance(error, commands.errors.MissingRequiredArgment):
    #         await ctx.send("請輸入參數")

def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(Event(bot))

