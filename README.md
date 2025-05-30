# Whisper Speech-to-Text Script

This project provides a simple command-line tool to transcribe audio files to text using OpenAI's Whisper model.

## Features
- Supports audio formats: mp3, wav, m4a, flac, ogg
- Automatic device selection (CUDA if available, otherwise CPU)
- Real-time progress indicator during transcription
- Clear error messages and usage tips

## Requirements
- Python 3.8+
- [OpenAI Whisper](https://github.com/openai/whisper)
- [PyTorch](https://pytorch.org/)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```
2. Install dependencies:
   ```sh
   pip install torch whisper
   ```

## Usage
You can run the script in two ways:

### 1. With an audio file path as an argument
```sh
python whisperku.py "path/to/your/audio.mp3"
```

### 2. Without an argument (manual input)
```sh
python whisperku.py
```
Then enter the path to your audio file when prompted.

## Output
- The script will print the transcription result to the terminal.
- Progress and elapsed time will be shown during processing.

## Notes
- For best results, use clear, undamaged audio files.
- You can change the Whisper model by editing the `model_name` variable in the script.

---

**Made with ❤️ using [OpenAI Whisper](https://github.com/openai/whisper)** 