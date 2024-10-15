from modules.db import DB
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup
from pyrogram import Client

db = DB()

async def join_check(client: Client, message: Message):
     userid = message.from_user.id
     chats_id = db.get_chat_id()
     if len(chats_id) == 0:
          return True
     for chat_id in chats_id:
          try:
               await client.get_chat_member(chat_id[0], userid)
          except Exception:
               return False
     return True


async def join_msg(client: Client, message: Message):
     chats_link = db.get_chat_link()
     btns = []
     for chat_link in chats_link:
          btns.append([InlineKeyboardButton("🔗Join", url=chat_link[0])])
     reply_markup = InlineKeyboardMarkup(btns)
     await message.reply("<b>⚠️برای استفاده از امکانات ربات ابتدا عضو کانال های زیر شوید.</b>", reply_markup=reply_markup)