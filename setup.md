
                                                    # NOTES


**Slash command setup**


import discord
from discord.ext import commands
from discord import app_commands

class slash_command_name(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(".py is Ready!")
    

    @app_commands.command(description="A random number generator")
    async def random(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"response of the slash command")



async def setup(client):
    await client.add_cog(Random(client))


*Normal command setup*
import discord
from discord.ext import commands
class Normal_command_name(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("file.py is Ready!")
    

    @commands.command(description="description of the command")
    async def random(self, ctx):
        await ctx.send("something to respond too lmao")



async def setup(client):
    await client.add_cog(Normal_command_name(client))

