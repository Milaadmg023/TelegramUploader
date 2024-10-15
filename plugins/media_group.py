from pyrogram import Client, filters
from pyrogram.types import Message
import config
from modules import reply

admins = config.OWNERS_ID
TRACK_CHANNEL = config.TRACK_CHANNEL

# Store file
media_group_id = 0


@Client.on_message(filters.media & filters.private & filters.media_group & filters.user(admins))
async def _main_grop(client:Client, message:Message):
    global media_group_id
    if int(media_group_id) != int(message.media_group_id):
        media_group_id = message.media_group_id
        copied = (await client.copy_media_group(TRACK_CHANNEL, message.from_user.id, message.id))[0]
        await reply.__reply(message, copied)
    else:
        return


@Client.on_message(filters.media & filters.private & ~filters.media_group & filters.user(admins))
async def _main(client: Client, message: Message):
    copied = await message.copy(TRACK_CHANNEL)
    await reply.__reply(message, copied)