---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for implementation-facing architecture that maps SYNGAN's accepted semantic and experience contracts into representations, interfaces, identities, persistence/data boundaries, runtime/extension contracts, recovery, Evidence/Provenance/history, enterprise security, and deployable platform integration.

Architecture remains downstream of design authority, accepted concepts/synchronizations, and experience authority. Implementation/platform convenience MUST NOT redefine semantic ownership.

## Start here

For implementation planning, read:

1. [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md) — frozen cross-architecture implementation contract and invariants;
2. the specific detailed architecture authority relevant to the implementation slice;
3. [Architecture Decision Records](../decisions/index.md) only when decision rationale/alternatives are needed;
4. Phase 004 records only for design execution history.

This progressive-disclosure order avoids requiring agents or implementers to ingest every detailed Phase 004 document for each task.

## Canonical architecture authorities

- [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md) — cross-architecture exit contract.
- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md) — 004-A architecture constitution.
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md) — 004-B public resource/handle architecture.
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md) — 004-C durable control-plane architecture.
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md) — 004-D distributed data/materialization architecture.
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md) — 004-E extension/runtime architecture.
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md) — 004-F operational continuation architecture.
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md) — 004-G Evidence/history/query architecture.
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md) — 004-H enterprise dependency/security architecture.
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](deployment-scalability-observability-portability-compatibility-platform-integration.md) — 004-I deployment/platform architecture.

## Architecture baseline

The consolidated contract freezes, among other rules:

- stable logical identity distinct from mutable locations/platform/runtime objects;
- immutable semantic revisions/commitment snapshots with separately versioned lifecycle state;
- typed durable handles that are not bearer credentials;
- bounded control-plane state referencing distributed source/output/Learned-State/checkpoint/diagnostic material;
- Spark-native distributed data boundaries without universal Spark ML or driver-local materialization;
- model-neutral Strategy/method semantics separated from executable implementation bindings;
- one logical Execution across fenced/reconcilable Attempts;
- at-least-once physical work with single authoritative semantic promotion;
- checkpoint/candidate/runtime results distinct from Learned State/completed output/Evidence;
- exact sealed-candidate binding for completion Evaluation and idempotent Generation promotion;
- immutable Evidence findings with bounded claim strength and separately versioned applicability;
- canonical typed Provenance over stable references with derived non-authoritative query projections;
- qualified target-specific reproducibility rather than a Boolean state;
- explicit dependency identity/trust/authorization/network/egress boundaries and no hidden acquisition/fallback;
- scoped Attempt capabilities, secret isolation, truthful redaction/withholding, and protected derived query paths;
- portable semantic/application/control contracts with capability-negotiated platform adapters;
- Databricks as an important managed target rather than semantic/package identity;
- generic/self-managed Spark and private/offline profiles when required guarantees are supplied;
- multi-axis compatibility, restartable durable coordination, and distinct canonical history/runtime telemetry/security audit lanes.

The complete invariant set is authoritative in the [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md).

## Active ADR rationale

- [ADR-0001 — Typed Resource/Handle Public API](../decisions/ADR-0001-typed-resource-handle-public-api.md)
- [ADR-0002 — Immutable Semantic Snapshots & Versioned Lifecycle State](../decisions/ADR-0002-immutable-semantic-snapshots-versioned-lifecycle-state.md)
- [ADR-0003 — Sealed Manifest-Gated Distributed Output Promotion](../decisions/ADR-0003-sealed-manifest-gated-output-promotion.md)
- [ADR-0004 — Semantic Extension & Runtime Binding Separation](../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)
- [ADR-0005 — Attempt-Epoch Fencing & Recoverable At-Least-Once Execution](../decisions/ADR-0005-attempt-epoch-fencing-recoverable-at-least-once-execution.md)
- [ADR-0006 — Typed Canonical Provenance & Derived Historical Projections](../decisions/ADR-0006-typed-provenance-canonical-derived-history-projections.md)
- [ADR-0007 — Explicit Dependency Resolution & Scoped Capability Security](../decisions/ADR-0007-explicit-dependency-resolution-scoped-capability-security.md)
- [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](../decisions/ADR-0008-portable-core-capability-negotiated-platform-adapters.md)

No ADR was superseded by the Phase 004 exit audit.

## Phase status

**Phase 004 — Representation & Architecture Design: complete.**

Exit: [004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit](../phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md).

**Current phase: [Phase 005 — Implementation Planning & Delivery Decomposition](../phases/005/index.md).**

Next:

**005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**

## Remaining implementation-choice boundary

Phase 004 intentionally does not select final Python package/class spelling, persistence technology, ID encoding, Spark storage/catalog provider, manifest/checkpoint format, scheduler/fencing implementation, plugin discovery technology, distributed model runtime, Provenance query store, IAM/policy/secret/network stack, observability vendor, Databricks API topology, CI/CD/deployment topology, benchmark values, or support matrix.

Those choices are now constrained implementation-planning work under Phase 005, not permission to reopen the accepted semantic/architecture contract.
