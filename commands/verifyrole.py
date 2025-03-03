import discord
from discord.ext import commands

class Menu(discord.ui.View):
    def __init__(self, role: discord.Role ,role_to_remove: discord.Role, timeout: float = 315360000):
        super().__init__(timeout=timeout)
        self.role = role
        self.role_to_remove = role_to_remove

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, emoji="✅")
    async def menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        if self.role in member.roles:
            await interaction.response.send_message(f"You already have the role {self.role.name}.", ephemeral=True)
        else:
            await member.add_roles(self.role)
            await interaction.response.send_message(f"You have successfully verified and received the {self.role.name} role!", ephemeral=True)
            await member.remove_roles(self.role_to_remove)
            
class NormalCommandName(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("file.py is Ready!")

    @commands.command(description="description of the command")
    @commands.is_owner()
    @commands.has_permissions(manage_roles=True)
    async def random(self, ctx):
        # Replace 'ROLE_ID' with the actual role ID you want to assign
        role_id = 1092805438287913000  # Example role ID
        role_id2 = 1081618446426583100
        role = ctx.guild.get_role(role_id)
        role_to_remove = ctx.guild.get_role(role_id2)
        if role is None  or role_to_remove is None:
            await ctx.send("Role not found.")
            return

        view = Menu(role, role_to_remove)
        embed = discord.Embed(title="ೃ༄ Verification ⋆｡˚",description="""<:_:1258733506469826610> Welcome to our server! Thank you for joining, **before you get access to the rest of the server**, you MUST click the button below to receive your roles! ✶
<:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961><:_:1258478497136119961> 
*﹒⟡If you still need any further assistance to verify, please contact our support. ⟡ ﹒*""", color=0xFCA4FD)
        await ctx.send("Click the button to verify and receive the role!", view=view)

async def setup(client):
    await client.add_cog(NormalCommandName(client))