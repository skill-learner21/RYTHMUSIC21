from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ ˹𝙻𝙾𝙵𝙸 ✗ 𝙼𝚄𝚂𝙸𝙲˼

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹𝙻𝙾𝙵𝙸 ✗ 𝙼𝚄𝚂𝙸𝙲˼ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/TitanXSupport"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/Want_To_Know_Mee"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/829d73d62e52f5d945f2e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
