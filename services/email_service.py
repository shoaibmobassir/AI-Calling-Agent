import os
import sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

def send_summary_email(to_email, subject, content):
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=to_email,
        subject=subject,
        plain_text_content=content
    )
    try:
        response = sg.send(message)
        print(f"[Email] Status: {response.status_code}")
    except Exception as e:
        print(f"[Email] Error: {e}")
