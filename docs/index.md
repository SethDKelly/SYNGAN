---
okf_version: "0.2"
type: Knowledge Bundle
title: SYNGAN Design Knowledge
status: active
---

# SYNGAN Design Knowledge

This directory is the canonical design and implementation-planning knowledge bundle for SYNGAN.

## Progressive disclosure

- [Authority](authority/index.md) — methodology, documentation governance, terminology, source/provenance, network/external-dependency, and reproducibility rules.
- [Problem Knowledge](problem/index.md) — problem, purpose, actors, outcomes and enterprise scale envelope.
- [Domain Terminology](terminology/index.md) — canonical vocabulary and compatibility mappings.
- [Accepted Concepts](concepts/index.md) — canonical concept purpose, ownership, actions, lifecycle, invariants and boundaries.
- [Accepted Synchronizations](synchronizations/index.md) — canonical cross-concept coordination rules.
- [Experience & Workflow Design](experience/index.md) — start implementation-facing experience review with the [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).
- [Representation & Architecture Design](architecture/index.md) — start with the [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).
- [Implementation Planning & Delivery Authority](implementation/index.md) — current implementation-planning governance, verification, source/toolchain, control-plane and distributed-data plans.
- [Architecture Decision Records](decisions/index.md) — architecture rationale/alternatives/supersession; current normative architecture remains under `docs/architecture/`.
- [Concept Discovery](discovery/index.md) — historical hypotheses, alternatives and design provenance.
- [Phases](phases/index.md) — phase plans, outcomes and exit reviews.
- `references/` — external references used by the design.
- `backlog/` — unresolved/deferred work that is not canonical authority.

## Authority rule

A durable fact, definition, requirement, invariant, policy, design decision, or implementation rule has one canonical home. Other documents SHOULD reference that authority rather than restating it as a competing source of truth.

```text
authority
  > concepts / synchronizations
  > experience
  > architecture
  > implementation planning authority
  > future code / deployment
  > ADR rationale / phase history / summaries / backlog where applicable
```

Implementation planning and later code MUST NOT override upstream semantic, experience, or architecture contracts for convenience.

## Completed design layers

### Phase 001 — Design Foundation & Concept Discovery — complete

Exit: [001-H — Phase 001 Consolidation & Initial Concept Catalog](phases/001/001-H-phase-001-consolidation-initial-concept-catalog.md).

### Phase 002 — Concept Specification & Invariant Refinement — complete

Exit: [002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review](phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md).

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules.

### Phase 003 — Experience & Workflow Design — complete

Exit: [003-I — Cross-Workflow Consistency & Phase 003 Consolidation Review](phases/003/003-I-cross-workflow-consistency-phase-003-consolidation-review.md).

Exit authority: [Phase 003 Consolidated Experience Contract](experience/phase-003-consolidated-experience-contract.md).

### Phase 004 — Representation & Architecture Design — complete

Exit: [004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit](phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md).

Exit authority: [Phase 004 Consolidated Architecture Contract](architecture/phase-004-consolidated-architecture-contract.md).

## Current phase

**[Phase 005 — Implementation Planning & Delivery Decomposition](phases/005/index.md) is current and remains planning-only.**

No production source, package scaffold, database schema/migration, Spark/runtime adapter, test suite, CI workflow, or deployment infrastructure is implemented during Phase 005. Concrete package paths, technologies and sequences are future implementation plans only until a later phase explicitly authorizes coding.

Completed:

- [005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](phases/005/005-A-implementation-authority-delivery-governance-toolchain-repository-enforcement.md)
- [005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates](phases/005/005-B-verification-strategy-test-harness-architecture-fitness-evidence-fixtures-quality-gates.md)
- [005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement](phases/005/005-C-source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md)
- [005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan](phases/005/005-D-public-resource-api-control-plane-identity-state-persistence-transactions-migration-implementation.md)
- [005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan](phases/005/005-E-spark-data-boundary-source-output-references-manifest-materialization-promotion-implementation-plan.md)

Canonical implementation-planning authority now includes:

- [implementation/delivery governance](implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md);
- [verification layers, fitness functions, fixtures and quality gates](implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [source/package topology, foundational toolchain and dependency enforcement](implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [public resource/control-plane identity, persistence, transaction and migration plan](implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [Spark data boundary, exact source-state, manifest/candidate/sealed-snapshot and promotion plan](implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md).

The planning baseline now includes:

- one future `src/syngan` package with enforced inward boundaries and optional runtime/platform isolation;
- Python >=3.11 and the accepted uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions toolchain plan;
- typed AuthorityId/ResourceId/ResourceRef/RevisionRef/SnapshotId/StateVersion/SchemaVersion conventions;
- immutable public specs/handles/views plus a non-authoritative `SynGANClient` facade;
- exact typed historical resolution and explicit versioned JSON codecs;
- SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg control-persistence plan with CAS/transactions/outbox;
- optional Spark capability isolation from the base package;
- DataFrame/table/path/query selectors separated from exact `SourceStateRef` history;
- conservative snapshot-before-commit behavior for unresolved mutable/ephemeral Spark sources;
- bounded manifest roots with distributed/provider-native component indexes;
- a portable manifested-Parquet file profile without making Parquet or a table format semantic authority;
- distinct Generation candidate, sealed snapshot and logical output roles;
- idempotent metadata-only promotion using the 005-D control substrate.

Next:

**005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**

005-F must remain planning-only while defining the future model-neutral runtime/provider boundary over the durable control and distributed-data plans already accepted.

## Documentation governance note

The repository continues to use its project-specific OKF profile. The separate question of strict external OKF 0.2 reserved-file/frontmatter normalization has not been falsely declared resolved and remains documentation-governance debt until explicitly audited against current external authority.
