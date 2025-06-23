import time
from agents.agent_runner import run_agent_for_contact

# Replace this with DB or Google Sheets access
CONTACTS = [
    {"name": "Rahul Sharma", "phone": "+919999999999"},
    {"name": "Anjali Patel", "phone": "+918888888888"},
]

def schedule_calls():
    print("[Scheduler] Starting scheduled calls...")
    for contact in CONTACTS:
        run_agent_for_contact(contact)
        time.sleep(2)  # delay between calls
