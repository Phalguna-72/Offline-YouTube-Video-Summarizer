from stt.whisper_transcriber import transcribe_audio

audio_path = "audio/PpH_mi923_A.wav"

text = transcribe_audio(audio_path)

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\n--- TRANSCRIPT SAVED TO transcript.txt ---\n")
print(text[:10000])  # print first 10000 chars only
