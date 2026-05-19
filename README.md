# ⚡ AI-Powered Incident Root Cause Analyzer

> An intelligent incident analysis system that uses LLM agents and RAG to automatically identify root causes, retrieve relevant logs, and recommend actions — from a single incident description.

🔗 **Live Demo:** [https://rockerspace.github.io/incident-analyzer/frontend/](https://rockerspace.github.io/incident-analyzer/frontend/)

---

## 🧠 How It Works

1. You describe an incident (e.g. *"Payment service throwing 503 errors since last deployment"*)
2. The system retrieves semantically similar logs from a vector store (ChromaDB + HuggingFace)
3. LLM agents reason over the logs and generate a root cause analysis
4. Recommended remediation actions are returned in seconds

---

## 🏗️ Architecture

| Layer | Technology | Role |
|---|---|---|
| Frontend | HTML/CSS/JS | Incident input UI |
| API Gateway | Spring Boot (port 8080) | REST API gateway |
| AI Agent Pipeline | Python FastAPI (port 8000) | Multi-agent orchestration |
| LLM | Groq — llama-3.1-8b-instant | Root cause reasoning |
| Vector Store | ChromaDB + HuggingFace | Semantic log retrieval |

---

## 🚀 Running Locally

### 1. Python Agent (AI Pipeline)

```bash
cd python-agent
source venv/bin/activate
uvicorn main:app --port 8000
```

### 2. Spring Boot Backend

```bash
cd spring-backend
./gradlew bootRun
```

### 3. Frontend

Open `frontend/index.html` in your browser, or serve it locally:

```bash
open frontend/index.html
```

---

## 📡 API

**Analyze an incident:**

```
POST http://localhost:8080/api/v1/incidents/analyze
Content-Type: application/json

{
  "incidentDescription": "Payment service 503 errors"
}
```

**Response includes:**
- `root_cause` — LLM-generated root cause explanation
- `recommended_actions` — ordered remediation steps
- `retrieved_logs` — top matching logs from the vector store
- `agent_messages` — trace of agent reasoning steps

---

## 🛠️ Tech Stack

- **Java** — Spring Boot REST gateway
- **Python** — FastAPI + LangChain agent pipeline
- **Groq API** — blazing-fast LLM inference (llama-3.1-8b-instant)
- **ChromaDB** — local vector database
- **HuggingFace Embeddings** — semantic similarity search

---

## 📁 Project Structure

```
incident-analyzer/
├── spring-backend/        # Java Spring Boot API gateway
├── python-agent/          # Python FastAPI AI agent
└── frontend/
    └── index.html         # Web UI
```

---

## 📄 License

MIT
