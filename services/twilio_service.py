import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def initiate_call(to_number):
    call = client.calls.create(
        twiml='<Response><Say>Hi, this is your AI assistant calling.</Say></Response>',
        to=to_number,
        from_=TWILIO_PHONE_NUMBER
    )
    print(f"[Twilio] Call initiated: {call.sid}")
    return call.sid

def play_audio(call_sid, audio_url):
    call = client.calls(call_sid).update(
        twiml=f'<Response><Play>{audio_url}</Play></Response>'
    )
    print(f"[Twilio] Audio played to {call.to}")
