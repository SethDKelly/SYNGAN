---
type: Implementation Authority
title: Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan
status: active
---

# Strategy/Method Extension SPI, Learning/Generation/Evaluation Runtime & Learned-State Implementation Plan

## Purpose

Define the concrete **future implementation plan** for SYNGAN's model-neutral executable extension boundary: Strategy implementation bindings, Evaluation-method implementation bindings, extension discovery, typed runtime SPIs, immutable Attempt-scoped invocation specifications, Learning/Generation/Evaluation runtime result boundaries, Learned-State candidate materialization/representation/codec loading, and optional PyTorch/Spark-native/future runtime coexistence.

This document is the canonical Phase 005-F implementation-planning authority.

**Phase 005 remains planning-only.** This document specifies future source/package responsibilities, interfaces, representations, dependency boundaries, sequencing, and verification obligations. It does **not** create production Python source, extension packages, PyTorch/Spark runtimes, state codecs, model artifacts, tests, CI workflows, or runtime infrastructure.

## Governing authority

005-F is downstream of:

- [Phase 004 Consolidated Architecture Contract](../architecture/phase-004-consolidated-architecture-contract.md);
- [Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture](../architecture/strategy-extension-learning-generation-evaluation-runtime-adapter.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](../architecture/spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [005-B Verification Strategy](verification-strategy-test-harness-architecture-fitness-evidence-quality-gates.md);
- [005-C Source Topology](source-topology-module-package-boundaries-shared-foundation-dependency-enforcement.md);
- [005-D Public Resource/Control-Plane Plan](public-resource-control-plane-identity-state-persistence-transactions-migration-plan.md);
- [005-E Spark Data Boundary Plan](spark-data-boundary-source-output-reference-manifest-materialization-promotion-plan.md).

The governing implementation-planning rule is:

> **Executable code realizes an exact committed Strategy/method contract through an exact implementation binding and immutable runtime invocation. Installed plugins, runtime model objects, package versions, Spark/PyTorch jobs, and loaded state objects never become semantic authority.**

## Planning-only boundary

005-F SHALL NOT be interpreted as permission to begin production implementation.

Names such as `StrategyImplementationBinding`, `LearningRuntimeAdapter`, `StateCodec`, and `RuntimeInvocationSpec` below identify accepted future implementation roles and intended spelling. They are not classes currently present in the repository.

## Accepted future implementation choices

005-F accepts the following implementation baseline:

- separate durable implementation-binding records for Strategy implementations and Evaluation-method implementations;
- binding identity/revision remains separate from Strategy semantic revision, package version, SPI version, state-codec version, and runtime/platform version;
- standard-library `typing.Protocol` is the preferred future structural SPI mechanism rather than requiring third-party extensions to subclass SYNGAN ABCs;
- runtime SPIs remain activity-specific (`Learning`, `Generation`, `Evaluation`) even when they share supporting protocols;
- a generic `run(context) -> Result` contract is rejected as the sole extension boundary;
- extension providers may be supplied explicitly by deployment/bootstrap composition and may additionally be discovered through Python package entry points;
- Python entry-point discovery is optional infrastructure only and MUST NOT itself authorize, select, or semantically register an implementation;
- the planned entry-point group is `syngan.runtime_extensions`, subject to the repository's separate external package/name review before public ecosystem release;
- discovery/loading never installs missing packages or downloads models/artifacts;
- deployment composition builds an immutable process-local extension catalog from explicitly approved providers/bindings; there is no universal mutable global plugin registry;
- every committed runtime Attempt receives an immutable, versioned, activity-specific invocation specification derived from the committed activity plus exact implementation binding;
- runtime adapters receive bounded references/capabilities/sinks rather than arbitrary canonical repositories or database sessions;
- runtime results remain non-final typed envelopes: Learning returns candidate Learned-State representation facts, Generation returns candidate materialization facts, Evaluation returns method-result facts;
- runtime success never establishes Learned State, completed Generation output, or Evidence directly;
- Learned State logical identity remains separate from physical state representation and loaded runtime object;
- Learned-State physical representation uses an explicit codec/manifest contract with distributed component support and no mandatory full-driver load;
- the portable core does not require or endorse Python pickle as a universal state representation; codecs that require unsafe/code-executing deserialization must declare that property for 005-I policy enforcement;
- direct-generation Strategies remain first-class and MUST NOT fabricate Learning/Learned State;
- PyTorch remains optional behind the `torch` capability extra; Spark remains optional behind `spark`; hybrid runtimes may require both explicitly;
- 005-F does not choose `torchrun`, TorchDistributor, Kubernetes, Databricks jobs, or another concrete launcher—the Execution/launcher/platform realization remains 005-G/005-J responsibility.

## Version and identity model

### Implementation-binding resources

005-F reserves future `ResourceKind` values equivalent to:

```text
strategy_implementation_binding
evaluation_method_binding
learned_state_candidate
learned_state_representation
```

These are implementation/integration resource kinds, not additions to the accepted concept catalog.

### `ImplementationBindingRef`

A runtime binding is modeled as a stable revisioned integration resource using the 005-D identity model:

```text
ImplementationBindingRef
    family: ResourceRef(kind = strategy_implementation_binding
                        or evaluation_method_binding)
    revision: RevisionNumber
```

The binding revision changes when material executable compatibility/requirements/limitations change even if the Strategy semantic revision does not.

### Version axes remain distinct

The future implementation must distinguish at least:

```text
Strategy / Criterion-method semantic revision
ImplementationBindingRef revision
RuntimeSpiVersion
Python distribution/package version
implementation build identity/digest where available
LearnedStateCodecId + codec version
state representation SchemaVersion
runtime/framework version
platform/launcher version
```

No generic `plugin_version` field may silently represent several of these axes.

### `RuntimeSpiVersion`

005-F accepts an explicit major/minor SPI version value:

```text
RuntimeSpiVersion(major, minor)
```

Rules:

- major change means an incompatible SPI contract unless an adapter explicitly supports both versions;
- minor change may add backward-compatible fields/capabilities under the accepted compatibility rules;
- SPI compatibility never implies Strategy semantic compatibility;
- persisted invocation envelopes record the exact SPI version used.

## Strategy implementation binding

A future immutable binding revision contains bounded facts equivalent to:

```text
StrategyImplementationBinding
    binding_ref
    supported_strategy_revisions / revision range
    supported_configuration_schema(s)
    supported_modes
        learning
        learned_state_generation
        direct_generation
    extension_provider_identity
    Python distribution name/version/build identity
    RuntimeSpiVersion
    runtime_adapter_kind
    supported data-reference/read contracts
    Learned-State codec/representation compatibility
    candidate-writer compatibility
    runtime/software/accelerator requirements
    declared scale/resource envelope
    dependency/artifact requirements
    network/egress requirements
    reproducibility/nondeterminism characteristics
    implementation-specific limitations
```

A binding MAY narrow a Strategy's declared capability. It MUST NOT silently broaden semantic capabilities or reinterpret Strategy configuration meaning.

If executable behavior changes Strategy semantics/capabilities/configuration meaning/dependency posture materially, the Strategy authority must be revised rather than hiding the change inside a new binding revision.

## Evaluation-method implementation binding

A future `EvaluationMethodBinding` follows the same integration model but binds exact Evaluation method identity/configuration rather than creating an Evaluation Method concept.

It records bounded facts equivalent to:

```text
method identity/configuration schemas supported
subject/reference kinds supported
coverage modes supported
uncertainty/error capabilities
scale/resource limits
diagnostic-output behavior
runtime/dependency/network requirements
RuntimeSpiVersion
package/build identity
known limitations
```

A method binding cannot redefine the Criterion question or claim a stronger result than the committed method/scope/coverage can support.

## Extension provider and discovery model

### Explicit composition is primary

A future deployment/bootstrap creates runtime availability from explicitly supplied/approved extension providers and implementation-binding records.

The conceptual boundary is:

```text
installed/available extension provider
        ↓ inspect + trust/compatibility checks
binding declarations
        ↓ deployment selection/approval
immutable RuntimeExtensionCatalog
        ↓ exact ImplementationBindingRef resolution
runtime adapter factory
```

The catalog is a process-local/read-model/composition mechanism. It is not canonical Strategy authority and does not own historical binding state.

### Python entry-point discovery

Python packaging entry points are accepted as an optional discovery mechanism for separately installed extension distributions.

Planned group:

```text
syngan.runtime_extensions
```

Each entry point resolves to a provider factory/object satisfying the extension-provider protocol.

Rules:

- `import syngan` MUST NOT scan/load entry points eagerly;
- enumerating installed entry-point metadata does not authorize loading code;
- loading an entry point executes/imports third-party code and therefore occurs only after 005-I trust/authorization policy permits it;
- duplicate/unqualified entry-point names do not decide authority; distribution identity and explicit deployment selection resolve conflicts;
- missing providers fail explicitly; runtime code never installs them automatically;
- an entry-point provider may expose Strategy bindings, Evaluation-method bindings, state codecs, or supporting runtime capabilities through typed descriptors, but those descriptors remain integration declarations.

### No global mutable registry

The future runtime implementation MUST NOT expose a process-global mutable `register_plugin(...)` registry as canonical availability/authority.

Tests or embedding applications MAY explicitly construct catalogs/providers in memory. Bootstrap may cache an immutable catalog for one configured client/deployment lifecycle.

## SPI shape

005-F selects standard-library structural protocols for the primary future extension contract.

Conceptually:

```text
RuntimeExtensionProvider (Protocol)
    describe() -> ExtensionProviderDescriptor
    create_strategy_runtime(binding_ref, mode) -> activity-specific adapter
    create_evaluation_runtime(binding_ref) -> EvaluationRuntimeAdapter
    resolve_state_codec(codec_ref) -> StateCodec
```

The exact factory split may be refined during coding when type ergonomics are proven, but activity-specific adapter boundaries are mandatory.

### `LearningRuntimeAdapter`

Future protocol responsibility:

```text
preflight(LearningInvocationSpec) -> RuntimePreflightReport
execute(LearningInvocationSpec, LearningRuntimePorts) -> LearningRuntimeResult
```

It may write Learning candidate-state material and operational/checkpoint data only through supplied ports.

### `GenerationRuntimeAdapter`

Future protocol responsibility:

```text
preflight(GenerationInvocationSpec) -> RuntimePreflightReport
execute(GenerationInvocationSpec, GenerationRuntimePorts) -> GenerationRuntimeResult
```

It writes only through the 005-E candidate sink/data ports authorized for the exact Generation/Attempt.

### `EvaluationRuntimeAdapter`

Future protocol responsibility:

```text
preflight(EvaluationInvocationSpec) -> RuntimePreflightReport
execute(EvaluationInvocationSpec, EvaluationRuntimePorts) -> EvaluationRuntimeResult
```

It reads exact subject/reference state and writes only bounded results plus separately referenced diagnostics.

### Supporting ports

Activity-specific runtime port bundles may compose narrower protocols for:

- exact data access;
- candidate/state materialization sinks;
- diagnostic sinks;
- dependency/artifact resolution;
- progress/health reporting;
- checkpoint creation hints/ports;
- cancellation observation;
- bounded runtime facts/provenance reporting;
- secrets/network capabilities supplied by later security planning.

The port bundle MUST NOT contain an unrestricted `SynGANClient`, SQL repository/session, arbitrary control-store mutation interface, or service locator.

## Immutable runtime invocation specifications

The future application/Execution boundary prepares one immutable invocation snapshot for each Attempt.

### Common envelope

All three activity-specific invocation specs share a bounded envelope equivalent to:

```text
RuntimeInvocationEnvelope
    schema_version
    RuntimeSpiVersion
    activity ResourceRef
    activity commitment SnapshotId
    exact ImplementationBindingRef
    exact runtime/provider identity required by the binding
    resolved dependency/artifact refs
    committed network/no-egress posture refs
    runtime operational parameters
    Attempt/Execution authority context supplied by 005-G
```

The envelope remains JSON-compatible/reference-oriented and contains no full DataFrame/model/payload.

### `LearningInvocationSpec`

Adds exact:

- `SourceStateRef`;
- Strategy/configuration revision;
- Data Meaning/Constraint references required by the implementation;
- sampling/approximation/randomness commitments;
- candidate Learned-State materialization target;
- permitted operational/runtime tuning.

### `GenerationInvocationSpec`

Adds exact:

- Strategy/configuration revision;
- Conditions and Generation-owned material values required by runtime;
- either exact Learned State + representation binding or exact direct-input/source refs according to Strategy mode;
- exact 005-E `CandidateWriteTarget`;
- permitted randomness/resource behavior.

A direct-generation invocation contains no fabricated Learned-State reference.

### `EvaluationInvocationSpec`

Adds exact:

- Evaluation Criterion/method/configuration binding;
- exact immutable subject/reference refs;
- scope/coverage/approximation/randomness commitments;
- diagnostic sink refs;
- claim-support inputs required by method interpretation.

For Generation-completion Evaluation, the subject is the exact `SealedDataSnapshotRef` from 005-E.

### Immutability rule

Once an Attempt begins, runtime code cannot silently modify the invocation.

A material change to source, state, Strategy/configuration, Conditions, Constraint handling, Criterion/method/scope, dependency identity, or network/egress posture requires rejection/replanning and, when semantic, a new domain commitment rather than a runtime fallback.

## Runtime operational parameters

005-F separates semantic commitment values from **operational tuning** that may vary between Attempts.

Examples that may be operational-only when the binding declares them semantically neutral include:

- executor/worker count;
- memory allocation;
- cluster placement;
- local scratch sizing;
- scheduling priority;
- bounded batch/concurrency settings proven not to change semantic behavior.

If batch size, precision, topology, algorithm mode, determinism setting, or another parameter materially affects Strategy/method semantics or reproducibility, it must be committed or explicitly attributable—not silently varied as an operational retry detail.

005-G owns Attempt-to-Attempt mutation rules; 005-H owns reproducibility attribution.

## Runtime preflight result

A common future `RuntimePreflightReport` is a contextual derived value reporting facts such as:

```text
compatible
compatible_with_limitations
incompatible
indeterminate
```

plus structured reasons for:

- SPI incompatibility;
- binding/Strategy or method mismatch;
- missing runtime/software/accelerator capability;
- unavailable/incompatible state codec;
- unsupported source/data-reference contract;
- dependency identity/version mismatch;
- scale/resource cliff;
- network/egress incompatibility;
- portability limitation.

Preflight does not make a Strategy effective or commit an activity.

## Learning runtime and Learned-State candidate boundary

### Candidate Learned-State resource

Learning runtime writes into a non-final candidate state resource equivalent to:

```text
LearnedStateCandidateRef
    ResourceRef(kind=learned_state_candidate)
    parent Learning ResourceRef
    candidate state/version
    representation workspace descriptor
```

This is distinct from checkpoint material and from the logical Learned State result.

### State representation manifest

A finished candidate is sealed into a state representation equivalent to:

```text
LearnedStateRepresentationRef
    ResourceRef(kind=learned_state_representation)
    parent Learning/candidate refs
    StateRepresentationDescriptor
```

The descriptor is bounded and references distributed/provider-native component detail rather than requiring all model/state bytes in the control plane.

`StateRepresentationDescriptor` contains or resolves facts equivalent to:

```text
schema_version
codec id + codec version
representation kind
component/manifest root
structural/component summary
required immutable base-artifact refs
integrity descriptor
runtime/binding compatibility facts
created/sealed context
```

### No universal state byte format

005-F intentionally does not require one serialization format for all Strategies.

A statistical Strategy, PyTorch Strategy, Spark-native Strategy, or future runtime may require different component types.

The common contract is the explicit codec/manifest boundary, not a universal `.pkl`, `.pt`, Spark model directory, ONNX file, or model-registry artifact.

### `StateCodec`

A future state codec protocol is equivalent to:

```text
StateCodec
    codec_id
    codec_version
    supported binding/state representation schemas
    describe/load/validate/convert capabilities
    safety characteristics
```

A codec declares whether loading may execute arbitrary code or requires trusted implementation objects.

The portable/core architecture does not silently deserialize arbitrary pickle/joblib/runtime objects. Where an implementation genuinely requires a risky representation, that property is explicit so 005-I can deny or constrain loading.

### Distributed state loading

`LearnedStateRepresentationRef` must support Strategies whose state exceeds driver memory.

The future loader may:

- shard/stream components directly to workers/accelerators;
- use provider-native distributed state loading;
- use bounded coordinator metadata plus distributed component reads;
- exploit runtime-specific distributed-checkpoint capabilities.

It MUST NOT make full state deserialization on the coordinator a universal requirement.

### Learning result envelope

`LearningRuntimeResult` contains bounded facts equivalent to:

```text
candidate LearnedStateCandidateRef / representation candidate
physical/codec/integrity summary
runtime/implementation/dependency facts
warnings/limitations
operational outcome
```

It cannot return a canonical `LearnedStateHandle` as though runtime success established the domain result.

### Learned State establishment

Future Learning/application logic performs the semantic barrier:

```text
Learning runtime result
        ↓
sealed LearnedStateRepresentationRef
        ↓
validate exact invocation + integrity + required facts
        ↓
Learning semantic completion transaction
        ↓
LearnedState ResourceId
+ representation binding
```

Establishment may reuse the sealed physical representation without copying it.

The one logical Learned State remains separate from the representation, codec, loaded runtime object, and producing checkpoint.

## Learned-State loading for Generation

Generation resolves:

```text
LearnedStateHandle / ResourceRef
        ↓
current allowed-use state
        ↓
exact representation binding
        ↓
StateCodec + runtime binding compatibility
        ↓
loaded/sharded runtime object
```

The loaded object is ephemeral.

Generation compatibility remains contextual and may fail even when the Learned State itself remains historically valid.

Representation conversion may preserve one Learned State identity only under an explicit equivalence/integrity contract with prior representation history retained. Fine-tuning/adaptation that changes learned behavior creates a new distinguishable Learned State, normally through Learning.

## Generation runtime plan

### Learned-State path

```text
Generation commitment
+ exact Learned State
+ exact representation binding
        ↓
GenerationInvocationSpec
        ↓
GenerationRuntimeAdapter
        ↓
005-E CandidateMaterializationRef
```

### Direct-generation path

```text
Generation commitment
+ exact direct source/input refs
        ↓
GenerationInvocationSpec
        ↓
GenerationRuntimeAdapter
        ↓
005-E CandidateMaterializationRef
```

No Learning or Learned State is fabricated for the direct path.

### Generation result envelope

`GenerationRuntimeResult` contains bounded facts such as:

- exact candidate ref;
- physical extent summary;
- generation diagnostics/warnings;
- material implementation/runtime/dependency identities;
- operational outcome.

It does not establish a sealed snapshot or completed Generation output by itself. 005-E candidate sealing, Evaluation, and Generation promotion remain separate barriers.

## Evaluation runtime plan

### Exact subject binding

The Evaluation invocation receives exact immutable subject/reference identities from the committed Evaluation.

Runtime code does not reread a mutable table/path/alias to discover a replacement subject.

### `EvaluationRuntimeResult`

The future result envelope may contain:

```text
measurements/statistics
coverage achieved
uncertainty/error
method validity/assumption diagnostics
count/extent summaries
bounded claim-support facts
diagnostic data references
runtime/binding/dependency facts
warnings/limitations
operational outcome
```

It MUST NOT collapse all methods into a universal scalar score or `passed` Boolean.

Large per-row/attack/nearest-neighbor/violation diagnostics remain referenced data-plane material.

Evaluation/application logic later checks method/Criterion/subject/scope/coverage/uncertainty semantics before 005-H Evidence establishment.

## Runtime facts and attribution

Every future runtime adapter returns bounded material runtime facts sufficient for later Provenance/reproducibility analysis, including where applicable:

- exact binding ref;
- package/distribution version/build identity;
- SPI version;
- runtime/framework version;
- codec/version;
- important deterministic/nondeterministic settings;
- resource/topology facts declared material by the binding;
- dependency/base-artifact identities;
- provider/launcher correlation refs supplied by Execution/platform layers;
- material warnings/limitations.

Adapters report these facts; they do not write Provenance directly.

005-H defines canonical Provenance/reproducibility persistence and interpretation.

## PyTorch runtime planning

### Optional dependency boundary

005-C's reserved `torch` extra is retained.

Future packaging is equivalent to:

```text
syngan base
    no torch import requirement

syngan[torch]
    PyTorch state/runtime support

syngan[spark,torch]
    deployment may compose Spark data access with PyTorch runtime support
```

There is no broad `all` extra.

### PyTorch is a runtime family, not Strategy semantics

A PyTorch adapter may provide:

- tensor/state codecs;
- distributed state loading helpers;
- runtime factories;
- Strategy-specific PyTorch implementation providers;
- integration with a launcher selected later.

It does not own Learning, Learned State, Generation, or Evaluation semantics.

### Launcher intentionally deferred

005-F does not choose among:

- in-process/local PyTorch;
- `torchrun`/elastic launch;
- Spark/Databricks-specific distributors;
- Kubernetes jobs;
- managed GPU jobs;
- another distributed launcher.

005-G defines Execution/Attempt/recovery interaction and 005-J defines deployment/platform launcher capability mapping.

The runtime SPI therefore accepts an Execution/Attempt-supplied environment/context rather than embedding one scheduler product.

## Spark-native runtime planning

Strategies/evaluation methods may also have Spark-native executable bindings.

Such bindings may use Spark data-processing operations through the 005-E data adapter but remain behind runtime implementation boundaries.

The existence of Spark-native adapters does not make Spark ML Estimator/Model the universal SPI.

A Strategy may use Spark for distributed data preparation and a non-Spark model runtime for training/generation while still satisfying the Spark-native data-boundary contract.

## Runtime package ownership

005-F refines the future 005-C package topology with responsibilities equivalent to:

```text
src/syngan/
├── ports/
│   └── runtime/
│       ├── spi.py
│       ├── bindings.py
│       ├── invocation.py
│       ├── learning.py
│       ├── generation.py
│       ├── evaluation.py
│       └── state.py
├── application/
│   └── runtime/
│       ├── discovery.py
│       ├── binding_resolution.py
│       ├── invocation_planning.py
│       ├── learning_completion.py
│       └── state_resolution.py
├── api/
│   └── extensions.py
└── adapters/
    └── runtime/
        ├── builtin/
        ├── spark/
        ├── torch/
        └── entry_points/
```

Exact leaf-file spelling may be simplified during a later coding phase. The inward dependency direction and activity-specific SPI separation are mandatory.

`adapters.runtime.entry_points` uses standard-library package metadata discovery and stays optional/side-effect free until invoked explicitly.

## Persistence/control-plane impact

Future bounded control records are equivalent to:

```text
strategy_implementation_binding revision
evaluation_method_binding revision
learned_state_candidate
learned_state_representation
learned_state -> current representation binding
runtime invocation snapshot (owned/persisted with Attempt in 005-G)
```

These reuse 005-D ResourceRef/RevisionNumber/StateVersion/SchemaVersion/CAS/transaction conventions.

No migration is created during Phase 005.

Implementation-binding history remains resolvable even if the executable package is later uninstalled; current inability to load it becomes availability/reproducibility context, not rewritten history.

## Dependency/network rules

Runtime extensions MUST NOT:

- `pip install` or otherwise install missing code during committed runtime execution;
- download a missing model/base artifact silently;
- switch to a hosted service automatically;
- enable telemetry/network behavior not declared by the binding and permitted by the commitment/security policy;
- substitute a different state codec/dependency/package version because the exact one is unavailable.

Discovery is local installed-environment inspection only unless a separately authorized provisioning workflow occurs outside the committed runtime.

005-I defines trust, artifact authorization, network/no-egress enforcement, secret delivery, and unsafe-deserialization policy.

## Error and result taxonomy

The future runtime boundary preserves structured distinctions equivalent to:

```text
binding_not_found
binding_incompatible
spi_incompatible
runtime_dependency_unavailable
runtime_dependency_identity_mismatch
state_codec_unavailable
state_codec_incompatible
source_or_subject_resolution_failure
policy_or_network_incompatible
adapter_protocol_defect
recoverable_runtime_failure
terminal_runtime_failure
candidate_materialization_failure
runtime_success_semantic_validation_failure
unknown_or_indeterminate_runtime_outcome
```

These categories may be expressed through typed issues/results/exceptions as appropriate, but they are not collapsed into an opaque exception string.

005-G refines operational failure/recovery classification.

## Conformance and verification plan

005-F primarily owns future V6 verification and contributes to V2/V3/V5/V8/V9/V10/V11.

Relevant architecture-fitness obligations include:

```text
AF-02  optional/runtime dependencies remain isolated from portable core
AF-04  runtime/candidate/state representation != semantic promoted result
AF-09  runtime/platform success cannot establish semantic completion
AF-12  no hidden acquisition/remote fallback/telemetry
AF-13  enterprise runtime/data paths do not require full-driver collection
AF-14  runtime/provider fallback preserves semantics or reports incompatibility
AF-20  platform/runtime identities remain subordinate to SYNGAN authority
```

Future reusable conformance suites are required for:

- Strategy binding declaration/compatibility;
- Evaluation-method binding declaration/compatibility;
- `LearningRuntimeAdapter`;
- `GenerationRuntimeAdapter`;
- `EvaluationRuntimeAdapter`;
- `StateCodec`;
- extension-provider discovery/loading.

### Required future scenarios

Verification must include at least:

1. installed/discovered plugin is not automatically semantically effective or selected;
2. `import syngan` does not scan/load entry points or import PyTorch/Spark runtime extras;
3. duplicate entry-point names do not silently choose one implementation;
4. binding can narrow but cannot broaden Strategy capability without a semantic revision;
5. exact binding/SPI/package identities survive historical persistence after extension uninstall;
6. immutable runtime invocation rejects source/Strategy/Condition/method/dependency substitution;
7. adapter cannot mutate canonical semantic state through runtime ports;
8. Learning runtime success yields only candidate representation, not Learned State;
9. checkpoint material cannot satisfy Learned-State representation/result type;
10. direct Generation works without fabricated Learning/Learned State;
11. Generation runtime success yields a candidate, not sealed/completed output;
12. Evaluation runtime binds exact sealed subject and returns method result, not Evidence;
13. large diagnostics remain references rather than control-envelope payloads;
14. unknown/unsupported state codec fails explicitly rather than loading with another codec;
15. risky/unsafe deserialization is declared and policy-addressable;
16. large Learned State can be represented/loaded without universal driver-local materialization;
17. hidden network/model/package acquisition fails core/offline conformance;
18. runtime operational tuning cannot silently change a material semantic/reproducibility parameter.

### Statistical/runtime quality tests

Model quality/fidelity tests remain separate from SPI correctness.

A Strategy runtime can pass extension conformance while producing unfavorable Evaluation Evidence for one dataset; extension protocol compliance is not a quality claim.

## Future implementation sequence

Only after a later phase explicitly authorizes coding:

```text
F1  SPI/version/binding value contracts
F2  extension provider + explicit/entry-point discovery boundary
F3  activity-specific immutable invocation specifications
F4  Learning/Generation/Evaluation runtime protocols and result envelopes
F5  Learned-State candidate/representation/codec contracts
F6  application binding/preflight/invocation/completion coordination
F7  minimal built-in/reference conformance providers/fakes
F8  optional Spark-native runtime integration
F9  optional PyTorch runtime/state support
F10 reusable V6 conformance and Q1/Q2 integration profiles
```

None of F1-F10 is executed during Phase 005.

## Deferred ownership

005-F deliberately leaves to later planning:

- Execution/Attempt identity, fencing, checkpoint ownership, retry/resume/cancellation — 005-G;
- Evidence establishment, Provenance persistence, runtime-fact historical queries and reproducibility assessment — 005-H;
- extension/package/artifact trust, authorization, unsafe-code/state loading policy, network/egress and secrets — 005-I;
- concrete distributed launchers, Databricks/TorchDistributor/torchrun/Kubernetes mappings, compatibility matrix and observability — 005-J;
- final coding-phase sequencing and backlog closure — 005-K.

## No new domain concepts

005-F does not introduce domain concepts for:

- Plugin;
- Extension;
- Runtime Adapter;
- Runtime Binding;
- Evaluation Method Plugin;
- State Codec;
- Runtime Invocation;
- Runtime Result;
- Extension Catalog;
- Model Runtime;
- Launcher.

They remain implementation/integration mechanisms beneath accepted concepts.

## No upstream revision required

005-F requires no change to the eleven accepted concepts, fifteen synchronizations, Phase 003 experience contract, Phase 004 architecture, ADR-0001 through ADR-0008, 005-C package direction, 005-D durable control substrate, or 005-E distributed data contract.

No new architecture ADR is required.

## Exit criteria

- [x] planning-only boundary preserved;
- [x] implementation-binding identity/revision model defined;
- [x] SPI version axis defined separately;
- [x] Protocol-based, activity-specific SPI direction selected;
- [x] explicit composition plus optional Python entry-point discovery selected;
- [x] no-global-registry/no-auto-install rules defined;
- [x] immutable activity-specific runtime invocation contracts defined;
- [x] semantic versus operational runtime parameters separated;
- [x] Learning/Generation/Evaluation result boundaries defined;
- [x] Learned-State candidate/representation/codec contract defined;
- [x] distributed Learned-State loading requirement preserved;
- [x] direct-generation path preserved;
- [x] optional Spark/PyTorch dependency/runtime roles defined;
- [x] concrete launcher choice deferred to owning slices;
- [x] persistence/package impacts mapped;
- [x] V6/fitness/conformance requirements mapped;
- [x] future F1-F10 sequence defined without execution.

## Exit decision

**005-F — implementation plan complete; no production implementation performed.**

Next:

**005-G — Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Implementation Plan**.
