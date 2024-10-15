from pyrogram import Client
import config

API_HASH = config.API_HASH
APP_ID = config.APP_ID
BOT_TOKEN = config.BOT_TOKEN


plugins = dict(root="plugins")


app = Client('uploader', 
             api_id=APP_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN, 
             plugins=plugins)
with app:
    print("Bot is online....")


app.run()