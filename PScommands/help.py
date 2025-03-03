import discord
from discord.ext import commands
from discord import app_commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is Ready!")
    

    @app_commands.command(description="List all of Preppy Service's Commands")
    async def help(self, interaction: discord.Interaction):


        embed = discord.Embed(title="Preppy Services commands", description="""
**Commands with that require a prefix** ``[!]`` <:_:1258733176155537418>
<:_:1260380236437258270> ``rename``
<:_:1260380236437258270> ``say``
<:_:1260380236437258270> ``suggest``
<:_:1260380236437258270> ``Vouch``
**Slash commands** <:_:1258733176155537418>
<:_:1264170104497766473> `Review`
<:_:1264170104497766473> `help`""",color=0xFCA4FD)
        await interaction.response.send_message(embed=embed, ephemeral=True)



async def setup(client):
    await client.add_cog(help(client))