package com.incident.analyzer.controller;
import com.incident.analyzer.model.AnalyzeRequest;
import com.incident.analyzer.model.AnalyzeResponse;
import com.incident.analyzer.service.IncidentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/api/v1/incidents")
@CrossOrigin(origins = "*")
public class IncidentController {
    private final IncidentService incidentService;
    public IncidentController(IncidentService incidentService) { this.incidentService = incidentService; }
    @PostMapping("/analyze")
    public ResponseEntity<AnalyzeResponse> analyzeIncident(@RequestBody AnalyzeRequest request) {
        return ResponseEntity.ok(incidentService.analyzeIncident(request));
    }
    @GetMapping("/health")
    public ResponseEntity<String> health() { return ResponseEntity.ok("Incident Analyzer is running"); }
}
