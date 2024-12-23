import discord
from discord.ext import commands


from SlashCommands.Strava.get_strava_data import get_last_10_hikes, get_most_recent_activity

#class for different slash commands that return different links
class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.slash_command(description="Get link to SFU Hikers Playlist") 
    async def get_playlist(self, ctx):
        await ctx.respond("Here is the SFU Hikers Official Playlist: https://open.spotify.com/playlist/6vYqxLulN18MAl9lFzkTV9?si=5563c46ceee44901")

    @discord.slash_command(description="Get link to our Hike Waivers")
    async def get_waiver(self, ctx):
        await ctx.respond(f"Here is the waiver: https://drive.google.com/file/d/1wqu9yPJ3D7ZCLysH6vXiON0fJQ1Xh2lr/view?fbclid=IwAR2JU27KQXWYfa7_HkhvqX2dphbKE8cJWPsMwKtycsjZsjCEtx1FXYPr98wj")

    @discord.slash_command(description="Get link to our Instagram Account")
    async def instagram_link(self, ctx):
        await ctx.respond("SFU Hikers Instagram: https://www.instagram.com/sfuhikers")
    
    @discord.slash_command(description="Get info for the last hike done by the hiking club")
    async def get_last_hike(self,ctx):
        last_hike = get_most_recent_activity()
        if last_hike != None:
            embed=discord.Embed()
            embed.add_field(name="Last Hike done by the Hiking Club:", value=last_hike, inline=False)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond('Error: Currently unable to get the last Hike. Please try again later.', ephemeral=True) 
    
    @discord.slash_command(description="Get info for the last 10 hikes done by the hiking club")
    async def get_last_10_hikes(self,ctx):
        last_10_hikes = get_last_10_hikes()
        if last_10_hikes and len(last_10_hikes) > 0:
            embed=discord.Embed()
            for i,hike in enumerate(last_10_hikes,1):
                if i <= 10:
                    embed.add_field(name=f"Hike {i}:", value=hike, inline=False)
            await ctx.respond(embed=embed)

        else:
            await ctx.respond('Error: Currently unable to get the last 10 Hikes. Please try again later.', ephemeral=True) 


def setup(bot):
    bot.add_cog(Links(bot))
