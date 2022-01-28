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
    clients = gnewsclient.NewsClient(language='english',location='world',topic='technology')
    news_list = clients.get_news()    
    for i in range(5):
      item=news_list[i]      
      await message.channel.send(item['link'])

  if message.content.startswith('/2'):
    clients = gnewsclient.NewsClient(language='english',location='world',topic='health')
    news_list = clients.get_news()    
    for i in range(5):
      item=news_list[i]      
      await message.channel.send(item['link'])

  if message.content.startswith('/3'):
    clientss = gnewsclient.NewsClient(language='english',  location='world',topic='entertainment')
    news_lists = clientss.get_news()   
    print(news_lists)
    for i in range(5):
      items=news_lists[i]        
      await message.channel.send(items['link'])    



my_secret = os.environ['token']
client.run(my_secret)

