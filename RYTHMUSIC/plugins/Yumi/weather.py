from pyrogram import Client, filters
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/ALONE_xD_MUSIC_BOT?startgroup=true"),
    ],
]

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="✦ ʜᴇʀᴇ's ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ.\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ˹𝙻𝙾𝙵𝙸 ✗ 𝙼𝚄𝚂𝙸𝙲˼", reply_markup=InlineKeyboardMarkup(EVAA),)
    except IndexError:
        # User didn't provide a location
        message.reply_text("✦ Please provide a location. ♥︎ Use /weather NEW YORK")
        
