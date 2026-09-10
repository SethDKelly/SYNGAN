---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation/architecture design downstream of accepted concepts, synchronizations and experience authority.

## Start here — current architecture continuation

For current design, read only what the active question needs:

1. [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md);
2. [007-D Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md);
3. [007-E Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md);
4. [007-F Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md);
5. [007-G Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md);
6. [007-H Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation](phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md);
7. [007-I Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation](phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md);
8. [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md) where not refined later;
9. only directly relevant Phase 004 detailed authorities;
10. [ADRs](../decisions/index.md) for rationale/history.

## Current posture

Architecture design is **active**; production implementation expansion and new executable architecture enforcement remain frozen.

Existing 007-A through 007-C implementation artifacts are provisional feasibility/history evidence and may be revised later.

## 007-D / 007-E / 007-F foundations

007-D separates identity, semantic revision/commitment, mutable state version/freshness, representation schema version and provider/authority scope. 007-E defines technology-neutral persistence, transaction, CAS, durable-intent, exact-history and migration/recovery boundaries. 007-F defines logical distributed subjects/scopes, exact source-state strength, bounded manifested representation, candidate/seal separation and Generation-owned promotion.

## 007-G — executable realization / security / runtime closure

007-G establishes this current architecture:

```text
semantic Strategy / method / activity commitment
        ↓
implementation binding
        ↓
exact implementation + dependency closure
        ↓
identity / integrity / trust / compatibility
        ↓
current authorization + network/egress qualification
        ↓
role-specific distributed runtime closure
        ↓
immutable Attempt invocation
        +
current scoped capabilities / secret access
        ↓
physical runtime realization
        ↓
non-final result
        ↓
owner semantic validation
```

Key rules include semantic Strategy/method authority distinct from executable realization, exact Attempt-scoped composite closure, no silent in-Attempt substitution, explicit acquisition outside material runtime, current authorization separate from historical commitment, use-time secret resolution, role-specific distributed closure including dynamic workers, and no topology simplification merely because an implementation is narrower.

Earlier Phase 005-F/005-I SPI, entry-point, package-extra and concrete security/dependency choices remain implementation candidates rather than architecture requirements.

## 007-H — execution / recovery / admission

007-H establishes the operational authority chain beneath the committed activity and 007-G invocation:

```text
committed activity / stable Execution
        ↓
current admission + recovery-continuity qualification
        ↓
non-regressing recovery-authority frontier
        ↓
current Attempt authority + resource-local preconditions
        ↓
immutable Attempt invocation
        ↓
physical work / checkpoint / candidate / method-result effects
        ↓
reconciliation + owner validation
        ↓
at-most-one authoritative semantic result transition
```

Key rules include distinct Attempt observed state versus mutation authority, operation-scoped idempotency, Attempt epoch insufficiency after regressive restore, recovery quarantine plus fresh stale-writer exclusion, current-authority adoption/reconstruction of surviving effects, immutable qualified checkpoints, durable cancellation, admission distinct from semantic readiness/authorization/queue/write authority, and at-least-once physical realization with fenced/idempotent/reconcilable canonical effects.

Earlier Phase 005-G concrete execution types, enums, integer epoch encoding and package/repository/API spelling remain implementation candidates.

## 007-I — Evaluation / Evidence / Provenance / history / reproducibility / disclosure

007-I establishes this current evidentiary/history architecture:

```text
committed Evaluation
        ↓
Execution / Attempts
        ↓
non-final method result
        ↓
Evaluation semantic validation
        ↓
idempotent Evidence establishment
        ↓
immutable Evidence finding + separate current applicability
        ↓
required typed Provenance
        ↓
exact historical query composition
        ↓
qualified reproducibility assessment
        ↓
actor-safe disclosure projection
```

Key rules:

- runtime/platform Evaluation success never becomes Evidence directly;
- Evidence establishment validates the exact Criterion, subject/reference, method/configuration, topology/scope/coverage, uncertainty, executable realization and retry/recovery contribution context;
- one Evaluation may establish zero or more independently interpretable findings under retry-idempotent logical finding identity;
- conflicting replay for one logical finding is a consistency defect rather than overwrite;
- immutable Evidence finding semantics remain distinct from current applicability;
- negative and indeterminate findings remain valid Evidence when the examination is valid;
- Generation retains the exact candidate/requirement/Criterion/Evidence completion basis used at promotion, which later Evidence cannot rewrite;
- privacy/disclosure Evidence is distinct from formal privacy guarantee, current disclosure permission and release/use approval;
- Provenance remains narrow typed historical relationship authority over exact references rather than a duplicated metadata graph;
- directly retained, reconstructed, partial and unknown historical knowledge remain distinguishable;
- object/reference resolution state is distinct from historical knowledge quality;
- historical query is bounded read composition, and derived projections cannot establish canonical absence or authority;
- historical comparison reports differences without inventing causal or quality claims;
- query freshness is represented truthfully rather than implying a universal cross-store snapshot;
- disclosure may protect existence, relationship shape, reverse traversal, counts/cardinality and reproducibility reasons as well as field values;
- canonical historical knowledge is distinct from one actor's visible knowledge;
- reproducibility separates historical supportability from current reproduction feasibility and actor-visible assessability;
- strongest-defensible reproduction class is constrained by the weakest material identity, nondeterminism, approximation, equivalence or historical-knowledge boundary;
- reproduction readiness is not reproduction success; actual reproduction is new domain work.

Earlier Phase 005-H concrete Evidence/history classes, SQL/relational storage assumptions, indexes, query APIs, package layout and cache design remain implementation candidates to reassess at explicit re-entry.

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts in 007-D..I    0
new synchronizations        0
new ADRs                    0
```

No `SYNC-16`.

007-I composes/refines ADR-0002, ADR-0006, ADR-0007 and ADR-0009 without superseding them. Existing ADRs remain sufficient.

## Current next boundary

The previously named 007-J executable vertical-slice proof is not automatically authorized under the design-first freeze.

**007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary** is the next eligible **design** subgroup.

Production implementation remains frozen independently of design progression.
