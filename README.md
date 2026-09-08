# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual, architectural, and implementation planning before production coding begins. Daniel Jackson's concept-design methodology governs the design program, and canonical knowledge is maintained as an OKF-oriented bundle.

## Documentation

Start with [`docs/index.md`](docs/index.md).

Primary implementation-facing authority:

- [`Phase 003 Consolidated Experience Contract`](docs/experience/phase-003-consolidated-experience-contract.md)
- [`Phase 004 Consolidated Architecture Contract`](docs/architecture/phase-004-consolidated-architecture-contract.md)
- [`Implementation Planning & Delivery Authority`](docs/implementation/index.md)
- [`AGENTS.md`](AGENTS.md) for repository-wide automated-agent rules

## Current status

- Phase 001 — Design Foundation & Concept Discovery — complete
- Phase 002 — Concept Specification & Invariant Refinement — complete
- Phase 003 — Experience & Workflow Design — complete
- Phase 004 — Representation & Architecture Design — complete
- **Phase 005 — Implementation Planning & Delivery Decomposition — current and planning-only**

005-A through 005-J are complete as future implementation plans. No production package, schema, adapter, test suite, CI workflow, platform integration or deployment infrastructure has been created by those phases.

The planning baseline now covers:

- package/toolchain/dependency topology and verification gates;
- durable identity/control persistence/migrations;
- Spark-scale exact data references, manifests and promotion;
- model-neutral runtime SPI and Learned-State representation;
- Execution/Attempt fencing, recovery, reconciliation and cancellation;
- Evidence, canonical Provenance, historical queries and reproducibility;
- dependency trust, offline/no-egress, authorization, secrets, redaction and isolation;
- local, portable Spark, Databricks-oriented and private/offline deployment profiles;
- capability-negotiated platform adapters rather than platform-name authority;
- separate canonical history, platform telemetry and security audit;
- compatibility/support matrices, rolling upgrades and multi-dimensional scale/performance evidence;
- disaster recovery that prevents stale writer authority from being resurrected by a regressive control-store restore.

## Jackson/design completeness gate

The project does **not** assume that finishing Phase 005 means coding should automatically begin.

Next:

**005-K — Cross-Slice Integration, Delivery Sequencing, Backlog Closure, Jackson-Methodology Completeness & Implementation-Readiness Exit**

005-K must audit the complete design/planning program and decide either:

```text
DESIGN COMPLETE ENOUGH FOR A LATER EXPLICIT IMPLEMENTATION-AUTHORITY PHASE
```

or:

```text
FURTHER DESIGN / REFINEMENT REQUIRED
```

Even a positive 005-K result does not itself authorize coding.
