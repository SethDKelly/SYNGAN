---
type: Phase Record
title: 004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture
status: complete
---

# 004-E — Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture

## Objective

Translate accepted Strategy, Learning, Learned State, Generation, Evaluation, Execution, public handle, control-plane identity, and distributed data-reference contracts into an executable extension/runtime architecture that remains model-neutral, Spark-scale, offline-capable, and semantically subordinate.

004-E must make executable code extensible without allowing plugin/runtime objects to become canonical Strategy identity, activity identity, Learned State, completed output, Evidence, or Execution authority.

## Governing authority

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](../../architecture/architecture-authority-representation-layering.md)
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](../../architecture/public-api-resource-handle-workflow-semantic-mapping.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md)
- [Synthesis Strategy](../../concepts/synthesis-strategy.md)
- [Learning](../../concepts/learning.md)
- [Learned State](../../concepts/learned-state.md)
- [Generation](../../concepts/generation.md)
- [Evaluation](../../concepts/evaluation.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)

## Canonical architecture created

- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md)

## ADR created

- [ADR-0004 — Semantic Extension & Runtime Binding Separation](../../decisions/ADR-0004-semantic-extension-runtime-binding-separation.md)

## Main decisions

### 1. Semantic declaration, implementation binding, and runtime realization are separate

The accepted architecture is:

```text
Strategy/method semantic authority
        ↓
implementation binding
        ↓
immutable activity/Attempt runtime invocation
        ↓
runtime adapter
        ↓
non-final physical/method result
        ↓
semantic owner validates/promotes
```

A plugin class is not a Strategy. A runtime result is not a domain result.

### 2. Strategy implementation bindings are explicit architecture state

A binding records which exact Strategy revision/configuration contract an implementation can realize and its package/runtime/state-codec/dependency/resource limitations.

Bindings may narrow Strategy capability but may not silently broaden it.

### 3. Implementation version and semantic Strategy revision remain distinct

A package/runtime update can remain under the same Strategy revision when semantic behavior/capability/configuration meaning is unchanged, while the material implementation identity still remains historical Provenance/reproducibility context.

If semantic behavior/capability/dependency/configuration meaning changes materially, the Strategy/configuration authority must change as well.

### 4. Evaluation methods use the same binding principle without creating a new concept

Evaluation commits method identity/configuration, scope, subject/reference, coverage, and uncertainty semantics.

Executable method bindings declare how that method is realized in a given runtime. They do not own Criterion or Evidence.

### 5. Discovery/registration is infrastructure only

Python entry points, dependency injection, managed catalogs, configuration, or built-in registration remain possible discovery mechanisms.

No mechanism is selected yet.

Discovery does not make a Strategy effective/compatible/authorized simply because code is installed.

### 6. No hidden runtime package/model acquisition

Missing extension code, dependencies, models, or artifacts cannot trigger undeclared runtime downloads or remote fallback.

Provisioning/acquisition remains explicit under network/dependency policy.

### 7. Version axes remain separate

At least the following remain distinguishable:

- Strategy semantic revision;
- implementation-binding revision;
- extension/SPI version;
- package/build version;
- Learned State state-codec/representation version.

### 8. Runtime invocation is a bounded immutable Attempt-scoped contract

The application/control layer resolves the exact committed activity, implementation binding, source/subject/reference/Learned State dependencies, runtime resources, network/no-egress posture, output sinks, and Attempt/fencing context before calling runtime code.

Runtime adapters do not query arbitrary canonical repositories or mutate committed semantics.

### 9. Runtime adapters report facts through ports rather than mutate canonical state

Adapters may read exact references, run compute, write non-final material, report progress/checkpoints/results, and emit material runtime facts.

They cannot directly:

- complete Learning/Generation/Evaluation;
- establish Learned State;
- promote output;
- establish Evidence;
- authorize network/egress;
- silently substitute dependencies.

### 10. Learning uses a non-final Learned State materialization boundary

Learning adapters write checkpoints/intermediates and candidate final learned components through explicit framework-approved materialization/workspace roles.

A candidate learned representation is sealed/integrity-checked and remains non-final until Learning performs semantic validation and establishes the one primary Learned State.

Checkpoint durability remains distinct from Learned State establishment.

### 11. Learned State logical identity remains separate from runtime load objects

A PyTorch module, Spark ML model, statistical object, or other loaded model state is a transient runtime realization of a Learned State representation.

The logical Learned State survives runtime teardown and may be loaded by another explicitly compatible binding.

### 12. Learned State can remain distributed

Adapters may load/shard learned components directly into workers/accelerators from durable references.

Enterprise operation does not require full Learned State payload loading to driver memory.

### 13. Representation conversion requires explicit equivalence

Codec/storage conversion may preserve Learned State identity only when learned semantics are explicitly preserved.

Fine-tuning/adaptation/material behavior change creates a new distinguishable learned result, normally through Learning.

### 14. Generation preserves Learned-State and direct-generation runtime paths

A Strategy may generate from Learned State or generate directly from committed source/input/configuration.

Direct-generation Strategies do not fabricate Learning/Learned State.

### 15. Generation runtime writes only through supplied candidate sinks

Candidate/materialization identity, approved output destination, manifest membership, Attempt/writer fencing context, and seal handoff remain framework-owned architecture.

The adapter cannot directly publish a final output.

### 16. Generation runtime success is not Generation completion

An adapter may report candidate extent and operational success, but required Evaluation/Condition/Constraint/provenance obligations and 004-D promotion still determine Generation completion.

### 17. Evaluation runtime binds exact immutable subject/reference

Completion Evaluations examine the exact sealed candidate snapshot, not a mutable alias that may have changed after commitment.

### 18. Evaluation adapter results remain richer than pass/fail

Adapters preserve measurements, coverage, uncertainty, assumptions, diagnostics, limitations, and claim-support facts required by Evaluation.

Evaluation—not the adapter—decides whether interpretable Evidence can be established.

### 19. Large Evaluation diagnostics remain data-plane state

Violation rows, attack traces, nearest-neighbor examples, samples, or detailed per-row results remain referenced data-plane outputs rather than inflated Evidence/control-plane payloads.

### 20. Operational realization stays under Execution

Runtime launchers may create Spark jobs, Databricks runs, Kubernetes jobs, PyTorch processes, workers, or remote calls, but those platform objects remain subordinate to one SYNGAN Execution/Attempt.

### 21. No universal runtime family is selected

Conformant implementations may be Spark-native, bounded local, distributed PyTorch/other ML, accelerator-oriented, hybrid, or optional remote-service based.

No runtime family becomes package-wide semantics.

### 22. Spark-native remains a data-boundary guarantee

A PyTorch or other non-Spark model runtime is fully compatible with SYNGAN when large structured source/output interaction remains distributed and exact under the 004-D reference/materialization architecture.

`Collect all Spark rows to pandas on the driver` is not an acceptable ordinary enterprise-scale adapter design merely because a model API is local.

### 23. Platform specialization may add capability but cannot weaken common guarantees

Databricks/GPU/provider-specific adapters can optimize snapshotting, launch, checkpointing, streaming, or observability but must preserve source/output identity, no-hidden-egress, semantic completion, and historical/reproducibility boundaries.

### 24. Dependency and egress behavior remain explicit

Runtime bindings may declare concrete software, accelerator, local artifact, Spark, topology, service, scratch-space, or network requirements.

Network connectivity does not grant data-egress authority.

### 25. Runtime progress stays operational

Stages, epochs, partitions, loss, work units, checkpoints, and health are Execution-facing operational facts and do not become universal semantic completion percentages.

### 26. Checkpoint/cancellation architecture remains subordinate to 004-F

004-E defines extension-facing checkpoint and cooperative-cancellation ports only.

004-F will define authoritative checkpoint/recovery qualification, fencing, retry/idempotency, cancellation races, and reconciliation.

### 27. Runtime failure categories remain structured

The architecture preserves extension unavailable, SPI incompatible, dependency missing/mismatched, policy incompatible, reference failure, adapter protocol defect, recoverable/terminal runtime failure, codec incompatibility, materialization integrity defect, semantic result invalidity, and unknown runtime outcome as distinct conditions where material.

### 28. Extension conformance requires declarations plus behavior

Executable registration alone is not conformance.

A conformant extension identifies its semantic contract, declares material runtime/dependency/network behavior, respects immutable committed references, uses approved state/output boundaries, keeps intermediates non-final, reports material Provenance/reproducibility facts, and does not silently weaken scale/security guarantees.

## Alternatives rejected as canonical architecture

- Strategy equals Python plugin class;
- one generic `run(context) -> Result` extension contract as the only typed boundary;
- every implementation release creates a new Strategy revision;
- implementation identity ignored whenever Strategy revision is unchanged;
- plugin/runtime code writes canonical domain state directly;
- Spark ML Estimator/Model as universal Strategy abstraction;
- PyTorch as universal model/runtime abstraction;
- hidden package/model acquisition on missing dependency;
- full-corpus driver collection as generic bridge between Spark and model runtimes.

## Architecture consequences for later groups

### 004-F

Must define Execution/Attempt invocation identity, leases/fencing, checkpoint records, resume compatibility, retry/idempotency, cancellation, unknown outcomes, and reconciliation underneath these runtime ports.

### 004-G

Must preserve exact implementation-binding/runtime/dependency/subject/candidate identities in Evidence/Provenance/reproducibility without copying runtime payloads.

### 004-H

Must define extension/package/artifact trust, dependency resolution authority, credentials, runtime-network controls, egress enforcement, and disclosure/redaction.

### 004-I

Must define deployment/launcher topology, platform compatibility matrices, Spark/Databricks integration, accelerator/distributed runtime specialization, observability, and portability behavior.

## No new concept result

004-E does not introduce domain concepts for:

- Plugin;
- Extension;
- Strategy Implementation;
- Runtime Adapter;
- Evaluation Method Plugin;
- Runtime Binding;
- Launcher;
- Driver;
- Worker;
- State Codec;
- State Materialization;
- Model Runtime;
- Runtime Result.

These remain architecture/implementation roles beneath accepted concepts.

## Deferred decisions

004-E intentionally does not settle:

- Python plugin discovery/loading mechanism;
- final package/module layout;
- ABC versus Protocol versus another interface style;
- exact runtime request/result classes;
- Spark ML integration details;
- PyTorch/TorchDistributor/torchrun selection;
- distributed-training framework;
- Learned State serialization/manifest schema;
- model-registry integration;
- remote-service SDK strategy;
- scheduler/orchestrator;
- checkpoint store;
- plugin signing/sandboxing/trust enforcement;
- process/container isolation;
- progress/cancellation callback spelling;
- exception/result-envelope classes.

## Exit criteria

- [x] Strategy semantics separated from executable implementation binding;
- [x] implementation-binding version/provenance contract established;
- [x] Evaluation method binding role established without new domain concept;
- [x] extension discovery/registration kept infrastructural;
- [x] no hidden runtime acquisition/fallback allowed;
- [x] SPI/package/Strategy/state-codec version axes kept distinct;
- [x] immutable bounded runtime invocation architecture established;
- [x] runtime adapters prevented from mutating semantic authority directly;
- [x] Learning candidate-state materialization and semantic establishment separated;
- [x] Learned State identity separated from loaded runtime model/state;
- [x] distributed Learned State loading supported;
- [x] direct and Learned-State Generation paths preserved;
- [x] Generation candidate sink boundary integrated with 004-D;
- [x] Evaluation exact-subject and method-result envelope defined;
- [x] Evidence establishment kept outside method runtime;
- [x] Execution/platform job boundary preserved;
- [x] Spark-native/model-neutral portability preserved;
- [x] dependency/network/egress declarations preserved;
- [x] extension conformance and enterprise-scale testing obligations established;
- [x] no runtime ecosystem or plugin god-concept selected;
- [x] ADR rationale recorded.

## Exit assessment

**Status: complete.**

SYNGAN now has an accepted extension/runtime architecture in which semantic Strategy/method authority is distinct from executable implementation binding, committed activities invoke typed runtime adapters through immutable bounded specifications, Learning and Generation write non-final material through framework-owned boundaries, Evaluation adapters return bounded method results rather than Evidence authority, and Spark-scale data semantics remain compatible with local, distributed ML, accelerator, hybrid, or explicitly networked runtimes.

## Next phase

**004-F — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture**
