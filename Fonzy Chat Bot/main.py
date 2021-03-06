import os
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from itertools import cycle

SERVER_ID = os.environ.get('SERVER_ID')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "$", intents=intents)

# List of statuses to be displayed
status = cycle(["MOBDEVE","CSNETWK","CSMODEL","CSSWENG"])


@client.event
async def on_ready():
    change_status.start()
    print("We have logged in as {0.user}".format(client))

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lupang Hinirang"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command does not exist!\nType $command to see all valid commands")

@client.command(pass_context=True)
async def members(ctx):
    await ctx.send(f"Number of members: {ctx.guild.member_count}")

@client.command(pass_context=True)
async def roles(ctx):
    await ctx.send("----------ROLES----------")
    for role in ctx.guild.roles:
        role_itr = ctx.guild.get_role(role.id)
        await ctx.send(f"{str(role.name)}: {str(len(role_itr.members))}")

@client.command(pass_context=True,aliases=["clear","empty"])
async def _clear(ctx, amount=5): #Clears 5 messages if no given parameter
    await ctx.channel.purge(limit=int(amount)+1)
    return

@_clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please type a number")
        return

@client.command(pass_context=True)
async def play(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("april.wav")
        player = voice.play(source)
        await ctx.send("Now Playing Music")
    return

@client.command(pass_context=True)
async def study(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("Studymusic.wav")
        player = voice.play(source)
        await ctx.send("Now Playing Study Music")
    return
    
@client.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()
    return


client.run(TOKEN)
