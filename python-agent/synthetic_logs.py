SYNTHETIC_LOGS = [
    {
        "id": "log001",
        "text": "ERROR 2024-01-15 03:42:11 [payment-service] Connection pool exhausted. Max connections: 100, Active: 100, Pending: 47. Database: payments-db host: db-primary:5432",
        "metadata": {"service": "payment-service", "level": "ERROR", "category": "database"}
    },
    {
        "id": "log002",
        "text": "WARN 2024-01-15 03:41:55 [payment-service] Slow query detected. Query took 8432ms. Table: transactions. Query: SELECT * FROM transactions WHERE user_id=? AND status='pending'",
        "metadata": {"service": "payment-service", "level": "WARN", "category": "performance"}
    },
    {
        "id": "log003",
        "text": "ERROR 2024-01-15 03:42:15 [api-gateway] Upstream timeout. Service: payment-service. Timeout after 5000ms. Request: POST /api/v1/payments",
        "metadata": {"service": "api-gateway", "level": "ERROR", "category": "timeout"}
    },
    {
        "id": "log004",
        "text": "ERROR 2024-01-15 03:42:20 [order-service] Payment validation failed. payment-service returned 503 Service Unavailable. Order ID: ORD-98234 will be retried.",
        "metadata": {"service": "order-service", "level": "ERROR", "category": "cascade"}
    },
    {
        "id": "log005",
        "text": "CRITICAL 2024-01-15 03:43:00 [alertmanager] P1 Alert fired: payment-service error rate > 50% for 2 minutes. Current rate: 78%. SLO breach imminent.",
        "metadata": {"service": "alertmanager", "level": "CRITICAL", "category": "alert"}
    },
    {
        "id": "log006",
        "text": "INFO 2024-01-15 03:40:00 [deployment-service] Deployment started: payment-service v2.4.1 -> v2.4.2. Change: increased max_connections from 50 to 100. Rolled out to prod.",
        "metadata": {"service": "deployment-service", "level": "INFO", "category": "deployment"}
    },
    {
        "id": "log007",
        "text": "ERROR 2024-01-15 03:42:30 [payment-service] HikariPool-1 - Connection is not available, request timed out after 30000ms.",
        "metadata": {"service": "payment-service", "level": "ERROR", "category": "database"}
    },
    {
        "id": "log008",
        "text": "WARN 2024-01-15 03:41:00 [db-primary] High connection count warning. Current connections: 95/100. Consider scaling or optimizing connection usage.",
        "metadata": {"service": "db-primary", "level": "WARN", "category": "database"}
    },
    {
        "id": "runbook001",
        "text": "RUNBOOK: Database connection pool exhaustion. Symptoms: HikariPool timeout errors, slow queries, upstream timeouts. Resolution: 1) Check active connections with SELECT count(*) FROM pg_stat_activity. 2) Kill long-running queries. 3) Restart connection pool. 4) Scale database replicas if persistent.",
        "metadata": {"service": "runbook", "level": "INFO", "category": "runbook"}
    },
    {
        "id": "runbook002",
        "text": "RUNBOOK: Cascading service failure. When payment-service is down, order-service and api-gateway will show 503 errors. Mitigation: Enable circuit breaker, redirect traffic to fallback payment processor.",
        "metadata": {"service": "runbook", "level": "INFO", "category": "runbook"}
    }
]
