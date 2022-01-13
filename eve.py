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

secret_discord_token = os.environ['eve_token']

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is now online.')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('w.help'):
    await message.channel.send('Welcome to one of two Chat Bot for Discord, created by Andrea Ma and Martin Zhao using Python!')
    await message.channel.send('Current Commands are: ')
    await message.channel.send('https://tenor.com/view/wall-e-humans-lazy-eve-disney-gif-5471514')

  if message.content.startswith('w.hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith('w.inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(secret_discord_token)

