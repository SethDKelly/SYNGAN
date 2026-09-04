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
- **002-E — Evaluation Criterion, Evaluation & Evidence Specification**
- **002-F — Execution, Attempt History, Failure & Recovery Semantics**

Current design includes:

- supported core structured/tabular synthesis without required outbound network access;
- explicit Strategy dependency/network profiles;
- stable Learning commitment and distributed/composite Learned State;
- Generation Request/Condition semantics, direct and Learned-State generation paths, and a semantic output-promotion barrier;
- Criterion/Evaluation/Evidence separation with explicit coverage, uncertainty, and claim-strength limits;
- one logical Execution independent of Spark/Databricks/Kubernetes/PyTorch physical jobs;
- Attempt as subordinate operational history rather than a platform-run synonym;
- retry/resume that preserves committed domain semantics;
- checkpoint/intermediate state that cannot become Learned State, completed output, or Evidence merely by being durable;
- explicit partial operational success and unknown/indeterminate platform state;
- contextual retryability, recovery reconciliation, and cancellation-race semantics;
- single semantic promotion instead of an unrealistic exactly-once physical-computation guarantee;
- duplicate physical work permitted only when canonical Learned State/output/Evidence effects remain unambiguous;
- operational history that remains enterprise-scale control-plane state rather than a copy of every task/log/telemetry event.

Next:

- **002-G — Provenance, Reproducibility Contract & Historical Binding Specification**

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, scheduler/orchestrator, checkpoint technology, output storage/publication mechanism, evidence/reporting technology, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
