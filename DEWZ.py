import os
import discord
from gnewsclient import gnewsclient


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  
  if message.content.startswith('/news'):
    await message.channel.send('which type of news would u prefer :1.tech&sci, 2.health&sports, 3.film&music [include / and numer of the topic]')
   
  if message.content.startswith('/1'):
    clients = gnewsclient.NewsClient(language='english',location='world',topic='technology and science')
    news_list = clients.get_news()
    #print(news_list)
    for i in range(5):
      item=news_list[i]
      #msg=str(item['title'],item['link'])  
      await message.channel.send(item['link'])
      



my_secret = os.environ['token']
client.run(my_secret)

