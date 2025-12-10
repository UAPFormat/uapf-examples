# Loan approval process (UAPF example)

This example shows a simple retail loan approval process, combining:

- **BPMN** for the end-to-end workflow (from application intake to decision).
- **DMN** for eligibility and risk decisions.
- Optional **agent metadata** for mapping human and AI roles.

## Scenario summary

A customer submits a loan application through a digital channel. The process:

1. Validates the application and collects missing data.
2. Calls a DMN decision table to determine basic eligibility.
3. Routes to manual underwriting when required.
4. Produces an approval or rejection, with clear reasons.

## Package structure

```text
loan-approval.uapf/
  manifest.json
  process/
    loan-approval.bpmn.xml
  decisions/
    loan-eligibility.dmn.xml
    glossary.json
  agents/
    roles.json
    capabilities.json
    bindings.json
  integration/
    mcp-tools.json
    a2a-schemas.json
    api-endpoints.json
  metadata/
    version.json
    provenance.json
    compliance.json
```

Use this package as a reference for how to structure financial-services processes that combine BPMN and DMN in a single UAPF artifact.
