import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

app = Client("yt_dl_bot")

@app.on_callback_query()
def handle_callbacks(client, callback_query: CallbackQuery):
    query_data = callback_query.data

    if query_data == "song":
        # Handle song download
        client.send_message(callback_query.message.chat.id, "You selected: Download a Song")
    elif query_data == "video":
        # Handle video download
        client.send_message(callback_query.message.chat.id, "You selected: Download a Video")
    elif query_data == "help":
        # Handle help command
        client.send_message(callback_query.message.chat.id, "You selected: Help")
    elif query_data == "about":
        # Handle about command
        client.send_message(callback_query.message.chat.id, "You selected: About")

    # Answer the callback query to remove the "loading" state from the button
    callback_query.answer()

app.run()
