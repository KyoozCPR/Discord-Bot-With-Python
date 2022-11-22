import discord
from dotenv import load_dotenv
import os




client = discord.Client(intents=discord.Intents.default())
load_dotenv()
TOKEN = os.getenv("TOKEN")





@client.event
async def on_ready():
    print(f"We have logged with {client.user}") #print the string with the name of the bot



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
        
  



client.run(TOKEN)





