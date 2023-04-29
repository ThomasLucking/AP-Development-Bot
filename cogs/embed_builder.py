import discord
from discord.ext import commands
from discord import app_commands
from discord import ui


class MyModal(ui.Modal, title="embed builder"):
    title_embed = ui.TextInput(label="TITLE",placeholder="title of them embed", style=discord.TextStyle.short)
    content_embed = ui.TextInput(label="CONTENT",placeholder="content of the embed", style=discord.TextStyle.long)
    color_embed = ui.TextInput(label="COLOR",placeholder="color of the embed (hex code)", style=discord.TextStyle.short)
    image_embed = ui.TextInput(label="IMAGE",placeholder="image of the embed(URL)", style=discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):
        discord_embed = discord.Embed(title=f"{self.title_embed}", description=f"{self.content_embed}", color=discord.Color(int(f"{self.color_embed}", 16)))
        discord_embed.set_image(url=f"{self.image_embed}")
        await interaction.response.send_message(embed=discord_embed)
    



class embed_builder(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("embed_builder is Ready!")
    

    @app_commands.command(description="Embed Builder")
    async def embed(self, interaction: discord.Interaction):
        await interaction.response.send_modal(MyModal())
    


async def setup(client):
    await client.add_cog(embed_builder(client))