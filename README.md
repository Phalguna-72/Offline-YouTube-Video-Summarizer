# Offline-YouTube-Video-Summarizer
This project is an end-to-end offline AI system that takes a public YouTube video URL and generates a concise textual summary of its content.

Offline YouTube Video Summarizer
Project Overview

This project is an end-to-end offline AI system that takes a public YouTube video URL and generates a concise textual summary of its content.

The system is designed to work entirely offline for all core AI tasks, including:

Speech-to-Text (STT)

Text Summarization

No cloud APIs or external AI services are used. All models are downloaded once and run locally.

System Architecture
YouTube URL
   ↓
Audio Download (yt-dlp + FFmpeg)
   ↓
Speech-to-Text (Whisper – offline)
   ↓
Transcript Chunking
   ↓
Hierarchical Text Summarization (BART – offline)
   ↓
Final Summary Output


The system follows a modular pipeline design, allowing each component to be independently tested, debugged, and extended.

Core Components
1. YouTube Audio Downloader

Library: yt-dlp

Purpose: Extracts and downloads the audio track from a public YouTube video.

Why: Reliable, actively maintained, and works well with FFmpeg for audio extraction.

2. Offline Speech-to-Text (STT)

Model: OpenAI Whisper (base)

Why Whisper:

Fully offline inference

Strong transcription accuracy across accents

Robust for long-form audio

Execution: Runs locally on CPU (automatically handles segmentation for long audio).

3. Offline Text Summarization

Model: facebook/bart-large-cnn

Type: Abstractive summarization

Why BART:

Industry-standard summarization model

Produces coherent, human-readable summaries

Fully offline once downloaded

4. Chunking & Hierarchical Summarization

To handle long videos (including multi-hour lectures), the system implements:

Transcript chunking to avoid context-length limits

Two-stage (hierarchical) summarization:

Summarize individual chunks

Re-summarize combined chunk summaries to extract high-level meaning

This improves abstraction quality and prevents name-dumping or overly verbose outputs.

Project Structure
offline-youtube-summarizer/
│
├── app.py                     # CLI entry point
│
├── downloader/
│   └── youtube_audio.py       # Audio download logic
│
├── stt/
│   └── whisper_transcriber.py # Offline STT
│
├── summarizer/
│   └── bart_summarizer.py     # Hierarchical summarization
│
├── utils/
│   └── chunker.py             # Text chunking utility
│
├── transcript.txt             # Generated transcript
├── summary.txt                # Final summary
├── requirements.txt
└── README.md

Setup & Installation
1. Create Virtual Environment
python -m venv venv


Activate:

Windows (CMD)

venv\Scripts\activate.bat

2. Install Dependencies
pip install -r requirements.txt

3. Install FFmpeg (Required)

FFmpeg must be installed as a system dependency and added to PATH.

Verify installation:

ffmpeg -version

Usage

Run the application from the project root:

python app.py --url "https://www.youtube.com/watch?v=VIDEO_ID"

Outputs

Extracted audio (.wav)

transcript.txt – full transcription

summary.txt – final summarized output

Summary printed in terminal

Handling Long Videos

The system is designed to handle long-form content, including multi-hour lectures, by:

Processing transcripts in fixed-size chunks

Applying hierarchical summarization

Dynamically adjusting summary length based on input size

This ensures stable memory usage and avoids model context overflow.

Design Choices & Trade-offs
Offline-Only Constraint

All AI models are downloaded once and run locally

Ensures privacy, reproducibility, and independence from external APIs

Accuracy vs Performance

CPU-based inference ensures portability

Longer videos require more processing time, which is acceptable for an offline batch system

Challenges Faced

Managing Windows execution policies for virtual environments

Ensuring correct Whisper installation (avoiding incompatible packages)

Improving summarization abstraction while avoiding hallucinations

Handling long transcripts without exceeding model context limits

Each challenge was addressed through modular design, chunking, and hierarchical summarization.

Demonstration

A short screencast is provided showing:

Running the CLI with a YouTube URL

Audio download

Transcription

Final summary generation

Conclusion

This project demonstrates the design and implementation of a robust offline AI pipeline, combining practical software engineering with modern NLP techniques. It is modular, scalable, and suitable for real-world long-form content processing.
