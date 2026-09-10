---
type: Authority Index
title: SYNGAN Design Authority
status: active
---

# Design Authority

These documents define how SYNGAN design knowledge is created, interpreted, changed, and eventually implemented.

## Methodology and governance

- [Design methodology](design-methodology.md)
- [Documentation governance](documentation-governance.md)
- [Terminology policy](terminology-policy.md)
- [Source and provenance policy](source-provenance-policy.md)
- [Network and external dependency policy](network-external-dependency-policy.md)
- [Reproducibility contract](reproducibility-contract.md)

## Phase 006 promoted cross-cutting authority

- [Operational Authority Continuity & Regressive Recovery Contract](operational-authority-continuity-regressive-recovery-contract.md)
- [Self-Contained Execution & Runtime Distribution Closure Contract](self-contained-execution-runtime-distribution-closure-contract.md)
- [Enterprise Scale, Resource Admission, Approximation & Degraded Operation Contract](enterprise-scale-resource-admission-approximation-degraded-operation-contract.md)
- [Privacy, Disclosure Risk, Formal Guarantee & External Release Boundary Contract](privacy-disclosure-formal-guarantee-release-boundary-contract.md)
- [Structured-Data Topology & Relationship Semantics Contract](structured-data-topology-relationship-semantics-contract.md)

## Current design posture

[Phase 007 Design Continuation & Implementation Freeze](phase-007-design-continuation-implementation-freeze.md) is the current delivery-posture authority.

```text
concept / synchronization baseline   retained — 11 / 15
experience authority                 retained
architecture design                  ACTIVE
new production implementation        FROZEN
new executable architecture gates    FROZEN
```

Phase 007-A through 007-C remain historical/provisional bootstrap work. Existing source/tests/tooling may inform feasibility but do not outrank current design.

## Current architecture continuation

Completed current design groups:

- [007-D — Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](../architecture/phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](../architecture/phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md)
- [007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](../architecture/phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md)
- [007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](../architecture/phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md)
- [007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation](../architecture/phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md)
- [007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation](../architecture/phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md)

All are architecture/design authority only. Their production implementation is not authorized.

007-G preserves semantic Strategy/method authority separately from executable binding, dependency closure, trust/authorization, secrets and role-specific distributed runtime closure.

007-H preserves stable Execution/Attempt history while separating observed physical state, current mutation authority, idempotency, fencing, recovery-frontier continuity, checkpoint reuse, cancellation and admission.

007-I preserves Evaluation semantic validation separately from Evidence establishment; immutable Evidence separately from current applicability; typed Provenance separately from canonical owner payloads; historical resolution separately from historical-knowledge quality; historical supportability separately from current reproduction feasibility; and canonical history separately from actor-visible disclosure. Disclosure may protect existence, relationship shape, counts and reason text without rewriting internal truth.

007-G through 007-I select no concrete runtime/security/scheduler/fencing/checkpoint/Evidence/provenance/query/redaction technology.

The next eligible design group is:

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary**.

007-J is design-only unless a later explicit implementation re-entry decision separately authorizes executable work.

## Historical readiness authority

[Phase 006 Consolidated Design Readiness Contract](phase-006-consolidated-design-readiness-contract.md) remains historically accurate but is reopened for current work by the Phase 007 design-continuation authority.

Later documents must conform to current authority unless an explicit superseding design decision changes it.
