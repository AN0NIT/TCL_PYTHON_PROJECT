import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_msg(message):
  if message.author == client.user:
    return

  if message.content.startswith('/news'):
    await message.channel.send('Hallo')

my_secret = os.environ['token']
client.run(my_secret)

