package com.incident.analyzer.service;
import com.incident.analyzer.model.AnalyzeRequest;
import com.incident.analyzer.model.AnalyzeResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;
@Service
public class IncidentService {
    private final RestTemplate restTemplate;
    private final String pythonAgentUrl;
    public IncidentService(RestTemplate restTemplate, @Value("${python.agent.url}") String pythonAgentUrl) {
        this.restTemplate = restTemplate;
        this.pythonAgentUrl = pythonAgentUrl;
    }
    public AnalyzeResponse analyzeIncident(AnalyzeRequest request) {
        Map<String, Object> payload = new HashMap<>();
        payload.put("incident_description", request.getIncidentDescription());
        payload.put("human_approved", request.getHumanApproved());
        return restTemplate.postForObject(pythonAgentUrl + "/analyze", payload, AnalyzeResponse.class);
    }
}
