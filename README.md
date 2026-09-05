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

**Phase 003 — Experience & Workflow Design: complete.**

**Phase 004 — Representation & Architecture Design: complete.**

Phase 004 closed through [`004-J — Cross-Architecture Invariant Audit, Decision Consolidation & Phase 004 Exit`](docs/phases/004/004-J-cross-architecture-invariant-audit-decision-consolidation-phase-004-exit.md) with no blocking redesign required.

## Current phase

**Phase 005 — Implementation Planning & Delivery Decomposition is current.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**

Canonical implementation authority is under [`docs/implementation/`](docs/implementation/index.md).

### Implementation baseline through 005-C

The accepted implementation scaffold remains a plan rather than production code:

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

Foundational tooling includes Python >=3.11, uv/`uv.lock`, Hatchling, pytest/Hypothesis/pytest-socket, Ruff, mypy, Import Linter, coverage diagnostics and GitHub Actions with Q0-Q4 verification semantics.

### Durable public/control-plane baseline from 005-D

005-D now fixes the implementation plan for the shared control substrate:

- opaque AuthorityId and UUIDv4 ResourceId identities;
- typed ResourceRef, family-scoped RevisionNumber/RevisionRef, SnapshotId, StateVersion and SchemaVersion axes;
- immutable standard-library public/domain values and owner-specific lifecycle states;
- `LearningSpec`, `GenerationSpec`, `EvaluationSpec`, typed handles/views and a non-authoritative `SynGANClient` facade;
- exact typed historical resolution preserving absent/unavailable/unknown/invalid/withheld distinctions;
- explicit versioned JSON codecs and no pickle for canonical control/wire state;
- owner-meaningful persistence ports rather than a universal metadata registry;
- SQLAlchemy Core 2.x as the built-in relational persistence adapter technology;
- Alembic 1.x migrations;
- PostgreSQL as the reference production control backend and SQLite as the local/test backend;
- Psycopg 3 as the PostgreSQL driver family;
- optional `sql`/`postgres` persistence capability isolation from the base package;
- expected-version CAS, bounded transactions/locks, operation-scoped idempotency support, transactional outbox/durable intent, explicit tombstones and migration rules preserving immutable history.

005-D remains an implementation plan; it has not yet created production resource/persistence code.

Next:

- **005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**

005-E will map Spark DataFrames/table/file selectors to exact 005-D resource/history references, define distributed source/output/manifests and candidate sealing, and specify Generation promotion without making DataFrames/paths/table aliases canonical identity or requiring full driver-local materialization.

Runtime/plugin implementation, scheduler/fencing/recovery, Evidence/Provenance/history, security/authorization, Databricks/deployment integration and support/scale matrices remain downstream Phase 005 work.
