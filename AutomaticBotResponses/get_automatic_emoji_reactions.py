# responds to a message with emojis automatically, if certain keywords are detected
async def respond_with_emoji_automatically(bot,message): 
    msg = message.content.lower()
    if "big way" in msg:
        await message.add_reaction(bot.get_emoji(1294155830941454398))
    if "the cure" in msg:
        await message.add_reaction(bot.get_emoji(1317397518379913250))