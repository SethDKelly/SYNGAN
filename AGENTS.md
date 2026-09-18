# SYNGAN Agent Instructions

These instructions apply repository-wide to automated coding/documentation agents.

## Current posture

**Jackson concept design is complete for the current product scope. Phase 013 architecture reconciliation is ACTIVE; 013-A through 013-G are complete, and 013-H is next. Implementation remains held.**

Start with:

- `docs/index.md`
- `docs/problem/problem-purpose.md`
- `docs/authority/design-methodology.md`
- `docs/authority/jackson-design-completion-implementation-hold.md`
- `docs/authority/jackson-methodology-completion-matrix.md`
- `docs/authority/phase-013-architecture-reconciliation-authority.md`
- `docs/phases/013/index.md`
- `docs/phases/013/013-G-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-external-governance-reconciliation.md`
- `docs/architecture/phase-013-g-evaluation-evidence-provenance-history-reproducibility-disclosure-governance-reconciliation.md`
- `docs/architecture/phase-013-f-execution-attempt-fencing-idempotency-checkpoint-cancellation-recovery-admission-reconciliation.md`
- `docs/authority/reproducibility-contract.md`
- `docs/authority/operational-authority-continuity-regressive-recovery-contract.md`
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
013-H                                NEXT ELIGIBLE
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

## Reconciled architecture invariants through 013-G

Preserve:

- architecture machinery downstream of semantic ownership;
- stable logical identity and exact historical bindings independent of provider/runtime identity;
- persistence as durability, not generic semantic CRUD;
- physical/provider/runtime facts only at their actual evidentiary strength;
- non-regressing recovery authority after potentially regressive restore;
- physical data/manifest/seal state distinct from Generation semantic completion;
- Strategy/method semantics distinct from implementation binding/runtime identity;
- no hidden runtime acquisition, dependency substitution, remote fallback or egress expansion;
- every material runtime role satisfying compatible exact closure;
- runtime capabilities/secrets as current operational material, not durable semantic authority;
- one stable Execution distinct from subordinate Attempts and provider jobs;
- Attempt physical observation distinct from current framework mutation authority;
- operation-scoped idempotency plus fencing rather than exactly-once physical execution;
- immutable checkpoints separate from current resume eligibility and semantic results;
- cancellation intent distinct from terminal operational outcome;
- admission as current operational eligibility, not semantic readiness or write authority;
- runtime Evaluation results distinct from semantically valid Evaluation completion and Evidence establishment;
- retry-safe independently interpretable Evidence findings;
- immutable Evidence finding semantics distinct from current applicability;
- Evidence claim strength bounded by actual method/scope/coverage/uncertainty;
- Generation ownership of its exact Evidence-based completion basis;
- Provenance as typed relationship authority with low authority fan-out;
- direct/reconstructed/partial/unknown historical knowledge distinct from current resolution/disclosure state;
- derived query/search/report projections as non-authoritative;
- historical comparison unable to invent causality/superiority;
- Reproducibility historical supportability distinct from current feasibility and actor-visible assessability;
- disclosure/redaction as current view authority, including protection of existence/graph shape/counts;
- empirical privacy Evidence distinct from formal privacy guarantees;
- external governance decisions remaining external rather than hidden SYNGAN approval state;
- external lineage/metadata observations remaining non-canonical until validated through SYNGAN authority.

## 013-H next scope

013-H reconciles deployment, scalability, observability, portability, compatibility and platform integration.

It must verify at least:

- the portable Python/Spark core remains independent of any one Databricks/Kubernetes/cloud/provider control plane;
- platform support means the required semantic/runtime/recovery/security guarantees can actually be preserved, not merely that Spark/Python can launch;
- provider `SUCCESS`, job/run identity, model/artifact registration, catalog state and lineage remain evidence/integration facts rather than semantic owners;
- deployment capability negotiation can limit or reject workloads without silently weakening Strategy, Generation, Evaluation, Evidence or security semantics;
- telemetry/logging/metrics remain observability rather than canonical Execution/Evidence/Provenance state unless an owning transition promotes a bounded fact;
- loss of optional telemetry can degrade observability without fabricating semantic failure, while mandatory audit/monitoring policy remains explicit;
- scale/support claims remain workload-dimensional rather than one row-count/provider label;
- no ordinary path requires source/output/model/task telemetry to be collected centrally merely for correctness;
- platform adapters preserve exact identity, distributed runtime closure, fencing, recovery, checkpoint, candidate, Evidence/history and disclosure boundaries;
- provider-specific guarantees are consumed only at the strength actually established;
- unsupported provider guarantees become explicit `limited / incompatible / indeterminate` profiles rather than semantic weakening;
- platform portability does not require lowest-common-denominator semantics;
- external lineage/catalog/observability integration remains projection/evidence, not canonical authority;
- no future M8 governance/privacy/publication/session/economic subsystem is introduced as a deployment placeholder.

## Synchronization carry-forward

Current synchronization authority is `15 historical IDs / 13 active synchronizations`.

```text
SYNC-08  retired — Generation-local output lifecycle
SYNC-15  historical/reclassified — Reproducibility contract
```

Remaining current-looking pre-Phase-009 synchronization references are explicit 013-I corpus-cleanup obligations. They are not current synchronization authority.

## Durable quality rules

Decision-material disclosure:

> **Do not hide a qualifier whose omission could change the actor's immediate semantic decision or make current state appear stronger than its owner supports.**

Provider evidence:

> **Consume provider facts only at the evidentiary strength they actually establish.**

Future rediscovery:

> **New independent product-facing purpose/state/actions/lifecycle returns to concept discovery before architecture or implementation.**

## Implementation boundary

Phase 013 is design/reconciliation only.

Do not begin production behavior, migrations, schemas, data-plane implementation, runtime/security integrations, Execution/recovery machinery, Evidence/Provenance/history services, platform adapters, IaC/deployment integration, public API stabilization, package refactoring, benchmarks or executable conformance work.

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

**013-H — Deployment, Scalability, Observability, Portability, Compatibility & Platform-Integration Reconciliation** is next eligible.
