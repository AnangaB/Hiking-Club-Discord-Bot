import os
import discord
from dotenv import load_dotenv

from AutomaticBotResponses.get_automatic_emoji_reactions import respond_with_emoji_automatically
from AutomaticBotResponses.get_faqs_response import is_msg_a_faq

# Load environment variables
load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is explicitly enabled

# Initialize the bot with intents
bot = discord.Bot(intents=intents)

#load the slash commands
bot.load_extension("SlashCommands.links")
bot.load_extension("SlashCommands.custom_text_for_bot")
bot.load_extension("SlashCommands.hikes_data")
bot.load_extension("SlashCommands.sfu_live_webcam")

@bot.event
async def on_message(message):
    
    # Ignore messages from bots
    if message.author.bot:
        return
    
    msg = message.content.lower()

    faq_answer = is_msg_a_faq(msg)
    if faq_answer is not None:
        await message.channel.send(faq_answer)

    await respond_with_emoji_automatically(bot, message)


bot.run(os.getenv('TOKEN'))
