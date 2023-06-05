import discord
from discord import app_commands
from discord.ext import commands



class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("mute.py is Ready!")
    

    @app_commands.command(description="Mutes a member")
    async def mute(interaction: discord.Interaction, member: discord.Member, time: int, *, reason: str):
        await member.edit(timed_out_until=f"{time}")
        await interaction.response.send_message(f"{member}, has been muted for {reason} duration: {time}")


    





async def setup(client):
    await client.add_cog(mute(client))
