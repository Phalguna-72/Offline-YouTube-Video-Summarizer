# Offline YouTube Video Summarizer

## Project Overview
This project is an end-to-end **offline AI application** that takes a public YouTube video URL and generates a concise textual summary of the video content.

The system performs the following steps:
1. Downloads audio from a YouTube video
2. Transcribes the audio to text using an offline speech-to-text model
3. Summarizes the transcribed text using an offline text summarization model

All AI models run **entirely offline** using open-source models. No cloud-based APIs are used for transcription or summarization.

---

## Setup and Installation Instructions

### Prerequisites
- Python 3.9 or higher
- FFmpeg (system dependency)
- Internet connection (only for initial model download)

---

### Step 1: Create a Virtual Environment
```bash
python -m venv venv
```

Activate the environment:

**Windows (CMD)**
```bash
venv\Scripts\activate.bat
```

---

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

The `requirements.txt` includes:
- yt-dlp
- openai-whisper
- torch
- transformers
- ffmpeg-python
- tqdm

---

### Step 3: Install FFmpeg
FFmpeg must be installed as a system dependency and added to PATH.

Verify installation:
```bash
ffmpeg -version
```

---

### Step 4: Model Download (One-Time)
The following models are downloaded automatically during first execution:
- Whisper (Speech-to-Text)
- BART (`facebook/bart-large-cnn`) for summarization

After this, the application runs fully offline.

---

## Design Choices and Justification

### Speech-to-Text Model: Whisper
**Model:** OpenAI Whisper (base)

**Reason for selection:**
- Fully offline inference
- High transcription accuracy
- Handles long-form audio reliably
- Widely adopted open-source model

**Trade-off:**
- Slower inference on CPU compared to cloud APIs, but ensures offline compliance and portability.

---

### Text Summarization Model: BART
**Model:** facebook/bart-large-cnn

**Reason for selection:**
- Strong abstractive summarization capability
- Produces coherent and readable summaries
- Well-documented and widely used

**Trade-off:**
- Higher memory usage than smaller models, but significantly better summary quality.

---

### Handling Long Videos
Long videos (including multi-hour lectures) are handled using:
- Transcript chunking
- Hierarchical (two-stage) summarization

This avoids model context-length limitations and ensures stable memory usage.

---

## Usage

Run the application from the project root directory:

```bash
python app.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Outputs
- Extracted audio file (`.wav`)
- `transcript.txt` – full transcription
- `summary.txt` – final summarized output

The summary is also printed to the terminal.

---

## Challenges Faced

### Offline Model Setup
Ensuring all AI processing ran offline required careful selection and setup of models.

**Solution:**  
Used open-source Whisper and BART models with local inference.

---

### Long Transcript Processing
Long transcripts exceeded the context window of summarization models.

**Solution:**  
Implemented chunking and hierarchical summarization.

---

### Windows Environment Issues
Encountered execution policy and dependency issues on Windows systems.

**Solution:**  
Used CMD-based virtual environment activation and validated system-level dependencies such as FFmpeg.

---

## Demonstration
A short screencast is provided demonstrating:
1. Running the CLI with a sample YouTube URL
2. Audio download
3. Offline transcription
4. Offline summarization
5. Final summary output

---

## Conclusion
This project demonstrates a robust offline AI pipeline that combines practical software engineering with modern NLP techniques. The system is modular, scalable, and suitable for processing long-form video content while remaining fully offline.
