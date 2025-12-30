from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DEVA import app
from config import BOT_USERNAME

repo_caption = """**
✪ 𝐊𝐇𝐔𝐃 𝐁𝐀𝐍𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 ✪
 
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/medevu"),
            InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/BotzEmpire")
        ],
        [
            InlineKeyboardButton("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Yaaro_kimehfill"),
            InlineKeyboardButton("𝐌ᴀ꯭ᴛ꯭ʟ꯭ᴀ꯭ʙ꯭ɪ꯭ 𝗗꯭ᴜ꯭ɴ꯭ɪ꯭ʏ꯭ᴀ꯭", url="https://t.me/Matlabi_Duniyah")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    try:
        await msg.reply_photo(
            photo="https://files.catbox.moe/lp5sel.jpg",
            caption=repo_caption,
            reply_markup=reply_markup
        )
    except:
        pass
