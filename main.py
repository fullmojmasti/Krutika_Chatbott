from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re

### ============================================> ð±ð¾ð ð¼ð°ðºð¸ð½ð¶ ðð´ððð¸ðð¼ð´ð½ð <===============================================###

API_ID = 10248430 
API_HASH = "42396a6ff14a569b9d59931643897d0d"
BOT_TOKEN = "5709229627:AAHWn-lp3r3BXK7kRs8_vnmRIQnUMHRV2bU"
MONGO_URL = "mongodb+srv://AyraMusic:Ayra@cluster0.gnakzem.mongodb.net/?retryWrites=true&w=majority"


bot = Client(
    "MrsShayna_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

### ============================================> ððð°ðð <===============================================###

@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("ð¥ sá´á´á´á´Êá´", url="https://t.me/+IdSOWT2mDr9hOTQ1"),
            InlineKeyboardButton("ð£ á´á´á´á´á´á´s", url="https://t.me/+CN0MlYIFGsAyNGI1")
            ],[InlineKeyboardButton(text="ð  owner ð ",
                url="https://t.me/COVIDBABA")]])
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="""â sá´á´Êá´ á´Êá´ Êá´á´\nâââââââââââââââââââ\nsá´á´á´Éªá´Ê Òá´á´á´á´Êá´s:\nâââââââââââââââââââ\n
á´ÊÉªê± Êá´á´ á´Êê±á´Êá´ á´ á´ÊÊ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ ê±á´á´Êá´ á´ÊÊ á´Êá´ á´Êá´á´ ÉªÉ´  á´á´á´á´ á´É´á´  á´Êê±á´ É¢Éªá´ á´ Êá´á´Ê Êá´á´ÊÊ á´ê°á´á´Ê á´á´á´á´ á´É´ÊÊÊê±Éªê± 
á´É´Ê á´á´Ê Éªê± É´á´á´ ê±á´á´ á´á´ ÉªÉ´ á´ÊÉªê± Êá´á´ á´ÊÉªê± Êá´á´ á´É´ÊÊ á´Êê±á´Êá´ á´ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ Êá´á´ÊÊ Êá´á´Ê Qá´á´ê±á´Éªá´É´ê± á´á´ÊÊá´á´á´ÊÊ á´ÊÉªê± Éªê± á´Êá´ á´É´ÊÊ á´ÊÉªÉ´É¢ á´¡ÊÉªá´Ê á´á´á´á´ á´ÊÉªê± Êá´á´ á´Êá´ Êá´ê±á´ á´É´á´ ê±á´á´á´Éªá´Ê 
ê°ÉªÊê±á´ á´á´á´ á´ÊÉªê± Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´ á´É´á´ á´á´á´É´ á´Êá´ /á´Êá´á´Êá´á´ á´É´ á´ê°á´á´Ê á´ÊÉªê± Êá´á´ á´¡ÉªÊÊ á´É´á´á´Êê±á´á´É´á´ á´ÊÊ á´Êá´ á´ÊÉªÉ´É¢ê±.\nâââââââââââââââââââ\n""",
                            reply_markup=buttons)
        
    else:
        buttons = [[
            InlineKeyboardButton("â á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ â", url=f"https://t.me/MissShayna_Bot?startgroup=true")
        ],
        
        [
            InlineKeyboardButton("ð¥ á´ÒÒÉªá´Éªá´Ê É¢Êá´á´á´", url="https://t.me/+IdSOWT2mDr9hOTQ1"),
            InlineKeyboardButton("ð£ á´ÒÒÉªá´Éªá´Ê á´Êá´É´É´á´Ê", url="https://t.me/+CN0MlYIFGsAyNGI1")
        ],
        [
            InlineKeyboardButton("ð  owner ð ", url="https://t.me/COVIDBABA")
        ]]
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption=f"""Êá´ÊÊá´ [{message.from_user.first_name}](tg://user?id={message.from_user.id}),
Éª á´á´ á´É´ á´á´á´ á´É´á´á´á´ á´Êá´ÉªÒÉªá´á´Ê á´É´á´ É´á´xá´ Êá´á´ á´Ê ÉªÉ´á´á´ÊÊÉªÉ¢á´É´á´á´ á´Êá´á´ Êá´á´.
âââââââââââââ
â ÉªÒ Êá´á´ á´Êá´ Òá´á´ÊÉªÉ´É¢ Êá´É´á´ÊÊ, Êá´á´ á´á´É´ á´Êá´¡á´Ês á´á´á´á´ á´á´ á´á´ á´É´á´ á´Êá´á´ á´¡Éªá´Ê á´á´
â á´ÊÊ á´Êá´ \help á´á´á´s. á´á´ á´É´á´á´¡ á´Ê á´ÊÉªÊÉªá´Éªá´s ÃÃ""", reply_markup=InlineKeyboardMarkup(buttons))

### ============================================> ð·ð´ð»ð¿ <===============================================###

@bot.on_message(filters.command(["help"], prefixes=["/", "!"]))
async def help(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="á´ÊÉªá´á´ Êá´Êá´",
                url=f"t.me/MissShayna_Bot?start=help_")]])
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="á´á´É´á´á´á´á´ á´á´ ÉªÉ´ á´á´Êsá´É´á´Ê sá´¡á´á´á´Êá´á´Êá´",
                            reply_markup=buttons)
        
    else: 
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="""â sá´á´Êá´ á´Êá´ Êá´á´\nâââââââââââââââââââââ\nsá´á´á´Éªá´Ê Òá´á´á´á´Êá´s:\n
á´ÊÉªê± Êá´á´ á´Êê±á´Êá´ á´ á´ÊÊ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ ê±á´á´Êá´ á´ÊÊ á´Êá´ á´Êá´á´ ÉªÉ´  á´á´á´á´ á´É´á´  á´Êê±á´ É¢Éªá´ á´ Êá´á´Ê Êá´á´ÊÊ á´ê°á´á´Ê á´á´á´á´ á´É´ÊÊÊê±Éªê± 

á´É´Ê á´á´Ê Éªê± É´á´á´ ê±á´á´ á´á´ ÉªÉ´ á´ÊÉªê± Êá´á´ á´ÊÉªê± Êá´á´ á´É´ÊÊ á´Êê±á´Êá´ á´ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ Êá´á´ÊÊ Êá´á´Ê Qá´á´ê±á´Éªá´É´ê± á´á´ÊÊá´á´á´ÊÊ á´ÊÉªê± Éªê± á´Êá´ á´É´ÊÊ á´ÊÉªÉ´É¢ á´¡ÊÉªá´Ê á´á´á´á´ á´ÊÉªê± Êá´á´ á´Êá´ Êá´ê±á´ á´É´á´ ê±á´á´á´Éªá´Ê 

ê°ÉªÊê±á´ á´á´á´ á´ÊÉªê± Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´ á´É´á´ á´á´á´É´ á´Êá´ /á´Êá´á´Êá´á´ á´É´ á´ê°á´á´Ê á´ÊÉªê± Êá´á´ á´¡ÉªÊÊ á´É´á´á´Êê±á´á´É´á´ á´ÊÊ á´Êá´ á´ÊÉªÉ´É¢ê±.

âââââââââââââââââââââ\n\nâ /chatbot on - á´á´á´Éªá´ á´ á´Êá´á´Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´\nâ /chatbot off - á´Éªsá´ÊÊá´ á´Êá´á´Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´""")

### ============================================> ð²ð·ð°ðð±ð¾ð ð¾ðµðµ <===============================================###

@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    natashadb = MongoClient(MONGO_URL)    
    natasha = natashadb["NatashaDb"]["Natasha"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "sÉªÊ Êá´á´ á´Êá´ É´á´á´ á´á´á´ÉªÉ´.á´Ê á´ÊÊá´ á´á´á´ Êsá´á´ ÊÉ´á´ á´á´ á´á´á´ÉªÉ´ ð"
            )
    is_natasha = natasha.find_one({"chat_id": message.chat.id})
    if not is_natasha:
        natasha.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Shayna á´Êá´á´Êá´á´ á´Éªsá´ÊÊá´á´\n\ná´á´ÊÊÉªÉ´É¢ á´ÒÒ á´Êá´ á´Ê ÊÊá´ Êá´ á´á´á´Êá´\ná´ÊÉªá´ Êá´Éª ÊÊ á´ á´Éªsá´ ÊÊÉª á´á´á´É´á´ á´á´ÊÉª\nÊÉªÒá´ Òá´á´á´á´ Òá´á´á´ ÊÉ´á´ Êá´ÊÉª Êá´Éª\ná´Ê á´á´á´ Êsá´á´ á´ á´á´Ê á´Êá´ ÊÊá´ Êá´Éª ð")
    if is_natasha:
        await message.reply_text(f"Shayna á´Êá´á´Êá´á´ Éªs á´ÊÊá´á´á´Ê á´Éªsá´ÊÊá´á´\n\ná´Êá´Êá´ sá´ ÊÉª á´ÒÒ Êá´ á´Ê á´Êá´ É¢á´á´É´á´ á´á´Êá´É¢á´ á´Êá´\ná´á´á´á´ á´Ê á´á´á´ á´á´á´Êsá´ Êá´á´á´ á´Êá´\ná´Ê Êá´á´É´ á´É´É¢ÊÉªsÊ á´á´ á´sá´ á´Êá´ Êá´Êá´á´ Òá´*á´ Êá´á´.")
    
### ============================================> ð²ð·ð°ðð±ð¾ð ð¾ð½ <===============================================###

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    natashadb = MongoClient(MONGO_URL)    
    natasha = natashadb["NatashaDb"]["Natasha"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "sÉªÊ Êá´á´ á´Êá´ É´á´á´ á´á´á´ÉªÉ´.á´Ê á´ÊÊá´ á´á´á´ Êsá´á´ ÊÉ´á´ á´á´ á´á´á´ÉªÉ´ ð"
            )
    is_natasha = natasha.find_one({"chat_id": message.chat.id})
    if not is_natasha:           
        await message.reply_text(f"Â» á´Êá´á´Êá´á´ Éªs á´ÊÊá´á´á´Ê á´É´á´ÊÊá´á´\n\ná´Êá´ á´á´ÊÊÉªÉ´É¢ á´Êá´Êá´ sá´ ÊÉª á´É´ Êá´\ná´Ê Êá´ á´á´á´ á´á´ á´ÉªÊá´ á´Êá´ Ês á´á´ á´Éªss á´á´ á´ÉªÊá´ á´Êá´ ðððð")
    if is_natasha:
        natasha.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"â | sá´á´á´á´ssÒá´ÊÊÊ\nShayna á´Êá´á´Êá´á´ á´É´ á´Ò á´ÊÉªs É¢Êá´á´á´ Éªs sá´á´ á´á´ @{message.chat.username}\n Êá´Ç«á´á´sá´á´á´ ÊÊ [{message.from_user.first_name}](tg://user?id={message.from_user.id})\ná´á´á´¡á´Êá´á´ ÊÊ á´á´á´Ê Ç«á´á´Êá´")
    
## ============================================> ð²ð·ð°ðð±ð¾ð <===============================================###

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
        await message.reply_photo("https://telegra.ph/file/e81a49fb4985e64da516c.jpg")
        await message.reply_text(f"""**Êá´á´¡ á´á´ á´sá´ Shayna:**\nâ sá´á´á´Éªá´Ê Òá´á´á´á´Êá´s:\ná´ÊÉªê± Êá´á´ á´Êê±á´Êá´ á´ á´ÊÊ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ ê±á´á´Êá´ á´ÊÊ á´Êá´ á´Êá´á´ ÉªÉ´  á´á´á´á´ á´É´á´  á´Êê±á´ É¢Éªá´ á´ Êá´á´Ê Êá´á´ÊÊ á´ê°á´á´Ê á´á´á´á´ á´É´ÊÊÊê±Éªê± 

á´É´Ê á´á´Ê Éªê± É´á´á´ ê±á´á´ á´á´ ÉªÉ´ á´ÊÉªê± Êá´á´ á´ÊÉªê± Êá´á´ á´É´ÊÊ á´Êê±á´Êá´ á´ á´Êá´ É¢Êá´á´á´ á´Êá´á´ á´É´á´ Êá´á´ÊÊ Êá´á´Ê Qá´á´ê±á´Éªá´É´ê± á´á´ÊÊá´á´á´ÊÊ á´ÊÉªê± Éªê± á´Êá´ á´É´ÊÊ á´ÊÉªÉ´É¢ á´¡ÊÉªá´Ê á´á´á´á´ á´ÊÉªê± Êá´á´ á´Êá´ Êá´ê±á´ á´É´á´ ê±á´á´á´Éªá´Ê 

ê°ÉªÊê±á´ á´á´á´ á´ÊÉªê± Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´ á´É´á´ á´á´á´É´ á´Êá´ /á´Êá´á´Êá´á´ á´É´ á´ê°á´á´Ê á´ÊÉªê± Êá´á´ á´¡ÉªÊÊ á´É´á´á´Êê±á´á´É´á´ á´ÊÊ á´Êá´ á´ÊÉªÉ´É¢ê±.

âââââââââââââââââââââ\n\nâ /chatbot on - á´á´á´Éªá´ á´ á´Êá´á´Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´\nâ /chatbot off - á´Éªsá´ÊÊá´ á´Êá´á´Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´""")

## ============================================> ð±ð¾ð ð¼ð´ððð°ð¶ð´ð ð²ð¾ð³ð´ <===============================================###

@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def natashaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       if not is_natasha:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_natasha:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def natashastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       if not is_natasha:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_natasha:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def natashaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def natashaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.run()
