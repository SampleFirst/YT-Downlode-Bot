import os
from pyrogram import Client, filters
from youtube_dl import YoutubeDL

app = Client("yt_dl_bot")

@app.on_message(filters.command("song") & filters.private)
def song(client, message):
    query = ' '.join(message.command[1:])
    if not query:
        client.send_message(chat_id=message.chat.id, text="Please provide a song name to search.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(os.getcwd(), 'downloads', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            search_results = ydl.extract_info(f"ytsearch1:{query}", download=False)['entries']
            if len(search_results) > 0:
                first_result = search_results[0]
                title = first_result['title']
                url = first_result['webpage_url']
                client.send_message(chat_id=message.chat.id, text=f"Downloading: {title}\nURL: {url}")
                ydl.download([url])
                client.send_audio(chat_id=message.chat.id, audio=f"{title}.mp3")
            else:
                client.send_message(chat_id=message.chat.id, text="No search results found.")
        except Exception as e:
            client.send_message(chat_id=message.chat.id, text=f"An error occurred: {str(e)}")

@app.on_message(filters.private & filters.regex(r'^https?://(?:www\.)?youtu\.?be(?:\.com)?/.*$'))
def video(client, message):
    url = message.text

    ydl_opts = {
        'outtmpl': os.path.join(os.getcwd(), 'downloads', '%(title)s.%(ext)s')
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            title = info['title']
            client.send_message(chat_id=message.chat.id, text=f"Downloading: {title}\nURL: {url}")
            ydl.download([url])
            client.send_video(chat_id=message.chat.id, video=f"{title}.{info['ext']}")
        except Exception as e:
            client.send_message(chat_id=message.chat.id, text=f"An error occurred: {str(e)}")

app.run()
