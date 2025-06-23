# main.py

import os
from dotenv import load_dotenv
from agents.agent_runner import run_agent_for_contact

# Load .env variables
load_dotenv()

def load_contacts():
    """
    For now, we're hardcoding contacts.
    Later, load from DB, Google Sheets, or CSV.
    """
    return [
        {"name": "Ramesh Kumar", "phone": "+911234567890"},
        {"name": "Meena Sharma", "phone": "+919876543210"}
    ]

def main():
    contacts = load_contacts()

    for contact in contacts:
        try:
            print(f"\n📞 Calling: {contact['name']} ({contact['phone']})")
            run_agent_for_contact(contact)
        except Exception as e:
            print(f"[main.py] ❌ Error handling {contact['name']}: {e}")

if __name__ == "__main__":
    main()
