import discord
from discord.ext import commands
from SlashCommands.Strava.get_strava_data import get_last_n_hikes, get_most_recent_activity
from constant import ICON_URL, STRAVA_PROFILE_LINK

#class for different slash commands that return different links
class HikeData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.slash_command(description="Get info for the last hike done by the hiking club")
    async def get_last_hike(self,ctx):
        last_hike = get_most_recent_activity()
        if last_hike != None:
            embed=discord.Embed(title="The Last Hike done by the Hiking Club",description=f"View all our other hikes on our Strava by clicking [here]({STRAVA_PROFILE_LINK})",color=discord.Color.blurple())

            embed.add_field(name="", value=last_hike, inline=False)
            embed.set_author(name="SFU Hiking Club", icon_url=f"{ICON_URL}")

            await ctx.respond(embed=embed)
        else:
            await ctx.respond('Error: Currently unable to get the last Hike. Please try again later.', ephemeral=True) 
    
    @discord.slash_command(description="Get info for the last 10 hikes done by the hiking club")
    async def get_last_10_hikes(self,ctx):
        last_10_hikes = get_last_n_hikes(10)
        if last_10_hikes and len(last_10_hikes) > 0:
            embed = get_multi_hikes_embed(10,last_10_hikes)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond('Error: Currently unable to get the last 10 Hikes. Please try again later.', ephemeral=True)
        
    @discord.slash_command(description="Get info for the last 5 hikes done by the hiking club")
    async def get_last_5_hikes(self,ctx):
        last_5_hikes = get_last_n_hikes(5)
        if last_5_hikes and len(last_5_hikes) > 0:
            embed = get_multi_hikes_embed(5,last_5_hikes)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond('Error: Currently unable to get the last 5 Hikes. Please try again later.', ephemeral=True)

def setup(bot):
    bot.add_cog(HikeData(bot))


def get_multi_hikes_embed(number_of_hikes, hike_data):
    
    embed=discord.Embed(title=f"The last {number_of_hikes} hikes done by the club",description=f"View the rest on our Strava by clicking [here]({STRAVA_PROFILE_LINK})",color=discord.Color.blurple())
                
    embed.set_author(name="SFU Hiking Club", icon_url=f"{ICON_URL}")

    for i,hike in enumerate(hike_data,1):
        if i <= 10:
            embed.add_field(name="", value=hike, inline=False)

    return embed