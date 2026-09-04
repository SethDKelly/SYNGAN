# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

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

**Phase 002 — Concept Specification & Invariant Refinement is in progress.**

Completed:

- **002-A — Data Meaning & Constraint Specification**
- **002-B — Synthesis Strategy Specification & Capability Semantics**

002-B also established a design requirement that supported core structured/tabular synthesis remain usable without outbound network access, while optional Strategies may explicitly declare local-artifact, acquisition-network, or runtime-network dependencies.

Next:

- **002-C — Learning & Learned State Specification**

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
