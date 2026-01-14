from stt import speech_to_text
from llm import ask_llm
from tts import speak_with_emotion
while True:
    user_text = speech_to_text()

    if not user_text:
        continue

    print("👤 You:", user_text)

    if user_text.lower() in ["exit", "quit", "bye"]:
        break

    ai_text = ask_llm(user_text)
    print("Sana:", ai_text)

    speak_with_emotion(ai_text)
