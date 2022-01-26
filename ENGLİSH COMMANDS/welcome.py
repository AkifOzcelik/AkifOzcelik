import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="r!", intents=intents)

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "welcome")
    await channel.send(f"**{member}** joined us, welcome!")
    print(f"{member} joined us, welcome!")

@Bot.event
async def on_member_remove(member):
    print(f"**{member}** left us")

Bot.run('OTI5NDk1MjM4NDMzNzEwMDkw.YdoJ5g.nQuhtNmi49dMhTg7o-v-ji26pi4')