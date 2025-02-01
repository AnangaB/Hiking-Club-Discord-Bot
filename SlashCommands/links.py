import discord
from discord.ext import commands
from constant import HIKERS_PLAYLIST_LINK, HIKERS_WAIVER_LINK, ICON_URL, INSTAGRAM_LINK, STRAVA_PROFILE_LINK

#class for different slash commands that return different links
class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @discord.slash_command(description="Get link to SFU Hikers Playlist") 
    async def get_playlist(self, ctx):
        await ctx.respond(f"Here is the SFU Hikers Official Playlist:{HIKERS_PLAYLIST_LINK}")

    @discord.slash_command(description="Get link to our Hike Waivers")
    async def get_waiver(self, ctx):
        await ctx.respond(f"Here is our waiver: {HIKERS_WAIVER_LINK}")

    @discord.slash_command(description="Get link to our Instagram Account")
    async def instagram_link(self, ctx):
        await ctx.respond(f"SFU Hikers Instagram: {INSTAGRAM_LINK}")
  
def setup(bot):
    bot.add_cog(Links(bot))
