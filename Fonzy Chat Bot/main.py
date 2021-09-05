import discord
import random

#TOKEN = "ODg0MDg0NDYwMzU2NzY3Nzg0.YTTV0A.hhnTNHQE-sznjYAGU7EeEdp74xw"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return

    
    if channel == "chat-fonzy":
        if "hello" in user_message.lower() or user_message.lower() == "hi":
            await message.channel.send(f"ulol pakyu @{username}! tanginang hello yan")
            return
        if username == "madeleine":
            await message.channel.send("Madeleine panget")
            return
        if username == "leigh" or username == "pinxx" or username == "bea b":
            await message.channel.send(f"lul @{username} amoy boorat")
            return

    if channel == "music":
        await message.channel.send("Hey I like that song too! :>")
        return

    if channel == "noodles":
        if "teleparty" in user_message.lower():
            await message.channel.send("wow u made this time sanaolways")
            return
        
    
client.run(TOKEN)
