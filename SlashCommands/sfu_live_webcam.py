import time
import discord
from discord.ext import commands

from constant import ICON_URL, SFU_UDN_WEBCAM_LINK, SFU_WEBCAM_LINK

#class for slash commands that return webcam images of SFU
class SFU_Outside_Live_Cam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Show a live picture of outdoors at SFU. Check if it's snowing!")
    async def show_current_sfu(self, ctx):
        timestamp = int(time.time())
        url = f"{SFU_UDN_WEBCAM_LINK}{timestamp}"
        embed = discord.Embed(
            title="SFU Live Webcam",
            description=f"Below is a live image of SFU, showing University Drive North. [View more live outdoor SFU pictures.]({SFU_WEBCAM_LINK})."
        )
        embed.set_author(name="SFU Hiking Club", icon_url=f"{ICON_URL}")

        embed.set_image(url=url)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(SFU_Outside_Live_Cam(bot))

