import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="r!", intents=intents)

@Bot.event
async def on_ready():
    print("Bot's online")

@Bot.command()
async def RealAx(msg):
    await msg.send("The Best!")

@Bot.command()
async def sunucu(msg):
    await msg.send("İşte benim resmi sunucum: https://discord.gg/MpBP4nAKAy")

@Bot.command()
async def server(msg):
    await msg.send("Here is my offical server: https://discord.gg/j5h7egKq2S")



Bot.run('TOKEN')
