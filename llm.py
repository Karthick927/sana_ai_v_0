from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Please set the GROQ_API_KEY environment variable in .env file")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

SYSTEM = (
    "You are Sana, a snarky anime girl. "
    "Always call the user senpai."
)

def ask_llm(text):
    """
    Ask Groq AI with system prompt
    
    Available models:
    - llama-3.3-70b-versatile (BEST - most capable)
    - llama-3.1-70b-versatile
    - llama-3.1-8b-instant (FASTEST)
    - mixtral-8x7b-32768
    """
    
    messages = [
        {
            "role": "system",
            "content": SYSTEM
        },
        {
            "role": "user",
            "content": text
        }
    ]
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Best model
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False
    )
    
    return response.choices[0].message.content


# Test it
if __name__ == "__main__":
    response = ask_llm("Hello! Who are you?")
    print(response)

## **Your .env file should have:**