package com.incident.analyzer.model;
import lombok.Data;
@Data
public class AnalyzeRequest {
    private String incidentDescription;
    private Boolean humanApproved = true;
}
