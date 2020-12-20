import os
import random
import time
from keep_alive import keep_alive       #To keep the bot running 24*7
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions, types
except:
    os.sysytem('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

list_bhati = ['bhati op', 'machaya bhati']
greetings = ['hi', 'hey', 'hello','hi!', 'hey!', 'hello!', 'heya']
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
id = os.getenv('id')
client = TelegramClient('tele', api_id, api_hash)
client.start()
@client.on(events.NewMessage(chats=os.getenv('Bansal'))) 

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bhai. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)               #Delays response time of bot to make conversations more natural
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.respond(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Saumil'))) 

async def my_event_handler(event):
    message = event.message.message
    dictb = {'sun' : 'bol', 'oye': 'bol','aur bta' : 'wahi same bhai. tu bta'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        for item in dictb.keys():
            if message.lower() == item:
                await event.reply(dictb[item])

@client.on(events.NewMessage(chats=os.getenv('Bhati')))

async def my_event_handler(event):
    message = event.message.message
    dictb = {'sun' : 'bol', 'oye': 'bol', 'kya kar raha hai': 'kuch nahi. bata'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        for item in dictb.keys():
            if message.lower() == item:
                await event.reply(dictb[item])

@client.on(events.NewMessage(chats=os.getenv('Me')))

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'tu bta', 'oye': 'bol','aur bta' : 'wahi same bhai. tu bta'}
    time.sleep(5)
    for x in list_bhati:
        if x == event.text.lower():
            await event.reply('Bhati always OP!')
        
    for y in greetings:
        if y == event.text.lower():
            await event.respond(random.choice(greetings).capitalize())
    
    for item in dicta.keys():
        if message.lower() == item:
            await event.reply(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Adit'))) 

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bhai. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.reply(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Tanishka'))) 

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bro. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.reply(dicta[item])
    
@client.on(events.NewMessage(chats=os.getenv('Akshay'))) 

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bhai. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.respond(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Anshu')))

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bro. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.respond(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Nandana')))

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bro. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.respond(dicta[item])

@client.on(events.NewMessage(chats=os.getenv('Shruti'))) #Shruti

async def my_event_handler(event):
    message = event.message.message
    dicta = {'aur bta' : 'wahi same bro. tu bta', 'oye': 'bol'}
    if event.message.from_id.user_id != id:
        time.sleep(5)
        for x in list_bhati:
            if x == event.text.lower():
                await event.reply('Bhati always OP!')
        
        for y in greetings:
            if y == event.text.lower():
                await event.respond(random.choice(greetings).capitalize())
        
        

        for item in dicta.keys():
            if message.lower() == item:
                await event.respond(dicta[item])

keep_alive()
client.run_until_disconnected()
