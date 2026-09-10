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
7. [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md) where not refined later;
8. only directly relevant Phase 004 detailed authorities;
9. [ADRs](../decisions/index.md) for rationale/history.

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

Key rules:

- Strategy/method semantics remain distinct from executable binding/package/runtime identity;
- one binding may resolve a composite implementation closure rather than one package/model;
- every Attempt freezes one exact realization; runtime cannot hot-swap missing components silently;
- a later Attempt may use another compatible implementation only when unchanged semantic commitment permits it and the new Attempt is independently attributable;
- dependency requirement, resolution, exact identity, integrity/authenticity, trust, compatibility and current authorization remain separate axes;
- explicit provisioning may occur before runtime, while hidden runtime acquisition/fallback is prohibited;
- installed/discovered third-party code is not trusted merely by presence, and code-loading/unsafe deserialization are protected actions where material;
- network capability is distinct from data egress, and remote-service reproducibility is limited to the identity/version guarantees the provider actually exposes;
- historical semantic commitment and current authorization remain separate;
- live runtime capabilities are bounded operational authority and are not serialized bearer authority;
- secret values stay outside canonical semantic/history/provenance data and are resolved at use time;
- driver/coordinator readiness never establishes distributed closure;
- every material runtime role, including dynamic workers, must satisfy its role-specific closure or be ineligible;
- large Learned State/model/artifact loading cannot universally require driver memory/broadcast;
- implementation topology limitations cannot redefine or simplify Data Meaning/Generation/Constraint semantics;
- self-contained source-derived free-form text remains a complete-baseline requirement.

Earlier Phase 005-F/005-I choices such as `typing.Protocol`, Python entry points, named runtime SPIs, `spark`/`torch` extras and concrete security/dependency type names remain implementation candidates rather than architecture requirements.

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

Key rules:

- stable Execution identity survives valid same-semantics recovery while material re-realization receives distinguishable Attempt history;
- Attempt observed physical state and current mutation authority are separate;
- provider-internal worker/task retry may remain within one Attempt when its immutable invocation and authority boundary do not change;
- idempotency is scoped to the intended operation/effect and never substitutes for fencing or current authorization;
- Attempt epoch alone is insufficient after potentially regressive control-state recovery;
- material write authority composes the current recovery frontier, current Execution/Attempt authority, resource-local preconditions where required and current authorization;
- regressive restore enters recovery quarantine and establishes fresh stale-writer exclusion before ordinary writes resume;
- surviving effects are reconciled/reconstructed/adopted by current authority rather than reviving their old writer;
- committed checkpoints remain immutable operational recovery state and require contextual resume qualification;
- a later compatible implementation binding is not automatically checkpoint-compatible;
- cancellation is durable intent that blocks ordinary new admission and is not erased by regressive restore;
- late provider success is historical fact, not renewed promotion authority;
- admission is current operational eligibility, distinct from semantic readiness, authorization, executable closure, queue placement and write authority;
- temporary resource shortage remains distinguishable from true incompatibility and stale admission must be requalified before launch;
- dynamic workers satisfy role-specific 007-G closure before material work;
- the target is at-least-once physical realization with fenced/idempotent/reconcilable effects, not exactly-once computation.

Earlier Phase 005-G concrete execution types, enums, integer epoch encoding, package topology and repository/API spelling remain implementation candidates to reassess at explicit re-entry.

## Current design counts

```text
accepted concepts          11
accepted synchronizations  15
active ADRs                10
new concepts in 007-D..H    0
new synchronizations        0
new ADRs                    0
```

No `SYNC-16`.

007-H composes/refines ADR-0002, ADR-0007 and ADR-0009 without superseding them. Existing ADRs remain sufficient.

## Current next boundary

**007-I — Evaluation/Evidence, Provenance, Historical Query, Reproducibility & Disclosure Foundation** is the next eligible **design** subgroup.

Production implementation remains frozen independently of design progression.
