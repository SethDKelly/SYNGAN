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
- **002-D — Generation Specification, Request/Condition Semantics & Output Completion**

Current design includes:

- supported core structured/tabular synthesis without required outbound network access;
- explicit Strategy dependency/network profiles;
- Learning commitment with stable source/semantic/Strategy/Constraint context;
- checkpoint/intermediate state separated from completed Learned State;
- Learned State that may be distributed/composite, reused non-mutatively, and is not presumed private or release-safe;
- Generation Request and Condition as Generation-owned semantics rather than separate concepts;
- direct-generation and Learned-State generation paths;
- mandatory versus best-effort Condition semantics;
- required Constraint handling that cannot be silently weakened;
- candidate/partial materialization kept distinct from completed synthetic output;
- a Generation completion barrier that requires mandatory request/Condition/Constraint/dependency/provenance obligations before one logical output result is promoted as complete;
- completion that remains distinct from Execution success, privacy guarantees, or external release/use approval.

Next:

- **002-E — Evaluation Criterion, Evaluation & Evidence Specification**

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, output storage/publication mechanism, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
