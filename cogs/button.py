import discord
import asyncio
from discord.ext import commands
from discord import app_commands



class menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None   

    @discord.ui.button(label="zest", style=discord.ButtonStyle.blurple)
    async def menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("This reminder has already been confirmed", ephemeral=True)
        self.value = True


class Button(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Button.py is Ready!")

    @commands.command()
    async def button(self, ctx):
        while True:
            embedV10 = discord.Embed(
                title="Send", 
                description=""":m 👋🏼 Feel free to join our community by joining our communications. We host a lot of events and giveaways! Code: orlando1\n\n**Status:** <:NO:1094514840950812673>""",
                color=discord.Color.red()
        )

            View = menu()
            idk = await ctx.send(embed=embedV10, view=View)
            await View.wait()
            if View.value:
                embed = discord.Embed(
                    title="Sent",
                    description=""":m 👋🏼 Feel free to join our community by joining our communications. We host a lot of events and giveaways! Code: orlando1\n\n**Status:** <:Succes:1081615147975594155>""",
                    color=discord.Color.green()
            )
            await idk.edit(embed=embed, view=View)
            button = View.children[0] # get the button from the view
            button.disabled = True # disable the button
            await asyncio.sleep(20)

        


async def setup(client):
    await client.add_cog(Button(client))