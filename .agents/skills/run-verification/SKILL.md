---
name: run-verification
description: Run or guide the lowest appropriate deterministic SYNGAN repository verification for the selected task and report evidence faithfully. A1 by default; does not authorize fixes or external actions.
---

# Run verification

## Boundary

This workflow is A1 by default even though it may execute safe non-destructive repository checks. If the enclosing human task also authorizes fixes, those edits remain inside that A2 task.

## Workflow

1. Resolve the selected task/change and the claims that require evidence.
2. Prefer repository-owned commands and profiles over remembered or provider-specific commands.
3. Select the lowest-cost verification that covers the changed claim; use `python tools/verify.py portable` for the standard portable gate and narrower profiles when sufficient.
4. Run only safe non-destructive checks available in the environment.
5. Capture pass/fail/skipped/unavailable results and exact limitations.
6. Distinguish documentation/process conformance, executable product tests, provider/runtime qualification, and production evidence.
7. Report failures against the requirement. Do not weaken or rewrite a requirement to convert failure into success.
8. Stop for explicit authorization before A3 external/destructive/privileged actions.

## Output

Report checks selected and why, commands/profiles used, pass/fail/skipped/unavailable evidence, coverage limitations, and bounded remediation needs.

## Stop conditions

Do not deploy, mutate external systems, retrieve secrets, fix failures without enclosing A2 authority, or treat a passing check as authority beyond the proposition it validates.
