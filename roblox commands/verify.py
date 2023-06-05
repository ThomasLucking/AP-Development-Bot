import discord
import json
import requests
from discord.ext import commands
from discord import app_commands
from discord import ui



class menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None   

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green)
    async def menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(MyModal())


class MyModal(ui.Modal, title="verify"):
    userid = ui.TextInput(label="User ID",placeholder="Place your roblox user id", style=discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):
        file_path = "./data/roblox.json"
        with open(file_path, "r") as f:
            roblox_data = json.load(f)
        
        a = json.dumps(roblox_data)
        x = json.loads(a)
        b = x["endpoints"]["user_info"]

        user_info = requests.get(b.format(user_id=self.userid.value)).json()
        order = ["id", "Id"]

        if not user_info:
            await interaction.response.send_message("Invalid Roblox user ID. Please try again.", ephemeral=True)
        else:
            embed = discord.Embed()

            for attr in order:
                if attr in user_info:
                    sattr = attr
                    embed.add_field(name=f"{sattr}", value=f"{user_info[sattr]}", inline=False)

            await interaction.response.send_message(embed=embed)



        await interaction.response.send_message(embed=embed)


        


class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("verify.py is Ready!")

    @app_commands.command()
    async def verify(self, interaction: discord.Interaction):


        # file_path = "./data/roblox.json"
        # with open(file_path, "r") as f:
        #     roblox_data = json.load(f)
            
        # a = json.dumps(roblox_data)
        # x = json.loads(a)
        # user_info = requests.get(b.format(user_id=user_id)).json()
        # # b = x["endpoints"]["user_info"]





        View = menu()
        await interaction.response.send_message("test", view=View)





async def setup(client):
    await client.add_cog(Verify(client))
    