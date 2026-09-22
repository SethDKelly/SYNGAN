# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design and Phases 013-015 are complete; C0-C9 are active/passing. Phase 016 pre-implementation hardening is ACTIVE. 016-A through 016-H are complete; 016-I is AUTHORIZED / ACTIVE. No product/provider/runtime delivery program is authorized.**

## Start with

For most tasks, read only:

1. docs/authority/current-repository-status.md
2. docs/index.md
3. the smallest current owner routed from docs/authority/canonical-knowledge-ownership-map.md
4. docs/phases/016/index.md only when the task concerns active Phase 016 work

Use docs/history/ only for rationale, provenance, supersession analysis, or reconstruction. Do not treat search rank or historical detail as current authority.

When a `syngan://...` knowledge reference is supplied, resolve it exactly through the repository stable-reference registry/resolver. Do not guess a path from the reference text or substitute search results for failed resolution.

## Agent authority and scope

Canonical agent operating authority is [Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries](docs/authority/agent-authority-human-directed-scope-security-trust.md).

Use its A1-A4 model:

- A1 review/plan work is read-only unless edits are also requested.
- A2 may complete the explicitly selected repository task plus directly necessary supporting changes.
- A3 external/destructive/privilege-expanding/scope-expanding actions require specific human authorization and normal environment/repository gates.
- A4 semantic/architecture/product-scope changes require the governing reopen/change-control path.

A1-A4 describe action/consequence authority; P16-0..P16-4 describe Phase 016 change impact. Do not launder a higher-impact change through a lower class.

Completing the selected work does not authorize the next phase, subphase, backlog item, or product program.

## Context and portable workflows

Bounded context and tool portability are governed by [Agent Context, Portable Workflows & Tool Adapter Contract](docs/authority/agent-context-portable-workflows-tool-adapters.md).

Use exact `syngan://...` resolution when a stable reference is known; otherwise route through `docs/index.md` to the smallest current owner. Loading another file requires a concrete task question it answers.

Canonical reusable workflows live under `.agents/skills/`: `resolve-context`, `resolve-reference`, `execute-selected-work`, `review-change`, `run-verification`, and `update-traceability`. Skills are procedures only; invoking one does not expand the human-selected task or change A1-A4 authority.
## Agentic conformance

Repository agentic/documentation conformance is governed by [Agentic Conformance, Negative Controls, Drift Detection & CI](docs/authority/agentic-conformance-policy.md).

Use `python tools/run_agentic_conformance.py` for deterministic repository configuration checks. A PASS does not prove product/runtime health or provider runtime compatibility, and a FAIL does not authorize edits outside the human-selected task.
## Implementation packages and ADR change control

Prospective material implementation packages are governed by [Implementation Package, Traceability & ADR Change Control](docs/implementation/implementation-package-traceability-adr-change-control.md).

A package is scope/evidence metadata, never authorization. Class 1/2 work traces current `syngan://...` authority to code/test evidence; Class 3/4 conflicts stop and reopen the smallest upstream owner. Architecture ADRs under `docs/decisions/` preserve rationale and may not be rewritten by ordinary implementation to make code appear conformant.
## Durable authority rules

- One proposition should have one preferred current owner.
- Indexes route; they do not replace semantic owners.
- Historical code, tests, phase records, provider behavior, or implementation cost may expose a problem but cannot independently create product semantics.
- Reopen only the smallest owning authority when a genuine contradiction exists.
- Human-selected work defines the task envelope; do not self-authorize the next phase or product program.
- Provider facts may be consumed only at the evidentiary strength they establish.
- Do not turn the complete concept catalog into a mandatory universal runtime pipeline.
- Do not hide a qualifier whose omission could change an actor's immediate semantic decision or make current state appear stronger than its owner supports.

## Phase 016 boundary

Phase 016 may harden documentation topology, OKF routing, agentic-development governance, deterministic context discovery, implementation-package discipline, development security/supply-chain policy, and readiness evidence.

Phase 016 does **not** authorize:

- new product semantics;
- provider/runtime integrations;
- new public product APIs;
- deployment/IaC;
- unsupported scale/support claims;
- automatic post-Phase-016 implementation.

Current status and subphase authorization are owned by docs/authority/current-repository-status.md.

## Current next boundary

**016-I — Dependency / Supply-Chain / Secrets, Compatibility / Benchmark / API-Versioning Preflight is AUTHORIZED / ACTIVE. 016-J remains NOT AUTHORIZED.**
