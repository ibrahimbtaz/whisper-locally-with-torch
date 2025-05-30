import whisper
import torch
import os
import time
import sys
import threading

try:
    # 🎧 Input audio file from argument or manual input
    if len(sys.argv) > 1:
        audio_path = " ".join(sys.argv[1:]).strip('"')
    else:
        audio_path = input("🎤 Enter audio file path (e.g., recording.mp3): ").strip('"')

    # Show the path being checked
    print(f"🟨 Checking path: {audio_path}")

    # File validation
    if not os.path.isfile(audio_path):
        print(f"❌ File not found!\nChecked path: {os.path.abspath(audio_path)}")
        # 🌟 Whisper Usage Info
        print("\n================ Whisper Speech-to-Text ================" )
        print("Whisper by OpenAI: Automatically transcribe audio to text.")
        print("Docs: https://platform.openai.com/docs/guides/speech-to-text")
        print("\nSupported formats: mp3, wav, m4a, flac, ogg")
        print("Tips:")
        print("- Use clear, undamaged audio files.")
        print("- Path can be relative or absolute.")
        print("- Default model: small (can be changed in code)")
        print("========================================================\n")
        os._exit(1)
    else:
        print(f"✅ Path is valid!")

    allowed_ext = {'.mp3', '.wav', '.m4a', '.flac', '.ogg'}
    _, ext = os.path.splitext(audio_path)
    if ext.lower() not in allowed_ext:
        print(f"❌ File format '{ext}' is not supported! Supported formats: {', '.join(allowed_ext)}")
        os._exit(1)

    # 🔍 Device check
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🚀 Active device: {device.upper()}")

    # 📥 Load model
    model_name = "small"
    print(f"📦 Loading model '{model_name}'...")
    model = whisper.load_model(model_name, device=device)
    print(f"✅ Model '{model_name}' loaded successfully!")

    # 🧠 Transcription process with real-time info
    print("\n⏳ Transcription started. Please wait...\n")
    progress = True
    spinner = ['⏳', '⏲️', '⌛', '⏰']

    def show_progress():
        t = 0
        idx = 0
        while progress:
            print(f"  {spinner[idx % len(spinner)]} Processing... {t} seconds", end='\r')
            time.sleep(1)
            t += 1
            idx += 1

    thread = threading.Thread(target=show_progress)
    thread.start()

    start = time.time()
    try:
        result = model.transcribe(audio_path, task="transcribe", language="en", verbose=True)
    except KeyboardInterrupt:
        progress = False
        thread.join()
        print("\n❌ Transcription cancelled by user (Ctrl+C). Exiting.")
        os._exit(0)
    end = time.time()
    progress = False
    thread.join()

    print("\n✅ Transcription finished!")
    print(f"⏱️ Elapsed time: {end - start:.2f} seconds")

except KeyboardInterrupt:
    print("\n❌ Operation cancelled by user (Ctrl+C). Exiting.")
    os._exit(0)