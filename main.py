import random
import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='`')
client = discord.Client()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    ''''
    sendMsg = True
    if sendMsg == True:
        channel = client.get_channel(787215182572027957)
        await channel.channel.send("I home now, you doing da study lah???!!??!?")
        sendMsg = False
    '''
    if message.content.startswith('are you proud of me'):
        await message.channel.send("no")
    if message.content.startswith('mum') and not " " in message.content:
        await message.channel.send("yes?")
    if message.content.startswith('am i'):
        await message.channel.send("yes... yes you are")

    if "fuck" in message.content or "FUCK" in message.content or "shit" in message.content or "SHIT" in message.content:
        await message.channel.send(
            "mmM?! What did I just hear?! WHO made your tounge dirty?! Do I need to wash your tounge out with soap hmmMM??!!"
        )

    if "pog" in message.content or "poggers" in message.content or "POG" in message.content or "POGGERS" in message.content or "lol" in message.content or "lmao" in message.content or "LMAO" in message.content or "idk" in message.content:
        await message.channel.send(
            "What is this word that you youth are using these days?! No wonder you aren't getting A's or A+, you can't even talk properly!"
        )

    if "anime" in message.content and not ("hate" in message.content
                                           or "dislike" in message.content):
        await message.channel.send(
            "and you ask me everyday why you can't get a girlfriend lah")
    if message.content.startswith('is'):
        await message.channel.send(
            "yea... you already know this get on with your work")

    if "want to be a" in message.content and not ("doctor" in message.content or "lawyer" in message.content or "surgeon" in message.content or "engineer" in message.content):
        await message.channel.send(
            "No. Thats a stupid career choice. You're a disappointment")

    if message.content.startswith("how big is") and "penis" in message.content:
        rNum = random.randint(1, 12)
        if rNum > 5:
            await message.channel.send("It is " + str(rNum) + " inches.")
        else:
            await message.channel.send("It is " + str(rNum) + " inches. Shame")

    if "failed" in message.content or "I got a A in my" in message.content:
      await message.channel.send("You didn't try hard enough. You dont get dinner, diss-apointments don't dinner.")


    if "minecraft" in message.content or "apex" in message.content or "r6" in message.content or "siege" in message.content or "video games" in message.content or "join vc" in message.content or "osu" in message.content:
        await message.channel.send(
            "STOP PLAYING VIDEO GAMES AND DO YOUR WORK! **I DONT SEND PAY FOR YOUR EDUCATION FOR NO REASON MMM K?!**"
        )

    if "australian" in message.content or "austraila" in message.content or "aussie" in message.content or "morning" in message.content:
        await message.channel.send("G'day Cunt")
  

keep_alive();
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
