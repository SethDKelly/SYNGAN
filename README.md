# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

**Phase 002 — Concept Specification & Invariant Refinement is complete.**

Phase 002 refined the accepted semantic model and closed with no concept/synchronization redesign required.

The current semantic design includes:

- eleven accepted concepts with clear ownership and lifecycle boundaries;
- fifteen accepted synchronization rules;
- supported core structured/tabular synthesis without required outbound network access;
- explicit Strategy dependency/network profiles and no hidden model/artifact acquisition;
- stable semantic commitment and historical binding across Learning, Generation and Evaluation;
- distributed/composite Learned State with non-mutating reuse;
- Generation Request/Condition semantics, direct and Learned-State generation paths, and a semantic output-promotion barrier;
- Criterion/Evaluation/Evidence separation with explicit coverage, uncertainty, and claim-strength limits;
- one logical Execution independent of Spark/Databricks/Kubernetes/PyTorch physical jobs;
- retry/resume/checkpoint recovery that preserves committed semantics and uses single semantic promotion rather than exactly-once physical computation;
- Provenance as typed stable-reference history rather than a copy of domain state or platform telemetry;
- a cross-cutting Reproducibility Contract distinguishing exact deterministic, semantic, statistical, bounded/approximate, comparative, and explicitly insufficient/not-reproducible outcomes;
- enterprise-scale semantics that do not require full source/output/model/log collection to driver-local memory;
- explicit separation of synthetic origin, privacy evidence/guarantees, and external release/use authority.

Phase 002 exit review:

- [`002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review`](docs/phases/002/002-H-cross-concept-invariant-synchronization-consolidation-review.md)

**Current phase: Phase 003 — Experience & Workflow Design.**

Completed:

- **003-A — Workflow Entry, Source Context & Lifecycle Orientation**

003-A established the canonical [`docs/experience/`](docs/experience/index.md) layer. The experience model now supports multiple legitimate entry intents, composes source context without creating a Dataset/Workflow god-concept, distinguishes mutable locators from historical identity, makes semantic commitment explicit, separates semantic status from Execution/Attempt state, keeps candidate/intermediate material distinct from authoritative results, preserves indeterminacy, and exposes network/dependency posture before commitment.

Next:

- **003-B — Data Meaning, Constraint & Strategy Preparation Experience**

See [`docs/phases/003/index.md`](docs/phases/003/index.md).

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, scheduler/orchestrator, checkpoint technology, provenance store, identity/fingerprint mechanism, output publication mechanism, evidence/reporting technology, final workflow/session object, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
