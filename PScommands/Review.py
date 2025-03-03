import discord
from discord import Member
import asyncio
from discord.ext import commands
from discord import app_commands


class menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None   

    @discord.ui.button(label="Thanks for using our Service!", style=discord.ButtonStyle.gray, disabled=True, emoji="<:_:1258733666117619782>")
    async def menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True

class Review(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.value = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Review.py is Ready!")
    

    
    @app_commands.command(description="Review a pet sitters work")
    @app_commands.choices(ratings=[
        discord.app_commands.Choice(name="1 Star", value="⭐"),
        discord.app_commands.Choice(name="2 Stars", value="⭐⭐"),
        discord.app_commands.Choice(name="3 Stars", value="⭐⭐⭐"),
        discord.app_commands.Choice(name="4 Stars", value="⭐⭐⭐⭐"),
        discord.app_commands.Choice(name="5 Stars", value="⭐⭐⭐⭐⭐")

    ])
    async def review(self, interaction: discord.Interaction, staff: discord.Member ,ratings: str, work: str, reason: str):
        await interaction.response.send_message("Review Submitted!", ephemeral=True)

            
        Message = staff.mention
        EmbedV12 = discord.Embed(title="ೃ༄ Staff Member Review ",description=f"""<:_:1258735642205225060> **Staff Member:** {staff.mention} \n<:_:1258736660426784829> **Work:** {work}\n<:_:1258735360419037346> **Stars:** {ratings} \n<:_:1258735969910128641> **Reason:** {reason}""", color=0xFCA4FD)
        


        buttonV2 = menu()
        channel_id = 1135617012090028153
        send_channel = self.client.get_channel(channel_id)
        await send_channel.send(Message,embed=EmbedV12, view=buttonV2)
                     


async def setup(client):
    await client.add_cog(Review(client))