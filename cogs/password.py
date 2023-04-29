import discord
import string
import random
from discord.ext import commands
from discord import app_commands


class password(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("password.py is Ready!")
    

    @app_commands.command(description="Password generator")
    async def generator(self, interaction: discord.Interaction):
        for i in range(10):
            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 21
            password1 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password2 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password3 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password4 = "".join(random.sample(characters, password_length))
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password5 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password6 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password7 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password8 = "".join(random.sample(characters, password_length))

            characters = string.ascii_letters + string.digits + string.punctuation
            password_length = 20
            password9 = "".join(random.sample(characters, password_length))

            await interaction.response.send_message(f"**Random passwords:**\n```{password1}\n {password2}\n {password3}\n {password4}\n {password5}\n {password6}\n {password7}\n {password8}\n {password9}```")



async def setup(client):
    await client.add_cog(password(client))