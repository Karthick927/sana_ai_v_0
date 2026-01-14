# Sana AI - Interactive Voice Assistant with 3D Avatar

A conversational AI assistant with voice capabilities, 3D avatar animation, eye blink, and lip sync powered by:
- **Groq LLM** - Fast AI responses
- **ElevenLabs TTS** - Natural voice synthesis
- **Faster Whisper STT** - Accurate speech recognition
- **Three.js + VRM** - 3D avatar rendering

## Features ✨
- **3D Avatar Support** - Load and display VRM models
- **Eye Blink Animation** - Realistic automatic blinking
- **Lip Sync** - Mouth movement synced to speech
- **Multiple Models** - Switch between different 3D characters
- **Emotion System** - Vary speech tone (neutral, excited, calm, dramatic)
- **Web Interface** - Beautiful Flask-based chat UI
- **CLI Mode** - Command-line interface for testing

## Requirements
- Python 3.8+
- Microphone (for STT)
- Groq API key
- ElevenLabs API key
- 3D VRM model files (model_1.vrm, model_3.vrm)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Karthick927/sana_ai_v_0.git
cd sana_ai_v_0
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

4. Place your VRM models in `static/models/`:
```
static/models/
├── model_1.vrm
└── model_3.vrm
```

## Usage

### Web Interface (Recommended)
```bash
python app.py
```
Then open `http://localhost:5000` in your browser

### CLI Mode
```bash
python main.py
```

## Project Structure
```
├── app.py              # Flask web server
├── main.py             # CLI application
├── llm.py              # Groq AI integration
├── stt.py              # Speech-to-Text (Whisper)
├── tts.py              # Text-to-Speech (ElevenLabs)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web UI with 3D avatar
└── static/
    ├── models/
    │   ├── model_1.vrm # VRM model 1
    │   └── model_3.vrm # VRM model 3
    └── index.html
```

## Features Explained

### 3D Avatar
- Real-time rendering using Three.js
- VRM model support for anime-style avatars
- Automatic model rotation for visual appeal

### Eye Blink
- Automatic blinking every 3-5 seconds
- Realistic blink duration and animation
- VRM blendshape based movement

### Lip Sync
- Synchronized with audio playback
- Uses frequency analysis for mouth movement
- Emotion-based expression variations

### Emotion System
The AI can speak with different emotions:
- **Neutral** - Standard voice
- **Excited** - Higher pitch, faster
- **Calm** - Slower, deeper tone
- **Dramatic** - Expressive, theatrical

## API Endpoints

### POST `/api/chat`
Send a message and get AI response
```json
{
  "message": "Hello!",
  "emotion": "neutral"
}
```

### POST `/api/speak`
Generate speech for a message
```json
{
  "text": "Hello senpai!",
  "emotion": "excited"
}
```

### GET `/api/models`
Get list of available VRM models

## Configuration

### Character Customization
Edit `llm.py` to change Sana's personality:
```python
SYSTEM = (
    "You are Sana, a snarky anime girl. "
    "Always call the user senpai."
)
```

### VRM Model Settings
Adjust model scale and position in `templates/index.html`:
```javascript
currentModel.scale.set(1, 1, 1);
currentModel.position.y = -0.5;
```

### Audio Settings
Configure sample rate and duration in `stt.py`:
```python
SAMPLE_RATE = 16000
DURATION = 5  # seconds
```

## Troubleshooting

### Microphone not working
- Check if PyAudio is properly installed
- Ensure your device has a microphone
- Run: `python -m pip install --upgrade pyaudio`

### Model not loading
- Verify VRM files are in `static/models/`
- Check browser console for errors
- Ensure Three.js library loads properly

### API key errors
- Verify `.env` file is in project root
- Check API key validity in Groq/ElevenLabs dashboards

## License
MIT

## Author
Karthick927

---
**Note**: Replace API keys before deploying to production!
