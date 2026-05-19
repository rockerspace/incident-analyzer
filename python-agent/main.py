from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
from contextlib import asynccontextmanager

from vector_store import get_vector_store
from agents import run_analysis

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Seeding ChromaDB vector store...")
    get_vector_store()
    print("Vector store ready.")
    yield

app = FastAPI(title="Incident Root Cause Analyzer - AI Layer", version="1.0.0", lifespan=lifespan)

class AnalyzeRequest(BaseModel):
    incident_description: str
    human_approved: Optional[bool] = True

class AnalyzeResponse(BaseModel):
    incident_description: str
    root_cause: str
    summary: str
    recommended_actions: List[str]
    retrieved_logs: List[str]
    anomalies: str
    agent_messages: List[str]

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_incident(request: AnalyzeRequest):
    try:
        result = run_analysis(
            incident_description=request.incident_description,
            human_approved=request.human_approved
        )
        return AnalyzeResponse(
            incident_description=result["incident_description"],
            root_cause=result["root_cause"],
            summary=result["summary"],
            recommended_actions=result["recommended_actions"],
            retrieved_logs=result["retrieved_logs"],
            anomalies=result["anomalies"],
            agent_messages=result["messages"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "service": "python-ai-agent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
