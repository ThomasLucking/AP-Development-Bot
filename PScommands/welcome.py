import discord
from discord.ext import commands

class idk(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("welcome.py is Ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1135446567038500917
        send_channel = self.client.get_channel(channel_id)


        Welcome = discord.Embed(title="⋆｡˚❀ Welcome to Preppy services !",description="""
                              
                            <:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961>
                            <:_:1258735969910128641> **Welcome!**
                            <:_:1258733666117619782>  *Thank you for joining!*
                            <:_:1258733421149294662> **Enjoy your stay!** 
                            ✶ Check out these channels:
                            <:_:1258733068194283670> ⁠<#1135460959717167186>
                            <:_:1258733068194283670> <#1135623721692962838>
                            <:_:1258733068194283670> ⁠<#1135605872979091577>
                              """)
        await send_channel.send(member.mention)
        await send_channel.send(embed=Welcome)

    




async def setup(client):
    await client.add_cog(idk(client))