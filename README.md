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

## Current phase

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**

Canonical implementation authority is under [`docs/implementation/`](docs/implementation/index.md).

005-C now freezes the initial implementation scaffold **as a plan, not as production code**:

```text
src/syngan/
├── foundation/
├── domain/
├── ports/
├── application/
├── api/
├── adapters/
└── bootstrap/
```

The selected foundational implementation posture includes:

- one initial `syngan` import package/distribution using `src/` layout;
- Python >=3.11 portable-core floor;
- uv + committed `uv.lock` for reproducible project environments;
- Hatchling build backend;
- pytest, Hypothesis and pytest-socket for verification;
- Ruff for lint/format;
- mypy for static typing;
- Import Linter for enforced inward package dependency contracts;
- coverage reporting as diagnostic evidence rather than a correctness substitute;
- GitHub Actions as repository CI;
- stable Q0-Q4 developer/CI command meanings through a repository-only `tools/verify.py` orchestrator;
- model/platform-neutral base dependencies with Spark/Torch/Databricks isolated as optional capability extras when their later slices define exact dependencies;
- a test topology separating unit, contract, fitness, reusable conformance, integration, scale, scenario and compatibility-golden concerns;
- clean built-wheel/base-install/no-hidden-network/optional-import verification.

No production resource/persistence/Spark/runtime/recovery/Evidence/security/platform implementation has been started by 005-C.

Next:

- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**

005-D will define the durable public/control-plane substrate that all downstream implementation slices depend upon: typed specifications/handles/resources, IDs/revisions/state versions, persistence/transaction/CAS boundaries, historical resolution and migrations.

Concrete persistence technology, Spark table/catalog implementation, runtime/plugin implementation, scheduler/fencing backend, Provenance query store, IAM/network/security stack, observability/platform adapters, public release policy and support/scale matrices remain downstream Phase 005 decisions constrained by the accepted architecture and verification authority.
