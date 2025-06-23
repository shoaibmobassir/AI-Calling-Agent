<<<<<<< HEAD
# AI-Calling-Agent
=======
## 📞 AI Caller Agent System

An AI-driven multi-lingual (Hindi/English) caller agent that can:

* Make automated calls via Twilio
* Converse with users in real time using TTS + STT
* Summarize calls and detect intent
* Book appointments on Google Calendar
* Send follow-up emails to customers

> Powered by LangGraph, Twilio, Gemini/OpenAI, Cartesia, Google Calendar API, and SendGrid.

---

## 📁 Project Structure

```
ai-agent-system/
├── agents/               # Call orchestration & memory
├── services/             # Twilio, TTS, STT, NLP, Calendar, Email, Sessions
├── processors/           # Summarizer and transcript handler
├── config/               # Prompt templates, company context
├── utils/                # Logging, helpers
├── test/                 # Test scripts
├── data/                 # Session transcripts and logs
├── main.py               # Entry point for the calling flow
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker config
├── docker-compose.yml    # Multi-service runner (optional)
├── .env                  # Secrets (not committed)
└── README.md             # This file
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.11+
* Twilio account (for calling)
* Google Cloud project + Calendar API
* Gemini or OpenAI API key
* SendGrid (or Gmail) for emailing
* Cartesia STT access key (for real-time voice transcription)

---

### 📥 Setup Instructions

```bash
# Clone and enter the repo
git clone https://github.com/your-org/ai-agent-system.git
cd ai-agent-system

# Install dependencies
pip install -r requirements.txt

# Copy .env example and add your keys
cp .env.example .env

# Run test flow
python main.py
```

---

### 🐳 Docker (Optional)

```bash
# Build and run with Docker Compose
docker-compose up --build
```

---

## 🔐 .env Variables

Update `.env` in root folder with:

```env
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+91xxxxxxxxxx

GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key

CARTESIA_API_KEY=your_cartesia_key

SENDGRID_API_KEY=your_sendgrid_key
EMAIL_SENDER=your@email.com

GOOGLE_SERVICE_ACCOUNT_JSON=config/google_creds.json
```

---

## 🧠 Memory + Context

This system uses:

| Type       | Tool                       | Purpose                               |
| ---------- | -------------------------- | ------------------------------------- |
| Short-Term | `ConversationBufferMemory` | Tracks current call memory            |
| Transcript | `.txt` file per session    | Saved for summarization & audit       |
| Long-Term  | Coming soon (Chroma)       | Cross-call memory for user follow-ups |

**Business tone/brand context** is loaded from:

```
config/company_context.txt
```

---

## 🧪 Test Scripts

Run these to test modules independently:

```bash
python test/test_summarizer.py
python test/test_mock_speech.py
python test/test_resume.py
```

---

## 🛠️ Key Services

| File                  | Description                          |
| --------------------- | ------------------------------------ |
| `twilio_service.py`   | Voice call control                   |
| `stt_service.py`      | Real-time voice to text via Cartesia |
| `tts_service.py`      | Text to speech via Gemini/OpenAI     |
| `nlp_service.py`      | LLM-driven dialog logic + memory     |
| `calendar_service.py` | Google Calendar appointment booking  |
| `email_service.py`    | Follow-up email with summary         |
| `session_manager.py`  | Tracks and resumes sessions          |

---

## ✨ Future Plans

* ✅ Vector-based memory with Chroma
* ✅ Web dashboard to view & trigger sessions
* ✅ CRM integration
* ✅ Smart fallback for no response / DND
* ✅ Hindi/English code-switching refinements

---

## 🤝 Contributing

Pull requests, ideas, and improvements welcome!
If you'd like to collaborate or extend this to your own use case (e.g. sales, service, medical), reach out!

---

## 📄 License

MIT License

---
>>>>>>> 257bdba (Initial commit)
