import os
from dotenv import load_dotenv
from typing import TypedDict, List, Annotated
import operator

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END

from vector_store import get_retriever

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
retriever = get_retriever()

class IncidentState(TypedDict):
    incident_description: str
    retrieved_logs: List[str]
    anomalies: str
    correlated_metrics: str
    root_cause: str
    summary: str
    recommended_actions: List[str]
    human_approved: bool
    messages: Annotated[List[str], operator.add]

def log_analyzer_agent(state: IncidentState) -> IncidentState:
    docs = retriever.invoke(state["incident_description"])
    log_texts = [doc.page_content for doc in docs]
    response = llm.invoke([
        SystemMessage(content="You are a Log Analyzer agent. Analyze the provided logs and identify anomalies, error patterns, and timeline of events. Be specific about timestamps, services, and error types."),
        HumanMessage(content=f"Incident: {state['incident_description']}\n\nRetrieved Logs:\n{chr(10).join(log_texts)}\n\nIdentify: 1) Key anomalies 2) Error patterns 3) Affected services 4) Timeline")
    ])
    return {**state, "retrieved_logs": log_texts, "anomalies": response.content, "messages": [f"[LogAnalyzer] Analyzed {len(log_texts)} log entries"]}

def metric_correlator_agent(state: IncidentState) -> IncidentState:
    response = llm.invoke([
        SystemMessage(content="You are a Metric Correlator agent. Correlate the anomalies found in logs with system metrics and deployment events. Identify causal chains."),
        HumanMessage(content=f"Incident: {state['incident_description']}\n\nAnomalies Found:\n{state['anomalies']}\n\nCorrelate with connection pool metrics, response time degradation, deployment events, and cascade failures.")
    ])
    return {**state, "correlated_metrics": response.content, "messages": ["[MetricCorrelator] Correlation analysis complete"]}

def root_cause_agent(state: IncidentState) -> IncidentState:
    response = llm.invoke([
        SystemMessage(content="You are a Root Cause Analysis expert. Use the 5-Why methodology. Be definitive and concise."),
        HumanMessage(content=f"Incident: {state['incident_description']}\n\nLog Anomalies:\n{state['anomalies']}\n\nMetric Correlations:\n{state['correlated_metrics']}\n\nProvide: 1. ROOT CAUSE (1-2 sentences) 2. Five-Why Chain 3. Contributing factors")
    ])
    return {**state, "root_cause": response.content, "messages": ["[RootCauseAgent] Root cause identified"]}

def human_approval_checkpoint(state: IncidentState) -> str:
    if state.get("human_approved", True):
        return "approved"
    return "rejected"

def summary_writer_agent(state: IncidentState) -> IncidentState:
    response = llm.invoke([
        SystemMessage(content="You are an Incident Summary Writer. Write clear, concise incident summaries. Format: Executive Summary, Timeline, Root Cause, Impact, Actions. End with RECOMMENDED_ACTIONS: followed by numbered items."),
        HumanMessage(content=f"Incident: {state['incident_description']}\nRoot Cause: {state['root_cause']}\nAnomalies: {state['anomalies']}")
    ])
    content = response.content
    actions = []
    if "RECOMMENDED_ACTIONS:" in content:
        actions_text = content.split("RECOMMENDED_ACTIONS:")[1].strip()
        actions = [line.strip() for line in actions_text.split("\n") if line.strip() and line.strip()[0].isdigit()]
    return {**state, "summary": content, "recommended_actions": actions or ["Review logs", "Scale database", "Enable circuit breaker"], "messages": ["[SummaryWriter] Incident summary generated"]}

def build_graph():
    graph = StateGraph(IncidentState)
    graph.add_node("log_analyzer", log_analyzer_agent)
    graph.add_node("metric_correlator", metric_correlator_agent)
    graph.add_node("root_cause_reasoner", root_cause_agent)
    graph.add_node("summary_writer", summary_writer_agent)
    graph.set_entry_point("log_analyzer")
    graph.add_edge("log_analyzer", "metric_correlator")
    graph.add_edge("metric_correlator", "root_cause_reasoner")
    graph.add_conditional_edges("root_cause_reasoner", human_approval_checkpoint, {"approved": "summary_writer", "rejected": END})
    graph.add_edge("summary_writer", END)
    return graph.compile()

app_graph = build_graph()

def run_analysis(incident_description: str, human_approved: bool = True) -> dict:
    initial_state: IncidentState = {
        "incident_description": incident_description,
        "retrieved_logs": [],
        "anomalies": "",
        "correlated_metrics": "",
        "root_cause": "",
        "summary": "",
        "recommended_actions": [],
        "human_approved": human_approved,
        "messages": []
    }
    return app_graph.invoke(initial_state)
