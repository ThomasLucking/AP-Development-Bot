import discord
from discord.ext import commands
from discord import app_commands


async def check_staff_role(interaction: discord.Interaction, role_ids: list[int]) -> bool:
    return any(role.id in role_ids for role in interaction.user.roles)

def required_roles(*role_ids):
    async def predicate(interaction: discord.Interaction) -> bool:
        return await check_staff_role(interaction, role_ids)
    return app_commands.check(predicate)

class Terminate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("terminate.py is Ready!")


    @app_commands.command(description="Staff members Termination command")
    @required_roles(1081618446426583100, 1070077819624902778)
    async def terminate(self, interaction: discord.Interaction, staff: discord.Member, reason: str, rank: discord.Role):

        await interaction.response.send_message("**Command Successfully Executed!**", ephemeral=True)
        
        user_dm = await staff.create_dm()
        messagembed = discord.Embed(
            title="<:mark1:1271846361670619196>  Staff Termination",
            description=f"""
<:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961>
*We sincerely thank you for your work here, if any, and we appreciate your assistance. However, the high ranking team has decided to remove you from the server’s staff team, we wish you luck on your future! <:shinylove:1269090302371823636>*
**<:pinkdot:1260380236437258270> Reason: {reason}**
*<:crown:1271646487171960852> Signed by the management team.*
**Preppy services staff team**.""", color=0xFCA4FD)
        await user_dm.send(embed=messagembed)
        
        embed_log = discord.Embed(
            title="<:mark1:1271846361670619196> Staff Termination log", 
            description=f"""
<:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961><:line:1258478497136119961>
**Staff username: {staff.mention}**
**Reason: {reason}** 
**Past rank: {rank.mention}**
**Issuer: {interaction.user.mention}**""", color=0xFCA4FD)
        
        send_channel = self.client.get_channel(1102628036957966507)
        
        if send_channel is not None:
            await send_channel.send(embed=embed_log)
        else:
            await interaction.response.send_message("Log channel not found.", ephemeral=True)


    @terminate.error
    async def terminate_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CheckFailure):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        else:
            await interaction.response.send_message("An error occurred while executing the command, please contact Thomas", ephemeral=True)

async def setup(client):
    await client.add_cog(Terminate(client))

