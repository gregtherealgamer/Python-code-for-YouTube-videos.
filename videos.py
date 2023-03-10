import youtube_dl

# set the URL of the video to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# create a YoutubeDL object
ydl = youtube_dl.YoutubeDL()

# set the options
opts = {
    "format": "bestaudio/best",
    "outtmpl": "video.%(ext)s",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }]
}

# download the video
ydl.download([url])
