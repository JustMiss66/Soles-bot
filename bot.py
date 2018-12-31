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
import datetime
import requests
import json
import aiohttp






client = commands.Bot(command_prefix = ']')

client.remove_command('help')

def dev(m):
    return m.author == "342364288310312970"

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: ]"))
    print("The bot is online and connected with Discord!") 

@client.command(pass_context = True)
@commands.check(dev)

    
async def restart():
    
        
    await client.logout()

@client.command()
async def help():
    embed = discord.Embed(title = "Help commands!", color = 0xBA55D3)
    embed.set_footer(text = "Bot made by Nela say congrats to her please :)")
    embed.add_field(name = "Prefix:", value = "``]``",inline=False)
    embed.add_field(name = "feet", value = "Shows an awesome foot!", inline=False)
    embed.add_field(name = "toes", value = "Shows some toes ;)",inline=False)
    embed.add_field(name = "cfeet", value = "Shows cum on feet pic/gif! (Preparing)",inline=False)
    embed.add_field(name = "anime_feet", value = "Shows Anime feet :smirk:",inline=False)
    await client.say(embed=embed)
                     





@client.command()
async def feet():
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/feet/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Take some feets :D', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
@client.command()
async def update():
    embed = discord.Embed(title = "New Update!", color = 0xFFB6C1)
    embed.add_field(name = "Added:", value = "**]anime_feet!**", inline=True)
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
        
@client.command(pass_context=True)
async def anime_feet(ctx):
    embed = discord.Embed(color = 0xFF00FF, title = random.choice([
        "Wow isnt this great?",
        "If you dont like it then idk what happen to you.."]))
    embed.set_image(url = random.choice([
        "https://i.pinimg.com/originals/76/59/97/765997fbe30e3c7ffd7f720c79b8b8d2.png",
        "https://i.pinimg.com/originals/aa/f5/b8/aaf5b8d355383ad8d0116bdd3bcd4d7f.jpg",
        "https://www.oyunoyna.us/wp-content/uploads/2018/04/einverstandniserklarung-nutzung-fotos-luxus-wykop-newsy-aktualnoac29bci-gry-wiadomoac29bci-muzyka-of-einverstandniserklarung-nutzung-fotos-1.jpg",
        "https://c.wallhere.com/photos/a8/aa/anime_anime_girls_underwear_legs_feet_short_hair_blue_hair_blue_eyes-1370773.jpg!d",
        "http://i.imgur.com/pYuJ5.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQl6OthUM2DOK2JvXPGU-fHojvmoBKD21evmetQ3zXh4cIqmcLr",
        "https://i.pinimg.com/originals/10/0a/24/100a24d66a560feeab6b9526ceb0d548.png",
        "https://steamusercontent-a.akamaihd.net/ugc/307738934713973831/383AB085056139AE110C306A1AD56873DE66CCBB/"]))
    
    embed.set_footer(text = "Requested by {0}".format(ctx.message.author.name))
    await client.say(embed=embed)
 
#Logs are down ↓ #          

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    cannel = message.channel
    channel = discord.utils.get(client.get_all_channels(), name='chat')
    embed = discord.Embed(title = "Message Deleted!", color = 0xA52A2A)
    embed.add_field(name="Message sent by:",value="{0}".format(author), inline=False)
    embed.add_field(name="Message Deleted:",value="{0}".format(content), inline=False)
    embed.add_field(name="In Channel:",value="{0}".format(cannel), inline=False)
    await client.send_message(channel, embed=embed)
    
@client.event
async def on_member_join(user: discord.Member):
    name = user.name
    channel = discord.utils.get(client.get_all_channels(), name='chat')
    joined = user.joined_at
    uid = user.id
    tma = user.avatar_url
    embed = discord.Embed(title="Member Joined!", color = 0x00FF0C)
    embed.add_field(name="Member Profile Picture:",value="Is on right side",inline=False)
    embed.add_field(name = "Member Name:",value="{0}".format(name), inline=False)
    embed.add_field(name = "Member ID:",value = "{0}".format(uid), inline=False)
    embed.add_field(name = "Joined:",value="{0}".format(joined), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)
    
@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player(url, ytdl_options=None, **kwargs)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start()

@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")

@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')

@client.event
async def on_member_remove(user: discord.Member):
    name = user.name
    channel = discord.utils.get(client.get_all_channels(), name='chat')
    joined = user.joined_at
    uid = user.id
    tma = user.avatar_url
    embed = discord.Embed(title="Member left!", color = 0x00FF0C)
    embed.add_field(name="Member Profile Picture:",value="Is on right side if no then he have default profile picture.",inline=False)
    embed.add_field(name = "Member Name:",value="{0}".format(name), inline=False)
    embed.add_field(name = "Member ID:",value = "{0}".format(uid), inline=False)
    embed.add_field(name = "Joined:",value="{0}".format(joined), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)
    
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("Use this command like ``] trolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if value is None:
        await client.say("Use this command like ``]rolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await client.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await client.say("{} role colour has been edited.".format(role))

client.run(os.getenv("BOT_TOKEN"))
