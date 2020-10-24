# Maxwell Wisnieski
import discord

# importing the module 
import json 
  
# Opening JSON file 
print("Loading ALL of english")
with open('words_dictionary.json') as json_file: 
    english_words = json.load(json_file) 
print("shoot, that's a lot of english: " + str(len(english_words)))

accceptable_words = []

async def cheeseburger(client, message):
    if message.content.contains("Good morning"):
        await message.channel.send("Cheeseburger")
        
async def fantano(client, message):
    await message.channel.send("Melon gave TBHC a 5/10!!!")
    
async def dummy(client, message):
    global english_words
    words = message.content.split()
    chan = client.get_channel(769239365162631228);
    #print(chan.name)
    if message.author.id == 317349964894437376:
        msg = ""
        for word in words:
            if not (word.lower() in english_words) and not (word.lower() in accceptable_words):
                msg += word
                msg += " "
        if msg:
            await chan.send(msg)
