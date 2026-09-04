# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

**Phase 002 — Concept Specification & Invariant Refinement is complete.**

Phase 002 closed with:

- eleven accepted concepts with clear ownership/lifecycle boundaries;
- fifteen accepted synchronization rules;
- core structured/tabular operation without required outbound network access;
- explicit Strategy dependency/network profiles and no hidden artifact acquisition;
- stable semantic commitment and historical binding;
- distributed/composite Learned State with non-mutating reuse;
- direct and Learned-State Generation paths plus a semantic output-promotion barrier;
- Criterion/Evaluation/Evidence separation with explicit claim-strength limits;
- one logical Execution independent of physical platform jobs;
- retry/resume/checkpoint recovery using single semantic promotion rather than exactly-once physical computation;
- typed Provenance and a qualified Reproducibility Contract;
- enterprise-scale semantics that avoid mandatory full driver-local source/output/model/log materialization;
- explicit separation of synthetic origin, privacy evidence/guarantees, and external release/use authority.

**Phase 003 — Experience & Workflow Design is complete.**

Phase 003 established canonical actor-visible/programmatic experiences for:

- workflow/source/lifecycle entry;
- Data Meaning/Constraint/Strategy preparation;
- Learning and Learned State lifecycle;
- Generation request/Condition/validation/output promotion;
- Evaluation/Evidence/review;
- Execution monitoring/failure/recovery/cancellation;
- Provenance/reproducibility/historical inspection;
- enterprise dependency/offline/no-egress/safety.

The [Phase 003 Consolidated Experience Contract](docs/experience/phase-003-consolidated-experience-contract.md) freezes the cross-workflow rules for readiness versus commitment, semantic versus operational state, checkpoint/candidate/result promotion, Evidence claim strength, historical versus current state, qualified reproducibility, dependency/network/egress posture, truthful restricted disclosure, human/programmatic parity, and enterprise-scale bounded control-plane behavior.

The 003-I exit audit found no concept or synchronization redesign required before architecture work.

**Current phase: Phase 004 — Representation & Architecture Design.**

See [`docs/architecture/index.md`](docs/architecture/index.md) and [`docs/phases/004/index.md`](docs/phases/004/index.md).

Phase 004 will decide implementation-facing architecture for:

- public API/resource/handle mapping;
- control-plane identity, revisions and persistence;
- Spark-scale source/output references, manifests and semantic promotion;
- Strategy extension and Learning/Generation/Evaluation runtime adapters;
- Execution/Attempt/checkpoint/recovery/fencing/idempotency/cancellation;
- Evaluation/Evidence/Provenance/reproducibility representation and historical queries;
- dependency resolution, offline/no-egress, authorization/redaction and enterprise security;
- deployment, scalability, observability, portability and platform integration.

Next:

- **004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction**

No Python package/module layout, public class hierarchy, persistence technology, plugin system, scheduler/orchestrator, checkpoint format, provenance store, source/output manifest/fingerprint mechanism, model registry, authentication/authorization engine, egress-control technology, or deployment topology should be treated as settled until Phase 004 establishes it.