import discord
import os

from dotenv import load_dotenv
load_dotenv()

import commands

#from monitor import keep_alive

#keep_alive()

client = discord.Client()

command_dict = {
    "fantano": commands.fantano
   
}

flag_dict = {
    "Good morning": commands.cheeseburger,
    "" : commands.strodl

}

token = str(os.getenv("TOKEN"))
prefix = 'AM'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Gentrifying Clavius"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith(prefix):
        command = message.content[len(prefix):] #strip the prefix
        for opcode, method in command_dict.items():
            if command.startswith(opcode):
                await method(client, message)

    
    for flag, method in flag_dict.items():
        if flag in message.content.lower():
            await method(client, message)

client.run(token)