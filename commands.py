# Maxwell Wisnieski
import discord
import random


async def cheeseburger(client, message):
    if message.content.contains("Good morning"):
        await message.channel.send("Cheeseburger")
        
async def fantano(client, message):
    await message.channel.send("Melon gave TBHC a 5/10!!!")

async def strodl(client, message):
	if random.randint(0,10) == 10:
		await message.add_reaction('\U0001F4B2') #strodl bot functionality