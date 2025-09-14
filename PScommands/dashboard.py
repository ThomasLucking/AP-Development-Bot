import discord
from discord.ext import commands

class DashboardCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='dashboard')
    async def dashboard(self, ctx):
        """Display the Ontario Provincial Roleplay dashboard"""
        
        # Create the first embed with DPD Banner
        embed1 = discord.Embed(color=0xFA5959)
        embed1.set_image(url="https://cdn.discordapp.com/attachments/1403401152262967420/1403717457054793919/DPD_Banner_1_1.png?ex=68989141&is=68973fc1&hm=22f352e90a6343e5be357347d5311ec4d83057a1b56b260aedf38629294ebd69&")
        
        # Create the main dashboard embed
        embed2 = discord.Embed(
            description="# Dashboard \n> **Ontario Provincial Roleplay** community, bringing the authentic feel of **Ontario** to Liberty County. We focus on realism, professionalism, and immersive scenarios that follow Ontario laws, emergency service procedures, and community life.\n\n",
            color=0xFA5959
        )
        
        # Add fields
        embed2.add_field(
            name=" **Community Resources**",
            value="\n- Affiliation Request\n- Staff Application\n- Our Regulations\n- Roblox Group\n- Ban Appeal\n\n",
            inline=True
        )
        
        embed2.add_field(
            name=" **Command Chain**",
            value="- <@&ROLE_ID_1>\n- <@&ROLE_ID_2>\n- <@&ROLE_ID_3>\n- <@&ROLE_ID_4>\n- <@&ROLE_ID_5>",  # Replace with actual role IDs
            inline=True
        )
        
        # Set the footer image
        embed2.set_image(url="https://cdn.discordapp.com/attachments/1403401152262967420/1403718369995133109/WCSO_Footer_1_1.png?ex=6898921b&is=6897409b&hm=eded60bf41c453776021161bc3fc6e98930c5b68e43b69404ebd9ae888614802&")
        
        # Send both embeds
        await ctx.send(embeds=[embed1, embed2])

async def setup(client):
    await client.add_cog(DashboardCog(client))