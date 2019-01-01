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
    embed.add_field(name = "slap", value = "Slaps a user. Usage: ``]slap @user``",inline=False)
    embed.add_field(name = "hug", vlaue = "Hugs a user! Usage: ``]hug @user``",inline=False)
    embed.add_field(namd = "kiss", value = "Kiss a perso. :) Usage: ``]kiss @user``",inline=False)
    await client.say(embed=embed)
                     





@client.command(pass_context = True)
async def feet(ctx):
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
    embed.add_field(name = "Added:", value = "Some fun commands: __]slap @user__ and __]hug @user__ and ]kiss @user__ ! I hope you will enjoy!", inline=True)
    embed.add_field(name = "Removed:", value = "**Non**",inline=True)
    embed.set_footer(text="Bot made by: Nela | v1.3")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def toes(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/toes/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Wow I like this!', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command()
async def cfeet():
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/cums_on_feet/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Dont tell me you dont like it.', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command(pass_context=True)
async def anime_feet(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        
        async with session.get("https://api.reddit.com/r/neko_feet/random") as r:
            
            data = await r.json()
            embed = discord.Embed(title='I like Anime!', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
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
    embed = discord.Embed(title="Member left!", color = 0xA52A2A)
    embed.add_field(name="Member Profile Picture:",value="Is on right side if no then he have default profile picture.",inline=False)
    embed.add_field(name = "Member Name:",value="{0}".format(name), inline=False)
    embed.add_field(name = "Member ID:",value = "{0}".format(uid), inline=False)
    embed.add_field(name = "Joined:",value="{0}".format(joined), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)
    
@client.command(pass_context=True)
async def slap(ctx, userName: discord.User):
    embed = discord.Embed(title = "Wow", color = 0x000000)
    embed.add_field(name = "{0} slapped".format(ctx.message.author.display_name), value = "@{0}".format(userName), inline=False)
    embed.set_image(url = random.choice([
        "https://cdn.discordapp.com/attachments/526206250363519016/529497927924580373/Witch-slap-umineko-no-naku-koro-ni-32769184-300-170.gif",
        "https://cdn.discordapp.com/attachments/526206250363519016/529496839637041184/giphy.gif"]))
    await client.send_message(ctx.message.channel, "{0} slapped {1}".format(ctx.message.author.mention, userName), embed=embed)
                                  
@client.command(pass_context=True)
async def hug(ctx, userName: discord.User):
    embed = discord.Embed(title = "Awww", color = 0x000000)
    embed.add_field(name = "{0} You got hug from".format(userName), value = "{0}".format(ctx.message.author.display_name), inline=False)
    embed.set_image(url = random.choice([
        "https://cdn.discordapp.com/attachments/526206250363519016/529497926557499403/r9aU2xv.gif",
        "https://cdn.discordapp.com/attachments/526206250363519016/529497926024560680/tenor.gif"]))
    await client.send_message(ctx.message.channel, "{0} Got hug from {1}!".format(userName, ctx.message.author.display_name), embed=embed)
       
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.User):
    embed = discord.Embed(title = "Awww", color = 0x000000)
    embed.add_field(name = "{0} You got kiss from".format(userName), value = "{0}".format(ctx.message.author.display_name), inline=False)
    embed.set_image(url = random.choice([
        "https://cdn.discordapp.com/attachments/526206250363519016/529497927417200650/original.gif",
        "https://cdn.discordapp.com/attachments/526206250363519016/529497926557499402/3ec77ac0e01df5f57623d8ce140a6de80720d598_00.gif",
        "https://cdn.discordapp.com/attachments/526206250363519016/529497925152276513/eKcWCgS.gif"]))
    await client.send_message(ctx.message.channel, "{0} You got kiss from {1} <3!".format(userName, ctx.message.author.display_name), embed=embed)
    
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
