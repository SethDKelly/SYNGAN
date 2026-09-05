---
type: Phase Record
title: 005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan
status: complete
---

# 005-F — Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan

## Objective

Translate the accepted Phase 004-E runtime-extension architecture plus the 005-D/005-E durable control/data boundaries into a concrete **future implementation plan** for executable Strategy/method bindings, extension discovery, Learning/Generation/Evaluation runtime SPIs, immutable runtime invocation, Learned-State candidate representation/codecs, and optional Spark/PyTorch runtime integration.

**No production implementation is authorized or performed by this phase.** Phase 005 remains implementation planning and delivery decomposition.

## Entry authority

005-F is downstream of:

- [Phase 004 Consolidated Architecture Contract](../../architecture/phase-004-consolidated-architecture-contract.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [005-B Verification Strategy](../../implementation/verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](../../implementation/source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](../../implementation/public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](../../implementation/spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md).

## Canonical authority created

005-F establishes:

[Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan](../../implementation/strategy-method-extension-spi-learning-generation-evaluation-runtime-learned-state-plan.md).

## Planning-only clarification

005-F creates no Python package, plugin, entry point, runtime adapter, model code, state codec, artifact, test, CI workflow, or platform launcher.

All package paths, protocols, resource kinds, result envelopes and F1-F10 steps are future implementation contracts only.

## Core extension/runtime decisions

Accepted future rules include:

- semantic Strategy/method authority remains separate from executable implementation binding;
- implementation bindings use stable 005-D `ResourceRef` + revision identity;
- Strategy semantic revision, binding revision, SPI version, package/build version and state-codec version remain distinct axes;
- standard-library `typing.Protocol` is the preferred SPI mechanism;
- Learning/Generation/Evaluation use separate typed adapter protocols rather than one generic `run(context) -> Result` interface;
- extension providers are explicitly composed/approved by deployment bootstrap;
- Python package entry points are an optional discovery mechanism using a planned `syngan.runtime_extensions` group;
- entry-point discovery does not authorize, select, trust or semantically register code;
- no global mutable plugin registry is accepted;
- missing extensions/models/packages are never downloaded or installed implicitly during committed runtime;
- every Attempt executes an immutable activity-specific invocation snapshot bound to exact commitment and implementation identities;
- adapters receive only bounded runtime ports/capabilities rather than canonical repositories/SQL sessions/clients;
- runtime success cannot establish Learned State, completed output or Evidence;
- direct-generation remains first-class and does not fabricate Learning/Learned State;
- PyTorch and Spark runtime support remain optional capability families;
- concrete distributed launchers remain owned by 005-G/005-J.

## Binding/version plan

Reserved future `ResourceKind` roles include:

```text
strategy_implementation_binding
evaluation_method_binding
learned_state_candidate
learned_state_representation
```

Implementation binding uses:

```text
ImplementationBindingRef
    family ResourceRef
    RevisionNumber
```

The future SPI also introduces an explicit:

```text
RuntimeSpiVersion(major, minor)
```

which remains separate from semantic revision, binding revision, package version, state codec and representation schema version.

## Discovery plan

Future deployment composition follows:

```text
installed/explicit extension provider
        ↓
trust/compatibility inspection
        ↓
implementation binding declarations
        ↓
immutable process-local RuntimeExtensionCatalog
        ↓
exact binding resolution
        ↓
activity-specific runtime adapter factory
```

The catalog is a derived composition/read mechanism rather than semantic authority.

The planned Python entry-point group is:

```text
syngan.runtime_extensions
```

Entry-point scanning/loading remains lazy/explicit; `import syngan` must not load extensions or optional runtimes.

## Runtime SPI plan

Future structural protocols are equivalent to:

```text
LearningRuntimeAdapter
GenerationRuntimeAdapter
EvaluationRuntimeAdapter
StateCodec
RuntimeExtensionProvider
```

Each activity adapter has separate preflight and execute behavior and receives an activity-specific immutable invocation spec plus narrow runtime ports.

Supporting runtime ports may cover exact data access, candidate/state/diagnostic sinks, dependency resolution, progress, checkpoint hints, cancellation observation, runtime facts and later security capabilities.

They cannot expose unrestricted canonical state mutation.

## Immutable invocation plan

All runtime invocations share bounded facts including:

```text
activity ResourceRef
commitment SnapshotId
exact ImplementationBindingRef
RuntimeSpiVersion
resolved dependency/artifact identities
committed network/no-egress posture
operational runtime parameters
Execution/Attempt authority context (005-G)
```

Activity-specific specifications add exact Learning source/Strategy context, Generation Learned-State/direct-input/candidate-target context, or Evaluation Criterion/method/subject/scope context.

Runtime code cannot silently substitute committed source, Strategy/configuration, Learned State, Conditions, method/scope, dependency identity or network posture.

## Learned-State plan

Learning runtime writes a non-final:

```text
LearnedStateCandidateRef
```

and may seal it into:

```text
LearnedStateRepresentationRef
```

with a bounded state representation descriptor containing codec identity/version, distributed component/manifest root, base-artifact refs, integrity and compatibility facts.

This representation remains separate from:

```text
checkpoint
Learned State logical identity
loaded runtime model/object
```

No universal `.pkl`, `.pt`, Spark-model directory, ONNX file or model-registry representation is accepted.

`StateCodec` owns implementation-specific encoding/loading behavior and must declare safety characteristics such as arbitrary-code/unsafe deserialization risk.

Large Learned State must be representable/loadable through distributed/sharded/streaming mechanisms without a universal full-driver deserialization requirement.

Learning/application logic—not the runtime adapter—later establishes the logical Learned State and representation binding through the 005-D control transition.

## Generation runtime plan

Two paths remain first-class:

```text
Generation + Learned State -> state load -> runtime -> candidate
```

and:

```text
Generation + direct exact input/source -> runtime -> candidate
```

`GenerationRuntimeResult` reports the exact candidate and bounded runtime facts only. It cannot seal/promote the candidate or mark Generation complete.

005-E sealing/Evaluation/promotion remain separate barriers.

## Evaluation runtime plan

Evaluation runtime consumes exact immutable subject/reference identities and produces a bounded `EvaluationRuntimeResult` containing measurements/statistics, achieved coverage, uncertainty/error, validity/assumption diagnostics, diagnostic refs, runtime facts, warnings and operational outcome.

It does not establish Evidence and does not reduce all Evaluation to a universal score/Boolean.

005-H owns Evidence establishment and historical Provenance/reproducibility interpretation.

## Optional runtime dependency plan

005-C's optional capability isolation remains:

```text
syngan base        -> no torch / pyspark requirement
syngan[torch]      -> future PyTorch state/runtime support
syngan[spark]      -> future Spark data/runtime support
syngan[spark,torch] -> explicit hybrid capability composition
```

No broad `all` extra is introduced.

PyTorch/Spark implementation packages remain adapters and do not become Strategy semantics.

## Launcher boundary

005-F deliberately does not choose:

```text
torchrun
TorchDistributor
Databricks jobs
Kubernetes jobs
managed GPU jobs
```

or another launcher.

The SPI remains launcher-neutral. 005-G defines Execution/Attempt/recovery integration and 005-J defines concrete platform capability/launcher mappings.

## Persistence impact plan

Future bounded control records include:

```text
strategy implementation binding revisions
evaluation method binding revisions
Learned-State candidate records
Learned-State representation records
Learned-State current representation binding
Attempt-owned runtime invocation snapshot (005-G)
```

All reuse 005-D ResourceRef/RevisionNumber/StateVersion/SchemaVersion/CAS/transaction conventions.

No schema or migration is implemented during Phase 005.

## Verification mapping

005-F primarily maps future work to V6, with material contributions to V2/V3/V5/V8/V9/V10/V11.

Relevant fitness obligations include:

```text
AF-02 optional runtime dependency isolation
AF-04 runtime/candidate/representation != semantic result
AF-09 runtime success != semantic completion
AF-12 no hidden acquisition/remote fallback/telemetry
AF-13 no universal full-driver data/state collection
AF-14 semantics-preserving runtime/provider fallback
AF-20 runtime/platform identities subordinate to SYNGAN authority
```

Future conformance suites are required for Strategy bindings, Evaluation-method bindings, each activity adapter, StateCodec and extension-provider discovery/loading.

Required future scenarios include lazy/non-authoritative plugin discovery, duplicate entry-point conflicts, immutable invocation substitution rejection, no direct canonical mutation, candidate-vs-semantic-result separation, direct-generation behavior, exact Evaluation subject binding, codec incompatibility/safety, distributed Learned-State loading and offline/no-hidden-download behavior.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
F1  SPI/version/binding contracts
F2  extension provider + discovery boundary
F3  immutable activity-specific invocation specs
F4  Learning/Generation/Evaluation runtime protocols/results
F5  Learned-State candidate/representation/codec contracts
F6  application binding/preflight/invocation/completion coordination
F7  reference/fake conformance providers
F8  optional Spark-native runtime integration
F9  optional PyTorch runtime/state integration
F10 V6 conformance + Q1/Q2 profiles
```

None of F1-F10 is executed during Phase 005.

## Deferred ownership

005-F leaves to:

- 005-G — Execution/Attempt, checkpoint, recovery, fencing, idempotency and cancellation;
- 005-H — Evidence, Provenance, runtime-fact history and reproducibility;
- 005-I — extension/artifact trust, unsafe-state loading policy, authorization, network/egress and secrets;
- 005-J — concrete launchers, platform integrations, runtime compatibility matrix and observability;
- 005-K — final delivery sequencing and implementation-readiness exit.

## No new concepts or upstream revision

005-F adds no Plugin/Extension/Runtime Adapter/Runtime Binding/State Codec/Runtime Invocation/Launcher concept.

No change is required to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture, ADR-0001 through ADR-0008, or 005-C through 005-E implementation-planning authority.

## Exit criteria

- [x] planning-only boundary preserved;
- [x] binding identity/revision/version axes defined;
- [x] Protocol-based activity-specific SPI selected;
- [x] explicit composition + optional entry-point discovery selected;
- [x] no-global-registry/no-auto-install rules defined;
- [x] immutable runtime invocation boundary defined;
- [x] Learning/Generation/Evaluation result boundaries defined;
- [x] Learned-State candidate/representation/codec plan defined;
- [x] state serialization remains runtime-specific and safety-declared;
- [x] distributed Learned-State loading preserved;
- [x] direct Generation preserved;
- [x] optional Spark/PyTorch roles defined;
- [x] launcher selection deferred correctly;
- [x] future persistence/package impacts mapped;
- [x] V6/fitness/conformance obligations mapped;
- [x] F1-F10 future coding sequence defined without execution.

## Exit decision

**005-F — implementation plan complete; no production implementation performed.**

Next:

**005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**.
