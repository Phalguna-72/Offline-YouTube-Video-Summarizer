import argparse
import os

from downloader.youtube_audio import download_audio
from stt.whisper_transcriber import transcribe_audio
from summarizer.bart_summarizer import summarize_text


def main():
    parser = argparse.ArgumentParser(
        description="Offline YouTube Video Summarizer"
    )
    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="Public YouTube video URL"
    )
    args = parser.parse_args()

    youtube_url = args.url

    print("[INFO] Downloading audio from YouTube...")
    audio_path = download_audio(youtube_url)

    print("[INFO] Transcribing audio (offline)...")
    transcript = transcribe_audio(audio_path)

    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    print("[INFO] Transcript saved to transcript.txt")

    print("[INFO] Generating summary (offline)...")
    summary = summarize_text(transcript)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n--- FINAL SUMMARY ---\n")
    print(summary)
    print("\n[INFO] Summary saved to summary.txt")


if __name__ == "__main__":
    main()
