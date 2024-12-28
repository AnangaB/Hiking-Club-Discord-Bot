import discord
from discord.ext import commands
import os

#class with a slash command, that makes the bot accont speak anything pas
class CustomBotText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Send a message as the bot.") 
    async def send_text(self, ctx, arg):
        # only allow one user to use this command
        #print("tsets:",ctx.author.id, os.getenv('OWNER_ID'))
        if str(ctx.author.id) != str(os.getenv('OWNER_ID')):
            await ctx.respond("You do not have permission to use this command.", ephemeral=True)
            return
        await ctx.send(arg)



def setup(bot):
    bot.add_cog(CustomBotText(bot))
