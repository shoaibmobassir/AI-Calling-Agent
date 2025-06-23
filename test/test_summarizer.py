from processors.summarizer import summarize_conversation

sample_transcript = [
    "User: Hello",
    "Agent: Hi there, how can I help?",
    "User: I want to schedule an appointment for tomorrow at 3pm.",
    "Agent: Noted. Booking it now."
]

def test_summary():
    summary = summarize_conversation(sample_transcript)
    print("SUMMARY:\n", summary)

if __name__ == "__main__":
    test_summary()