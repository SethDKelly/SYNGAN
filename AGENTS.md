# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A through 013-H are complete, and 013-I is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-H-deployment-scalability-observability-portability-compatibility-platform-integration-reconciliation.md`
- `docs/architecture/phase-013-h-deployment-scalability-observability-portability-compatibility-platform-integration-reconciliation.md`
- `docs/architecture/index.md`

## Current state

```text
accepted concepts                    11
active synchronizations              13
Phase 012                            COMPLETE
A1-H2                                CURRENTLY CLOSED
Jackson concept design               COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                            ACTIVE
013-A                                COMPLETE
013-B                                COMPLETE
013-C                                COMPLETE
013-D                                COMPLETE
013-E                                COMPLETE
013-F                                COMPLETE
013-G                                COMPLETE
013-H                                COMPLETE
013-I                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and completed Phase 013 reconciliation decisions are upstream authority for unreconciled retained material. Legacy architecture, ADRs, code, tests and provider models may expose a genuine defect, but they may not redefine semantics merely to preserve historical choices.**

Only a demonstrated `AR-9` genuine upstream contradiction may justify `UPSTREAM-REOPEN`.

## Phase 013 finding discipline

Use `AR-0..AR-9`, `AMAT-0..AMAT-3`, and:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

These are design/documentation classifications, not runtime enums/resources/issues.

## Reconciled architecture invariants through 013-H

Preserve:

- architecture machinery downstream of semantic ownership;
- stable logical identity/exact historical bindings independent of provider/runtime identity;
- persistence as durability rather than generic semantic CRUD;
- physical/provider/runtime/telemetry facts only at their actual evidentiary strength;
- non-regressing recovery authority after potentially regressive restore;
- sealed physical state distinct from Generation semantic completion;
- Strategy/method semantics distinct from implementation binding/runtime identity;
- no hidden runtime acquisition, dependency substitution, remote fallback or egress expansion;
- every material runtime role satisfying compatible exact closure;
- one stable Execution distinct from Attempts/provider jobs;
- Attempt observation distinct from current mutation authority;
- scoped idempotency plus fencing rather than exactly-once physical execution;
- checkpoint durability distinct from resume eligibility and semantic result;
- cancellation intent distinct from terminal outcome;
- admission as current operational eligibility rather than semantic readiness/write authority;
- Evaluation semantic validity distinct from runtime success;
- retry-safe independently interpretable Evidence findings;
- immutable Evidence semantics distinct from current applicability;
- Evidence claim strength bounded by actual method/scope/coverage/uncertainty;
- Generation owning its Evidence-based completion transition/basis;
- Provenance as typed relationship authority with low authority fan-out;
- direct/reconstructed/partial/unknown historical knowledge distinct from current resolution/disclosure;
- derived query/search/report projections as non-authoritative;
- Reproducibility historical supportability distinct from current feasibility and actor-visible assessability;
- disclosure/redaction as current view authority;
- empirical privacy Evidence distinct from formal privacy guarantees/release approval;
- external governance/lineage remaining outside canonical owner authority;
- provider/product identity distinct from actual capability guarantees;
- architecture-compatible, implemented, conformance-verified and scale-qualified support levels remaining distinct;
- multi-axis/directional compatibility rather than one global Boolean;
- provider HA/backup/restore beneath SYNGAN non-regressing recovery authority;
- multidimensional enterprise scale rather than row-count/Spark-name claims;
- canonical history, runtime observability and security audit as distinct lanes;
- capability-specific degraded operation rather than one global health owner;
- platform specialization behind portable contracts;
- private/offline/no-egress profiles without hidden public services.

## 013-I next scope

013-I is a **cross-architecture composition and corpus-authority closure pass**, not a new substantive architecture design phase.

It must:

- audit 013-B through 013-H together as one current architecture chain;
- detect cross-domain contradictions, duplicated ownership, hidden coordinators or incompatible terminology that local subgroup passes could have missed;
- finalize ADR-0001..ADR-0010 dispositions against the current architecture baseline;
- reconcile legacy Phase 004/006/007 `active/current/canonical` metadata and handoff wording that could still mislead;
- close M6 synchronization-count/ID/link drift, including stale `15`-rule, `SYNC-08` and `SYNC-15` references;
- correct accepted-concept synchronization tails where they still present historical `SYNC-15` as active;
- distinguish retained historical rationale from current authority rather than rewriting history indiscriminately;
- identify implementation-only choices that are still framed too strongly as architecture mandates;
- verify no M8 future-scope trigger has acquired placeholder services/state/APIs;
- create one explicit residual architecture-misfit register covering all AMAT-2/3, unresolved AR-3..AR-9, supersession obligations, ADR changes, M6, M8 and upstream-reopen decisions;
- leave R1 open for 013-J even if the register is clean.

013-I must not use corpus cleanup as a pretext to reopen completed concept design unless genuine AR-9 evidence emerges.

## Synchronization carry-forward

```text
historical synchronization IDs   15
active synchronizations           13
SYNC-08                           retired — Generation-local output lifecycle
SYNC-15                           historical/reclassified — Reproducibility contract
```

Current Phase 009 and completed Phase 013 authority control. Remaining legacy references are cleanup targets, not semantic inputs.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, schemas, data-plane implementation, runtime/security integrations, Execution/recovery machinery, Evidence/Provenance/history services, platform adapters, deployment automation, public API stabilization, package refactoring, benchmarks or executable conformance work.

```text
Phase 013  architecture reconciliation — ACTIVE
Phase 014  whole-design / implementation-readiness decision
Phase 015  implementation authority — FUTURE ONLY
```

Until Phase 014 positively passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## Current next boundary

**013-I — Cross-Architecture Composition, ADR/Legacy Contract Reconciliation, M6 Cleanup & Residual Architecture Misfit Register** is next eligible.
