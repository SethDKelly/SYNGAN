---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for representation/architecture design downstream of accepted concepts, synchronizations and experience authority.

## Start here — current architecture

For current implementation-facing architecture, begin with:

1. [Phase 007 Consolidated Architecture Contract](phase-007-consolidated-architecture-contract.md);
2. [Phase 007 Consolidated Architecture & Implementation-Reentry Readiness Contract](../authority/phase-007-consolidated-architecture-implementation-reentry-readiness-contract.md);
3. only the directly relevant 007-D through 007-J detailed authority;
4. [ADRs](../decisions/index.md) for rationale/history;
5. Phase 006/004 architecture only where the Phase 007 consolidated authority delegates or has not refined the question.

## Current posture

Phase 007 architecture design is **complete and consolidated**.

Controlled implementation re-entry is approved for a bounded scaffold/verification reconciliation tranche only. Owner-specific feature implementation remains unauthorized until that tranche completes and a later implementation subgroup is separately approved.

The previous [Phase 007 Design Continuation & Implementation Freeze](../authority/phase-007-design-continuation-implementation-freeze.md) is historical/superseded.

## Detailed Phase 007 architecture authorities

- [007-D — Identity, Revision, Serialization, Resource/Handle & Programmatic-View Foundation](phase-007-d-identity-revision-serialization-resource-handle-programmatic-view-foundation.md)
- [007-E — Control Persistence, Transactions, CAS, Outbox, Historical References & Migration Baseline](phase-007-e-control-persistence-transactions-cas-outbox-historical-reference-migration-baseline.md)
- [007-F — Distributed Data-State, Structured Topology, Manifest, Candidate/Seal & Promotion Foundation](phase-007-f-distributed-data-state-structured-topology-manifest-candidate-seal-promotion-foundation.md)
- [007-G — Strategy/Method Binding, Dependency Trust, Authorization, Secrets & Distributed Runtime Closure Foundation](phase-007-g-strategy-method-binding-dependency-trust-authorization-secrets-distributed-runtime-closure-foundation.md)
- [007-H — Execution/Attempt, Idempotency, Fencing, Non-Regressing Recovery, Checkpoint, Cancellation & Admission Foundation](phase-007-h-execution-attempt-idempotency-fencing-non-regressing-recovery-checkpoint-cancellation-admission-foundation.md)
- [007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation](phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md)
- [007-J — Reference Vertical-Slice Scope Re-evaluation, Architecture Completeness & Implementation-Proof Boundary](phase-007-j-reference-vertical-slice-scope-re-evaluation-architecture-completeness-implementation-proof-boundary.md)

## Consolidated architecture spine

The current architecture preserves this composition:

```text
semantic authority / exact commitments
        ↓
typed exact identity / revisions / references / views
        ↓
owner-controlled persistence / concurrency / exact history
        ↓
logical data state / composable topology / manifested representation
        ↓
semantic Strategy/method ↔ exact executable/dependency/runtime realization
        ↓
stable Execution / distinguishable Attempts / current mutation authority
        ↓
candidate sealing / owner semantic completion and promotion
        ↓
Evaluation semantic validation / Evidence / typed Provenance
        ↓
historical query / qualified reproducibility / actor-safe disclosure
        ↓
explicit proof and claim boundaries
```

This is an authority composition, not a required one-size-fits-all workflow. Direct Generation may omit Learning/Learned State when its Strategy semantics do not require them.

## Core cross-cutting rules

Current architecture requires at least:

- logical identity != semantic revision != mutable state version != representation schema version;
- handle/view != canonical owner;
- historical exact reference != current/latest substitution;
- persistence durability != semantic completion;
- CAS != semantic transition validation;
- logical data subject != physical representation;
- physical layout != Data Meaning/topology semantics;
- open candidate != sealed subject != promoted output;
- semantic Strategy/method != implementation binding/dependency/runtime identity;
- explicit provisioning != material runtime acquisition;
- current authorization != historical commitment;
- secret values != canonical history/Provenance;
- driver readiness != distributed worker closure;
- Execution != provider job/run;
- Attempt observed state != current mutation authority;
- idempotency != fencing != authorization;
- lease/liveness != stale-writer exclusion;
- restored state != current mutation authority;
- checkpoint durability != resume eligibility != semantic result;
- admission != semantic readiness != queue placement != write authority;
- runtime/platform completion != Learning/Generation/Evaluation completion;
- Evaluation runtime result != Evidence;
- immutable Evidence finding != current applicability;
- favorable privacy Evidence != formal guarantee != release approval;
- Provenance != duplicated canonical metadata graph;
- reference resolution != historical-knowledge quality;
- directly retained != reconstructed != partial/unknown history;
- derived query/projection != canonical historical authority;
- historical difference != causal/quality claim;
- canonical truth != actor-visible disclosure;
- historical reproducibility support != current reproduction feasibility != reproduction success.

## Complete capability target

The complete structured-data baseline remains:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with composable topology and a supported self-contained Strategy path for each required family before complete-baseline support is claimed.

The supported baseline also requires source-derived/local free-form-text synthesis without mandatory pretrained model, public model hub, first-use model download or runtime inference service.

## Implementation-proof boundary

Implementation evidence must distinguish:

```text
architecture-conformance proof
capability proof
runtime/platform-profile proof
resilience/adversarial proof
scale/release qualification
```

A learning-based single-table local/Spark-local reference path may be the first bounded user-visible proof after later feature authority, but it is not proof of direct-generation neutrality, time-series, multi-table, distributed runtime, regressive recovery, enterprise scale, privacy/release guarantees or release readiness.

## Historical scaffold status

The retained 007-B/007-C source/tool/test scaffold is feasibility evidence, not architecture authority.

The exact seven-package set, Import Linter contracts, tool versions, root import restrictions, socket exceptions and historical delivery-state fitness tests must be reconciled in the next R0/008-A tranche before owner-specific feature implementation begins.

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
provisional concepts        0
```

No `SYNC-16`.

## Current next boundary

**008-A — Implementation Re-entry Authority, Scaffold Reconciliation & Verification Re-baseline** is the next eligible tranche after an explicit proceed decision.

008-A is limited to making the implementation substrate and executable verification truthful against this consolidated architecture. It does not authorize domain/runtime feature implementation.
