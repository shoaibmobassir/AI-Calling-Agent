import os
import json
from datetime import datetime

SESSION_LOG_PATH = "data/sessions/sessions.json"
os.makedirs(os.path.dirname(SESSION_LOG_PATH), exist_ok=True)

def save_session_metadata(session_id, contact, result):
    """
    Save session metadata like phone, contact name, summary, and memory dump.
    """
    session_data = {
        "session_id": session_id,
        "timestamp": datetime.now().isoformat(),
        "contact_name": contact["name"],
        "phone": contact["phone"],
        "summary": result.get("summary", ""),
        "memory": result.get("memory_dump", {}),
        "status": "completed"
    }

    sessions = load_all_sessions()
    sessions[session_id] = session_data

    with open(SESSION_LOG_PATH, "w") as f:
        json.dump(sessions, f, indent=2)

    print(f"[SessionManager] Session {session_id} saved.")

def load_all_sessions():
    if not os.path.exists(SESSION_LOG_PATH):
        return {}
    with open(SESSION_LOG_PATH, "r") as f:
        return json.load(f)

def get_session_by_id(session_id):
    sessions = load_all_sessions()
    return sessions.get(session_id)

def resume_session(session_id):
    session = get_session_by_id(session_id)
    if session:
        print(f"[SessionManager] Resuming session {session_id}")
        return session
    else:
        print(f"[SessionManager] Session {session_id} not found.")
        return None
