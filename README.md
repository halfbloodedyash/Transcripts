

```markdown
# 🎥 YouTube Transcript & Video Info App

A simple Flask web app that lets you extract captions, timestamps, and metadata from any YouTube video using just the video URL. Built with Python, Flask, and `youtube_transcript_api`.

---

## 🚀 Features

- ✅ Get clean transcripts from YouTube videos
- ⏱ Generate human-readable timestamps from captions
- 📊 Fetch video metadata (title, author, thumbnail, etc.)
- 🌐 Works with YouTube links like `youtu.be`, `youtube.com/watch`, `youtube.com/embed`, etc.

---

## 🛠 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/youtube-transcript-app.git
cd youtube-transcript-app
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run the app

```bash
python3 app.py
```

Visit `http://127.0.0.1:5000` in your browser and drop in a YouTube link.

---

## 🧾 Example usage

Paste a YouTube URL like:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

And you'll get:
- The video’s metadata (title, author, thumbnail)
- Full transcript (if available)
- Clean timestamped summary

---

## 📂 Project Structure

```
.
├── app.py                 # Flask app
├── youtube_tools.py       # Transcript + Metadata logic
├── templates/
│   └── index.html         # HTML template
├── requirements.txt
└── README.md
```

---

## 📦 Dependencies

- Flask
- youtube_transcript_api

Install using:

```bash
pip install -r requirements.txt
```

---

## 📌 To-Do (if you're feelin' fancy)

- [ ] Add error handling for private/unavailable videos
- [ ] UI glow-up with Bootstrap or Tailwind
- [ ] Add download as `.txt` or `.srt`
- [ ] Support translation / subtitle language toggle

---

## ⚠️ Disclaimer

This tool uses the unofficial YouTube Transcript API and may not work with videos that have:
- No captions
- Auto-generated-only captions in unsupported languages
- Restricted access

---



## 🌟 Like it?

Give it a ⭐ on GitHub (if you're hosting it there) or just flex it on your portfolio 😎
