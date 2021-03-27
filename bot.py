#Thanks to @Anonymous_Machinee 😇

from vars import var
from pyrogram import  Client,filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

import logging
logging.basicConfig(level=logging.INFO)

Delevents = Client("Delete Events Bot",
                   api_id=var.API_ID,
                   api_hash=var.API_HASH,
                   bot_token=var.BOT_TOKEN
                   )

@Delevents.on_message(filters.service)
async def main(client , message):
    await message.delete()

    

@Delevents.on_message(filters.new_chat_members & filters.me)
async def greet(client,message):
    await message.reply_text("**Thanks for Adding me ⚡!\n\nMake me Admin with right of Deleting Messages.**")


@Delevents.on_message(filters.private & filters.command('start'))
async def pmfilter(client, message):
    me = await message._client.get_me()
    await message.reply_text( f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am Delete Service Messages bot, I can delete Service message. Just Add me in group as admin.⚡""",
                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="❤️ ADD Me ❤️",url=f"http://t.me/KeysDelEvents_bot?startgroup=true")]]),
                             quote=True)

@Delevents.on_message(filters.private & ~filters.command('start'))
async def okla(client,message):
    await message.reply_text("Hey Add Me to Group I am Delete Events Bot !!")


@Delevents.on_message(filters.group & filters.command('start'))
async def groupo(client,message):
    await message.reply_text("Hey, I am Alive",quote=True)

Delevents.run()
hm = Delevents.get_me()
print(f"{hm.username} Deployed Successfully !!")
print("done")
