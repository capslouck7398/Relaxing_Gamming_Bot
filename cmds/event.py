import discord
intents = discord.Intents.default()   #網關預設值
intents.typing = False
intents.presences = False
intents.members = True
from discord.ext import commands
from core.classes import Cog_Extension
import json

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
        keyword = ['apple', 'pen', 'pie']
        #if msg.content.endswith('apple'):
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('hi')
    

def setup(bot):   #傳回去bot.py裡面的bot
    bot.add_cog(Event(bot))