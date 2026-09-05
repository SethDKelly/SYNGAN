# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual, architectural, and implementation planning before coding is treated as implementation-complete. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

For implementation planning, the primary authority chain is:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Implementation Planning & Delivery Authority`](docs/implementation/index.md)

Repository-wide automated-agent rules are in [`AGENTS.md`](AGENTS.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules.

**Phase 003 — Experience & Workflow Design: complete.**

Phase 003 froze readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, dependency/network/egress, disclosure, programmatic-parity, and enterprise-scale experience obligations.

**Phase 004 — Representation & Architecture Design: complete.**

Phase 004 closed through [`004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit`](docs/phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md) with no blocking redesign required.

The [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md) freezes stable typed identity/commitments, bounded control/data-plane separation, exact Spark-scale source binding, sealed candidate/promotion semantics, model-neutral runtime adapters, fenced/reconcilable Execution, semantic Evidence/typed Provenance/qualified reproducibility, explicit dependency/security/no-egress semantics, and capability-negotiated portable platform adapters.

Architecture decision rationale is preserved in [`docs/decisions/`](docs/decisions/index.md), ADR-0001 through **ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters**.

## Current phase

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**

005-A establishes:

- implementation/code as downstream realization rather than authority override;
- explicit change classification and upstream conflict escalation;
- traceable delivery slices and mandatory acceptance evidence;
- repository-declared/reproducible toolchain governance without premature tool selection;
- dependency classification/intake rules, optional-integration isolation, and no hidden runtime acquisition;
- migration/compatibility discipline for public/persisted/SPI changes;
- repository-wide [`AGENTS.md`](AGENTS.md) rules for automated contributors;
- a GitHub pull-request checklist covering authority, tests/fitness evidence, dependencies, migration, security/network, scale, and deferred work;
- truthful deferral of CI/branch protection and concrete source/toolchain topology until their requirements are defined.

Next:

- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**

005-B will define the executable verification layers and required quality gates before 005-C selects detailed source/package topology and the foundational concrete Python/build/static-analysis toolchain.

The repository intentionally does not yet claim final Python/package layout, supported Python versions, dependency manager, build backend, test/lint/type tooling, database, Spark storage/catalog technology, scheduler/fencing mechanism, plugin/runtime implementation, IAM/network/security stack, observability vendor, Databricks API topology, CI/CD topology, or benchmark/support matrices. Those remain dependency-safe implementation-planning decisions constrained by the accepted architecture.
