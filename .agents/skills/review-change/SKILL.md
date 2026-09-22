---
name: review-change
description: Review a SYNGAN change against current canonical authority, selected scope, security/trust boundaries, and executable evidence. Findings do not authorize fixes. Read-only A1 workflow.
---

# Review change

## Boundary

This is A1 review work. Finding a defect does not authorize repository edits unless the human separately selects A2 fix work.

## Workflow

1. Resolve the intended change and human-selected scope.
2. Inspect the actual changed files/diff rather than relying on a prose summary.
3. Resolve affected current owners and exact stable references where available.
4. Check for semantic or architecture drift, authority duplication, scope expansion, and P16/A1-A4 class laundering.
5. Check least-privilege, secret/sensitive-data, untrusted-content, and external-action assumptions.
6. Check that tests/fixtures/validators establish the claims the change makes.
7. Check status/reference/OKF/documentation consistency only where materially affected.
8. Distinguish confirmed defects, questions, missing evidence, provider capability gaps, and style preferences.

## Output

For each material finding report impact, exact file/location, governing authority when known, why it matters, and bounded remediation direction. State validation gaps or that no material findings were found.

## Stop conditions

Do not edit files, invent requirements, or treat tool/model output as independent evidence.
