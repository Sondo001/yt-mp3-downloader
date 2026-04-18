# 🎬 YouTube Downloader (MP3 / MP4) - Python

Công cụ Python mạnh mẽ giúp tải video/audio từ YouTube với nhiều tính năng nâng cao:

---

## 🚀 Tính năng

* 🎵 Tải và chuyển đổi sang **MP3**
* 🎥 Tải video **MP4 (720p / 1080p / 4K)**
* 🎚️ Chọn **bitrate MP3** (128 / 192 / 320 kbps)
* 📂 Tự động nhận diện **playlist**

  * Tải toàn bộ playlist
  * Hoặc chọn từng video
* 🔗 Hỗ trợ nhập **nhiều link cùng lúc**
* ⚡ Hiển thị **progress (%, tốc độ, ETA)**
* 🧹 Tự động **làm sạch tên file**
* 📁 Lưu file theo tiêu đề video

---

## 🛠️ Cài đặt

### 1. Clone từ GitHub

```bash id="0x1m2n"
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
```

---

### 2. Cài thư viện Python

```bash id="c91t8r"
pip install yt-dlp
```

---

### 3. Cài FFmpeg (bắt buộc)

#### Windows

* Tải FFmpeg (bản static)
* Giải nén và thêm vào PATH

#### Linux (Ubuntu/Debian)

```bash id="z72k1a"
sudo apt install ffmpeg
```

---

## ▶️ Cách sử dụng

Chạy chương trình:

```bash id="d8e4l1"
python main.py
```

---

### 🎯 Bước 1: Chọn chế độ

* `1` → MP3 (audio)
* `2` → MP4 (video)

---

### 🎵 Nếu chọn MP3

Chọn bitrate:

* 128 kbps (nhẹ)
* 192 kbps (cân bằng)
* 320 kbps (chất lượng cao)

---

### 🎬 Nếu chọn MP4

Chọn chất lượng:

* 720p
* 1080p
* 4K

---

### 🔗 Bước 2: Nhập link

* Dán nhiều link (video hoặc playlist)
* Mỗi link 1 dòng
* Nhấn Enter trống để bắt đầu

---

## 📂 Xử lý playlist

Khi phát hiện playlist:

* Hỏi:

  * Tải toàn bộ
  * Hoặc chọn từng video

Ví dụ chọn:

```id="eg3b1f"
1,3,5
```

---

## ⚡ Hiển thị tiến trình

Trong lúc tải sẽ hiển thị:

* % hoàn thành
* Tốc độ tải
* Thời gian còn lại (ETA)

---

## 🧹 Làm sạch tên file

Tự động loại bỏ ký tự lỗi:

```
\ / : * ? " < > |
```

Giúp file tương thích Windows/Linux/macOS.

---

## 📁 Cấu trúc project

```bash id="9k1f2x"
youtube-downloader/
│── main.py
│── downloads/
│── README.md
```

---

## ⚙️ Tuỳ chỉnh

### 🔊 Đổi bitrate mặc định

```python id="zq2w7e"
return "192"
```

---

### 🎬 Đổi chất lượng video mặc định

```python id="n3b8ya"
return "best"
```

---

## ⚠️ Lưu ý

* Công cụ chỉ nên dùng cho mục đích cá nhân
* Đảm bảo bạn có quyền tải nội dung từ YouTube
* Không sử dụng cho mục đích vi phạm bản quyền

---

## 🧰 Công nghệ sử dụng

* Python 3
* yt-dlp
* FFmpeg

---

## ❤️ Đóng góp

Mọi đóng góp đều được hoan nghênh:

* Fork repository
* Tạo pull request
* Báo lỗi qua issue

---

## 📜 License

MIT License
