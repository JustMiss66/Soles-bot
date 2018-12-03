import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = ']')

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: ]"))
    print("The bot is online and connected with Discord!") 

@client.command()
async def help():
    embed = discord.Embed(title = "Help commands!", color = 0xBA55D3)
    embed.set_footer(text = "Bot made by Nela say congrats to her please :)")
    embed.add_field(name = "]feet", value = "Shows an awesome foot!", inline=False)
    embed.add_field(name = "]toes", value = "Shows some toes ;)",inline=False)
    embed.add_field(name = "]cfeet", value = "Shows cum on feet pic/gif! (Preparing)",inline=False)
    await client.say(embed=embed)
                     





@client.command()
async def feet():
         embed = discord.Embed(title="Oo check this feet!", color = 0xDA70D6)
         embed.set_footer(text="Tip: If the image didnt load try to use this command again! | Developer Nela | Bot version: 1.3")
         embed.set_image(url = random.choice([
             "https://cdn.psychologytoday.com/sites/default/files/styles/image-article_inline_full/public/blogs/315/2009/11/34495-16628.jpg?itok=Ge_x7sNX",
             "https://mfiles.alphacoders.com/431/431663.jpg",
             "https://i.pinimg.com/originals/c2/d2/fd/c2d2fd938526f05e2eb41a9e6012ad3a.jpg",
             "https://i.pinimg.com/736x/4d/28/e0/4d28e09859b3ea4f6d19dc6876885540.jpg",
             "https://i.pinimg.com/originals/32/e3/a8/32e3a84b0ce709c6849c6b62cb9108c3.jpg",
             "https://i.pinimg.com/originals/5f/be/a3/5fbea3dffe6dfb7e3c9325fdceacb2d1.png",
             "https://i.pinimg.com/originals/10/ed/c9/10edc98f708736f13ff6352f3dac796c.jpg"]))
         await client.say(embed=embed)
             
client.run(os.getenv("BOT_TOKEN"))
