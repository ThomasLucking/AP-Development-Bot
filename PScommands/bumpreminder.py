import discord
from discord.ext import commands
from discord.ext import commands, tasks
import asyncio

class Reminder(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("file.py is Ready!")
    

    @commands.command()
    async def reminder(self, ctx):
        # Define the channel and send a message there
            channel = self.client.get_channel(1035250415752712244)  # Replace YOUR_CHANNEL_ID with the actual channel ID
            Ping_roles = "<@&1135449483480674304> <@&1135449253574090863>"
            embed = discord.Embed(
                title="Bump reminder!",
                description="This mention is to remind you to bump the server on Disboard!",
                color=0xFCA4FD
            )
            await channel.send(Ping_roles, embed=embed)
            await asyncio.sleep(10)  # Sleep for 2 hours (7200 seconds)



async def setup(client):
    await client.add_cog(Reminder(client))