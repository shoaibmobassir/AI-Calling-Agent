import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def synthesize_speech(text, lang="hi"):
    # Dummy Gemini-style endpoint
    response = requests.post(
        "https://api.gemini.fake/tts",
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
        json={"text": text, "lang": lang}
    )
    result = response.json()
    audio_url = result.get("audio_url")
    print(f"[TTS] Synthesized audio URL: {audio_url}")
    return audio_url
