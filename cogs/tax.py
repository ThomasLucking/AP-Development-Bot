import discord
from discord.ext import commands
from discord import app_commands
import random


class Tax(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("tax.py is Ready!")

    @app_commands.command(description="Calculates the total earnings after Roblox takes tax.")
    async def calculate(self, interaction: discord.Interaction, total: int, tax_rate: float = 30.0):

       tax = total * (tax_rate / 100.0)
       earnings = total - tax

       tax_embed = discord.Embed(description=f"""
        ``Total price: {total}``
        ``Tax rate: {tax_rate}%``
        ``Total tax: {tax:.2f}``
        ``Total earnings: {earnings:.2f}``
    """,)
       tax_embed.color = 0x00ff00

       await interaction.response.send_message(embed=tax_embed)
    





async def setup(client):
    await client.add_cog(Tax(client))