---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — actor-visible/programmatic workflow semantics and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — current implementation-facing architecture authority.
- [Architecture Decision Records](decisions/index.md) — architecture rationale/alternatives/supersession; current normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved/deferred work that is not canonical authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, or design decision has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

The active downstream order is:

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > ADR rationale / phase records
  > summaries / examples / backlog
```

Architecture may choose representation and implementation-facing boundaries but MUST NOT override upstream semantic/experience contracts.

## Phase status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules, offline/no-outbound-network capable core semantics, explicit commitment/historical binding, single semantic promotion, typed Provenance, and qualified reproducibility.

**Phase 003 — Experience & Workflow Design: complete.**

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Phase 003 closed with eight detailed experience authorities and the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).

**Current phase: [Phase 004 — Representation & Architecture Design](phases/004/index.md).**

Completed in Phase 004:

- [004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction](phases/004/004-A-architecture-authority-representation-layering-dependency-direction.md)
- [004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](phases/004/004-B-public-api-resource-handle-workflow-semantic-mapping.md)
- [004-C — Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](phases/004/004-C-control-plane-identity-revision-state-persistence-historical-reference-architecture.md)
- [004-D — Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](phases/004/004-D-spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion-architecture.md)
- [004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](phases/004/004-E-strategy-extension-learning-generation-evaluation-runtime-adapter-architecture.md)
- [004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](phases/004/004-F-execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation-architecture.md)
- [004-G — Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](phases/004/004-G-evaluation-evidence-provenance-reproducibility-historical-query-architecture.md)
- [004-H — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Architecture](phases/004/004-H-dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security-architecture.md)
- [004-I — Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration Architecture](phases/004/004-I-deployment-scalability-observability-portability-compatibility-platform-integration-architecture.md)

Canonical architecture now includes:

- the [architecture constitution](architecture/architecture-authority-representation-layering.md);
- the [typed public resource/handle architecture](architecture/public-api-resource-handle-workflow-semantic-mapping.md);
- the [control-plane identity/state architecture](architecture/control-plane-identity-revision-state-persistence-historical-reference.md);
- the [Spark data boundary/materialization architecture](architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- the [Strategy extension/runtime adapter architecture](architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- the [Execution/recovery/fencing architecture](architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md);
- the [Evaluation/Evidence, Provenance, Reproducibility & Historical Query architecture](architecture/evaluation-evidence-provenance-reproducibility-historical-query.md);
- the [Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security architecture](architecture/dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md);
- the [Deployment, Scalability, Observability, Portability, Compatibility & Platform Integration architecture](architecture/deployment-scalability-observability-portability-compatibility-platform-integration.md).

004-I establishes deployable logical roles, restartable durable-state-first coordination, capability-negotiated platform adapters, multi-dimensional scale disclosure, distinct semantic/runtime/security observability lanes, generic/self-managed Spark portability, Databricks as a managed adapter target rather than package identity, multi-axis compatibility and rolling-version contracts, private/offline package/dependency distribution, and deployment enforcement obligations for the 004-H security model.

Decision rationale is preserved in ADR-0001 through [ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters](decisions/ADR-0008-portable-core-capability-negotiated-platform-adapters.md).

Next: **004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit**.
