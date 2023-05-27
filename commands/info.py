import discord
from discord.ext import commands
from discord import app_commands

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("user information.py is Ready!")
    

    @app_commands.command(description="Shows User information")
    async def discorduserinfo(self, interaction: discord.Interaction, user: discord.Member):
         embed1 = discord.Embed(title="User Information", description=f"""
         **Username:** {user}
         **Display name:** {user.display_name}
         **Mention :** {user.mention}

         **Joined at:** {user.joined_at}
         **Account Created:** {user.created_at}

         **Roles :** {user.mention.roles}

         """)
         embed1.set_footer(text=f"{user.id}")


         await interaction.response.send_message(embed=embed1)

async def setup(client):
    await client.add_cog(info(client))