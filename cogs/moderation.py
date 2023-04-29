import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is Ready!")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("**Missing permissions.**")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("**Missing Role [Staff].**")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("**Member Not Found.**")


    @commands.command(description="Kicks a member")
    @commands.has_any_role("Staff", "Bot Dev", "Owner", "*")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=""):
        if reason == "":
            await member.kick(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been kicked for **reason unspecified**.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been kicked for **{reason}**.")
        await ctx.message.delete()
    
    @commands.command(description="Bans a member")
    @commands.has_any_role("Staff", "Bot Dev", "Owner", "Administrator")
    @commands.has_permissions(ban_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason=""):
        if reason == "":
            await member.ban(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been Banned for **reason unspecified**.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been Banned for **{reason}**.")
        await ctx.message.delete()


    @commands.command(description="Warns a member")
    @commands.has_any_role("Staff", "Bot Dev", "idk", "*")
    async def Warn(self, ctx, member: discord.Member, *, reason=""):
        if reason == "":
            await member.ban(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been Banned for **reason unspecified**.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"<:check:1096065955819421836> **{member}** has been Banned for **{reason}**.")
        await ctx.message.delete()
        








async def setup(client):
    await client.add_cog(moderation(client))