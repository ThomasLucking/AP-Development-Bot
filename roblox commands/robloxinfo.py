import os
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

        print("Loading Roblox data from file...")
        try:
            file_path = "./data/roblox.json"
            with open(file_path, "r") as f:
                roblox_data = json.load(f)
            
            a = json.dumps(roblox_data)
            x = json.loads(a)

            b = x["endpoints"]["user_info"]
            user_info = requests.get(b.format(user_id=user_id)).json()
            print(user_info.keys())
            print(user_info.values())
            i = []
            for x in user_info.values():
                i.append(x)
            #print(i.keys())
            #date = i[1][0:10]
            #i[1] = date
            date = user_info["created"][0:10]
            user_info["created"] = date

            print("Roblox data loaded.")
        except Exception as e:
            print(f"Error loading Roblox data: {e}")
       
        # get user profile image by id
        endpoints = roblox_data["endpoints"]
        profile_info = requests.get(endpoints["profile_info"].format(user_id=i[5])).json()
        profile_image = (profile_info["data"][0]["imageUrl"])
        #profile_image = profile_info[fields["profile_image"][0]] [fields["profile_image"][1]][fields["profile_image"][2]]

        #embed = discord.Embed(title=f"{i[7]}", url=f"https://www.roblox.com/users/{i[5]}/profile", color=0x00b3ff)
        embed = discord.Embed(title=f"{i[7]}", url=f"https://www.roblox.com/users/{i[5]}/profile", color=0x00b3ff)
        embed.set_author(name="Roblox user")
        embed.set_footer(text=f"Made by {interaction.user}")

        #order = [ ["name", 6],["Display name", 7], ["id", 5],["Account created",1],["Description", 0] ]
        #for attr in order:
          #  embed.add_field(name=attr[0], value=f"{i[attr[1]]}", inline=False)

        #for key, value in user_info.items():
            #print(key, value)
            #embed.add_field(name=f"{key}", value=f"{value}", inline=False)

        #order = ["name","displayName", "id", "created","description"]
        #title = ["Name","Display Name", "Id", "Account Created ","Description"]
        #for attr in order:
            #print(user_info[attr])
            #embed.add_field(name=f"{attr}", value=f"{user_info[attr]}", inline=False)

        #for attr in range(0, len(order)):
            #embed.add_field(name=f"{title[attr]}", value=f"{user_info[order[attr]]}", inline=False)

        order = [["name", "Name"], ["displayName", "Display Name"],["id","Id" ], ["created","Account Created" ], ["description", "Description"]]
        for attr in order:
            #embed.add_field(name=f"{attr[0]}", value=f"{user_info[attr[1]]}", inline=False)
            #{user_info[order[attr]]}
            sattr = attr
            embed.add_field(name=f"{sattr[1]}", value=f"{user_info[sattr[0]]}", inline=False)

        #embed.add_field(name="Id", value=f"{i[5]}", inline=False)
        #embed.add_field(name="Display name", value=f"{i[7]}", inline=False)
        #embed.add_field(name="Account created", value=f"{i[1]}", inline=False)
        #embed.add_field(name="Description", value=f"{i[0]}", inline=False)

        embed.set_thumbnail(url=f"{profile_image}")
        


        await interaction.response.send_message(embed=embed)
        

async def setup(client):
    await client.add_cog(userinfo(client))