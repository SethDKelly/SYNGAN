# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project deliberately completes conceptual, experience, architecture, and implementation planning **before production coding begins**. Daniel Jackson's concept-design methodology governs discovery/specification, and canonical knowledge is maintained as an OKF-oriented bundle.

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

**Phase 005 — Implementation Planning & Delivery Decomposition is current and remains planning-only.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

During Phase 005, SYNGAN may select concrete future package paths, technologies, interfaces, persistence patterns, runtime boundaries, verification profiles and delivery sequences, but it does **not** create production source code, database schemas/migrations, Spark/runtime adapters, verification suites, CI workflows or deployment infrastructure. Actual coding begins only when a later phase explicitly authorizes implementation.

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**
- **005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**

Canonical implementation-planning authority is under [`docs/implementation/`](docs/implementation/index.md).

### Planned source/toolchain foundation

The accepted future scaffold remains a plan rather than production code:

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

Foundational tooling is planned around Python >=3.11, uv/`uv.lock`, Hatchling, pytest/Hypothesis/pytest-socket, Ruff, mypy, Import Linter, coverage diagnostics and GitHub Actions with Q0-Q4 verification semantics.

### Planned durable public/control-plane substrate

005-D fixes future AuthorityId/ResourceId/ResourceRef/RevisionRef/SnapshotId/StateVersion/SchemaVersion conventions, immutable public specs/handles/views, typed historical resolution, SQLAlchemy Core/Alembic/PostgreSQL/SQLite/Psycopg persistence, expected-version CAS, bounded transactions, idempotency/outbox and migration rules preserving immutable history.

No resource/persistence code or migration has been created.

### Planned Spark/distributed-data substrate

005-E now fixes the future distributed-data boundary:

- PySpark remains optional behind the `spark` capability extra;
- Spark DataFrame/table/path/query values are selectors/access objects rather than canonical history;
- committed work binds exact `SourceStateRef` state;
- arbitrary DataFrame/query/mutable-locator input defaults to explicit distributed snapshot preparation unless a provider proves exact stable native binding;
- manifest identity uses bounded roots plus distributed/provider-native component indexes;
- a manifested-Parquet profile is the first generic file representation plan, without making Parquet or any table format semantic authority;
- Generation candidate, sealed data snapshot and logical completed output remain distinct roles;
- required completion Evaluation binds the exact sealed snapshot;
- Generation promotion is idempotent, may be metadata-only, and reuses the 005-D control-plane transaction/CAS/outbox model;
- 005-G and 005-I retain ownership of writer fencing/recovery and security/no-egress enforcement.

No PySpark dependency, Spark adapter, manifest, storage layout, migration or Spark test suite has been created.

Next:

- **005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**

005-F will remain planning-only while defining future model-neutral runtime/provider contracts over the durable control and distributed-data plans already accepted.
