import requests
import pygame
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Set your ElevenLabs API key from environment variable
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

OUTPUT_FILE = "output.mp3"
pygame.mixer.init()

# Jessica's voice ID
JESSICA_VOICE_ID = "cgSgspJ2msm6clMCkdW9"

# ElevenLabs API endpoint
ELEVENLABS_API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{JESSICA_VOICE_ID}"


def speak(text):
    """
    Generate speech with Jessica's voice
    (Eloquent Villain - Character voice)
    """
    
    if not text.strip():
        return
    
    print(f"🎤 Generating speech with Jessica's voice...")
    start = time.time()
    
    try:
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY
        }
        
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.5,
                "use_speaker_boost": True
            }
        }
        
        response = requests.post(ELEVENLABS_API_URL, json=data, headers=headers)
        response.raise_for_status()
        
        # Unload any existing music first
        pygame.mixer.music.unload()
        
        # Save audio
        with open(OUTPUT_FILE, "wb") as f:
            f.write(response.content)
        
        elapsed = time.time() - start
        print(f"⏱️ Generated in {elapsed:.2f}s")
        
        # Play audio
        print("🔊 Playing...")
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Unload music to release file
        pygame.mixer.music.unload()
        time.sleep(0.1)  # Small delay to ensure file is released
        
        print("✅ Done!\n")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def speak_with_emotion(text, emotion="neutral"):
    """
    Speak with different emotions
    emotion: "neutral", "excited", "calm", "dramatic"
    """
    
    if not text.strip():
        return
    
    emotion_settings = {
        "neutral": {"stability": 0.5, "style": 0.5},
        "excited": {"stability": 0.3, "style": 0.8},
        "calm": {"stability": 0.7, "style": 0.3},
        "dramatic": {"stability": 0.4, "style": 0.9}
    }
    
    settings = emotion_settings.get(emotion, emotion_settings["neutral"])
    
    try:
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY
        }
        
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": settings["stability"],
                "similarity_boost": 0.75,
                "style": settings["style"],
                "use_speaker_boost": True
            }
        }
        
        response = requests.post(ELEVENLABS_API_URL, json=data, headers=headers)
        response.raise_for_status()
        
        # Unload any existing music first
        pygame.mixer.music.unload()
        
        with open(OUTPUT_FILE, "wb") as f:
            f.write(response.content)
        
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Unload music to release file
        pygame.mixer.music.unload()
        time.sleep(0.1)  # Small delay to ensure file is released
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Test Jessica's voice
    speak("Hello! I'm Jessica, your AI assistant with this elegant voice!")
    
    # Test with different emotions
    speak_with_emotion("This is exciting news!", emotion="excited")
    speak_with_emotion("Let me explain this calmly.", emotion="calm")
    speak_with_emotion("This is absolutely dramatic!", emotion="dramatic")