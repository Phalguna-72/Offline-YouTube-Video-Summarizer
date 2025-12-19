# Code Structure & Working Guide

This document explains the **code organization and execution flow** of the Offline YouTube Video Summarizer.  
It is intended for **reviewers and third-party readers** to easily understand how the system works.

---

## Project Directory Structure

```
offline-youtube-summarizer/
│
├── app.py
│
├── downloader/
│   └── youtube_audio.py
│
├── stt/
│   └── whisper_transcriber.py
│
├── summarizer/
│   └── bart_summarizer.py
│
├── utils/
│   └── chunker.py
│
├── transcript.txt
├── summary.txt
├── requirements.txt
└── README.md
```

---

## File-by-File Explanation

### 1. `app.py` (Entry Point)
This is the **main CLI entry point** of the application.

**Responsibilities:**
- Parses command-line arguments (`--url`)
- Orchestrates the full pipeline:
  1. Audio download
  2. Speech-to-text transcription
  3. Text summarization
- Saves intermediate and final outputs

---

### 2. `downloader/youtube_audio.py`
Handles **YouTube audio extraction**.

**Key Function:**
```python
download_audio(youtube_url)
```

**What it does:**
- Uses `yt-dlp` to download the best available audio
- Converts audio to `.wav` using FFmpeg
- Returns the local audio file path

---

### 3. `stt/whisper_transcriber.py`
Handles **offline speech-to-text transcription**.

**Key Function:**
```python
transcribe_audio(audio_path)
```

**What it does:**
- Loads the Whisper model locally
- Transcribes the audio file into text
- Returns the transcript as a string

---

### 4. `utils/chunker.py`
Utility module for **text chunking**.

**Purpose:**
- Splits long transcripts into smaller chunks
- Prevents exceeding model context limits
- Enables scalable summarization

---

### 5. `summarizer/bart_summarizer.py`
Handles **hierarchical text summarization**.

**How it works:**
1. Splits transcript into chunks
2. Summarizes each chunk individually
3. Combines chunk summaries
4. Re-summarizes combined text to produce an abstract final summary

---

## End-to-End Execution Flow

```
YouTube URL
   ↓
youtube_audio.py → audio.wav
   ↓
whisper_transcriber.py → transcript.txt
   ↓
chunker.py → text chunks
   ↓
bart_summarizer.py → summary.txt
```

---

## Why This Design Is Easy to Understand

- Clear separation of concerns
- Each module has a single responsibility
- The pipeline is linear and readable
- Intermediate outputs are saved for transparency
- Easy to debug and extend

---

## Summary
This project follows a clean, modular architecture where each component is independently testable and logically connected through a simple execution pipeline.
