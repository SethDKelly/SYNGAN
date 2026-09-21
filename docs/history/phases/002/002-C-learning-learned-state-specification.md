---
type: Phase Record
title: 002-C — Learning & Learned State Specification
status: complete
---

# 002-C — Learning & Learned State Specification

## Objective

Deepen the accepted [Learning](../../concepts/learning.md) and [Learned State](../../concepts/learned-state.md) concepts into precise semantic commitment, source-binding, lifecycle, completion, retry, checkpoint, reuse, compatibility, sensitivity, and enterprise-scale semantics.

The phase preserves the Phase 001 separation between the activity that derives reusable state and the reusable result that survives that activity.

## Governing authority

002-C is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)
- [002-A — Data Meaning & Constraint Specification](002-A-data-meaning-constraint-specification.md)
- [002-B — Synthesis Strategy Specification & Capability Semantics](002-B-synthesis-strategy-capability-semantics.md)

Canonical concept authority remains under `docs/concepts/`; this record preserves the refinement history and handoff.

## Scope

002-C specifies:

- when Learning exists and when direct-generation Strategies omit it;
- Learning proposal/validation/commitment semantics;
- stable source identity/history requirements;
- bound Data Meaning, Strategy/configuration, Constraint, dependency, sampling, and reproducibility context;
- Learning lifecycle and semantic completion;
- Learning ↔ Execution/Attempt separation;
- retry/resume invariance;
- checkpoint/intermediate-state boundary;
- one-Learning/one-primary-Learned-State cardinality;
- Learned State logical identity versus physical representation;
- Learned State lifecycle and contextual reuse compatibility;
- Learned State dependencies on base/pretrained artifacts;
- immutability, retirement, restriction, and invalidation;
- sensitivity/privacy boundary;
- enterprise-scale/distributed representation requirements;
- synchronization refinements to SYNC-04, SYNC-05, SYNC-06, SYNC-14, and SYNC-15.

## Non-goals

002-C does not select:

- Python `fit`/`train` API shape;
- Spark ML Estimator/Model mappings;
- PyTorch/TorchDistributor implementation;
- optimizer/training algorithms;
- checkpoint formats;
- source fingerprint/version mechanism;
- storage/serialization format for Learned State;
- model registry technology;
- scheduler/job mapping;
- retry policy implementation;
- artifact hashing/manifest format;
- public save/load APIs;
- privacy mechanism or privacy guarantee;
- exact Generation completion semantics;
- exact Evaluation evidence taxonomy.

## Canonical authority refined

002-C directly deepens:

1. [Learning](../../concepts/learning.md)
2. [Learned State](../../concepts/learned-state.md)
3. [Core Synchronizations](../../synchronizations/core-synchronizations.md)

No new standalone concept is introduced.

## Learning specification decisions

### 1. Learning is not universally required

Learning exists only when a Strategy requires or intentionally supports reusable source-derived state.

A Strategy capable of direct Generation without reusable Learned State does not create a no-op Learning occurrence merely for lifecycle symmetry.

### 2. Learning has an explicit semantic commitment boundary

A proposed Learning remains editable until its material prerequisites/context are validated and committed.

At commitment it binds, where material:

- source identity/version context;
- Data Meaning revision;
- Strategy/configuration revision;
- applicable Constraint revisions and learning handling dispositions;
- learning scope;
- sampling/approximation/summarization semantics;
- Strategy-specific learning parameters;
- dependency/network profile;
- local/pretrained artifact identity;
- reproducibility-relevant randomness/seed intent.

After commitment these facts define the historical Learning occurrence.

A material semantic/configuration change requires a new distinguishable Learning rather than in-place mutation.

### 3. Source identity is part of Learning history

A mutable table/location name alone is not sufficient historical identity when source contents can change materially.

The concept requires enough source identity to state what source state informed the Learned State.

Later representation may use versions, snapshots, fingerprints, manifests, or equivalent mechanisms, but the semantic requirement is stable historical attribution.

### 4. Retry/resume preserves Learning semantics

One committed Learning may span multiple Attempts through Execution.

Retry/resume changes operational realization, not the committed semantic Learning specification.

An Attempt MUST NOT silently change source, Data Meaning, Strategy/configuration, Constraints, sampling policy, dependency profile, or other bound Learning semantics.

### 5. Learning completion is semantic, not computational

`Execution.completed` is insufficient.

Learning completes only when:

- the committed derivation was realized sufficiently for Strategy semantics;
- no terminal defect invalidates the intended result;
- the result is distinguishable from partial/recovery state;
- one stable primary Learned State identity can be established;
- future-use requirements/limitations are available sufficiently for later validation;
- required provenance can be recorded consistently.

### 6. Checkpoints are not Learned State by default

Checkpoints, partial parameters, optimizer state, summaries, encodings, caches, or other durable intermediates may support recovery while Learning is incomplete.

Durability or physical reusability inside the training process does not make them the domain result.

A checkpoint becomes part of Learned State only through explicit successful-result validation/promotion under the Learning contract.

### 7. Learning is broader than neural training

Learning can derive reusable state through statistical, probabilistic, copula, sketch/summary, GAN/VAE/diffusion/autoregressive, embedding, hybrid, or other Strategy-defined methods.

`train` and `fit` remain implementation/API vocabulary rather than conceptual boundaries.

### 8. Full-source direct consumption is not required

Learning may use full distributed data, samples, sketches, summaries, staged methods, or approximate techniques where the Strategy supports them.

Material approximation/sampling semantics must remain inspectable when they affect interpretation, fidelity expectations, limitations, or reproducibility.

This preserves enterprise-scale flexibility without lowering transparency.

### 9. No-network commitment applies to Learning

If a Strategy/Learning is committed under a no-network/no-egress profile, missing artifacts, telemetry, remote training, remote inference, or remote fallback cannot be enabled silently.

Material local/pretrained artifact identity remains part of historical context when it affects behavior.

### 10. Learning does not imply privacy

Learning and Learned State may retain sensitive source information.

Successful Learning is not evidence that the reusable result is anonymous, disclosure-safe, or appropriate for export.

## Learned State specification decisions

### 1. Learned State is one logical durable result

Under the current model one Learning produces zero or one primary Learned State.

That state may be physically composed of many files, partitions, tensors, tables, statistics, encoders, or other components.

Logical cardinality is not storage cardinality.

If a future Strategy naturally produces several independently reusable outputs with separate lifecycle/purpose, that triggers explicit concept/cardinality review.

### 2. Learned State is not a model file

Learned State is not defined as:

- one PyTorch object/state dict;
- Spark ML `Model`;
- checkpoint;
- file;
- directory;
- artifact registry entry.

Those may be representations or components.

The concept is the reusable logical state plus the historical/compatibility meaning needed to use it correctly.

### 3. Learned State survives compute teardown

A reusable Learned State must remain independently identifiable after the original Learning Execution/process/cluster is gone.

It may require durable distributed representation and is not required to fit driver memory, one worker, one Python object, or one local file.

### 4. Learned State is historically immutable in meaning

After establishment its learned semantic identity is immutable.

Physical relocation, replication, compaction, or reserialization may later preserve logical identity if the representation contract guarantees equivalent behavior.

A transformation that materially changes synthesis behavior creates a new distinguishable learned result/activity rather than silently mutating the old identity.

### 5. Learned State has intrinsic lifecycle but contextual compatibility

Learned State may be:

- usable;
- restricted;
- retired;
- invalidated.

These are intrinsic future-use states.

Compatibility with one proposed Generation is contextual and belongs to Generation.

Learned State MUST NOT accumulate global pairwise compatibility truth.

### 6. Later semantic/rule/Strategy changes do not rewrite history

New Data Meaning, Constraint, or Strategy revisions create new future-use compatibility questions.

They do not mutate what an existing Learned State was derived from.

Future governance may restrict/invalidate the state or require new Learning, while historical Generations remain traceable to the state actually used.

### 7. Base/pretrained dependencies remain explicit

A Learned State may depend on an externally originating but locally provisioned base artifact.

If Generation requires that artifact, the Learned State must preserve enough dependency identity to avoid appearing self-contained.

Replacing the base artifact with materially different content is a new compatibility/reproducibility context.

Missing dependencies cannot trigger undeclared network acquisition under a no-network profile.

### 8. Ordinary reuse is non-mutating

One Learned State may support many Generations with different amounts, Conditions, seeds, output destinations, or evaluation plans.

Ordinary reuse does not mutate the state.

If a Generation adapts/fine-tunes/updates it materially, that behavior requires explicit new Learning/derived-state semantics rather than hidden mutation.

### 9. Learned State is potentially sensitive

Learned State may encode or memorize source information.

Therefore it is not automatically anonymous, safe to publish, or safe to send to an external service merely because it is not raw records.

This is an enterprise-security and later privacy-evaluation concern, not a formal privacy conclusion.

## Learning ↔ Learned State production boundary

The central Phase 002-C rule is:

> **Learning establishes Learned State only at successful semantic completion; physical durability before completion is not sufficient.**

This prevents checkpoints, partial models, or transient distributed state from accidentally entering the reusable catalog as valid synthesis state.

## Source mutation and future reuse

If source data changes after Learning:

- existing Learning history remains tied to the source state actually used;
- Learned State remains historically tied to that Learning;
- future reuse may still be allowed or rejected depending on Generation context;
- new source data does not silently update Learned State;
- incorporating new source information requires new Learning or another explicit derivation path.

## Scale conclusions

### Learning

Learning may use large distributed compute and corpus-growing transient state, but its canonical specification/lifecycle remains control-plane state.

Ordinary enterprise Learning MUST NOT require complete source-corpus driver/local materialization.

### Learned State

Learned State may itself be large and distributed.

Later architecture must allow a logical Learned State to refer to distributed material rather than forcing a single driver-local serialized object.

Any coordinator-local size-growing requirement must be justified explicitly.

## Synchronization refinements

### SYNC-04 — Learning operational realization

Now explicitly defines:

- Learning semantic commitment versus Execution operation;
- retry/resume invariance;
- failed Attempt versus terminal Learning failure;
- checkpoint/intermediate material as non-Learned-State by default.

### SYNC-05 — Learning produces Learned State

Now explicitly defines:

- semantic completion conditions;
- one-primary-Learned-State cardinality;
- distributed/composite physical representation;
- traceability to source/meaning/Strategy/Constraint/dependency/sampling context;
- retirement/restriction/invalidation as future-use state.

### SYNC-06 — Generation compatibility

Now explicitly treats Learned State reuse as contextual validation owned by Generation and prohibits ordinary reuse from mutating/adapting Learned State silently.

### SYNC-14 — Provenance

Now records the material Learning → Learned State derivation chain, including source identity, semantic/configuration revisions, sampling/approximation, dependencies, and relevant Execution/Attempt facts without copying source/model payloads.

### SYNC-15 — Reproducibility

Now requires Learning source identity and learned-state derivation/dependency context to be sufficient to state supported reproduction/comparison semantics.

## Invariant set added/refined

### Learning invariants

1. Learning is required only when reusable source-informed state is part of Strategy intent.
2. committed Learning binds stable source/semantic/Strategy/Constraint/dependency context;
3. material post-commitment changes do not mutate the activity;
4. retry/resume does not change committed semantics;
5. Execution completion is not Learning completion;
6. checkpoints/intermediates are not Learned State by durability alone;
7. failed/cancelled/incomplete Learning cannot establish usable Learned State;
8. one Learning produces zero or one primary Learned State under the current model;
9. material sampling/approximation is inspectable;
10. ordinary large-scale Learning does not require full-corpus driver materialization;
11. no-network commitments cannot be bypassed silently;
12. Learning does not imply privacy.

### Learned State invariants

1. independently identifiable after producing compute is gone;
2. logical identity is distinct from files/objects/checkpoints;
3. only successful Learning establishes it;
4. historically immutable learned meaning;
5. contextual compatibility belongs to Generation;
6. later Data Meaning/Constraint/Strategy changes do not rewrite derivation history;
7. required base/pretrained dependencies remain explicit;
8. ordinary reuse does not mutate the state;
9. restriction/retirement/invalidation affects future use, not historical truth;
10. Learned State may be distributed and larger than driver/local memory;
11. Learned State is not presumed private or release-safe.

## Deferred questions handed forward

### To 002-D — Generation

- exact Learned State compatibility decision at Generation commitment;
- interaction among Conditions, Constraints, Learned State limitations, and Generation completion;
- whether/when Generation can operate with a restricted Learned State;
- handling of partial output when state/dependency problems occur;
- explicit treatment of any adaptive generation behavior that would otherwise mutate Learned State.

### To 002-E — Evaluation / Evidence

- Criteria/Evidence for learned-state or generated-output fidelity/utility/privacy risk;
- how to preserve evidence limitations when Learning used sampling/approximation;
- whether Learned State itself becomes an Evaluation input for certain privacy/risk assessments.

### To 002-F — Execution

- detailed Attempt/checkpoint/retry/resume lifecycle;
- cancellation race/terminal-state semantics;
- operational progress and recovery without redefining Learning completion.

### To 002-G — Provenance / Reproducibility

- exact source identity/fingerprint requirements;
- learned-state/base-artifact identity requirements;
- software/runtime/environment facts needed for reproduction;
- lineage rules for retirement/invalidation/migration.

## Exit criteria

002-C is complete when:

- [x] Learning applicability and direct-generation omission are explicit;
- [x] semantic commitment boundary is specified;
- [x] source identity/history requirement is explicit;
- [x] Learning validation and lifecycle semantics are defined;
- [x] retry/resume preserves committed semantics;
- [x] checkpoint/intermediate state is separated from Learned State;
- [x] semantic completion criteria are explicit;
- [x] Learning method remains model-neutral;
- [x] sampling/approximation transparency is explicit;
- [x] no-network/dependency requirements are preserved;
- [x] one-primary-Learned-State cardinality is explicit;
- [x] Learned State logical identity is separated from physical representation;
- [x] lifecycle/restriction/retirement/invalidation semantics are explicit;
- [x] contextual reuse compatibility is separated from intrinsic Learned State state;
- [x] external/base artifact dependencies are explicit;
- [x] ordinary reuse is non-mutating;
- [x] Learned State sensitivity/privacy boundary is explicit;
- [x] enterprise-scale/distributed state semantics are explicit;
- [x] canonical synchronization authority is refined without adding new concepts;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Learning and Learned State are now sufficiently specified for Generation to make a precise contextual reuse decision without conflating training jobs, checkpoints, model files, source updates, or external artifacts with the semantic reusable state being selected.

## Next phase

**002-D — Generation Specification, Request/Condition Semantics & Output Completion**

002-D should define Generation commitment, request/Condition semantics, direct versus Learned-State generation, contextual compatibility, required Constraint handling/satisfaction, partial-output semantics, completion/failure/cancellation, output identity, and non-mutating Learned State reuse.