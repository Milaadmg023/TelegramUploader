from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import config
from modules.db import DB
import asyncio

db = DB()
track_channel = config.TRACK_CHANNEL
admins = config.OWNERS_ID
admin_btns = [
    [
        InlineKeyboardButton("جوین اجباری", callback_data="required"),
        InlineKeyboardButton("آمار ربات", callback_data="bot_stats"),
    ],
    [
        InlineKeyboardButton("پیام همگانی", callback_data="all_msg"),
        InlineKeyboardButton("بک آپ", callback_data="backup"),
    ]
]


@Client.on_message(filters.command("admin") & filters.user(admins))
async def admin(client: Client, message: Message):
    await message.reply("Please choose:", reply_markup=InlineKeyboardMarkup(admin_btns))


@Client.on_callback_query(filters.regex("required"))
async def required(client: Client, query: CallbackQuery):
    chats = db.get_chats()
    if len(chats) == 0 or not chats:
        await query.message.reply("No chats found" , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Add", callback_data="add_chat")]]))
        return
    msg = ""
    for chat in chats:
        msg += f"ID: {chat[0]}\nLink: {chat[1]}\n\n"
    await query.message.reply(msg, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Add", callback_data="add_chat")]]) , disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("bot_stats"))
async def bot_stats(client: Client, query: CallbackQuery):
    stats = db.get_users()
    await query.message.reply(f"Total users: {len(stats)}")


@Client.on_callback_query(filters.regex("all_msg"))
async def all_msg(client: Client, query: CallbackQuery):
    await query.message.reply("پیام خود را وارد نمایید.\n\nفرمت : Msg-text")


@Client.on_callback_query(filters.regex("add_chat"))
async def add_chat(client: Client, query: CallbackQuery):
    await query.message.reply("لینک و آیدی عددی کانال مورد نظر را وارد کنید.\n\nفرمت : Chat-id-link")


@Client.on_message(filters.user(admins) &( filters.regex("Msg-") | filters.regex("Chat-")) )
async def admin_msg(client: Client, message: Message):
    msg = message.text.split("-")
    if len(msg) == 2:
        users = db.get_users()
        if len(users) == 0 or not users:
            await message.reply("No users found")
            return
        for user in users:
            try:
                await client.send_message(user[0], msg[1])
            except Exception as e:
                await client.send_message(track_channel, f"Error: {e}")
                pass
        await message.reply("Done")
    elif len(msg) == 3:
        chat_id = f"-100{msg[1]}"
        db.add_chat(int(chat_id), msg[2])
        await message.reply("Done")


@Client.on_callback_query(filters.regex("backup"))
async def backup(client: Client, query: CallbackQuery):
    await query.message.reply_document("database.db")