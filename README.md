
# Offline YouTube Video Summarizer

## Project Overview
This project is an end-to-end offline AI system that takes a public YouTube video URL and generates a concise textual summary of its content.

All AI components (speech-to-text and summarization) run entirely offline using open-source models, without relying on any cloud APIs.

## System Architecture
YouTube URL → Audio Download (yt-dlp + FFmpeg) → Speech-to-Text (Whisper) → Transcript Chunking → Hierarchical Summarization (BART) → Final Summary

## Core Components
- YouTube Audio Downloader: yt-dlp + FFmpeg
- Speech-to-Text: OpenAI Whisper (offline)
- Text Summarization: facebook/bart-large-cnn (offline)
- Chunking & hierarchical summarization for long videos

## Project Structure
offline-youtube-summarizer/
├── app.py
├── downloader/
├── stt/
├── summarizer/
├── utils/
├── transcript.txt
├── summary.txt
├── requirements.txt
└── README.md

## Setup & Installation
1. Create and activate virtual environment
2. Install dependencies using requirements.txt
3. Install FFmpeg and add to PATH

## Usage
python app.py --url "https://www.youtube.com/watch?v=VIDEO_ID"

## Handling Long Videos
Supports long-form videos using chunking and two-stage summarization to avoid context overflow.

## Challenges Faced
- Whisper installation issues on Windows
- Managing long transcripts
- Improving abstraction quality in summaries

## Conclusion
This project demonstrates a robust offline AI pipeline with modular design and scalable summarization.
