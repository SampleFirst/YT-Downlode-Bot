from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Client("yt_dl_bot")

@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    keyboard = [
        [
            InlineKeyboardButton("Download a Song", callback_data="song"),
            InlineKeyboardButton("Download a Video", callback_data="video")
        ],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    client.send_photo(
        chat_id=message.chat.id,
        photo="https://example.com/start_pic.jpg",
        caption="Welcome to the YouTube Downloader Bot!\n\n"
        "You can use this bot to download songs and videos from YouTube.\n"
        "Click on the buttons below to get started.",
        reply_markup=reply_markup
    )

app.run()
