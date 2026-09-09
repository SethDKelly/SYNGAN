---
type: Architecture Index
title: SYNGAN Representation & Architecture Design
status: active
---

# SYNGAN Representation & Architecture Design

## Purpose

This directory is the canonical home for implementation-facing architecture that maps accepted semantic and experience authority into representations, identities, persistence/data boundaries, runtime/extension contracts, recovery, Evidence/Provenance/history, enterprise security, and deployable platform integration.

Architecture remains downstream of design authority, accepted concepts/synchronizations, and experience authority. Implementation/platform convenience MUST NOT redefine semantic ownership.

## Start here — current authority

For current architecture or implementation-planning work, read in this order:

1. [Phase 006 Architecture Reconciliation Contract](phase-006-architecture-reconciliation-contract.md) — **current Phase 006 overlay and precedence authority**;
2. [Phase 004 Consolidated Architecture Contract](phase-004-consolidated-architecture-contract.md) — still authoritative where not refined by Phase 006;
3. only the directly relevant detailed Phase 004 architecture authority;
4. [Architecture Decision Records](../decisions/index.md) for rationale/supersession history;
5. [Phase 006 Implementation-Planning Reconciliation](../implementation/phase-006-implementation-planning-reconciliation.md) for downstream planning consequences.

Do not load the full architecture corpus by default.

## Current architecture overlays

### Phase 006 Architecture Reconciliation Contract

Phase 006 promotes five upstream refinements into current architecture:

- non-regressing authority after potentially regressive control-state recovery;
- self-contained acquisition + cluster-wide runtime-distribution closure;
- multidimensional scale, lossless admission/backpressure and capability-specific degraded support;
- privacy/disclosure/formal-guarantee/release boundaries;
- Data Meaning-owned structured topology for single-table, time-series, multi-table shared-key and composite shapes;
- orthogonal human/programmatic actionability, disclosure and historical-knowledge semantics.

The accepted concept/synchronization baseline remains **11 concepts / 15 synchronizations**.

## Phase 004 baseline authorities

The Phase 004 detailed authorities remain active beneath the Phase 006 overlay:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](strategy-extension-learning-generation-evaluation-runtime-adapter.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](evaluation-evidence-provenance-reproducibility-historical-query.md)
- [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md)
- [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](deployment-scalability-observability-portability-compatibility-platform-integration.md)

Where one of these conflicts with an explicit Phase 006 reconciliation rule, the Phase 006 overlay governs.

## Current reconciled architecture baseline

Future implementation must preserve, among other rules:

- stable logical identity distinct from mutable locations/platform/runtime objects;
- immutable semantic revisions/commitments with separate lifecycle/version/concurrency axes;
- typed handles that are identifiers, not bearer credentials;
- bounded control-plane state with distributed payload/reference boundaries;
- one logical Execution across fenced Attempts and at-least-once physical work;
- **non-regressing recovery authority** so restored stale state cannot resurrect writer/cancellation/security authority;
- candidate/checkpoint/runtime material distinct from semantic results;
- one logical completed Generation output even when represented by many tables/scopes/partitions;
- composable topology with Data Meaning-owned structural assertions rather than a Relationship concept;
- time-series semantics distinct from physical timestamp/partition order;
- exact Strategy/method implementation binding distinct from semantic authority;
- **cluster-wide runtime closure** across every material worker role, including dynamic workers;
- no hidden acquisition/model-hub/remote fallback for self-contained/offline profiles;
- large Learned State/model loading that does not universally depend on driver broadcast;
- Evidence claim strength bounded by exact Evaluation method/scope/coverage/uncertainty;
- empirical privacy Evidence distinct from formal privacy mechanisms and external release approval;
- typed canonical Provenance with derived non-authoritative history/search projections;
- reconstructed/partial/unknown/unavailable history distinct from directly retained fact;
- scoped authorization/redaction with non-disclosing outward responses when existence is protected;
- multidimensional scale/admission/backpressure semantics that cannot silently weaken committed quantity/horizon/topology/coverage/Constraint semantics;
- capability-negotiated platform support with capability-specific limitation/degraded states;
- canonical history, runtime telemetry and security audit as separate lanes;
- orthogonal programmatic/human views rather than one universal lifecycle/status/error.

## Active ADR rationale

The current active set is ADR-0001 through ADR-0010.

Phase 006 did **not** supersede ADR-0001 through ADR-0008.

Two additive decisions were introduced by 006-I:

- [ADR-0009 — Non-Regressing Authority After Regressive Control-State Recovery](../decisions/ADR-0009-non-regressing-authority-after-regressive-control-state-recovery.md)
- [ADR-0010 — Self-Contained Distributed Runtime Closure](../decisions/ADR-0010-self-contained-distributed-runtime-closure.md)

ADR-0009 extends ADR-0005. ADR-0010 extends ADR-0004 and ADR-0008.

## Phase status

**Phase 004 — Representation & Architecture Design: complete historical baseline.**

**Phase 006 — Post-Planning Design Validation & Adversarial Refinement: current.**

006-I has completed architecture/ADR reconciliation. Current next:

**006-J — Phase 006 Consolidation, Residual Design-Debt Audit & Implementation-Authority Readiness Decision**.

Production implementation remains unauthorized.

## Remaining implementation-choice boundary

Current architecture still intentionally does not select final Python class spelling, persistence technology, exact Spark storage/catalog or package-distribution mechanism, scheduler/fencing implementation, topology algorithm, privacy mechanism, policy/secret/network product, Databricks API topology, CI/deployment topology, benchmark values, SLOs, or exact support matrix.

Those remain later implementation/release decisions constrained by the reconciled architecture if a future explicit implementation-authority phase is approved.
