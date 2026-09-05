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
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**

005-A establishes implementation/code as downstream realization, explicit change classification, traceable delivery slices, dependency/toolchain/migration governance, mandatory acceptance evidence, repository-wide [`AGENTS.md`](AGENTS.md), and PR review discipline.

005-B establishes the executable verification baseline:

- logical verification layers V0-V11 from repository/unit checks through distributed, recovery, Evidence/history, security/offline, platform and scale/compatibility verification;
- stable architecture-fitness properties AF-01 through AF-20;
- synthetic/non-sensitive micro, generated-medium, ephemeral-scale and fault/control fixture classes;
- authority-derived test oracles and controlled golden-fixture updates;
- deterministic and statistical/stochastic test lanes without retry-until-green;
- explicit failure injection around durable mutation, launch, checkpoint, candidate seal, Evidence establishment and promotion;
- reusable common adapter conformance suites;
- default-deny portable/core outbound-network testing;
- Q0-Q4 local, PR, integration, scheduled and release/support quality gates;
- explicit flakiness, quarantine, waiver and acceptance-evidence governance.

Canonical verification authority: [`docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md`](docs/implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md).

Next:

- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**

005-C will now select the physical Python/source/test topology and foundational concrete build/test/static-analysis toolchain so the accepted architecture and verification contracts can be enforced mechanically.

The repository intentionally does not yet claim final Python/package layout, supported Python versions, dependency manager, build backend, test/lint/type tooling, database, Spark storage/catalog technology, scheduler/fencing mechanism, plugin/runtime implementation, IAM/network/security stack, observability vendor, Databricks API topology, CI/CD topology, or benchmark/support matrices. Those remain dependency-safe implementation-planning decisions constrained by the accepted architecture and verification authority.
