import discord
import os
from dotenv import load_dotenv

from get_faqs_response import is_msg_a_faq

# Load environment variables
load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is explicitly enabled

# Initialize the client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"Received message: '{message.content}' from {message.author}")

    if message.author == client.user:
        return

    msg = message.content

    faq_answer = is_msg_a_faq(msg)
    print(faq_answer)
    if faq_answer != None:
        await message.channel.send(faq_answer)


client.run(os.getenv('TOKEN'))
