import os

# Load once at startup
CONTEXT_FILE = "config/company_context.txt"

if os.path.exists(CONTEXT_FILE):
    with open(CONTEXT_FILE, "r") as f:
        COMPANY_CONTEXT = f.read()
else:
    COMPANY_CONTEXT = ""

def generate_response(user_prompt):
    """
    Generates an LLM response using the company context + memory.
    """
    full_prompt = f"{COMPANY_CONTEXT}\n\n{user_prompt}"
    
    # Use your LLM provider here (Gemini, OpenAI, etc.)
    # Example for OpenAI:
    from openai import OpenAI
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": COMPANY_CONTEXT},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content
