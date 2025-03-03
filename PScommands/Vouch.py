import discord
from discord.ext import commands
import os
import json

class Vouch(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.file_path = "./data/vouches.json"
        self.vouches_data = self.load_vouches()

    def load_vouches(self):
        if not os.path.exists(self.file_path):
            return {}  # Return an empty dictionary if the file doesn't exist
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}  # Return an empty dictionary if the JSON is invalid

    def save_vouches(self):
        with open(self.file_path, "w") as f:
            json.dump(self.vouches_data, f, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Vouch.py is Ready!")

    @commands.command(aliases=['vouch'])
    async def Vouch(self, ctx, petsitter: discord.Member, number_pets: int, *, pet_type: str):
        # Check if the member is trying to vouch themselves
        if ctx.author == petsitter:
            await ctx.send("**You can't vouch yourself!**")
            return

        # Check for mentions like @here or @everyone
        if petsitter.mention in ['@here', '@everyone']:
            await ctx.send("You cannot ping @here or @everyone!")
            return

        # Log the vouch
        petsitter_id = str(petsitter.id)
        if petsitter_id not in self.vouches_data:
            self.vouches_data[petsitter_id] = []
        
        self.vouches_data[petsitter_id].append({
            "vouched_by": ctx.author.name,
            "number_pets": number_pets,
            "pet_type": pet_type
        })

        self.save_vouches()  # Save the updated vouch data

        # Send a message to the specified channel
        channel_id = 1023281908492275785  # Your specific channel ID
        send_channel = self.client.get_channel(channel_id)

        if send_channel:
            embed = discord.Embed(
                title="<:pinkheart:1258735360419037346> **Vouch**",
                description=(
                    f"<:pinkdot2:1264170104497766473> **Member:** {ctx.author.mention}\n"
                    f"<:pinkdot:1260380236437258270> **Vouched sitter:** {petsitter.mention}\n"
                    f"<:pinkdot2:1264170104497766473> Number of pets: **{number_pets}**\n"
                    f"<:pinkdot:1260380236437258270> Pet rarity: **{pet_type}**"
                ),  
                color=0xFCA4FD
            )
            await send_channel.send(embed=embed)
        
        await ctx.send(f"**Thank you for Vouching! Please check** <#{channel_id}>")
        await ctx.message.delete()

    @commands.command(name='checkvouches')
    async def check_vouches(self, ctx, user: discord.User):
        user_id = str(user.id)
        if user_id not in self.vouches_data:
            await ctx.send(f"{user.mention} has no vouches.")
        else:
            vouch_count = len(self.vouches_data[user_id])
            vouch_details = "\n".join([
                f"<:_:1264170104497766473> **{v['vouched_by']}** vouched for **{v['number_pets']} {v['pet_type']}**"
                for v in self.vouches_data[user_id]
            ])

            embed = discord.Embed(
                title=f"Vouches for {user}",
                description=f"Total Vouches: **{vouch_count}**\n\n{vouch_details}",
                color=0xFCA4FD
            )
            embed.set_thumbnail(url=f"{user.avatar.url}")
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Vouch(client))
