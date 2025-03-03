import discord
from discord.ext import commands

class autorole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("autorole.py is Ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_ids = [1135473043712520262, 1135470970447069277, 1135473629791010907]  
        roles = [member.guild.get_role(role_id) for role_id in role_ids]
        
        for role in roles:
            if role:
                await member.add_roles(role)

async def setup(client):
    await client.add_cog(autorole(client))
