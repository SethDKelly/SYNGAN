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

Both are architecture/design authority only. Their production implementation is not authorized.

The next eligible design group is:

**007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation**.

## Historical readiness authority

[Phase 006 Consolidated Design Readiness Contract](phase-006-consolidated-design-readiness-contract.md) remains historically accurate but is reopened for current work by the Phase 007 design-continuation authority.

Later documents must conform to current authority unless an explicit superseding design decision changes it.
