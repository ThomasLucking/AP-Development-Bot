import discord
from discord.ext import commands
from discord import app_commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("test.py is Ready!")
    
    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):

        command = interaction.app_command
        ctx = interaction.context

        await ctx.send(f"An error occurred while executing the {command} command: {error}")
    





async def setup(client):
    await client.add_cog(test(client))