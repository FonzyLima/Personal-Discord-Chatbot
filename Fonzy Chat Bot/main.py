import discord
import random

TOKEN = "ODg0MDg0NDYwMzU2NzY3Nzg0.YTTV0A.uGIzF_o2HHkdWDaj4BZORd4oCBM"

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
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
client.run(TOKEN)
