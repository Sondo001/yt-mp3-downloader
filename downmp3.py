import yt_dlp

print("Nhập nhiều link (mỗi link 1 dòng, Enter 2 lần để chạy):")

urls = []
while True:
    line = input()
    if line == "":
        break
    urls.append(line.strip())

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

print("Tải MP3 hàng loạt hoàn tất!")