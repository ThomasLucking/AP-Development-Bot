import discord
from discord.ext import commands
class Normal_command_name(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("file.py is Ready!")
    

    @commands.command(description="description of the command")
    @commands.has_any_role(1135449483480674304,1135449253574090863,1135468354493227019)
    async def nitro(self, ctx):
        embed = discord.Embed(description="""## <:nitro:1265822503394349096>  Boosters Rewards

*To show our appreciation for our supporters, we have decided to give every support a reward for boosting us!*
<:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454><:lightline:1265819835229671454>
<:hollowstar:1265822520473292800>  **Rewards:**
<:smallarrow:1258733176155537418> Gifs permission 
<:smallarrow:1258733176155537418> image permission 
<:smallarrow:1258733176155537418> Your own custom role
<:smallarrow:1258733176155537418> 2 rare pets (adopt me)
<:smallarrow:1258733176155537418> <@&1262220711599013959> role, to make you a cute pink color

<:thiccarrow:1258733068194283670> **to claim these perks & rewards, open a customer support tickets!**""")
        await ctx.send(embed=embed)
        



async def setup(client):
    await client.add_cog(Normal_command_name(client))