from services.tts_service import synthesize_speech
from services.stt_service import transcribe_audio

# Simulate a call SID
call_sid = "mock-call-12345"

def test_speech():
    print("[TTS] Testing synthesis...")
    url = synthesize_speech("Hello, this is a test response.")
    print("Audio URL:", url)

    print("[STT] Simulating transcription...")
    text = transcribe_audio(call_sid)
    print("Transcribed Text:", text)

if __name__ == "__main__":
    test_speech()