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

**Phase 005 — Implementation Planning & Delivery Decomposition is current and planning-only.**

See [`docs/phases/005/index.md`](docs/phases/005/index.md).

Completing a Phase 005 group means its future implementation plan is complete. No production package, schema, migration, runtime adapter, test suite, CI workflow, or deployment infrastructure is created merely by completing these planning groups.

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**
- **005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**
- **005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**
- **005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**

Canonical implementation-planning authority is under [`docs/implementation/`](docs/implementation/index.md).

### Implementation-planning baseline through 005-G

The future implementation is planned around:

- one `src/syngan` package with `foundation`, `domain`, `ports`, `application`, `api`, `adapters`, and `bootstrap` boundaries;
- Python >=3.11 with uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions as the planned foundational toolchain;
- one durable `AuthorityId`/`ResourceId`/`ResourceRef`/revision/state/schema model shared across downstream slices;
- SQLAlchemy Core/Alembic with PostgreSQL as the reference production control store and SQLite as a local/test profile;
- exact distributed `SourceStateRef` binding, bounded manifests, candidate/sealed-snapshot/output separation, and a portable manifested-Parquet data profile;
- separate Strategy/Evaluation-method implementation-binding identity and `RuntimeSpiVersion` axes;
- Protocol-based, activity-specific Learning/Generation/Evaluation runtime contracts and immutable Attempt-scoped runtime invocation;
- Learned-State candidate and representation/codec boundaries distinct from logical Learned State and loaded runtime objects;
- one stable Execution with many durable Attempts and monotonic AttemptEpoch values;
- Attempt observed runtime state separated from current mutation authority;
- isolation-first stale-writer fencing at bounded registration/adoption/seal/completion boundaries;
- durable launch intent/correlation and unknown-state reconciliation rather than blind resubmission;
- immutable checkpoints with contextual resume qualification and explicit restart/resume/reconcile modes;
- operation-scoped idempotency rather than one global Execution key;
- cancellation/completion linearization in which accepted cancellation revokes old writer/promotion authority before physical termination is assumed;
- operational completion explicitly separate from Learning/Generation/Evaluation semantic completion.

No production implementation has begun.

Next:

- **005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**

005-H will plan idempotent Evidence establishment, typed/correctable Provenance assertions, historical indexes/query projections, explanation/comparison views, and reproducibility assessment using the exact semantic, runtime, Execution, Attempt, checkpoint and promotion facts now available through 005-G.

Security/authorization, platform/deployment integration, compatibility/scale, and final cross-slice implementation-readiness remain downstream Phase 005 planning work.
