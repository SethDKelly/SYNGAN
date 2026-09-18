# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A through 013-F are complete, and 013-G is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-F-execution-attempt-fencing-idempotency-checkpoint-cancellation-recovery-admission-reconciliation.md`
- `docs/architecture/phase-013-f-execution-attempt-fencing-idempotency-checkpoint-cancellation-recovery-admission-reconciliation.md`
- `docs/architecture/phase-013-e-strategy-runtime-dependency-authorization-secrets-distribution-reconciliation.md`
- `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`
- `docs/authority/reproducibility-contract.md`
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
013-G                                NEXT ELIGIBLE
R1 architecture reconciliation       DOWNSTREAM / IN PROGRESS
implementation readiness             NOT READY
implementation start                 NOT STARTED
implementation next                  NOT YET
```

## Primary authority rule

> **Completed concept design and completed Phase 013 reconciliation decisions are upstream authority for unreconciled architecture. Retained architecture, code, tests and provider models may expose a genuine defect, but they may not redefine semantics merely to preserve historical choices.**

Only a demonstrated `AR-9` genuine upstream contradiction may justify `UPSTREAM-REOPEN`. Use the smallest-authority reopen rule and revalidate the material blast radius.

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

These are documentation/design classifications, not runtime enums/resources/issues.

## Reconciled architecture invariants through 013-F

Preserve:

- architecture machinery downstream of semantic ownership;
- stable logical identity and exact historical bindings independent of provider/runtime identity;
- persistence as durability, not generic semantic CRUD;
- physical/provider/runtime facts only at their actual evidentiary strength;
- non-regressing recovery authority after potentially regressive restore;
- Data Meaning / Constraint / Generation / Strategy / Evaluation ownership boundaries for structured topology;
- sealed physical subject distinct from Generation semantic completion;
- Strategy/method semantics distinct from implementation binding/runtime identity;
- dependency availability distinct from identity/integrity/trust/compatibility/authorization;
- no hidden runtime acquisition, dependency substitution, remote fallback or egress expansion;
- every material runtime role satisfying compatible exact closure;
- runtime capabilities/secrets as current operational material, not durable semantic authority;
- one stable Execution distinct from subordinate Attempts and provider jobs;
- Attempt physical observation distinct from current framework mutation authority;
- write authority composed from current recovery frontier, Execution/Attempt authority, resource-local preconditions where needed, and current action authorization;
- lease/heartbeat as liveness coordination, not stale-writer proof;
- operation-scoped idempotency that never grants stale authority;
- immutable committed checkpoints separate from current resume eligibility and semantic results;
- regressive recovery quarantine plus fresh stale-writer exclusion before ordinary writes resume;
- cancellation intent distinct from terminal operational outcome;
- late provider success after cancellation/fencing unable to restore semantic authority;
- admission as current operational eligibility distinct from semantic readiness, authorization, runtime closure, queue/capacity and mutation authority;
- resource pressure unable to silently weaken committed semantic/security contracts;
- bounded operational history rather than a shadow provider telemetry store;
- multiple legitimate Evidence findings remaining compatible with retry-safe operational result establishment.

## 013-G next scope

013-G reconciles Evaluation, Evidence, Provenance, historical query, Reproducibility, disclosure and external-governance boundaries.

It must verify at least:

- Evaluation method/runtime observations remain distinct from Evaluation semantic validity;
- Evidence identity, claim strength, applicability and current status remain distinct from provider/runtime success;
- retries/recovery do not duplicate or overwrite one semantic finding merely because method work reran;
- multiple Evidence findings from one Evaluation remain supported where independently interpretable;
- Generation completion may consume exact sufficient Evidence but Evidence never owns Generation completion;
- Provenance remains typed relationship authority and does not absorb owner payloads, Execution logs, security audit or provider lineage as a shadow truth store;
- historical query composes exact owner truth without creating a new current-state owner;
- reconstructed/partial/unknown/unavailable historical knowledge remains truthfully qualified;
- Reproducibility remains a derived cross-cutting assessment rather than a concept/resource/synchronization;
- current disclosure/authorization may withhold details without rewriting canonical history;
- empirical privacy/disclosure-risk Evidence remains distinct from formal privacy guarantees and external release/use approval;
- external governance decisions remain external unless future independent product purpose triggers renewed concept discovery;
- M8 future-scope areas receive no placeholder governance/publication/privacy subsystems.

## Synchronization carry-forward

Current synchronization authority is `15 historical IDs / 13 active synchronizations`.

```text
SYNC-08  retired — Generation-local output lifecycle
SYNC-15  historical/reclassified — Reproducibility contract
```

013-F identifies remaining current-looking historical cross-references in Execution/operational/scale documents as explicit 013-I corpus-cleanup obligations. They are not current synchronization authority.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, persistence schemas, distributed-data implementation, runtime adapters, dependency/security integrations, Execution/Attempt scheduling, fencing/idempotency/checkpoint/recovery/admission mechanisms, Evidence/Provenance implementations, provider adapters, public API stabilization, package refactoring, benchmarks or executable conformance work.

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

**013-G — Evaluation, Evidence, Provenance, Historical Query, Reproducibility, Disclosure & External-Governance Boundary Reconciliation** is next eligible.
