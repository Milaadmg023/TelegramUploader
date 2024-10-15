import asyncio
import config

bot_id = config.BOT_ID

async def reply(message, copied):
    msg_id = copied.id
    media_types = [copied.video, copied.photo, copied.audio, copied.document, copied.sticker, copied.animation, copied.voice, copied.video_note]
    for media_type in media_types:
        if media_type:
            unique_idx = media_type.file_unique_id
            break
    await message.reply_text(
        '**لینک اشتراک فایل شما:\n\n**'f"`https://t.me/{bot_id}?start={unique_idx.lower()}-{str(msg_id)}`",True,
    )
    await asyncio.sleep(0.5)