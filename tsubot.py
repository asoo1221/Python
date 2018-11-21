"""
Asoo Azad
TsuBot
Discord Bot
"""
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready() :
    print("Bot is ready")


@client.event
async def on_message(message):
        if message.content.lower() == "cookie":
            await client.send_message(message.channel, ":cookie:")
        elif message.content.lower() == "ok":
            await client.send_message(message.channel, ":ok_hand:")
        elif message.content.lower() == "love":
            await client.send_message(message.channel, ":heart:")
        elif message.content.lower() == "kys":
            await client.send_message(message.channel, ":gun:")
        elif message.content.lower() == "bye":
            await client.send_message(message.channel, ":wave:")

        # commands

        if  message.content.startswith("$hello"):
            await client.send_message(message.channel, "`hello, how are you?`")
        elif message.content.startswith("$friend"):
            await client.send_message(message.channel, "`Yes, :3`")
        elif message.content.startswith("$love"):
            await client.send_message(message.channel, "`i love you <3`")
        elif message.content.startswith("$noob"):
            await client.send_message(message.channel, "` you are noobs!`")
        elif message.content.startswith("$hate"):
            await client.send_message(message.channel, "i hate you :angry:")
        elif message.content.startswith("$commands"):
            await client.send_message(message.channel, "`Commands:`" "\n" "`$hello`" "\n" "`$friend`" "\n" "`$love`" "\n" "`$noob`" "\n" "`$hate`"  "\n" "`$magicball`" )

        # warnings
        if message.content.startswith("!spamwarn"):
            await client.send_message(message.channel, ":ok_hand: STOP SPAMMING")
        elif message.content.startswith("!firstwarn"):
            await client.send_message(message.channel, ":ok_hand: First warning")
        elif message.content.startswith("!finalwarning"):
            await client.send_message(message.channel, ":ok_hand: Last warning! One more time and its a ban! :angry:")

        chatFilter = ['fuck', 'shit', 'piss', 'nigger', 'Kai' , 'Chai']
            # messageWords = message.content.split(" ")
        if message.content.startswith("$magicball"):
            ball8 = random.choice(
             ['It is certain', 'As i see it, yes', 'Dont count on it', 'Without a doubt', 'Definitely', 'Very doubtful','Outlook not so good', 'My sources say no', 'My reply is no', 'Most likely', 'You may rely on it',
             ])
            await client.send_message(message.channel, ball8)







client.run("NDk2NDI1OTk1MzkwMjg3ODgy.DpQcXg.zMOqOJPZS94mPbOI90OSCFavbPM")
