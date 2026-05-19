package com.incident.analyzer.model;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import java.util.List;
@Data
public class AnalyzeResponse {
    @JsonProperty("incident_description")
    private String incidentDescription;
    @JsonProperty("root_cause")
    private String rootCause;
    private String summary;
    @JsonProperty("recommended_actions")
    private List<String> recommendedActions;
    @JsonProperty("retrieved_logs")
    private List<String> retrievedLogs;
    private String anomalies;
    @JsonProperty("agent_messages")
    private List<String> agentMessages;
}
