# uapf-examples

Canonical **UAPF example packages** for multiple industries and scenarios.

These examples are intended to:

- Demonstrate idiomatic use of UAPF across workflows, decisions, and cases.
- Serve as fixtures for SDKs, engines, and viewers.
- Act as reference material for architects designing their own `.uapf` packages.

---

## Repository layout

Each top-level folder corresponds to a **scenario**, for example:

- `acme-docflow/`
  Illustrative government / enterprise **document flow**:
  - Intake → classification → routing → approvals → archival.
  - Shows how BPMN, DMN, and CMMN can be combined.
  - Demonstrates agent roles and MCP tools used at key steps.

- `rup-lifecycle/`
  Example of a **software development lifecycle** based on iterative methods:
  - Inception → elaboration → construction → transition.
  - Captures decision points and case handling around iterations.

- [`loan-approval/`](https://github.com/UAPFormat/uapf-examples/tree/main/loan-approval)
  Simple **retail loan approval** flow:
  - BPMN for intake → data collection → approval/rejection.
  - DMN for eligibility and risk guidance.
  - Agent metadata for applicant, loan officer, and risk engine.

- [`incident-management/`](https://github.com/UAPFormat/uapf-examples/tree/main/incident-management)
  IT **incident response** example:
  - CMMN to model the case and SLA milestones.
  - BPMN for triage, prioritization, escalation, and closure.
  - DMN for computing incident priority.

- [`public-sector-permit/`](https://github.com/UAPFormat/uapf-examples/tree/main/public-sector-permit)
  Generic **public administration permit** process:
  - BPMN for intake, document validation, committee review, and decision.
  - DMN for compliance and eligibility checks.
  - Roles for applicants, case workers, legal officers, and committees.

Each folder contains a ready-to-zip structure like:

```text
<scenario>.uapf/
  manifest.json
  process/
    *.bpmn.xml
    *.cmmn.xml
  decisions/
    *.dmn.xml
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

(Exact filenames may vary per example.)

---

## Building `.uapf` archives

Use the helper script:

```bash
python build_examples.py
```

This will create `.uapf` zip archives (e.g. `acme-docflow.uapf`) that can be:

- Opened by:
  - [`uapf-python`](https://github.com/UAPFormat/uapf-python)
  - [`uapf-typescript`](https://github.com/UAPFormat/uapf-typescript)
- Uploaded into:
  - [`uapf-viewer`](https://github.com/UAPFormat/uapf-viewer)
- Run by:
  - `uapf-engine` / `uapf-mcp` (reference implementations)

---

## Usage ideas

- Use as **fixtures** in your own UAPF implementation or SDK.
- Adapt an example as a starting point for your own process.
- Compare different modelling styles between BPMN/DMN/CMMN in one package.

---

## Contributing

Contributions are welcome:

- New scenarios (e.g., credit scoring, KYC, procurement).
- Improvements to existing flows, decisions, and agent mappings.
- Documentation that links examples to real-world narratives.

---

## License

MIT – see [`LICENSE`](LICENSE).

