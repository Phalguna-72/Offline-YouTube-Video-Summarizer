from summarizer.bart_summarizer import summarize_text
import os

TRANSCRIPT_FILE = "transcript.txt"
SUMMARY_FILE = "summary.txt"

def main():
    if not os.path.exists(TRANSCRIPT_FILE):
        raise FileNotFoundError("transcript.txt not found. Run Whisper first.")

    # Load transcript
    with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as f:
        transcript = f.read().strip()

    if len(transcript) == 0:
        raise ValueError("Transcript is empty.")

    # Generate summary
    summary = summarize_text(transcript)

    # Simple post-processing for better readability
    summary = summary.replace(" ,", ",").strip()
    summary = summary[0].upper() + summary[1:]

    # Save summary
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(summary)

    # Output
    print("\n--- FINAL SUMMARY ---\n")
    print(summary)

if __name__ == "__main__":
    main()
