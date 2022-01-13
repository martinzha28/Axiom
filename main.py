# https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org

import discord
import os
import requests
import json

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

secret_discord_token = os.environ['discord_token']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)


  elif message.content.startswith('$love'):
    await message.channel.send('https://tenor.com/view/hugs-love-heart-i-love-you-gif-15419493')

  elif message.content.startswith('$emoji'):
    await message.channel.send('Testing emoji: :thinking:')

  elif message.content.startswith('$discordstyles'):
    await message.channel.send('*italics* **bold** ***bold italics*** __underline__')
    await message.channel.send('`one line code`')

client.run(secret_discord_token)

