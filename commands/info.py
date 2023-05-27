import discord
from discord.ext import commands
from discord import app_commands

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(".py is Ready!")
    

    @app_commands.command()
    async def info(interaction: discord.Interaction, Username: str):
        embed = discord.Embed(title="User Information", description=f"""
        **Username:** {interaction.user}
        **Display name:** {Username.display_name}
        **Mention :** {Username.mention}

        Joined at: {Username.joined_at}
        Account Created: {Username.created_at}

        **Roles :** {Username.roles}



        
        """)

async def setup(client):
    await client.add_cog(info(client))