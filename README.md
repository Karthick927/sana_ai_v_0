# VoiceAI - Interactive Voice Assistant

A conversational AI assistant with voice capabilities powered by Groq LLM, ElevenLabs TTS, and Whisper STT.

## Features
- **Speech-to-Text**: Uses Faster Whisper for accurate transcription
- **Text-to-Speech**: Generates speech with Jessica's voice using ElevenLabs
- **LLM Integration**: Groq API with Sana AI personality
- **Emotion Recognition**: Different speech emotions (neutral, excited, calm, dramatic)
- **VRM Character**: Support for 3D character model animations

## Requirements
- Python 3.x
- Groq API key
- ElevenLabs API key

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Files
- `main.py` - Main application loop
- `stt.py` - Speech-to-Text module
- `llm.py` - LLM integration with Groq
- `tts.py` - Text-to-Speech module
- `character_config.yaml` - Character configuration

## Configuration
Set environment variables in `.env`:
```
GROQ_API_KEY=your_key_here
```
