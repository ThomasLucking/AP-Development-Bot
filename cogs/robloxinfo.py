import discord
import requests
import json
from discord.ext import commands
from discord import app_commands

class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("robloxinfo.py is Ready!")

    @app_commands.command()
    async def whois(interaction: discord.Interaction, user_id: int):
        user_info = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
        if "id" not in user_info:
            return await interaction.response.send_message("User not found")

        display_info = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
        display_name = display_info["displayName"]

        created_info = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
        account_created = created_info["created"]

        desc_info = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
        user_desc = desc_info.get("description", "No description available")

        profile_info = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=100x100&format=Png&isCircular=false").json()
        profile_image = profile_info["data"][0]["imageUrl"]

        embed = discord.Embed(title=f"{display_name}", url=f"https://www.roblox.com/users/{user_id}/profile", color=0x00b3ff)
        embed.set_author(name="RoUser")
        embed.set_footer(text="Made by AllysonStudiosDev")
        #embed.add_field(name="Status", value=f"{user_status}", inline=False)
        embed.add_field(name="Id", value=f"{user_id}", inline=False)
        embed.add_field(name="Display name", value=f"{display_name}", inline=True)
        embed.add_field(name="Account created", value=f"{account_created}", inline=False)
        embed.add_field(name="Description", value=f"{user_desc}", inline=True)
        embed.set_thumbnail(url=f"{profile_image}")
        await interaction.response.send_message(embed=embed)



    

    




async def setup(client):
    await client.add_cog(userinfo(client))