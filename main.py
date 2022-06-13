from email import message
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content=True

client = commands.Bot(command_prefix="q", intents = intents)

badwords= ( "Retarded", "Motherfucker", "Cunt", "Pussy", "Bitch", "Hoe", "Whore") #YOU CAN UPDATE THE LIST OF WORDS TO BE HONKED FROM HERE.


@client.event
async def on_ready():
    print("Honk!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('<@985787395859447821>'):
        await message.reply("Honk!")

    if message.content.startswith(badwords):
        #YOU CAN UPDATE YOUR EMOTE FROM HERE.
        await message.add_reaction('<:bonk:985813030287839303>')
        

    await client.process_commands(message)





client.run(#PUT YOUR BOT TOKEN HERE)