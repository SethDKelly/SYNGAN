# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design and Phases 013-016 are complete; C0-C9 are active/passing. Phase 017 implementation-program planning is AUTHORIZED / ACTIVE — PLANNING ONLY. Product implementation execution, Phase 018+, product/provider/runtime delivery, and release remain NOT AUTHORIZED.**

## Start with

For most tasks, read only:

1. docs/authority/current-repository-status.md
2. docs/index.md
3. the smallest current owner routed from docs/authority/canonical-knowledge-ownership-map.md
4. docs/implementation/repository-implementation-readiness-residual-risk.md when the task concerns implementation-program readiness or carried residuals

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
## Autonomous delivery and runtime qualification

Cursor/Codex bounded implementation roles and runtime qualification are governed by [Cursor/Codex Autonomous Delivery Operating Model & Runtime Qualification](docs/implementation/cursor-codex-autonomous-delivery-runtime-qualification.md).

Documented provider compatibility is not runtime qualification. Cursor and Codex remain `pending_tool_in_loop` until real provider evidence satisfies the runtime-qualification profile. Agent/tool switching never changes package scope, authority, or success criteria.

## Success visibility and independent evaluation

Success visibility, holdout generation, evaluator independence, replay, contamination rotation, and anti-gaming are governed by [Success Visibility, Holdout Evaluation & Anti-Gaming Methodology](docs/implementation/success-visibility-holdout-evaluation-anti-gaming.md).

Normative requirements remain visible. Exact holdout realization may be selected/generated after candidate freeze; it may never introduce a hidden requirement. Once an exact holdout is exposed for repair, treat it as regression evidence and use a fresh holdout for renewed independent evaluation.

## v0.x package-MVP and release boundary

The bounded v0.x target, capability milestones, version-selection policy, release-state separation, and support non-claims are governed by [v0.x Package MVP Scope, Capability/Version Milestones & Release Boundaries](docs/implementation/v0x-package-mvp-scope-version-release-boundaries.md).

A qualified package MVP is not automatically a release candidate. Do not map phase numbers mechanically to package versions, close release/provider/scale residuals by scope exclusion, or imply production Spark/Databricks/provider support from the bounded Spark-capable MVP path.

## v0.x implementation program

Phase 018-025 dependency order, package decomposition, candidate freeze, and qualification-repair routing are governed by [v0.x Implementation Program — Phase 018-025 Dependency & Package Strategy](docs/implementation/v0x-implementation-program-phase-018-025-dependency-package-strategy.md).

A phase is not a package. Actual IPKG manifests are derived only by an explicitly selected phase start gate. Package/phase completion never self-authorizes later work. Phase 025 is evaluation-only and may not repair its frozen candidate.

## MVP qualification

Phase 025 completion testing, qualification-plan freeze, evidence ledger, holdout portfolio, decision rules, and repair/requalification discipline are governed by [v0.x MVP Completion Testing, Qualification & Independent Exit Method](docs/implementation/v0x-mvp-completion-testing-qualification-independent-exit.md).

Qualification is non-compensatory by blocking obligation. Aggregate scores cannot erase a failed requirement. Every candidate change invalidates the frozen identity, requires the anchor suite and affected evidence to rerun, and requires fresh H1 for contaminated affected obligations.

## v1 coarse program and rediscovery

The post-MVP candidate themes, deferrals, Phase 026 re-entry boundary, F-1..F-7 extension classification, and dormant M8 rediscovery gates are governed by [v1 Coarse Program Design, Deferrals & Rediscovery Triggers](docs/implementation/v1-coarse-program-deferrals-rediscovery-triggers.md).

Do not interpret v1 as an automatic 1.0.0 version, release, provider-support, or scale promise. Do not decompose Phase 027+ before Phase 026 consumes qualified v0.x evidence. F-5/M8 capability pressure must return to concept discovery before implementation planning.

## Agentic conformance

Repository agentic/documentation conformance is governed by [Agentic Conformance, Negative Controls, Drift Detection & CI](docs/authority/agentic-conformance-policy.md).

Use `python tools/run_agentic_conformance.py` for deterministic repository configuration checks. A PASS does not prove product/runtime health or provider runtime compatibility, and a FAIL does not authorize edits outside the human-selected task.
## Implementation packages and ADR change control

Prospective material implementation packages are governed by [Implementation Package, Traceability & ADR Change Control](docs/implementation/implementation-package-traceability-adr-change-control.md).

A package is scope/evidence metadata, never authorization. Class 1/2 work traces current `syngan://...` authority to code/test evidence; Class 3/4 conflicts stop and reopen the smallest upstream owner. Architecture ADRs under `docs/decisions/` preserve rationale and may not be rewritten by ordinary implementation to make code appear conformant.
## Engineering preflight

Dependency, CI supply-chain, checked-in secret, compatibility/benchmark-claim, and version/release hygiene are governed by [Engineering Preflight](docs/implementation/engineering-preflight-dependency-supply-chain-secrets-compatibility-benchmark-versioning.md).

Use `python tools/verify.py preflight` when those surfaces change. A PASS is repository engineering evidence only; it does not establish release authorization, a license/legal decision, current vulnerability clearance, provider certification, or scale qualification.
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

Phase 016 is complete. Its documentation, OKF, agentic-development, implementation-package, engineering-preflight, and readiness authorities remain current until superseded through normal change control.

Phase 016 completion does **not** authorize:

- new product semantics;
- provider/runtime integrations;
- new public product APIs;
- deployment/IaC;
- unsupported scale/support claims;
- automatic post-Phase-016 implementation.

Current status and subphase authorization are owned by docs/authority/current-repository-status.md.

## Current next boundary

**Phase 017 planning is active by explicit human authorization. 017-A through 017-H are COMPLETE; 017-I is NEXT ELIGIBLE / NOT AUTHORIZED. Product implementation execution and Phase 018+ remain NOT AUTHORIZED.**
