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


"""    @discord.slash_command(description="Send a message as the bot.") 
    async def emoji_react_msg(self, ctx, msg_id, emoji_name):
        if str(ctx.author.id) != str(os.getenv('OWNER_ID')):
            await ctx.respond("You do not have permission to use this command.", ephemeral=True)
            return
        channel = ctx.channel

        message = await channel.fetch_message(msg_id)
        emoji = discord.utils.get(ctx.guild.emojis, name=emoji_name)
        if emoji:
            await message.add_reaction(emoji)
            await ctx.respond(f"Successfully reacted to the message with {emoji_name}.")
        else:
            await ctx.respond(f"Emoji '{emoji_name}' not found on this server.", ephemeral=True)

"""

def setup(bot):
    bot.add_cog(CustomBotText(bot))
