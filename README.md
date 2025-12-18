
# Offline YouTube Video Summarizer

## 1. Project Overview

This project is an end-to-end offline AI application that accepts a public YouTube video URL and generates a concise textual summary of the video content.

### The system performs:

1.Audio extraction from YouTube

2.Offline speech-to-text transcription

3.Offline text summarization

All AI models run entirely offline using open-source models, with no cloud-based APIs used for transcription or summarization.

All AI components (speech-to-text and summarization) run entirely offline using open-source models, without relying on any cloud APIs.



## 2. Setup and Installation Instructions

###  2.1 Prerequisites

1. Python 3.9+

2. FFmpeg (system dependency)

3. Internet access only for initial model download


### 2.2 Create Virtual Environment

''' python -m venv venv '''

### Activate:

''' venv\Scripts\activate.bat '''

### 2.3 Install Dependencies

''' pip install -r requirements.txt  '''

requirements.txt includes:

1.yt-dlp
2.openai-whisper
3.torch
4.transformers
5.ffmpeg-python

### 2.4 Install FFmpeg

FFmpeg must be installed as a system dependency and added to PATH.

''' ffmpeg -version  '''


### 2.5 Model Download (One-Time)

The following models are downloaded automatically on first run:

-> Whisper (speech-to-text)

-> BART (facebook/bart-large-cnn) for summarization

-> After this, the application runs fully offline.
































## System Architecture

YouTube URL 
    ↓
Audio Download (yt-dlp + FFmpeg)
    ↓
Speech-to-Text (Whisper)
    ↓
Transcript Chunking
    ↓
Hierarchical Summarization (BART)
    ↓
Final Summary

    
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
