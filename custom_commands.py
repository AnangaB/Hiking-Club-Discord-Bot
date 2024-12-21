import discord
from discord.ext import commands


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


def setup(bot):
    bot.add_cog(Links(bot))
