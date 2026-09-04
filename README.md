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
- **002-G — Provenance, Reproducibility Contract & Historical Binding Specification**

Current design includes:

- supported core structured/tabular synthesis without required outbound network access;
- explicit Strategy dependency/network profiles;
- stable Learning commitment and distributed/composite Learned State;
- Generation Request/Condition semantics, direct and Learned-State generation paths, and a semantic output-promotion barrier;
- Criterion/Evaluation/Evidence separation with explicit coverage, uncertainty, and claim-strength limits;
- one logical Execution independent of Spark/Databricks/Kubernetes/PyTorch physical jobs;
- retry/resume/checkpoint recovery that preserves committed semantics and uses single semantic promotion rather than exactly-once physical computation;
- Provenance as typed stable-reference history rather than a copy of all domain state or platform telemetry;
- historical bindings that remain tied to the exact source/meaning/Strategy/Constraint/Learned State/Condition/Criterion/method/dependency state actually used;
- a cross-cutting Reproducibility Contract that distinguishes exact deterministic, semantic, statistical, bounded/approximate, comparative, and explicitly insufficient/not-reproducible outcomes;
- explicit recognition that seeds, mutable aliases, URLs, or rerunnable jobs alone do not establish reproducibility;
- enterprise-scale provenance/reproducibility that does not require full source/output/model/log collection to driver-local memory.

Next:

- **002-H — Cross-Concept Invariant, Synchronization & Phase 002 Consolidation Review**

No Python package, model runtime, Spark ML mapping, persistence format, plugin architecture, scheduler/orchestrator, checkpoint technology, provenance store, identity/fingerprint mechanism, output publication mechanism, evidence/reporting technology, or model-hub/network integration should be treated as settled until the relevant downstream design phases establish it.
