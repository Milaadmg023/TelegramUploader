from pyrogram import Client, filters
from pyrogram.types import Message
import config
from modules.db import DB
from helpers.join_check import join_check , join_msg


db = DB()
TRACK_CHANNEL = config.TRACK_CHANNEL


@Client.on_message(filters.command('start') & filters.private)
async def startfile(bot: Client, update: Message):
    userid = int(update.from_user.id)
    db.add_user(userid)
    join = await join_check(bot, update)
    if not join:
        await join_msg(bot, update)
        return
    if update.text == '/start':
        return
    if len(update.command) != 2:
        return
    code = update.command[1]
    if '-' in code:
        msg_id = code.split('-')[-1]
        unique_id = '-'.join(code.split('-')[0:-1])
        if not msg_id.isdigit():
            return
        try:
            check_media_group = await bot.get_media_group(TRACK_CHANNEL, int(msg_id))
            check = check_media_group[0] 
        except Exception:
            check = await bot.get_messages(TRACK_CHANNEL, int(msg_id))

        if check.empty:
            await update.reply_text('<b>⚠️فایل مورد نظر وجود ندارد</b>')
            return
        if check.video:
            unique_idx = check.video.file_unique_id
        elif check.photo:
            unique_idx = check.photo.file_unique_id
        elif check.audio:
            unique_idx = check.audio.file_unique_id
        elif check.document:
            unique_idx = check.document.file_unique_id
        elif check.sticker:
            unique_idx = check.sticker.file_unique_id
        elif check.animation:
            unique_idx = check.animation.file_unique_id
        elif check.voice:
            unique_idx = check.voice.file_unique_id
        elif check.video_note:
            unique_idx = check.video_note.file_unique_id
        if unique_id != unique_idx.lower():
            return
        try:
            await bot.copy_media_group(update.from_user.id, TRACK_CHANNEL, int(msg_id))
        except Exception:
            await check.copy(update.from_user.id)
    else:
        return