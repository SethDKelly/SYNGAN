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

Completing a Phase 005 group means its future implementation plan is complete. No production package, schema, migration, runtime adapter, Evidence/Provenance store, test suite, CI workflow, or deployment infrastructure is created merely by completing these planning groups.

Completed:

- **005-A — Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement**
- **005-B — Verification Strategy, Test Harness, Architecture Fitness Functions, Evidence Fixtures & Quality Gates**
- **005-C — Source Topology, Module/Package Boundaries, Shared Foundation & Dependency Enforcement**
- **005-D — Public Resource API, Control-Plane Identity, State, Persistence, Transactions & Migration Implementation Plan**
- **005-E — Spark Data Boundary, Source/Output References, Manifest, Materialization & Promotion Implementation Plan**
- **005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan**
- **005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**
- **005-H — Evaluation/Evidence, Provenance, Historical Query & Reproducibility Implementation Plan**

Canonical implementation-planning authority is under [`docs/implementation/`](docs/implementation/index.md).

### Implementation-planning baseline through 005-H

The future implementation is planned around:

- one `src/syngan` package with `foundation`, `domain`, `ports`, `application`, `api`, `adapters`, and `bootstrap` boundaries;
- Python >=3.11 with the accepted uv/Hatchling/pytest/Hypothesis/pytest-socket/Ruff/mypy/Import Linter/GitHub Actions toolchain plan;
- one durable `AuthorityId`/`ResourceId`/`ResourceRef`/revision/state/schema model shared across downstream slices;
- SQLAlchemy Core/Alembic with PostgreSQL as the reference production control-store family and SQLite as a local/test profile;
- exact distributed `SourceStateRef` binding, bounded manifests, candidate/sealed-snapshot/output separation and a portable manifested-Parquet profile;
- separate Strategy/Evaluation-method implementation-binding identity and `RuntimeSpiVersion` axes;
- Protocol-based, activity-specific Learning/Generation/Evaluation runtime contracts;
- immutable Attempt-scoped runtime invocations and Learned-State candidate/representation/codec boundaries;
- one stable Execution with multiple Attempts, monotonic AttemptEpoch fencing, checkpoint/recovery, launch reconciliation and cancellation/completion linearization;
- owner-established Evidence with immutable finding content and separate current applicability state;
- exact Generation completion basis retaining the Evidence used at promotion time;
- canonical typed Provenance planned as indexed relational assertions rather than a graph-first metadata authority;
- derived bounded history/provenance/explain/compare projections that cannot overwrite canonical history;
- reproducibility as a qualified derived assessment separating historical support class from current feasibility;
- optional Spark/PyTorch runtime capability families without making either framework the semantic model.

No production implementation has begun.

## Jackson/design completeness gate

The project does **not** assume that reaching the end of Phase 005 automatically means coding should begin.

005-K must explicitly audit whether concept discovery/specification, synchronizations, experience design, architecture and implementation planning are sufficiently complete under the Jackson methodology. If gaps remain, another design-refinement phase is the correct next step.

Even a positive 005-K readiness result still requires a later explicit implementation-authority phase before production coding begins.

Next:

- **005-I — Dependency Resolution, Offline/No-Egress, Authorization, Redaction & Enterprise Security Implementation Plan**

005-I will plan dependency trust/resolution, offline/no-egress enforcement, current action authorization, runtime capabilities, secret handling, redaction/withholding and security-aware history/query behavior against the concrete surfaces defined through 005-H.

Deployment/platform integration, compatibility/scale and the final Jackson/design-completeness audit remain downstream Phase 005 planning work.
