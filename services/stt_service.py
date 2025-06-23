import os
import requests

CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")

def transcribe_audio(call_sid):
    # Simulate transcription call
    response = requests.post(
        "https://api.cartesia.ai/stt",
        headers={"Authorization": f"Bearer {CARTESIA_API_KEY}"},
        json={"call_sid": call_sid}
    )
    text = response.json().get("text", "")
    print(f"[STT] Transcribed: {text}")
    return text
