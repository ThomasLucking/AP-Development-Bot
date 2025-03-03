import discord
from discord.ext import commands

class ChannelManager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        unclaimed_category = discord.utils.get(after.guild.categories, id="1273352506151403562")  
        other_category = discord.utils.get(after.guild.categories, id="1273354454695149588")  

        if before.name != after.name and "unclaimed" in after.name.lower():
            if unclaimed_category: 
                await after.edit(category=unclaimed_category) 
                print(f"Moved channel {after.name} to {unclaimed_category.name}")
            else:
                print("Unclaimed category not found.")
        
        elif before.name != after.name and "unclaimed" not in after.name.lower():
            if other_category:  
                await after.edit(category=other_category)  
                print(f"Moved channel {after.name} to {other_category.name}")
            else:
                print("Other category not found.")


async def setup(client):
    await client.add_cog(ChannelManager(client))