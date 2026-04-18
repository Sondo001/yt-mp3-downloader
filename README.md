# 🎵 YouTube to MP3 Downloader (Python)

Ứng dụng Python giúp tải video từ YouTube và tự động chuyển đổi sang định dạng MP3.
Hỗ trợ tải nhiều link cùng lúc, nhanh và dễ sử dụng.

---

## 🚀 Tính năng

* Tải audio chất lượng cao từ YouTube
* Tự động chuyển sang MP3 (192kbps hoặc 320kbps)
* Hỗ trợ nhập **nhiều link cùng lúc**
* Có thể đọc danh sách link từ file `.txt`
* Lưu file theo tiêu đề video

---

## 🛠️ Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/sondo001/youtube-mp3-downloader.git
cd youtube-mp3-downloader
```

### 2. Cài thư viện cần thiết

```bash
pip install yt-dlp
```

### 3. Cài FFmpeg (bắt buộc để convert MP3)

* Windows: tải FFmpeg và thêm vào PATH
* Linux:

```bash
sudo apt install ffmpeg
```

---

## ▶️ Cách sử dụng

### Cách 1: Nhập nhiều link (phân cách bằng dấu phẩy)

```bash
python main.py
```

Ví dụ:

```
https://youtube.com/xxx, https://youtube.com/yyy
```

---

### Cách 2: Nhập nhiều dòng

* Dán mỗi link một dòng
* Nhấn Enter 2 lần để bắt đầu tải

---

### Cách 3: Dùng file links.txt

Tạo file `links.txt`:

```
https://youtube.com/xxx
https://youtube.com/yyy
https://youtube.com/zzz
```

Chạy:

```bash
python main.py
```

---

## 📁 Cấu trúc thư mục

```
youtube-mp3-downloader/
│── main.py
│── links.txt (tuỳ chọn)
│── downloads/
│── README.md
```

---

## ⚙️ Cấu hình

Bạn có thể chỉnh chất lượng MP3 trong code:

```python
'preferredquality': '192'  # hoặc '320'
```

---

## ⚠️ Lưu ý

* Công cụ này chỉ nên dùng cho mục đích cá nhân
* Hãy đảm bảo bạn có quyền tải nội dung từ YouTube
* Không sử dụng cho mục đích vi phạm bản quyền

---

## 📌 Công nghệ sử dụng

* Python 3
* yt-dlp
* FFmpeg

---

## ❤️ Đóng góp

Mọi đóng góp đều được hoan nghênh!
Hãy tạo pull request hoặc issue nếu bạn có ý tưởng mới.

---

## 📜 License

MIT License
