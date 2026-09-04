---
type: Architecture Authority
title: Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture
status: active
---

# Strategy Extension, Learning/Generation/Evaluation Runtime & Adapter Architecture

## Purpose

Define how SYNGAN's accepted Synthesis Strategy, Learning, Generation, Evaluation, Learned State, Execution, and distributed data/reference semantics map to built-in or third-party executable implementations without allowing a plugin class, runtime model object, Spark job, PyTorch process, remote service, or package registry to become semantic authority.

This document establishes the Phase 004-E runtime-extension architecture. It defines extension declaration, implementation binding, runtime invocation, Learning result materialization, Learned State loading, Generation candidate writing, Evaluation method execution, dependency/resource disclosure, and adapter conformance boundaries while leaving concrete plugin-loading technology and runtime products open.

## Governing authority

This architecture remains downstream of:

- [Architecture Authority, Representation Principles, Layering & Dependency Direction](architecture-authority-representation-layering.md);
- [Public API, Resource/Handle Model, Workflow Composition & Semantic Mapping](public-api-resource-handle-workflow-semantic-mapping.md);
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](control-plane-identity-revision-state-persistence-historical-reference.md);
- [Spark Data Boundary, Source/Output Reference, Distributed Materialization, Manifest & Promotion Architecture](spark-data-boundary-source-output-reference-distributed-materialization-manifest-promotion.md);
- [Synthesis Strategy](../concepts/synthesis-strategy.md);
- [Learning](../concepts/learning.md);
- [Learned State](../concepts/learned-state.md);
- [Generation](../concepts/generation.md);
- [Evaluation](../concepts/evaluation.md);
- [Execution](../concepts/execution.md);
- [Network and External Dependency Policy](../authority/network-external-dependency-policy.md).

## Primary decision

SYNGAN SHALL separate **semantic declaration**, **implementation binding**, and **runtime realization**.

```text
Synthesis Strategy revision/configuration
semantic capabilities / requirements / limitations
                 ↓ bind
Strategy implementation binding
implementation identity + supported semantic revision(s)
state/data codecs + runtime/dependency/resource envelope
                 ↓ resolve for committed activity
immutable runtime invocation specification
                 ↓ Execution / Attempt
runtime adapter
Spark-native / PyTorch-distributed / local / external-service / future runtime
                 ↓
non-final physical/runtime result
                 ↓ semantic owner validates/promotes
Learned State / completed output / Evidence
```

A plugin or adapter is executable realization machinery. It does **not** own the Strategy concept, committed Learning/Generation/Evaluation semantics, Execution identity, Learned State identity, Generation output promotion, Evidence authority, or external authorization.

The same architectural rule applies to Evaluation methods: a method implementation binding realizes the method identity/configuration committed by Evaluation without becoming Evaluation Criterion or Evidence authority.

## Semantic authority versus executable implementation

### Strategy authority remains canonical

A Strategy revision owns reusable synthesis declarations such as:

- semantic capability and requirement claims;
- supported Data Meaning/features;
- Constraint handling semantics;
- whether Learning/Learned State is required, optional, or absent;
- Generation/Condition capability semantics;
- scale/resource characteristics actors must know before commitment;
- reproducibility characteristics;
- external dependency/network profile;
- known limitations and configuration semantics.

Executable registration cannot create or broaden these claims implicitly.

### Implementation binding

A **Strategy implementation binding** is an architecture record that states that a particular executable implementation can realize one or more exact Strategy revision/configuration contracts under declared conditions.

It conceptually includes or resolves enough information equivalent to:

- stable implementation/binding identity and revision;
- supported Strategy family/revision/configuration-schema range;
- supported activity modes: Learning, Learned-State Generation, direct Generation, or combinations;
- implementation package/distribution identity and version;
- runtime adapter kind/version;
- supported data-reference/read interfaces;
- Learned State representation/codec compatibility where relevant;
- candidate-output writer compatibility;
- runtime/software/accelerator requirements;
- scale/resource limits narrower than or equal to the Strategy declaration;
- external artifact/network/egress requirements;
- material nondeterminism/reproducibility facts;
- extension-interface/SPI version;
- known implementation-specific limitations.

The implementation binding is architecture/integration state, not a new domain concept.

### Bindings may narrow, not silently broaden, semantic claims

An implementation binding MAY be more restrictive than the Strategy revision it realizes.

For example, a Strategy may semantically support distributed Learning while one implementation binding supports only a bounded single-node subset. Contextual readiness must then expose the binding limitation.

An implementation binding MUST NOT claim a semantic capability broader than the bound Strategy revision without a corresponding Strategy revision/declaration update.

### Implementation change versus Strategy change

A new executable implementation version does not automatically require a new Strategy revision when the declared synthesis semantics/capabilities/configuration meaning remain unchanged.

However:

- the exact material implementation identity/version MUST remain attributable when it can affect reproducibility, compatibility, or behavior;
- implementation-specific compatibility may change independently;
- if implementation changes alter Strategy semantics, capability claims, configuration meaning, dependency profile, or material limitations, the Strategy/configuration authority must be revised rather than hiding the change as an implementation patch.

Historical work binds both the semantic Strategy/configuration identity and the material executable binding/runtime identities needed to explain what happened.

## Evaluation method implementation boundary

Evaluation does not require a new standalone `Evaluation Method` domain concept.

The architecture nevertheless needs executable method bindings equivalent to:

```text
Evaluation commitment
Criterion + method identity/configuration + subject/reference + coverage
                 ↓
Evaluation method implementation binding
                 ↓
Evaluation runtime adapter
                 ↓
measurements / bounded findings / diagnostics
                 ↓
Evaluation semantic validation
                 ↓
Evidence establishment
```

A method implementation binding conceptually declares:

- stable method implementation identity/version;
- method/configuration schemas it can realize;
- supported input/reference kinds;
- supported coverage modes and scale/resource limits;
- uncertainty/error capabilities;
- dependency/network/egress behavior;
- diagnostic-output behavior;
- reproducibility/nondeterminism characteristics;
- extension/SPI compatibility;
- known limitations.

The binding cannot redefine the Criterion question or inflate claim strength beyond the committed Evaluation method/scope.

## Extension discovery and registration

### Discovery is infrastructure, not semantic authority

SYNGAN MAY later discover extensions through mechanisms such as:

- explicit dependency injection;
- Python entry points;
- configuration;
- package metadata;
- a managed extension catalog;
- static built-in registration;
- another compatible mechanism.

004-E selects none of these.

Discovery only identifies available executable bindings. It does not make a Strategy effective, compatible, authorized, or safe merely because code is installed.

### No universal mutable plugin registry authority

A registry/index MAY cache or search installed bindings, but it MUST NOT become the canonical owner of Strategy semantic declarations, activity compatibility, Learned State lifecycle, or Evaluation Evidence.

### No implicit remote installation

Extension discovery/loading MUST NOT silently download packages, models, code, or artifacts during Learning/Generation/Evaluation merely because a requested implementation is missing.

Any acquisition path must obey the Network and External Dependency Policy and later 004-H authorization rules.

Package installation/provisioning is distinct from runtime semantic execution.

## Extension contract/versioning

The architecture SHALL distinguish at least:

```text
Strategy semantic revision
Implementation-binding revision
Extension/SPI contract version
Implementation package/build version
Learned State representation/codec version (when applicable)
```

These MUST NOT be collapsed into one ambiguous plugin `version` value.

A newer SPI version may change invocation structure without changing Strategy semantics. A newer Strategy revision may change semantics while using the same SPI. A newer state codec may migrate physical representation without creating a semantically new Learned State when equivalence is explicitly preserved.

## Runtime invocation architecture

### Domain coordinator resolves before runtime

The application/control layer prepares a bounded immutable **runtime invocation specification** from the committed activity and the selected implementation binding.

The runtime specification contains only the material execution facts and references required to realize that exact commitment.

It SHOULD include or reference, as applicable:

- activity identity and immutable commitment-snapshot identity;
- Strategy/configuration or Evaluation method identity;
- exact implementation-binding identity/version;
- exact source/input/subject/reference data-state references;
- exact Learned State reference/representation binding when used;
- activity-owned sampling/approximation/coverage/randomness semantics;
- resolved local/external dependency identities;
- committed network/no-egress posture;
- bounded runtime/resource parameters permitted by the commitment;
- output/candidate/diagnostic sink references;
- Attempt/execution token/context required for safe writes;
- schema/SPI versions required for interpretation.

It MUST NOT require a full copy of unrelated control-plane state.

### Runtime invocation is immutable per Attempt

An Attempt executes against a resolved immutable invocation specification or an exact reference to one.

Runtime code MUST NOT silently change:

- Strategy/configuration semantics;
- source snapshot;
- Learned State;
- Generation Conditions;
- Constraint handling;
- Evaluation Criterion/method/scope;
- dependency/network/egress posture;
- output semantic destination.

If runtime realization requires a material semantic change, the Attempt must fail/return incompatibility and the owning activity must create a new commitment when appropriate.

### Runtime code does not receive semantic write authority

An adapter does not mutate canonical activity state directly through arbitrary repository/database access.

It reports bounded operational/result facts through defined ports. Application/control logic validates and performs owner-authorized transitions.

This keeps runtime implementation packages from gaining backdoor authority over Learning, Generation, Evaluation, Evidence, Provenance, or output promotion.

## Runtime adapter roles

004-E defines architectural roles, not final class names.

### Common runtime adapter responsibilities

A runtime adapter may:

- preflight its implementation/runtime/dependency requirements;
- resolve approved local/runtime dependencies through supplied ports;
- open exact source/input/subject references through supplied data resolvers;
- load Strategy-specific Learned State components;
- execute local/distributed/remote computation according to the binding;
- report progress/health/checkpoint hints through Execution ports;
- write non-final Learned State/candidate/diagnostic material through supplied sinks;
- return bounded runtime result summaries;
- report material implementation/runtime/dependency facts for Provenance/reproducibility.

A runtime adapter MUST NOT:

- commit a new domain activity;
- change committed semantic inputs;
- declare Learning/Generation/Evaluation semantically complete by itself;
- establish a Learned State identity directly;
- promote a Generation output directly;
- establish Evidence without Evaluation-level semantic validation;
- authorize network/data egress;
- substitute dependencies or runtime methods silently;
- use platform job identity as SYNGAN Execution identity.

### Separate contracts may share infrastructure

Learning, Generation, and Evaluation adapters MAY share runtime utilities, Spark readers, dependency resolution, serialization, resource launchers, and error envelopes.

They MUST still preserve activity-specific input/output contracts and semantic boundaries.

One generic `run(context) -> Result` contract is insufficient as the only extension boundary if it erases whether runtime output is Learned State candidate material, Generation candidate data, or Evaluation method result.

## Learning runtime architecture

### Learning adapter input

A Learning runtime adapter consumes a runtime specification bound to one committed Learning, including exact source-state/read references, Data Meaning/Constraint/Strategy context required by the implementation, sampling/approximation semantics, dependency identities, randomness intent, and an Attempt context.

The adapter should receive semantic facts in bounded implementation-facing forms rather than query arbitrary canonical repositories from worker code.

### Learned State materialization workspace

Learning runtime requires a representation boundary similar in spirit to Generation candidate materialization but with Learned State semantics.

A Learning adapter writes to an **unpromoted Learned State materialization/workspace** supplied or authorized by the framework.

That workspace may contain:

- model parameters/weights;
- statistical parameters/distributions;
- encoders/dictionaries;
- sketches/summaries;
- Strategy-specific serialized state;
- references to required immutable base artifacts;
- multiple distributed components.

Checkpoint/recovery material remains separately distinguishable from candidate final Learned State material even if some bytes can be reused.

### Candidate Learned State representation

When runtime work finishes, the adapter produces or helps seal a candidate Learned State representation/manifest containing enough information to establish:

- exact physical component extent;
- state codec/representation identity;
- dependency/base-artifact references required for loading;
- structural/integrity facts;
- runtime/implementation facts relevant to compatibility/reproducibility;
- distinction from checkpoint/intermediate material.

This candidate representation is not yet a Learned State domain result.

### Learning semantic establishment remains outside adapter

After runtime completion, Learning/application logic validates that:

- the executed invocation matches the committed Learning;
- the candidate state representation is complete/integrity-valid to the declared contract;
- no semantic/runtime defect invalidates the result;
- required dependency/provenance facts are available;
- the result is distinguishable from checkpoint/intermediate state.

Only then may Learning complete and establish the one primary logical Learned State.

Conceptually:

```text
Learning L7
   ↓ Execution/Attempt
Learning adapter
   ↓
candidate state materialization SM7
   ↓ seal / validate
candidate state representation SR7
   ↓ Learning semantic completion
Learned State LS7
```

The physical representation may be reused in place; establishing LS7 need not copy model/state bytes.

## Learned State runtime loading

### Logical state versus loaded runtime object

A Learned State handle remains canonical identity. A loaded runtime object is a transient adapter-local realization.

```text
Learned State LS7
   ↓ resolve representation/dependencies
state runtime binding
   ↓ adapter load
PyTorch module / Spark model / statistical object / distributed state
```

The loaded object MUST NOT become the historical identity of LS7.

### State runtime binding

A state runtime binding preserves or resolves enough information to determine:

- Learned State logical identity;
- producing Strategy/configuration;
- state representation/codec identity/version;
- component/manifest references;
- required base/pretrained artifact identities;
- implementation/runtime compatibility requirements;
- known portability/migration limitations.

Generation contextual compatibility remains owned by Generation.

### Distributed loading

Learned State may be larger than coordinator/driver memory.

Runtime adapters MUST be allowed to load or shard state directly into distributed/accelerator/runtime contexts from approved references rather than requiring full state deserialization on the driver.

### Representation migration/conversion

A representation/codec conversion that preserves learned semantics MAY retain one Learned State identity only under an explicit equivalence/integrity contract and with representation history retained.

A conversion/fine-tune/adaptation that materially changes synthesis behavior requires a new distinguishable Learned State, normally through explicit Learning semantics.

## Generation runtime architecture

### Two valid runtime paths

Generation adapters must support the Strategy declaration rather than force one universal path:

```text
Learned-State Strategy
Generation commitment + LS reference
        ↓ load/bind state
Generation runtime
```

and:

```text
Direct-generation Strategy
Generation commitment + direct input/source/config
        ↓
Generation runtime
```

A direct-generation adapter MUST NOT fabricate Learning or Learned State.

### Framework-owned candidate sink boundary

Generation runtime writes through a candidate-materialization/output-writer port consistent with 004-D.

The adapter may determine Strategy-specific partitioning/batching behavior allowed by the commitment, but it MUST NOT silently choose an unapproved output location or mark physical writes as completed SYNGAN output.

The candidate sink supplies or enforces:

- candidate/materialization identity;
- Attempt/writer ownership/fence context;
- approved physical target/resolver;
- manifest/component membership protocol;
- seal handoff;
- authorization/no-egress constraints where implemented.

004-F refines writer fencing/recovery mechanics.

### Generation runtime result

Runtime completion may report facts such as:

- candidate materialization reference;
- produced physical extent summaries;
- Strategy-specific generation diagnostics;
- runtime limitations/warnings;
- material dependency/runtime identities;
- operational success/failure information.

It does not report `Generation completed` as semantic authority.

Required validation binds the exact sealed candidate, and Generation promotion remains the separate control-plane transition defined in 004-D.

## Evaluation runtime architecture

### Exact subject/reference binding

Evaluation runtime receives exact immutable subject/reference identities from the committed Evaluation.

For Generation completion Evaluation, the subject is the exact sealed candidate snapshot identified by 004-D.

The adapter MUST NOT re-resolve a mutable alias to a later subject/reference during execution.

### Evaluation method result envelope

An Evaluation method adapter returns an implementation-facing result envelope sufficient for Evaluation/application logic to determine whether semantically interpretable Evidence can be established.

The envelope may include:

- measurements/statistics;
- coverage achieved;
- uncertainty/error values;
- method validity/assumption diagnostics;
- count/extent summaries;
- bounded claim-support metadata;
- diagnostic dataset references;
- implementation/runtime/dependency identity;
- warnings/limitations;
- operational result state.

The adapter MUST NOT reduce every result to `passed=true/false` or a single quality score.

### Evidence establishment remains semantic

Evaluation/application logic validates that the runtime result matches the committed Criterion/method/subject/reference/scope and that claim strength does not exceed the actual method/coverage/uncertainty support.

Only then does Evaluation complete and establish Evidence.

A successful method runtime may therefore produce unfavorable or indeterminate Evidence, while an operationally successful runtime whose assumptions were invalid may lead to Evaluation semantic failure.

### Diagnostics remain data-plane material

Large violation datasets, nearest-neighbor examples, attack traces, sampled records, per-row checks, or similar diagnostics remain separately referenced data-plane outputs.

The Evaluation adapter must not force them into the bounded Evidence/control-plane record.

## Execution relationship

### Runtime realization occurs through Execution

Committed Learning, Generation, and Evaluation use Execution/Attempts for operational realization when runtime work is required.

The application coordinator resolves the implementation binding and runtime invocation; Execution owns operational realization and Attempt history; the runtime adapter performs the concrete computation.

```text
domain activity
    ↓ request realization
Execution
    ↓ Attempt
runtime adapter invocation
    ↓ operational outcome
Execution/Attempt state
    ↓
domain owner determines semantic outcome
```

### Platform launcher is below Execution

An adapter or launcher may create Spark jobs, Databricks runs, Kubernetes jobs, PyTorch workers, subprocesses, or remote-service requests.

Those platform objects remain implementation references beneath one SYNGAN Execution/Attempt and cannot redefine its identity.

004-F refines retry/resume/checkpoint/cancellation/reconciliation semantics.

## Runtime portability and specialization

### No universal runtime

A conformant implementation may realize Strategy/Evaluation work through, for example:

- Spark-native distributed computation;
- coordinator/local bounded computation;
- distributed PyTorch or another ML runtime;
- accelerator-oriented workers;
- a hybrid Spark + external distributed compute path;
- an explicitly allowed remote service;
- future runtime families.

No one runtime family is universal SYNGAN semantics.

### Spark-native requirement remains data-centric

Even when the synthesis model is implemented in PyTorch or another runtime, enterprise-scale structured source/output interaction must honor the distributed data-reference/data-plane architecture.

A PyTorch implementation is not permitted to make `collect entire Spark source into one pandas DataFrame on the driver` the ordinary architecture merely because its local training API accepts pandas/NumPy.

An adapter may use bounded samples, distributed sharding/streaming, persisted distributed exchange, summaries, or other scale-compatible techniques declared by the Strategy.

### Runtime specialization may add capability, not weaken guarantees

A Databricks-specific or GPU-specific adapter may exploit platform features for performance, snapshotting, launch, checkpointing, or observability.

It must still preserve common semantic commitments, exact source/candidate identities, no-hidden-egress rules, state/result authority, and historical/reproducibility facts.

If a platform adapter cannot satisfy a required common guarantee, readiness reports incompatibility/limitation rather than silently weakening the guarantee.

## Dependency, network, and egress architecture

### Dependency resolution is explicit

The runtime adapter receives resolved/approved dependency references or uses dependency-resolution ports supplied by the framework.

It MUST NOT autonomously repair missing dependencies by downloading a model, switching endpoint, enabling telemetry, or using another artifact.

### Runtime dependency declaration

Implementation bindings may add implementation-specific requirements that are narrower/more concrete than the Strategy declaration, such as:

- CUDA/runtime version;
- Python/package compatibility;
- local model artifact/codec version;
- Spark capability/version;
- minimum worker topology;
- network destination/service identity;
- temporary scratch/storage needs.

Material requirements must be visible during readiness before commitment where required.

### Egress remains separately authorized

An adapter that uses network access must preserve the declared distinction among no content egress, metadata/configuration, source-derived state, source records, and generated records.

The adapter cannot infer authorization from network connectivity.

004-H defines the enforcement/authorization/redaction architecture.

## Resource and scale declarations

### Strategy declaration versus binding/runtime feasibility

Strategy owns reusable scale/resource characteristics actors need for semantic selection.

Implementation binding owns more concrete runtime feasibility such as supported accelerator/software/topology envelopes.

Activity readiness combines both with the actual deployment environment.

### No fake enterprise scale

An implementation MUST NOT be advertised as enterprise/Spark-scale solely because it can be invoked from Spark.

If a runtime implementation has a source-size/cardinality/model-size cliff, driver-memory requirement, or non-distributed bottleneck, the binding must expose it sufficiently for readiness and benchmarking.

### Bounded coordinator state

Runtime specifications, status, result summaries, dependency declarations, and manifest roots remain bounded control-plane/coordinator state.

Large tensors, rows, candidate output, learned components, per-row diagnostics, and platform telemetry remain in data/runtime planes.

## Progress and observability ports

Runtime adapters MAY report Strategy/method-specific progress facts to Execution, such as:

- phase/stage;
- epochs/iterations;
- partitions or work units processed;
- current loss/statistics;
- checkpoint availability;
- resource health;
- output extent.

These are operational facts and MUST NOT be translated automatically into domain semantic completion percentages.

Adapters SHOULD expose platform-native observability references where useful rather than duplicating all telemetry into SYNGAN.

004-I deepens observability/platform integration.

## Checkpoint and recovery boundary

004-E establishes only the extension-facing obligations:

- a runtime adapter may create checkpoint/recovery material through framework-approved checkpoint ports;
- checkpoint identity is scoped to the same committed activity/Execution/Attempt context;
- the adapter must state enough compatibility/codec/runtime facts to determine whether resume may be possible;
- a checkpoint is not a Learned State or completed Generation output;
- resume must use the same committed semantic invocation unless a new activity is created.

004-F defines checkpoint lifecycle, recovery qualification, fencing, idempotency, and cancellation mechanics.

## Cancellation boundary

Runtime adapters should support cooperative cancellation/interruption where the runtime permits it and must report whether cancellation was acknowledged/observed.

A cancellation signal delivered to the runtime does not by itself establish Execution or domain cancellation.

004-F owns the final operational architecture for cancellation races and reconciliation.

## Failure classification at the runtime boundary

The adapter boundary must allow callers to distinguish at least:

- extension/binding unavailable;
- extension/SPI incompatible;
- required runtime/software/resource dependency unavailable;
- dependency identity mismatch;
- policy/network/egress incompatibility;
- source/state/data-reference resolution failure;
- adapter protocol/conformance defect;
- recoverable Attempt/runtime failure;
- terminal runtime failure;
- checkpoint/state-codec incompatibility;
- candidate/state materialization integrity failure;
- runtime succeeded but semantic result validation failed;
- unknown/indeterminate platform/runtime outcome.

The adapter should not collapse these into an opaque exception string when structured state can be preserved.

Execution/domain layers map these facts to their own owner-specific lifecycle semantics.

## Extension conformance

A Strategy implementation extension is conformant only if it can demonstrate that it:

1. identifies the exact Strategy revision/configuration semantics it implements;
2. declares material implementation/runtime/dependency/network/egress behavior;
3. preserves the distinction between semantic activity identity and runtime/platform identity;
4. consumes immutable committed invocation facts rather than inventing new semantics during execution;
5. honors exact source/input/Learned State/candidate references;
6. writes through approved Learned-State/candidate/diagnostic materialization boundaries;
7. keeps checkpoint/intermediate state distinct from promoted semantic results;
8. does not establish Learning/Generation/Evaluation semantic completion directly;
9. supports required Provenance/reproducibility reporting of material implementation/runtime facts;
10. avoids mandatory ordinary full-corpus driver collection for Strategy capabilities advertised as enterprise-scale;
11. honors explicit network/no-egress policy without hidden acquisition/fallback;
12. exposes implementation limitations rather than weakening upstream semantics silently.

An Evaluation method extension follows equivalent rules for committed method/subject/reference/coverage semantics and Evidence establishment.

## Testing obligations implied by architecture

Later implementation planning must include conformance tests such as:

### Binding tests

- exact Strategy/method revision compatibility;
- incompatible SPI/package/state-codec versions rejected;
- implementation-specific limitations narrow rather than silently broaden declarations;
- dependency/network/egress declarations available before invocation.

### Learning adapter tests

- exact committed source state is read;
- checkpoints do not appear as Learned State;
- candidate Learned State material is sealed/validated before establishment;
- result identity survives runtime teardown;
- distributed state does not require full driver loading.

### Generation adapter tests

- learned-state and direct-generation paths remain distinct;
- writes occur only through the supplied candidate sink/fence;
- runtime success cannot directly publish completed output;
- candidate identity remains exact through sealing/Evaluation/promotion;
- stale/losing runtime work cannot silently become authoritative.

### Evaluation adapter tests

- exact subject/reference is examined;
- coverage/uncertainty/diagnostic information survives the adapter boundary;
- negative method findings are not mapped to runtime failure;
- operational success with invalid assumptions does not establish Evidence;
- claim-strength data cannot be inflated by the adapter.

### Enterprise tests

- no hidden network acquisition/telemetry;
- no unauthorized egress fallback;
- adapter/runtime unavailability does not mutate committed semantics;
- platform specialization does not weaken source/output identity guarantees;
- ordinary large-scale paths avoid full driver-local corpus/state/result collection.

## No new domain concept result

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
- Runtime Profile;
- Runtime Result.

These are implementation/representation roles beneath accepted Strategy/Learning/Generation/Evaluation/Execution semantics.

## Deferred decisions

004-E intentionally does not settle:

- Python entry points versus explicit registration;
- exact plugin package/module layout;
- abstract base class versus Protocol/interface style;
- Spark ML integration API;
- PyTorch/TorchDistributor/torchrun selection;
- GPU/distributed training framework;
- Learned State serialization format;
- state manifest/codec schema;
- model registry integration;
- remote-service SDK architecture;
- scheduler/orchestrator implementation;
- checkpoint store;
- extension sandboxing/signing/trust policy;
- runtime process/container isolation;
- exact progress/cancellation callback API;
- exact exception/result envelope classes.

Those choices must preserve the architecture above and are refined by 004-F/004-H/004-I or Phase 005 implementation planning.

## Architecture invariants

1. A Strategy extension implementation MUST NOT become Strategy semantic authority merely because executable code is registered.
2. Strategy semantic revision, implementation-binding revision, SPI version, package version, and state-codec version MUST remain distinguishable where material.
3. Implementation bindings MAY narrow Strategy capability but MUST NOT silently broaden it.
4. Material implementation identity/runtime facts MUST remain historically attributable when they affect behavior or reproducibility.
5. Runtime invocation MUST preserve the exact committed activity semantics and references.
6. Runtime adapters MUST NOT mutate canonical activity/result state directly outside owning control contracts.
7. Runtime/platform success MUST NOT establish Learning, Generation, or Evaluation semantic completion by itself.
8. Learning runtime material/checkpoints MUST remain distinct from established Learned State.
9. Learned State logical identity MUST remain distinct from loaded PyTorch/Spark/statistical runtime objects.
10. Direct-generation Strategies MUST NOT fabricate Learning/Learned State.
11. Generation runtime MUST write through non-final candidate materialization and cannot promote output directly.
12. Evaluation runtime MUST bind exact subject/reference and cannot create stronger Evidence than committed method/coverage supports.
13. Large diagnostics, rows, Learned State components, and output payloads MUST remain outside bounded control-plane result envelopes.
14. Platform jobs/processes MUST remain subordinate to SYNGAN Execution/Attempt identity.
15. Missing implementation/dependency/runtime capability MUST fail/limit readiness or realization explicitly rather than silently switch behavior.
16. Runtime-network or artifact acquisition behavior MUST remain explicit and opt-in under governing policy.
17. Advertised enterprise-scale runtime paths MUST NOT require unavoidable full-corpus driver/local collection.
18. Spark-native architecture MUST remain compatible with non-Spark model runtimes while preserving Spark-scale source/output data boundaries.
19. Model/runtime specialization MUST NOT make CTGAN, GANs, PyTorch, Spark ML, Databricks, HuggingFace, LLMs, or another ecosystem universal semantics.
20. No extension contract may create a permanent single-table invariant.

## Operational principle

A practitioner commits Learning against a 300-million-row versioned Spark source using a local neural Strategy. The Strategy revision declares locally executable distributed Learning, GPU requirements, no runtime network, and a specific Learned State representation family. Readiness resolves a compatible PyTorch-distributed implementation binding and exact local base artifacts. Execution invokes the adapter with an immutable bounded runtime specification and stable source reference; the adapter streams/shards distributed source data without collecting the entire corpus to the driver, writes checkpoints through recovery ports, and eventually seals candidate learned components. Learning—not the adapter—validates the candidate and establishes one logical Learned State.

Weeks later a Generation resolves that Learned State through the same or another explicitly compatible runtime binding, loads components directly into the required workers, and writes synthetic data through a fenced candidate sink. The adapter finishes successfully but the Generation remains awaiting validation. Evaluation adapters examine the exact sealed candidate; one exhaustive Constraint Evaluation and one statistical fidelity Evaluation produce bounded method results. Evaluation establishes Evidence, and only after mandatory completion obligations are satisfied does Generation promote one completed output.

A different Strategy may generate directly with a Spark-native adapter and no Learning occurrence. A future remote-service Strategy may also be supported, but only through explicit runtime-network/egress declarations and authorization; it does not alter the offline-capable core.

## Phase relationship

004-E supplies the runtime/extension boundaries required by:

- **004-F** — concrete Execution/Attempt, checkpoint, recovery, fencing, idempotency, and cancellation architecture;
- **004-G** — Evidence/Provenance/reproducibility structures and historical queries over exact runtime/data identities;
- **004-H** — dependency trust/resolution, authorization, redaction, plugin/runtime trust, and no-egress enforcement;
- **004-I** — deployment topology, platform integration, portability, compatibility matrices, observability, and operational scaling.
