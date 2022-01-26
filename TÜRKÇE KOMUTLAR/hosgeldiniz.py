import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="r!", intents=intents)

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "welcome")
    await channel.send(f"**{member}** aramıza katıldı, hoşgeldin!")
    print(f"{member} aramıza katıldı, hoşgeldin!")

@Bot.event
async def on_member_remove(member):
    print(f"**{member}** aramızdan ayrıldı")

Bot.run('TOKEN')
