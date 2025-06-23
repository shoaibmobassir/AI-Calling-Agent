from services.twilio_service import initiate_call, play_audio
from services.stt_service import transcribe_audio
from services.tts_service import synthesize_speech
from services.nlp_service import generate_response
from processors.summarizer import summarize_conversation
from processors.transcript_handler import save_transcript

from langchain.memory import ConversationBufferMemory

class DialogManager:
    def __init__(self, contact, session_id, context=None):
        self.contact = contact
        self.session_id = session_id
        self.transcript = []
        self.memory = ConversationBufferMemory(return_messages=True)
        self.context = context or "You are a helpful assistant."

    def handle_dialog(self, state):
        call_sid = initiate_call(self.contact["phone"])
        user_input = transcribe_audio(call_sid)

        while user_input:
            self.transcript.append(f"{self.contact['name']}: {user_input}")

            # Add to memory
            self.memory.chat_memory.add_user_message(user_input)

            # Build prompt from memory
            context = self.memory.load_memory_variables({})["history"]
            prompt = f"{self.context}\n\n{context}\nUser: {user_input}\nAssistant:"

            # Generate response
            response = generate_response(prompt)
            self.transcript.append(f"Agent: {response}")

            # Add to memory
            self.memory.chat_memory.add_ai_message(response)

            # Speak it
            audio = synthesize_speech(response)
            play_audio(call_sid, audio)

            # Next turn
            user_input = transcribe_audio(call_sid)

        save_transcript(self.contact["phone"], self.transcript)
        summary = summarize_conversation(self.transcript)

        return {
            "summary": summary,
            "memory_dump": self.memory.load_memory_variables({}),
            "contact": self.contact
        }
