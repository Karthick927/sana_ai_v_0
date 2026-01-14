"""
Sana AI - Voice Assistant with 3D Avatar
Run app.py to start the web interface with 3D avatar
Or use this CLI version below
"""
from stt import speech_to_text
from llm import ask_llm
from tts import speak_with_emotion

def cli_mode():
    """CLI mode for testing without web interface"""
    print("🎭 Sana AI - CLI Mode")
    print("Type 'exit', 'quit', or 'bye' to stop\n")
    
    while True:
        user_text = speech_to_text()

        if not user_text:
            continue

        print("👤 You:", user_text)

        if user_text.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye senpai!")
            break

        ai_text = ask_llm(user_text)
        print("Sana:", ai_text)

        speak_with_emotion(ai_text)

if __name__ == "__main__":
    cli_mode()
