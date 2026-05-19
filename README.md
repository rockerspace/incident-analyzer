# AI-Powered Incident Root Cause Analyzer

An intelligent incident analysis system that uses LLM agents and RAG to automatically identify root causes from incident descriptions.

## Architecture
- **Spring Boot** (port 8080) — REST API gateway
- **Python FastAPI** (port 8000) — AI agent pipeline
- **Groq LLM** (llama-3.1-8b-instant) — Root cause reasoning
- **ChromaDB + HuggingFace** — Vector store for log retrieval

## Running Locally

### Python Agent
cd python-agent && source venv/bin/activate && uvicorn main:app --port 8000

### Spring Backend
cd spring-backend && ./gradlew bootRun

## API
POST http://localhost:8080/api/v1/incidents/analyze
Body: {"incidentDescription": "Payment service 503 errors"}