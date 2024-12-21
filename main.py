import os
import discord
from dotenv import load_dotenv
from get_faqs_response import is_msg_a_faq

# Load environment variables
load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is explicitly enabled

# Initialize the bot with intents
bot = discord.Bot(intents=intents)

bot.load_extension("Cogs.links")
bot.load_extension("Cogs.custom_text_for_bot")



@bot.event
async def on_message(message):
    print(f"Received message: '{message.content}' from {message.author}")
    

    # Ignore messages from bots
    if message.author.bot:
        return
    
    msg = message.content

    faq_answer = is_msg_a_faq(msg)
    print(faq_answer)
    if faq_answer is not None:
        await message.channel.send(faq_answer)


bot.run(os.getenv('TOKEN'))
