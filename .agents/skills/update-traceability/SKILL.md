---
name: update-traceability
description: Update a selected SYNGAN implementation package with current authority, code, test, and evidence traceability already established by a human-authorized A2 task. Never creates behavior, authorization, or architecture authority from metadata.
---

# Update traceability

## Boundary

This is an A2 supporting workflow. Use it only inside an explicitly selected implementation/change task or when traceability maintenance is itself explicitly selected.

An implementation package is an evidence/scope container, not an authorization source.

## Workflow

1. Identify the selected task and applicable Class 0–4 change classification.
2. Resolve the package contract through `syngan://implementation/package-contract`.
3. Identify the selected `IPKG-####` manifest when one exists. Do not invent a package merely because future work is visible.
4. Resolve every current `syngan://...` authority reference exactly through the stable-reference resolver. Resolver success proves routing only, not implementation.
5. Inspect the implementation paths, verification paths, commands, CI evidence, compatibility/migration effects, ADR references, unresolved items, and explicit non-claims actually supported by the selected task.
6. Update obligation evidence states only to the level actually proven: `planned`, `implemented`, `verified`, `blocked`, or justified `not_applicable`.
7. For Class 2, preserve explicit compatibility and migration assessment even when the result is no impact.
8. If a Class 3/4 conflict appears, mark the affected work blocked and stop for the smallest-owner reopen. Do not edit an architecture ADR to make implementation appear conformant.
9. Run `python tools/validate_implementation_packages.py` and the relevant repository verification for the changed implementation behavior.
10. Mark a package complete only when its material obligations, verification evidence, unresolved items, and package validator satisfy the canonical completion rule.

## Evidence rule

Code existence, a stable reference, documentation prose, model confidence, an ADR, or an unrelated passing check is not sufficient implementation evidence.

History may explain rationale but does not replace current authority or current implementation/test evidence.

## Output

Report the package/traceability artifact changed, authority refs and section locators, implementation and verification evidence added, evidence-state changes, Class 0–4 classification, ADR references, unresolved/non-claimed items, and validation performed.

## Stop conditions

Do not:

- create or expand implementation scope from package metadata;
- mark unverified obligations verified;
- mark a package complete with blocking/unresolved work;
- continue Class 3/4 work as ordinary implementation;
- modify architecture ADR meaning without an explicitly authorized architecture reopen;
- start the next package, phase, backlog item, deployment, or provider/runtime integration.
