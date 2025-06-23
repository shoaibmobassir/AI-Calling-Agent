import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
calendar = build('calendar', 'v3', credentials=credentials)

def book_appointment(contact_name, summary, datetime_str):
    event = {
        'summary': f"Call with {contact_name}",
        'description': summary,
        'start': {'dateTime': datetime_str, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': datetime_str, 'timeZone': 'Asia/Kolkata'},
    }
    created_event = calendar.events().insert(calendarId='primary', body=event).execute()
    print(f"[Calendar] Event created: {created_event.get('htmlLink')}")
