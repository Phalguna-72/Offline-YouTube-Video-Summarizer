import whisper
import os

def transcribe_audio(audio_path, model_size="base"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print("[INFO] Loading Whisper model...")
    model = whisper.load_model(model_size)

    print("[INFO] Transcribing audio...")
    result = model.transcribe(audio_path)

    return result["text"]
