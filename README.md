# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

Phase 001 established:

- design/documentation authority and OKF governance;
- problem, actors, outcomes, and enterprise scale envelope;
- canonical domain terminology;
- an accepted initial catalog of eleven concepts;
- accepted cross-concept synchronization rules;
- explicit deferred boundaries for relational synthesis, mechanism-specific privacy, representation architecture, and public API design.

Next:

- **002-A — Data Meaning & Constraint Specification**

No Python package, model runtime, Spark ML mapping, persistence format, or plugin architecture should be treated as settled until the relevant downstream design phases establish it.
