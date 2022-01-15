# https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org

import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


walle_token = os.environ['walle_token']

call_walle = ["walle", "wall e", "WALLE", "WALL-E", "Walle", "Wall-e"]
respond_walle = ["WALL-E? WALL-E.", "Ta-Dah!", "Dirrrrr-ect-tivvve?", "EVA?"]

respond_8ball = [" It is certain.", "It is decidedly so.", "Without a doubt.", " Yes definitely.", " You may rely on it.", "As I see it, yes." "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", " Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]



@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is now online.')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.help'):
    await message.channel.send('Welcome to one of two Chat Bot for Discord, created by Andrea Ma and Martin Zhao using Python!')
    await message.channel.send('Current Commands are: ')
    await message.channel.send('https://tenor.com/view/wall-e-humans-lazy-eve-disney-gif-5471514')

  elif message.content.startswith('.hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith('.inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  elif message.content.startswith('.8ball'):
    await message.channel.send(random.choice(respond_8ball))

  elif any(word in message.content for word in call_walle): 
    await message.channel.send(random.choice(respond_walle))
    

    
    
keep_alive()
client.run(walle_token)

