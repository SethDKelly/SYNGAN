---
name: execute-selected-work
description: Execute one explicitly human-selected SYNGAN repository task or phase slice to verified completion within A2 scope, including necessary support edits, then stop. Never selects the next work item.
---

# Execute selected work

## Boundary

This is A2 bounded repository work. The human-selected task is the scope anchor.

## Workflow

1. Resolve task scope with root `AGENTS.md`, current status, the active work record/package, and the smallest canonical owners.
2. Classify the work under A1-A4 and the applicable repository change class. During Phase 016, preserve P16-0..P16-4 discipline.
3. Identify explicit exclusions and necessary supporting changes before editing.
4. Make the smallest implementation/documentation/configuration changes that complete the selected task.
5. Update directly stale tests, fixtures, status, references, OKF routing, or documentation when required for internal consistency.
6. Run the lowest appropriate repository verification and address in-scope failures without weakening requirements.
7. If P16-3/P16-4 or another A4 conflict appears, stop the affected change and use the governing reopen path.
8. If an A3 action becomes necessary, stop for task-specific authorization before performing it.
9. Record accurate completion evidence for the selected task.
10. Report the next eligible dependency as information only and stop.

## Supporting-change rule

An adjacent change is allowed only when leaving it unchanged would make the selected task incomplete, inconsistent, or unverifiable and it does not independently start another work item.

## Stop conditions

Do not choose the next phase/backlog item, perform unrelated cleanup, broaden privileges, deploy, or reinterpret accepted semantics merely to make implementation easier.
