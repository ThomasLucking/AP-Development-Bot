import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("say.py is Ready!")
    

    @commands.command(description="Say command")
    @commands.has_any_role(1135449483480674304,1135449253574090863,1135468354493227019)
    async def say(self, ctx, *, contents: str):
        await ctx.send(contents)
        await ctx.message.delete()


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("<:_:1260697295805222942> You do not have permission to run this command. ")


async def setup(client):
    await client.add_cog(Say(client))