import uuid
from langgraph.graph import StateGraph
from agents.dialog_manager import DialogManager
from services.session_manager import save_session_metadata

def run_agent_for_contact(contact):
    session_id = str(uuid.uuid4())  # 🔐 Unique session
    print(f"[AgentRunner] Starting session {session_id} for {contact['name']}...")

    dialog = DialogManager(contact, session_id)

    builder = StateGraph()
    builder.add_node("dialog", dialog.handle_dialog)
    builder.set_entry_point("dialog")

    graph = builder.compile()

    result = graph.invoke({"state": "start", "contact": contact, "session_id": session_id})

    print("[AgentRunner] Session complete. Summary:")
    print(result.get("summary", "No summary"))

    # Save metadata to session manager
    save_session_metadata(session_id, contact, result)
