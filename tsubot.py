"""
Asoo Azad
TsuBot
Discord Bot
"""
import random
import time
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import datetime
print(discord.__version__)


Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.content.lower() == "cookie":
      await message.channel.send(":cookie:")
    elif message.content.lower() == "ok":
            await message.channel.send(":ok_hand:")
    elif message.content.lower() == "love":
            await message.channel.send(":heart:")
    elif message.content.lower() == "kys":
            await message.channel.send(":gun:")
    elif message.content.lower() == "bye":
            await message.channel.send(":wave:")

    # commands

    if message.content.startswith("$hello"):
            await message.channel.send("hello, how are you?")
            await message.channel.send('https://gph.is/1JksT3z')
    elif message.content.startswith("$friend"):
            await message.channel.send("Yes, :3")
    elif message.content.startswith("$love"):
            await message.channel.send("i love you <3")
    elif message.content.startswith("$noob"):
            await message.channel.send("you are noobs!")
    elif message.content.startswith("$hate"):
            await message.channel.send("i hate you :angry:")
    elif message.content.startswith("$commands"):
            await message.channel.send("`Commands:`" "\n" "`$hello`" "\n" "`$friend`" "\n" "`$love`" "\n" "`$noob`" "\n" "`$hate`"  "\n" "`$magicball`")

    # warnings

    if message.content.startswith("!spamwarn"):
           await message.channel.send(":ok_hand: STOP SPAMMING")
    elif message.content.startswith("!firstwarn"):
            await message.channel.send(":ok_hand: First warning")
    elif message.content.startswith("!finalwarning"):
            await message.channel.send(":ok_hand: Last warning! One more time and its a ban! :angry:")

    if message.content.startswith("$magicball"):
            ball8 = random.choice(
             ['It is certain', 'As i see it, yes', 'Dont count on it', 'Without a doubt', 'Definitely', 'Very doubtful', 'Outlook not so good', 'My sources say no', 'My reply is no', 'Most likely', 'You may rely on it',
             ])
            await message.channel.send(ball8)

   # welcome

    if message.content.startswith("welcome"):
           await message.channel.send('Working')
           await message.channel.send('https://media1.giphy.com/media/yyVph7ANKftIs/giphy.gif')

   # Time

    if message.content.startswith("!time"):
            t = datetime.datetime.now()
            embed=discord.Embed(title="Time", colour = random.randint(0, 0xFFFFFF))
            embed.add_field(name = "GMT + 1 (Ireland)", value=t.strftime('%H:%M:%S %p'), inline=False)
            embed.set_thumbnail(url = 'https://i.imgur.com/SSWPDvX.gif')
            embed.set_footer(text="Msg for help")
            await message.channel.send(embed=embed)

    


        








client.run('')
