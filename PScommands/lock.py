import discord
from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("lock.py is ready!")

    @commands.command()
    @commands.has_any_role(1135449483480674304,1135449253574090863,1135468354493227019)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel  # This line should be reachable

        everyone_role = ctx.guild.default_role
        
        try:
            await channel.set_permissions(everyone_role, send_messages=False)

            embed = discord.Embed(description=f"**🔒 Channel has been locked** \n This channel has been locked due to too much drama or problems it will be unlocked soon than you for your patience.",color=0xFCA4FD)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I do not have permission to lock this channel.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(client):
    await client.add_cog(Lock(client))
