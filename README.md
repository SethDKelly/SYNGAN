# SYNGAN

SYNGAN is a design-first synthetic data generation framework intended for Spark-scale workloads.

The project is deliberately completing conceptual design before implementation. Daniel Jackson's concept-design methodology governs discovery and specification, and canonical design knowledge is maintained as an OKF 0.2 bundle.

## Design documentation

Start with [`docs/index.md`](docs/index.md).

## Current status

**Phase 001 — Design Foundation & Concept Discovery is complete.**

**Phase 002 — Concept Specification & Invariant Refinement is complete.**

Phase 002 closed with eleven accepted concepts, fifteen synchronization rules, offline/no-outbound-network-capable core semantics, stable commitment/historical binding, semantic result promotion, typed Provenance, qualified reproducibility, and enterprise-scale no-full-driver-materialization requirements.

**Phase 003 — Experience & Workflow Design is complete.**

The [Phase 003 Consolidated Experience Contract](docs/experience/phase-003-consolidated-experience-contract.md) freezes readiness/commitment, semantic/operational, promotion, Evidence, historical/current, reproducibility, dependency/network/egress, disclosure, programmatic-parity, and enterprise-scale experience obligations.

**Current phase: Phase 004 — Representation & Architecture Design.**

See [`docs/architecture/index.md`](docs/architecture/index.md) and [`docs/phases/004/index.md`](docs/phases/004/index.md).

Completed:

- **004-A — Architecture Authority, Representation Principles, Layering & Dependency Direction**

004-A establishes the canonical [`architecture constitution`](docs/architecture/architecture-authority-representation-layering.md):

- architecture remains downstream of authority, concepts, synchronizations, and experience;
- representation convenience cannot redefine semantic ownership;
- stable logical identity remains distinct from mutable physical/platform locators;
- bounded control-plane state references large distributed data-plane payloads;
- physical durability does not establish Learned State/output/Evidence promotion;
- dependencies point inward toward stable semantic/control contracts;
- platform/runtime integrations remain adapters rather than universal authority;
- bidirectional semantic synchronization does not justify cyclic package dependencies;
- supported offline/no-egress paths remain isolatable from optional network integrations;
- Spark-native means distributed Spark-scale data semantics rather than universal Spark ML;
- model-neutral semantics do not depend universally on CTGAN/GAN/PyTorch/HuggingFace/LLM/runtime families;
- convenience Session/Context/Manager/Metadata/Engine-style facades cannot become god-state owners;
- platform specialization may add capability but cannot silently weaken common guarantees;
- architecture decisions use [`docs/decisions/`](docs/decisions/index.md) for durable rationale/supersession while current normative rules remain under `docs/architecture/`.

Next:

- **004-B — Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping**

No final Python package/module tree, public class hierarchy, persistence engine, Spark output-manifest/promotion mechanism, strategy plugin loader, scheduler/orchestrator, checkpoint/fencing mechanism, provenance store, authorization engine, egress-control technology, model registry, or deployment topology should be treated as settled until the relevant later Phase 004 group accepts it.
