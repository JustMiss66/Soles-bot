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
             
@client.command()
async def updates():
    embed = discord.Embed(title = "New Update!", color = 0xFFB6C1)
    embed.add_field(name = "Added:", value = "**]toes** & **]cfeet!**", inline=True)
    embed.add_field(name = "Removed:", value = "**Non**",inline=True)
    embed.set_footer(text="Bot made by: Nela | v1.3")
    await client.say(embed=embed)

@client.command()
async def toes():
    embed = discord.Embed(title = "Look at this toe!", color = 0xFA8072)
    embed.set_footer(text=" Made by Nela! | v1.3")
    embed.set_image(url = random.choice([
        "https://dss.fosterwebmarketing.com/upload/coachellavalleypodiatrist.com/Claw%20Toe.jpg",
        "https://i.pinimg.com/236x/76/28/64/76286494f486844549952c19909ea510--sore-feet-big-toe.jpg",
        "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/articles/health_tools/common_foot_problems/istock_photo_of_womans_feet.jpg",
        "https://media4.s-nbcnews.com/j/streams/2013/may/130522/6c7531804-130522-feet-fungus-tease-1020a.nbcnews-ux-1024-900.jpg",
        "https://cdn.diabetesselfmanagement.com/2015/05/Zimmer051915.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR_Vqf7C3YbCBxMx1dAjGmZCSPK5qPYkLcdzJzCTz4Uw9uFlil7",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQGmd5sbGsdVPDs6W2p-GqRA3OO385WGbf4-SAOOf9pPp19s-u2",
        "https://www.bigodino.it/wp-content/uploads/2016/09/Piedi-idratati-tutto-lanno.jpg",
        "http://resize3-doctissimocom.ladmedia.fr/r/940,,force/crop/940,470/img/var/doctissimo/storage/images/common/belleza/novias/cuidados-antes-de-la-boda/pies-perfectos-el-dia-de-tu-boda/347277-1-esl-ES/luce-unos-pies-perfectos-el-dia-de-tu-boda.jpg"]))
    await client.say(embed=embed)
    
@client.command()
async def cfeet():
    embed = discord.Embed(title = "Do you like it? 😏", color = 0xFFA07A)
    embed.set_footer(text=" Made by Nela!| v1.3")
    embed.set_image(url = random.choice([
        "https://cdn4.images.motherlessmedia.com/images/5E6F284.jpg?fs=opencloud",
        "https://cdn4.images.motherlessmedia.com/images/0896404.jpg?fs=opencloud",
        "http://disney-info.info/images/8eedb10535483b3ea9e93fcb1441d984.jpg",
        "https://images.sex.com/images/pinporn/2015/10/10/300/13999327.gif",
        "https://66.media.tumblr.com/0da2d7a94217e4f7572d545b48636251/tumblr_okoi24JdHC1ulnn8jo1_500.gif",
        "https://cumfoot.files.wordpress.com/2012/04/foot107.gif"]))
    await client.say(embed=embed)
        
client.run(os.getenv("BOT_TOKEN"))
