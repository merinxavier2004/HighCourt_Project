# Malayalam Voice & Text Tools

This Flask application provides two main features:
1. Malayalam Voice to Text Transcription
2. English to Malayalam Text Translation

## Requirements

- Python 3.8 or higher
- FFmpeg (required for audio processing)
- CUDA-compatible GPU (optional, for faster processing)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd malayalam_project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the web interface to:
   - Upload Malayalam audio files for transcription
   - Enter English text for Malayalam translation

## Features

### Voice Transcription
- Supports various audio formats (MP3, WAV, etc.)
- Uses OpenAI's Whisper model for accurate Malayalam speech recognition
- Provides real-time transcription results

### Text Translation
- Translates English text to Malayalam
- Uses the MarianMT model from Helsinki-NLP
- Fast and accurate translations

## Notes

- The first run will download the required models, which might take some time
- GPU acceleration is automatically used if available
- Large audio files may take longer to process

## Troubleshooting

If you encounter any issues:

1. Make sure FFmpeg is installed and accessible from the command line
2. Check that all dependencies are correctly installed
3. Ensure you have sufficient disk space for the models
4. For audio files, ensure they are in a supported format 