import discord
import requests
import json
import datetime
from discord.ext import commands
from discord import app_commands

class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("robloxinfo.py is Ready!")

    @app_commands.command(description="Roblox's User information")
    async def whois(self,interaction: discord.Interaction, user_id: int):

        with open("roblox.json", "r") as f:
            roblox_data = json.load(f)

        endpoints = roblox_data["endpoints"]
        fields = roblox_data["fields"]

        # get user data by id
        user_info = requests.get(endpoints["user_info"].format(user_id=user_id)).json()
        if "id" not in user_info:
            return await interaction.response.send_message("User not found")

        # get user display name by id
        display_info = requests.get(endpoints["display_info"].format(user_id=user_id)).json()
        display_name = display_info[fields["display_name"][0]]

        # get user account creation date by id
        created_info = requests.get(endpoints["created_info"].format(user_id=user_id)).json()
        account_created = created_info[fields["account_created"][0]]

        # get user description by id
        desc_info = requests.get(endpoints["desc_info"].format(user_id=user_id)).json()
        user_desc = desc_info.get(fields["user_desc"][0], fields["user_desc"][1])
                
        # get user profile image by id
        profile_info = requests.get(endpoints["profile_info"].format(user_id=user_id)).json()
        profile_image = profile_info[fields["profile_image"][0]][fields["profile_image"][1]][fields["profile_image"][2]]

        embed = discord.Embed(title=f"{display_name}", url=f"https://www.roblox.com/users/{user_id}/profile", color=0x00b3ff)
        embed.set_author(name="Roblox user")
        embed.set_footer(text=f"Made by {interaction.user}")
        embed.add_field(name="Id", value=f"{user_id}", inline=False)
        embed.add_field(name="Display name", value=f"{display_name}", inline=True)
        embed.add_field(name="Account created", value=f"{account_created}", inline=False)
        embed.add_field(name="Description", value=f"{user_desc}", inline=True)
        embed.set_thumbnail(url=f"{profile_image}")



        # send embed
        await interaction.response.send_message(embed=embed)
        







 



    

    




async def setup(client):
    await client.add_cog(userinfo(client))