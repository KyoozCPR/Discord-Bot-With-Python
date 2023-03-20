
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv 
import os 
import responses 
import asyncio

"""
Base class to create the discord bot

MyClient class inherits all methods and attributes from the commands.Bot class and uses the super().__init__()
function to return a commands.Bot class instance and access the constructor in our MyClient classù
 
"""

class MyClient(commands.Bot):
    def __init__(self, WELCOME_CHANNEL, GOODBYE_CHANNEL):

        self.welcome_id = WELCOME_CHANNEL 
        self.goodbye_id = GOODBYE_CHANNEL 


        super().__init__(

            command_prefix= "!",
            intents=discord.Intents.all(), 
            description= "Welcome to the Kyooz&Papa bot \n Discord bot dashboard:  "

            )   



    async def on_ready(self):
        print(f"bot as logged as {self.user}")


    
    async def on_message(self, message):
        
        if message.author == self.user:
            return
        
        response = responses.respond_to_commands(message.content)
        
        if response is not None:

            if message.content[0] == "?":
                await message.author.send(f"{response} {message.author.mention}")
            else:
                await message.channel.send(f"{response} {message.author.mention}")

        await self.process_commands(message)
        
        
    


        

    async def load(self):
        for file in os.scandir(path="./KyoozPapaBot/commands"):
            if file.name.endswith(".py"):
                await self.load_extension(f"commands.{file.name[:-3]}") 
                


            


load_dotenv() #parse a .env file and load all the variables in it

LOGIN_TOKEN = os.getenv("TOKEN")
WELCOME_CHANNEL = os.getenv("WELCOME_CHANNEL_ID")
GOODBYE_CHANNEL = os.getenv("GOODBYE_CHANNEL_ID")
client = MyClient(WELCOME_CHANNEL, GOODBYE_CHANNEL)

async def main():
  
    await client.load()
    await client.start(LOGIN_TOKEN)



asyncio.run(main())
