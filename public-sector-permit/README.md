# Public-sector permit (UAPF example)

This example models a generic public-sector permit process (e.g. building permit, business license), with:

- **BPMN** for the application intake and review workflow.
- **DMN** for formal decision criteria (eligibility and compliance checks).
- Optional **CMMN** for managing complex, long-running cases.

Key elements:

1. Applicant submits a permit request.
2. Administration validates the application and required documents.
3. DMN rules evaluate compliance and legal criteria.
4. Manual review and multi-level approvals are performed when necessary.
5. A permit is granted or refused with a clear explanation.

Use this package as a reference for modelling public-sector workflows where legal rules and multi-stage approvals matter.
