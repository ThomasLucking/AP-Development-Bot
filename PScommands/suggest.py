
import discord
from discord.ext import commands

class Suggest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Suggestion.py is Ready!")
    

    @commands.command(description="description of the command")
    async def suggest(self, ctx, *, content: str):
        channel_id = 1259790631694504009
        send_channel = self.client.get_channel(channel_id)

        suggestembed = discord.Embed(description=f"<:_:1260380236437258270> **Submitter:** \n {ctx.author.mention} ", color=0xFCA4FD)
        suggestembed.add_field(name="", value=f"<:_:1260380236437258270> **Suggestion:** \n {content} " )
        suggestembed.set_thumbnail(url=f"{ctx.author.avatar}")
        await ctx.send("**Suggestion Submitted!** check <#1259790631694504009> ")
        msg = await send_channel.send(embed=suggestembed)
        await msg.add_reaction("<:_:1260698678927032471>")
        await msg.add_reaction("<:_:1260697295805222942>")



async def setup(client):
    await client.add_cog(Suggest(client))