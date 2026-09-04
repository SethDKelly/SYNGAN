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

**Current phase: Phase 003 — Experience & Workflow Design.**

Completed:

- **003-A — Workflow Entry, Source Context & Lifecycle Orientation**
- **003-B — Data Meaning, Constraint & Strategy Preparation Experience**
- **003-C — Learning & Learned State Lifecycle Experience**

Phase 003 now includes a canonical [`docs/experience/`](docs/experience/index.md) layer. 003-A established intent-oriented entry and lifecycle orientation. 003-B established pre-commit preparation that keeps Data Meaning, Constraint, and Synthesis Strategy distinct while making semantic/rule/Strategy readiness explainable. 003-C establishes Learning/Learned State lifecycle experience: commitment is explicit, semantic progress is kept separate from Execution/Attempt state, checkpoints remain non-final, semantic completion promotes one logical Learned State, `usable` does not mean globally compatible, restricted/retired/invalidated statuses remain distinct, and reuse remains non-mutating.

The experience design continues to preserve the enterprise-safe direction: no hidden network acquisition/fallback, no mandatory full driver-local source/model collection, no model artifact equated automatically with Learned State, and no implication that source-derived learned state is private or safe to export by default.

Next:

- **003-D — Generation Request, Condition, Validation & Output Promotion Experience**

See [`docs/phases/003/index.md`](docs/phases/003/index.md).

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, scheduler/orchestrator, checkpoint technology, model registry technology, provenance store, identity/fingerprint mechanism, output publication mechanism, evidence/reporting technology, final workflow/session/readiness object, compatibility engine, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
