import asyncio
import config

bot_id = config.BOT_ID


async def __reply(update, copied):
    msg_id = copied.id
    if copied.video:
        unique_idx = copied.video.file_unique_id
    elif copied.photo:
        unique_idx = copied.photo.file_unique_id
    elif copied.audio:
        unique_idx = copied.audio.file_unique_id
    elif copied.document:
        unique_idx = copied.document.file_unique_id
    elif copied.sticker:
        unique_idx = copied.sticker.file_unique_id
    elif copied.animation:
        unique_idx = copied.animation.file_unique_id
    elif copied.voice:
        unique_idx = copied.voice.file_unique_id
    elif copied.video_note:
        unique_idx = copied.video_note.file_unique_id
    else:
        await copied.delete()
        return

    await update.reply_text(
        f"**لینک اشتراک فایل شما:\n\n<code>https://t.me/{bot_id}?start={unique_idx.lower()}-{str(msg_id)}</code>**",
        True,
    )
    await asyncio.sleep(0.5)  # Wait do to avoid 5 sec flood ban
