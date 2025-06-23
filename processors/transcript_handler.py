import os
from datetime import datetime

TRANSCRIPT_DIR = "data/transcripts"

os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

def save_transcript(phone_number, transcript):
    """
    Saves the transcript to a .txt file per phone number + timestamp.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{phone_number}_{timestamp}.txt"
    filepath = os.path.join(TRANSCRIPT_DIR, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for line in transcript:
                f.write(line + "\n")
        print(f"[Transcript] Saved at {filepath}")
    except Exception as e:
        print(f"[Transcript] Error saving transcript: {e}")
