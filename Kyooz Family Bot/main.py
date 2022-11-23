import discord
from dotenv import load_dotenv
import os




load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents().all()
client = discord.Client(intents=intents)




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






