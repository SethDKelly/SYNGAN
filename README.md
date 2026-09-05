# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual and architectural design before implementation. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical design knowledge is maintained as an OKF-oriented bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

For implementation planning, the primary exit contracts are:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)

## Current status

**Phase 001 — Design Foundation & Concept Discovery: complete.**

**Phase 002 — Concept Specification & Invariant Refinement: complete.**

Phase 002 closed with eleven accepted concepts and fifteen synchronization rules.

**Phase 003 — Experience & Workflow Design: complete.**

Phase 003 froze readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, dependency/network/egress, disclosure, programmatic-parity, and enterprise-scale experience obligations.

**Phase 004 — Representation & Architecture Design: complete.**

Phase 004 closed through [`004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit`](docs/phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md) with no blocking redesign required.

The [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md) now freezes, among other guarantees:

- stable typed resource identity and immutable semantic commitments;
- bounded control-plane/distributed-data-plane separation;
- exact Spark-scale source-state binding and sealed candidate/output promotion;
- model-neutral Strategy/method implementation bindings;
- direct Generation without fabricated Learning;
- one logical Execution across fenced/reconcilable Attempts;
- at-least-once physical work with one authoritative semantic result;
- checkpoint/candidate/runtime-result boundaries distinct from Learned State/completed output/Evidence;
- Evaluation semantic validation before immutable Evidence establishment;
- typed canonical Provenance with derived non-authoritative query projections;
- qualified target-specific reproducibility rather than global Boolean state;
- explicit dependency identity/integrity/trust/authorization/network/egress distinctions;
- no hidden package/model acquisition, dependency substitution, remote fallback, telemetry, or egress;
- non-bearing durable handles and scoped Attempt data/dependency/network/secret capabilities;
- truthful withholding/redaction and security-aware history/query projections;
- portable semantic/application/control contracts with capability-negotiated platform adapters;
- Databricks as an important managed target rather than package/semantic identity;
- generic/self-managed Spark and private/offline deployment when required guarantees are supplied;
- non-Spark model runtimes behind scale-compatible distributed bridges;
- multi-axis compatibility, restartable durable coordination, and enterprise-scale no-full-driver-materialization requirements.

Architecture decision rationale is preserved in [`docs/decisions/`](docs/decisions/index.md), ADR-0001 through **ADR-0008 — Portable Core & Capability-Negotiated Platform Adapters**.

## Current phase

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Next:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**

Phase 005 will translate the accepted architecture into dependency-safe package/module boundaries, persisted/wire representations, implementation slices, verification/architecture fitness tests, migrations, platform adapters, delivery sequencing, and acceptance evidence before coding is treated as implementation-complete.

Concrete choices such as final Python package/class spelling, persistence technology, Spark storage/catalog implementation, manifest/checkpoint format, scheduler/fencing mechanism, plugin/runtime technology, Provenance query store, IAM/policy/secret/network stack, observability vendor, exact Databricks API topology, CI/CD/deployment topology, and benchmark/support matrices remain downstream implementation-planning work constrained by the Phase 004 contract.
