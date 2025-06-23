from services.session_manager import resume_session

session_id = "your-session-id-here"
session_data = resume_session(session_id)

if session_data:
    print("=== Resumed Session ===")
    print("Name:", session_data["contact_name"])
    print("Summary:", session_data["summary"])
    print("Memory:", session_data["memory"])