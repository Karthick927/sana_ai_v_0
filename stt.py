import pyaudio
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5  # seconds
CHUNK = 1024

model = WhisperModel("base", device="cpu", compute_type="int8")

def record_audio():
    print("🎤 Listening...")
    p = pyaudio.PyAudio()
    
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    frames = []
    for _ in range(0, int(SAMPLE_RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.float32))
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return np.concatenate(frames)

def speech_to_text():
    audio = record_audio()
    segments, _ = model.transcribe(audio)
    text = "".join([seg.text for seg in segments])
    return text.strip()

if __name__ == "__main__":
    print("You said:", speech_to_text())
