import discord
import requests
import time 

jokeurl = "https://official-joke-api.appspot.com/random_joke"

bot = discord.Client()

print("Starting bot")

@bot.event
async def on_message(message):
    text = message.content
    if(text == "!joke"):
        response = requests.get(jokeurl)
        joke = response.json()
        await message.channel.send(joke["setup"])
        time.sleep(3)
        await message.channel.send(joke["punchline"])



bot.run("")