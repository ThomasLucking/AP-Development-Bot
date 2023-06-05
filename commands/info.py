import discord
import datetime
from discord.ext import commands
from discord import app_commands
from discord.utils import format_dt
class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("user information.py is Ready!")
    

    @app_commands.command(description="Shows User information")
    async def discorduserinfo(self, interaction: discord.Interaction, user: discord.Member):

        roles = [role.mention for role in user.roles if role.name != '@everyone']
        roles_str = ' '.join(roles)
        
        time = datetime.datetime.utcnow()
        avatar = user.avatar
        joined_at = format_dt(user.joined_at, style="f")
        created_at = format_dt(user.created_at, style="f")

        embed1 = discord.Embed(title="User Information", description=f"""
         **Username:** {user}
         **Display name:** {user.display_name}
         **Mention :** {user.mention}

         **Joined at:** {joined_at}
         **Account Created:** {created_at}

         **Roles :** {roles_str}
         **Permissions :** {user.guild_permissions}

         """)
        embed1.set_footer(text=f"Id: {user.id} Created at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        embed1.set_thumbnail(url=avatar)



        await interaction.response.send_message(embed=embed1)
#.strftime('%Y-%m-%d')}``


async def setup(client):
    await client.add_cog(info(client))