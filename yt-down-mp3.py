import yt_dlp
import re
import os

# ====== Làm sạch tên file ======
def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r'\s+', " ", name).strip()
    return name


# ====== Progress ======
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"\r{d.get('_percent_str','')} | {d.get('_speed_str','')} | ETA {d.get('_eta_str','')}", end="")
    elif d['status'] == 'finished':
        print("\nĐang xử lý file...")


# ====== Bitrate MP3 ======
def get_bitrate(choice):
    return {
        "1": "128",
        "2": "192",
        "3": "320"
    }.get(choice, "192")


# ====== Chất lượng video ======
def get_format_by_quality(choice):
    if choice == "1":
        return "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif choice == "2":
        return "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    elif choice == "3":
        return "bestvideo[height<=2160]+bestaudio/best"
    return "best"


# ====== Lấy playlist ======
def get_playlist_entries(url):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            return info['entries']
        return None


# ====== Download ======
def download(urls, mode, quality_choice=None, bitrate_choice=None):
    os.makedirs("downloads", exist_ok=True)

    base_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'quiet': True,
    }

    # Rename sạch
    def clean_filename_hook(d):
        if d['status'] == 'finished':
            filename = d['filename']
            folder, file = os.path.split(filename)
            clean_name = sanitize_filename(file)
            new_path = os.path.join(folder, clean_name)
            if filename != new_path:
                os.rename(filename, new_path)

    base_opts['progress_hooks'].append(clean_filename_hook)

    # ===== MP3 =====
    if mode == "1":
        bitrate = get_bitrate(bitrate_choice)

        ydl_opts = {
            **base_opts,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': bitrate,
            }],
        }

    # ===== MP4 =====
    else:
        ydl_opts = {
            **base_opts,
            'format': get_format_by_quality(quality_choice),
            'merge_output_format': 'mp4',
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


# ====== MAIN ======
print("=== YouTube Downloader ===")
print("1. MP3")
print("2. MP4")
mode = input("Chọn (1/2): ").strip()

quality_choice = None
bitrate_choice = None

# ===== Chọn bitrate =====
if mode == "1":
    print("\nChọn bitrate MP3:")
    print("1. 128 kbps")
    print("2. 192 kbps")
    print("3. 320 kbps")
    bitrate_choice = input("Chọn (1/2/3): ").strip()

# ===== Chọn chất lượng video =====
elif mode == "2":
    print("\nChọn chất lượng video:")
    print("1. 720p")
    print("2. 1080p")
    print("3. 4K")
    quality_choice = input("Chọn (1/2/3): ").strip()

# ===== Nhập link =====
print("\nNhập link (có thể nhiều link, mỗi link 1 dòng - Enter trống để chạy):")

urls = []
while True:
    line = input()
    if line == "":
        break
    urls.append(line.strip())

if not urls:
    print("Không có link!")
    exit()

final_urls = []

# ===== Xử lý playlist =====
for url in urls:
    entries = get_playlist_entries(url)

    if entries:
        print(f"\n📂 Playlist phát hiện ({len(entries)} video)")
        print("1. Tải toàn bộ")
        print("2. Chọn từng video")

        choice = input("Chọn (1/2): ").strip()

        if choice == "1":
            final_urls.append(url)
        else:
            for i, video in enumerate(entries):
                print(f"{i+1}. {video.get('title')}")

            selected = input("\nNhập số (vd: 1,3,5): ")
            indexes = [int(x.strip()) - 1 for x in selected.split(",")]

            selected_urls = [
                entries[i]['webpage_url']
                for i in indexes if i < len(entries)
            ]

            final_urls.extend(selected_urls)

    else:
        final_urls.append(url)

# ===== Tải =====
download(final_urls, mode, quality_choice, bitrate_choice)

print("\n🎉 Tải xong toàn bộ!")
