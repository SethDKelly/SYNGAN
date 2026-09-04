# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

Phase 001 established the accepted concept catalog, core synchronization rules, enterprise scale boundary, canonical terminology, and explicit deferred representation concerns.

**Phase 002 — Concept Specification & Invariant Refinement is in progress.**

Completed:

- **002-A — Data Meaning & Constraint Specification**
- **002-B — Synthesis Strategy Specification & Capability Semantics**
- **002-C — Learning & Learned State Specification**

Current design includes:

- supported core structured/tabular synthesis without required outbound network access;
- explicit Strategy dependency/network profiles;
- Learning commitment with stable source/semantic/Strategy/Constraint context;
- retry/resume that preserves committed Learning semantics;
- checkpoint/intermediate state separated from completed Learned State;
- one primary logical Learned State per successful Learning under the current model;
- Learned State that may be distributed/composite and is not presumed private or release-safe.

Next:

- **002-D — Generation Specification, Request/Condition Semantics & Output Completion**

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
