import discord
from discord.ext import commands
class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("file.py is Ready!")
    

    @commands.has_permissions(manage_messages=True)
    @commands.has_any_role(1262040181410758677)
    @commands.command(name='purge')
    async def purge(self, ctx, amount: int):
        if amount < 1:
            await ctx.send("Please specify a number greater than 0.")
            return
        
        try:
            deleted = await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"<:_:1260698678927032471> Succesfully deleted **{len(deleted) - 1}** message(s)", delete_after=5)
        except discord.Forbidden:
            await ctx.send("I don't have permission to delete messages.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete messages: {e}")



async def setup(client):
    await client.add_cog(Purge(client))