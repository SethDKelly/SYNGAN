---
type: Concept
title: Learned State
status: accepted
---

# Learned State

## Purpose

Preserve reusable source-derived information independently of the Learning occurrence, Execution, and runtime object that produced it.

Learned State exists so reusable synthesis knowledge can survive compute teardown, be selected by later Generation, be compared or superseded by newer learned results, and remain historically attributable without being equated to a checkpoint, model file, Spark ML object, or PyTorch module.

## Concept boundary

Learned State is the **durable logical result of successful Learning**.

It owns:

- stable logical identity/version;
- producing Learning reference;
- bound Strategy/configuration identity inherited from that Learning;
- source/Data Meaning/Constraint/dependency provenance references needed to interpret reuse;
- intrinsic compatibility requirements and declared limitations;
- logical component/representation references sufficient to locate/use the state;
- future-use lifecycle such as usable, restricted, retired, or invalidated;
- learned-state-specific diagnostics/limitations where they remain material after Learning.

Learned State does not own:

- the Learning activity that produced it;
- generic Execution/Attempt history;
- checkpoint/recovery semantics;
- global compatibility with every possible Generation;
- physical persistence format;
- a generic Artifact catalog;
- Data Meaning, Constraint, or Strategy authority;
- privacy/release approval.

## Establishment rule

A Learned State identity MAY be established only by successful semantic completion of Learning under [SYNC-05](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state).

Physical material created during Learning—checkpoints, temporary tensors, partial statistics, caches, files, optimizer state, intermediate tables—does not become Learned State merely because it is durable or reusable by the training process.

The distinction is semantic:

> **Checkpoint/recovery state helps continue Learning. Learned State fulfills Learning's purpose after Learning is complete.**

A checkpoint can become or contribute to the final Learned State only when the Learning contract explicitly validates/promotes it as the completed reusable result.

## Logical identity versus physical representation

Learned State has one stable logical identity under the current concept model even when its physical representation is composite or distributed.

Its representation may include many components such as:

- neural model weights;
- statistical distributions/parameters;
- copula/dependency structures;
- encoders/decoders;
- category dictionaries;
- learned embeddings;
- sketches/summaries;
- rule-support structures;
- partitioned files/tables;
- strategy-specific state;
- references to immutable pretrained/base artifacts when required.

These components do not automatically become separate Learned State concepts.

If future Strategies produce several independently reusable results with different selection/lifecycle semantics, the one-Learning/one-primary-Learned-State cardinality must be revisited explicitly rather than hidden behind an arbitrary artifact container.

## Historical identity

Learned State MUST remain traceable to the exact committed Learning that established it.

That historical context includes, by reference where material:

- source identity/version context;
- Data Meaning revision;
- Strategy revision/configuration;
- applicable Constraint revisions and learning handling dispositions;
- material sampling/approximation semantics;
- dependency/network profile;
- material local/pretrained artifact identities;
- reproducibility-relevant Learning state;
- producing Execution/Attempt context through Provenance where needed.

Learned State does not duplicate all of that authority into one payload. It preserves stable references sufficient to explain and validate the result.

## Lifecycle semantics

A Learned State lifecycle must preserve distinctions equivalent to:

- **usable** — eligible for contextual validation and new Generation use;
- **restricted** — still historically valid but subject to an explicit future-use limitation requiring review or narrower compatibility;
- **retired** — intentionally removed from ordinary future selection without asserting that it was historically wrong;
- **invalidated** — known to be materially unsafe/incorrect/incompatible for new reliance under its declared semantics.

A later representation MAY use different labels but must preserve these meanings.

Historical identity remains even after retirement or invalidation.

## Restricted versus contextual incompatibility

`restricted` is an intrinsic future-use status or known limitation of the Learned State.

Contextual compatibility for one proposed Generation belongs to that Generation, not to Learned State as global mutable state.

Therefore Learned State MUST NOT accumulate fields such as:

```text
compatible_with_generation_X = true
compatible_with_dataset_Y = false
```

A Generation may determine that a usable Learned State is incompatible with its requested Data Meaning, Conditions, Constraints, deployment profile, or Strategy/runtime context. That result remains local to the Generation.

## Compatibility inputs

A Generation validating Learned State reuse may need to compare:

- Strategy identity/configuration compatibility;
- Data Meaning revision or semantic equivalence requirements;
- requested Condition/generation semantics;
- applicable Constraint requirements;
- Learned State format/runtime compatibility;
- required base/pretrained artifact identity;
- software/runtime compatibility where material;
- dependency/network policy;
- known Learned State limitations/restrictions;
- future privacy/risk restrictions where explicitly established.

Learned State owns its declared intrinsic requirements/limitations; Generation owns the contextual result.

## Data Meaning evolution

A later Data Meaning revision MUST NOT rewrite Learned State history.

If newer meaning reveals that the Learned State was produced under materially incorrect or obsolete semantics, later governance/compatibility assessment may:

- restrict future use;
- invalidate the Learned State for new use;
- require new Learning;
- allow limited use under explicit qualification.

Historical Generations that legitimately used the state remain traceable to the meaning known/bound at that time.

## Constraint evolution

A later Constraint revision does not become part of the historical Learning that produced the Learned State.

Future Generation may validate whether the Learned State/Strategy can support newer applicable Constraints, but this is a new contextual compatibility question.

A Learned State MAY be restricted/invalidated if a newly discovered issue makes future safe/correct use impossible, but that status does not rewrite the original rule set or Learning history.

## Strategy/configuration evolution

A later Strategy revision MUST NOT silently relabel an existing Learned State as though it were produced under the newer Strategy.

Reuse under a newer implementation/runtime may be allowed only through explicit compatibility semantics.

If a Strategy's learned-state representation/semantics are not compatible across versions, future Generation must reject or qualify reuse rather than silently migrate meaning.

Migration/conversion tooling, if later supported, must produce an explicitly identifiable result/history rather than mutate provenance invisibly.

## External/pretrained artifact dependencies

Learned State may depend on a locally provisioned or externally originating artifact that was part of the committed Strategy/Learning context.

Examples could include:

- pretrained base weights;
- tokenizer/vocabulary artifacts;
- reference tables;
- fixed encoders;
- foundation/base representations.

When generation requires such an artifact in addition to the source-derived state, Learned State must preserve enough identity/dependency information to avoid pretending it is self-contained.

Replacing a required base artifact with materially different content creates a new compatibility/reproducibility context and MUST NOT be treated as silent equivalence.

A missing required artifact MUST NOT trigger an undeclared network acquisition under a no-network profile.

## Self-contained versus dependent Learned State

002-C does not require every Learned State to be physically self-contained.

A Learned State may be:

- **self-contained for generation** — all materially required learned components are locally represented/resolvable;
- **dependent** — generation also requires explicitly identified Strategy/runtime/base artifacts.

This distinction is a reuse/dependency property, not a new concept.

The actual packaging format remains deferred.

## Reuse semantics

A usable Learned State can support zero, one, or many Generations over time.

Reuse does not mutate the Learned State merely because different Generation requests use:

- different output sizes;
- different Conditions;
- different seeds/randomness;
- different output destinations;
- different evaluation plans.

If a Generation operation updates/adapts the state materially, that behavior is not ordinary reuse and requires explicit concept treatment—likely a new Learning/derived Learned State rather than hidden mutation of the original.

## Immutability of learned semantics

Once established, the semantic content/identity of a Learned State is immutable for historical purposes.

Physical compaction, relocation, replication, reserialization, or storage migration MAY occur later if they preserve logical identity and behavior under an explicit representation contract.

A transformation that materially changes learned synthesis behavior MUST create a new distinguishable Learned State (normally through Learning or an explicitly specified derivation process) rather than mutating the existing identity.

## Sensitivity and privacy boundary

Learned State is source-derived and may retain information about sensitive source data.

Therefore:

- Learned State MUST NOT be presumed anonymous;
- Learned State MUST NOT be presumed safe to export or publish;
- synthetic-data privacy claims MUST NOT automatically extend to Learned State;
- remote transmission of Learned State or its components is a separate security/governance concern;
- later privacy/disclosure-risk work may treat Learned State differently from synthetic output.

A learned model can memorize or otherwise encode source information even when its generated outputs are intended to be synthetic. This concept makes no default privacy guarantee.

## Scale semantics

Learned State may be large, composite, distributed, or accelerator-oriented.

It MUST NOT be conceptually required to fit in:

- driver memory;
- one worker's memory;
- one local file;
- one Python object.

The logical state should remain identifiable and reusable when its representation spans partitions/files/object-store entries or other distributed material.

Later architecture must identify what portion, if any, must be coordinator-local and justify any size-growing local requirement.

## Durability semantics

A valid Learned State must outlive the transient compute resources that produced it to the degree promised by the Strategy/use contract.

That does not require infinite retention; it means reuse cannot depend on an in-memory object disappearing with the original Learning process unless the state was explicitly never declared durable/reusable—which would contradict Learning's purpose under the current concept.

Storage lifecycle/retention policy remains representation/governance work.

## Comparison and lineage

Actors may compare multiple Learned States produced from:

- different source revisions;
- different Data Meaning revisions;
- different Strategy/configurations;
- different random seeds;
- different sampling/approximation choices;
- different software/runtime versions.

Comparison does not create equivalence automatically.

Provenance must preserve enough derivation context for later Evaluation or governance to understand these differences.

## Retirement and invalidation

### Retire

Stops ordinary future selection without asserting historical error.

Possible reasons include:

- newer state is preferred;
- operational deprecation;
- cost/maintenance choice;
- superseding Learning.

### Invalidate

Prevents future reliance because a material defect, semantic incompatibility, unsafe dependency, or other issue makes the state unsuitable.

Examples may include:

- discovered source/meaning corruption;
- incorrect Strategy implementation affecting state validity;
- incompatible/missing required base artifact;
- security compromise of a material dependency;
- learned-state corruption.

Invalidation does not delete historical provenance or rewrite prior Generations.

## Actions

### Establish

Create a stable logical Learned State identity after successful Learning completion.

### Inspect

Review derivation, Strategy/configuration, dependencies, limitations, status, and representation references.

### Validate for intended use

Participate in Generation compatibility assessment by exposing intrinsic requirements/limitations. The Generation owns the contextual result.

### Select / reuse

Reference the Learned State for a compatible Generation without mutating it.

### Compare

Compare Learned States using provenance/metadata appropriate to the question without declaring universal superiority.

### Restrict

Apply an explicit future-use limitation while preserving historical validity.

### Retire

Remove from ordinary future selection.

### Invalidate

Block future reliance because of a known material defect/incompatibility.

## Invariants

1. Learned State MUST be independently identifiable after producing compute is gone.
2. Learned State MUST NOT be defined as one file, checkpoint, Python object, Spark ML Model, PyTorch module, or other physical representation.
3. Only successful semantic Learning completion may establish the primary Learned State result.
4. Checkpoint/intermediate durability alone MUST NOT imply Learned State status.
5. Learned State MUST trace to the Learning and Strategy/configuration that produced it.
6. Source, Data Meaning, Constraint, dependency, sampling/approximation, and reproducibility context materially affecting derivation MUST remain historically attributable through stable references/provenance.
7. Learned State semantic identity MUST NOT be mutated in place after establishment.
8. Contextual compatibility belongs to the consuming Generation; Learned State MUST NOT accumulate global pairwise compatibility truth.
9. Later Data Meaning, Constraint, or Strategy revisions MUST NOT rewrite Learned State history.
10. Retirement, restriction, or invalidation affects future use and MUST NOT rewrite historical Generations.
11. A required base/pretrained artifact dependency MUST remain explicit; the Learned State MUST NOT falsely appear self-contained.
12. Missing dependencies MUST NOT trigger undeclared network acquisition under a no-network profile.
13. Learned State MUST NOT be presumed private, anonymous, or safe for release merely because it is source-derived rather than source rows.
14. Learned State MUST support representations larger than driver/local memory where Strategy scale requires it.
15. Ordinary reuse MUST NOT mutate Learned State; material adaptation requires a new explicitly distinguishable result/activity.
16. One Learned State may support many Generations under the current model.

## Operational principle

A distributed Learning completes and establishes one logical Learned State composed of model parameters, encoders, and supporting statistics stored across durable locations. The original cluster terminates. Weeks later, a Generation validates that the same Strategy/configuration family, required local base artifact, Data Meaning expectations, and deployment profile are compatible, then reuses the Learned State to produce synthetic output.

A newer Learning later produces a second Learned State. The first is retired from ordinary selection but remains the historical source of prior Generations. When an incompatibility is discovered in the required base artifact, the first Learned State can be invalidated for future use without rewriting what earlier work actually used.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-05 — Learning produces Learned State](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state)
- [SYNC-06 — Generation commitment and compatibility](../synchronizations/core-synchronizations.md#sync-06--generation-commitment-and-compatibility)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-C does not decide:

- file/object/table/model serialization format;
- whether Learned State has a manifest or registry record;
- how distributed components are loaded;
- Spark ML `Model` mapping;
- PyTorch module/state-dict mapping;
- checkpoint promotion mechanics;
- artifact hashing/version format;
- retention/storage policy;
- migration/conversion API;
- public load/save method names.

Those representations must preserve this Learned State contract rather than redefine it.