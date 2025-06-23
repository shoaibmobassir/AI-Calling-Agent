import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_conversation(transcript):
    """
    Uses GPT to summarize the full call transcript.
    Returns a summary with key points, user intent, and next steps.
    """
    joined_text = "\n".join(transcript)
    prompt = (
        "You are an assistant summarizing customer support conversations.\n"
        "Summarize the following transcript in English or Hindi, and extract action items:\n\n"
        f"{joined_text}\n\nSummary:"
    )

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        summary = completion.choices[0].message["content"]
        print(f"[Summarizer] Summary generated.")
        return summary
    except Exception as e:
        print(f"[Summarizer] Error: {e}")
        return "Summary not available due to error."
