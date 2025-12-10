# Incident management (UAPF example)

This example models an IT incident management flow with:

- **CMMN** for the overall incident case and SLA-driven tasks.
- **BPMN** for structured activities such as triage and resolution.
- Optional **DMN** for priority calculation or escalation rules.

Scenario highlights:

- Incidents are logged via monitoring or user tickets.
- A case is opened, classified, and prioritized.
- Structured BPMN flows handle triage and resolution.
- Escalation to higher-level support occurs when SLAs are at risk.

The `.uapf` package demonstrates how to mix CMMN and BPMN to represent both the long-running case and concrete activities.
