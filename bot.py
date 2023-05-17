import os
from pyrogram import Client, filters
from yt_dl import song, video
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("yt_dl_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("song") & filters.private)
def song_handler(client, message):
    song(client, message)

@app.on_message(filters.private & filters.regex(r'^https?://(?:www\.)?youtu\.?be(?:\.com)?/.*$'))
def video_handler(client, message):
    video(client, message)

app.run()
