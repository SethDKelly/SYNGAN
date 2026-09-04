---
type: Concept
title: Learning
status: accepted
---

# Learning

## Purpose

Derive reusable source-informed state according to accepted source meaning, synthesis behavior, applicable rules, and an explicitly bound learning context.

Learning exists because deriving reusable state is a domain activity with its own semantic commitment, prerequisites, outcome, failure modes, and historical meaning. It is not equivalent to a training job, Spark action, optimization loop, model fit call, checkpoint sequence, or Execution.

## Concept boundary

Learning is the **domain activity that derives reusable source-informed state**.

It owns:

- learning intent/specification;
- source identity/reference sufficient for historical interpretation;
- bound Data Meaning revision;
- bound Synthesis Strategy/configuration revision;
- applicable Constraint revisions and learning-relevant handling dispositions;
- material sampling/approximation semantics used for learning;
- Strategy dependency/network profile as committed for the activity;
- semantic lifecycle and outcome;
- learning-specific diagnostics/limitations;
- association with the resulting Learned State after successful semantic completion.

Learning does not own:

- generic retry, Attempt, scheduler, worker, or process state — Execution owns those;
- the reusable Learned State after it is established;
- checkpoint/recovery state as final domain output;
- Data Meaning, Constraint, or Strategy authority;
- a PyTorch training loop, Spark ML fit call, or one algorithm-specific optimization model;
- a universal requirement that every Strategy learn before generation.

## Learning applicability

A Learning occurrence exists only when the selected Strategy requires or intentionally supports deriving reusable source-informed state.

A Strategy that can generate directly without reusable Learned State MUST NOT be forced through fabricated Learning merely to satisfy a uniform pipeline shape.

A Strategy MAY support both direct generation and learned-state-assisted generation. The actor/activity intent determines whether a Learning occurrence is required.

## Learning specification

Before semantic commitment, Learning has a specification sufficient to determine what reusable state is intended to be derived and under which authority.

The specification conceptually includes:

- logical source dataset/reference;
- source version/snapshot/fingerprint semantics sufficient to distinguish material source changes;
- bound Data Meaning revision;
- bound Strategy revision/configuration;
- applicable Constraint revisions;
- learning-relevant Constraint handling dispositions;
- requested learning scope and relevant feature/semantic scope;
- material sampling, weighting, filtering, approximation, or summarization semantics;
- Strategy-specific learning parameters whose values materially affect derived state;
- required local/pretrained artifact identities where applicable;
- committed deployment/dependency profile, including network restrictions;
- reproducibility-relevant randomness/seed intent where applicable;
- expected primary Learned State result semantics.

The representation of these facts is deferred.

## Source identity and mutability

Learning MUST preserve enough source identity to state what data corpus or source state informed the result.

The concept does not require one universal source-version mechanism, but a mutable table name alone is insufficient historical identity when its contents can change materially.

Depending on later representation, adequate source identity may rely on versioned tables, snapshots, stable dataset revisions, fingerprints, manifests, or other mechanisms.

The semantic rule is:

> **A completed Learned State must remain traceable to the source state that actually informed it.**

Later source mutation affects future Learning only and MUST NOT rewrite the historical source binding of existing Learning or Learned State.

## Validation before commitment

Learning validates its proposed context before semantic commitment.

Material validation includes, as applicable:

- required Data Meaning is effective and sufficiently resolved;
- selected Strategy/configuration is eligible and contextually compatible;
- applicable Constraints are identified and their learning handling is explicit;
- required source scope is identifiable and accessible under the intended contract;
- required external/local artifacts are available or explicitly allowed to be acquired;
- deployment/network policy permits the Strategy's learning requirements;
- required resource class/capability is not known to be unavailable where that is a commitment prerequisite;
- required sampling/approximation semantics are explicit;
- no known conflict makes the proposed Learning semantically invalid.

Validation may produce `compatible with limitations` or `indeterminate` outcomes under the Strategy contract. A material `indeterminate` prerequisite MUST NOT silently become commitment success.

## Semantic commitment boundary

Learning has an explicit **semantic commitment boundary**.

Before commitment, its proposed specification MAY be edited/revalidated.

At commitment, Learning binds the material identities/revisions/configuration that define what is being learned:

- source identity/version context;
- Data Meaning revision;
- Strategy/configuration revision;
- applicable Constraint revisions and handling;
- material learning scope/sampling semantics;
- dependency/network profile and material external artifact identities;
- reproducibility-relevant intent.

After commitment, these facts are historical authority for that Learning occurrence.

A material change after commitment MUST NOT mutate the committed Learning in place. It requires a new Learning occurrence or another explicitly distinguishable committed activity according to later experience/representation design.

Retrying or resuming the same committed work through Execution does not create a semantically new Learning merely because a new Attempt occurs.

## Semantic lifecycle

The Learning lifecycle must preserve distinctions equivalent to:

- **proposed** — specification is still editable and not committed;
- **validated/ready** — known prerequisites have been assessed sufficiently for possible commitment;
- **committed** — material semantic inputs/configuration are bound;
- **active** — operational realization is underway or has been initiated;
- **completed** — reusable source-informed state has been semantically established and associated as Learned State;
- **failed** — Learning cannot establish its intended Learned State under this committed occurrence;
- **cancelled** — Learning was intentionally terminated before successful semantic completion.

A later phase MAY refine surface labels, but MUST preserve the semantic distinctions.

`active` does not transfer ownership of operational progress to Learning. Execution owns detailed attempts/progress; Learning owns the domain fact that its committed derivation work is currently being realized.

## Operational realization and Attempt semantics

Learning may synchronize with Execution for long-running or distributed work.

One committed Learning may be realized through:

- one Execution;
- multiple Attempts within that Execution;
- checkpoint/resume behavior;
- multiple physical jobs/tasks/processes within an Attempt.

These mappings are representation details.

A failed Attempt does not automatically make Learning failed if the same committed Learning can retry/resume validly.

Similarly, `Execution.completed` does not establish Learning completion. Learning must still establish that its semantic result is valid.

## Intermediate state and checkpoints

Learning MAY create intermediate material during operational realization, including:

- checkpoints;
- partial model parameters;
- distributed statistics;
- intermediate encodings;
- optimizer/training state;
- temporary summaries or caches.

Such material is **not automatically Learned State**.

Intermediate material may support recovery or continuation without satisfying the purpose of durable reusable source-informed state.

Only successful Learning semantic completion may establish the primary Learned State result.

A checkpoint MAY later become or contribute to a Learned State only if the Learning contract explicitly validates/promotes it as the successful reusable result; physical existence alone is insufficient.

## Learning methods and model neutrality

Learning is broader than neural-network training.

It can conceptually derive reusable state through:

- statistical estimation;
- probabilistic/dependency fitting;
- copula parameter derivation;
- learned distributions or sketches;
- GAN/VAE/diffusion/autoregressive optimization;
- learned encodings or embeddings;
- hybrid methods;
- other Strategy-defined source-informed derivation.

The word `training` may describe a particular implementation or Strategy family, but it does not redefine Learning.

## Sampling, approximation, and source coverage

Learning does not imply every source row must be consumed directly by the learning algorithm.

A Strategy may validly use:

- full distributed source processing;
- bounded or stratified samples;
- distributed summaries/sketches;
- staged learning;
- partition-local statistics;
- approximate procedures;
- other scale-aware methods.

When these choices materially affect interpretation, fidelity expectations, reproducibility, or limitations, the committed Learning specification MUST preserve them explicitly enough for Provenance and later Evidence.

Using a sample or summary does not convert the resulting data into synthetic data; it is a learning-method choice.

## Network and external-artifact semantics

Learning MUST honor the bound Strategy dependency profile and the [Network and External Dependency Policy](../authority/network-external-dependency-policy.md).

For a Learning committed under a no-network/no-egress profile:

- missing artifacts MUST NOT trigger silent external acquisition;
- remote inference/training calls MUST NOT be enabled implicitly;
- telemetry MUST NOT become a hidden network dependency;
- a remote fallback MUST NOT replace local behavior silently.

If a required local/pretrained artifact materially affects Learning, its effective identity/version must remain historically attributable.

## Constraint semantics during Learning

Learning may enforce, incorporate, defer, or not support Constraints according to the bound Strategy and activity handling disposition.

Learning does not own the Constraint rule itself and MUST NOT reinterpret it.

A Constraint marked `validated later` does not prevent Learning completion solely because satisfaction has not yet been measured, unless the Learning contract specifically requires that validation for the reusable-state result.

Conversely, if a required Constraint is declared necessary for valid Learning and remains unsupported/unresolved, the Learning cannot silently proceed as though the requirement were satisfied.

The exact effect of Constraint handling on Generation completion remains Phase 002-D work.

## Semantic completion

Learning reaches `completed` only when all of the following are true:

1. the committed learning specification was realized sufficiently for the Strategy's declared learning semantics;
2. no unresolved failure makes the intended reusable result invalid;
3. the result is distinguishable from incomplete/checkpoint state;
4. a stable logical Learned State identity can be established;
5. required result metadata/compatibility/dependency facts are available enough for future validation and provenance;
6. required provenance relationships can be recorded according to the traceability contract.

Operational process success alone is insufficient.

If the Strategy produces no reusable state by design, there should be no Learning occurrence rather than a `completed` Learning with an empty fake result.

## Failure and cancellation semantics

Learning failure includes at least:

- semantic prerequisites become invalid before commitment;
- committed Strategy/dependency requirements cannot be realized;
- repeated/recoverable operational failure is exhausted or declared terminal;
- output cannot be distinguished as valid reusable state;
- required source/meaning/constraint bindings cannot be honored;
- required external artifact becomes unavailable/incompatible and no explicit compatible alternative is bound;
- post-run semantic/result validation fails;
- provenance consistency required for completion cannot be established.

Failure does not erase Attempt history or intermediate diagnostics.

Cancellation terminates the Learning occurrence without establishing usable Learned State unless the contract had already reached semantic completion before cancellation was accepted.

## Learning result cardinality

Under the current concept model, one Learning produces **zero or one primary Learned State**.

The physical representation of that Learned State may contain many files, partitions, tensors, tables, statistics, or components.

If a future Strategy naturally produces multiple independently reusable results with separate lifecycle/compatibility purposes, that is a signal for later concept/cardinality review rather than a reason to hide several logical learned states inside one arbitrary artifact container.

## Scale semantics

Learning is enterprise-scale domain activity, not driver-local training semantics.

A valid Learning design MUST NOT require the complete source corpus to be materialized in driver/local memory as an unavoidable condition of ordinary large-scale use.

Learning may involve large distributed compute and corpus-growing transient state, but its canonical control-plane specification/lifecycle SHOULD remain bounded by activity/configuration/state references rather than source row count.

A Strategy whose learning algorithm has a scale cliff must expose that limitation rather than relying on Spark invocation as evidence of scalability.

## Privacy and sensitivity boundary

Learning may derive state that retains information from sensitive source data.

Neither successful Learning nor production of Learned State establishes a privacy guarantee.

Learning MUST preserve enough information for later privacy/disclosure-risk Evaluation and governance to assess the result appropriately; it MUST NOT label learned state safe for release merely because it is not a row-for-row source copy.

## Actions

### Propose / define

Assemble a candidate Learning specification before commitment.

### Validate prerequisites

Assess semantic, Strategy, Constraint, dependency, source, and deployment requirements.

### Commit

Freeze/bind the material semantic context for one Learning occurrence.

### Initiate operational realization

Associate/request Execution where operational work is needed.

### Observe

Inspect Learning-level status/outcome while following Execution for detailed operational state.

### Cancel

Request termination when permitted without rewriting prior committed context.

### Fail

Enter terminal semantic failure when the committed Learning cannot validly establish its intended result.

### Complete

Confirm semantic result validity and establish/associate the primary Learned State.

## Invariants

1. Learning completion MUST mean reusable source-informed state was validly derived under the committed Strategy semantics.
2. Execution completion alone MUST NOT establish Learning completion.
3. Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.
4. Strategies requiring no reusable source-derived state MUST NOT be forced through no-op Learning.
5. Learning MUST bind stable source identity sufficient to distinguish material source changes for historical interpretation.
6. Data Meaning, Strategy/configuration, applicable Constraint revisions, material sampling/approximation semantics, and dependency profile MUST be historically bound at semantic commitment where material.
7. Material specification changes after commitment MUST NOT silently mutate the committed Learning.
8. A retry/resume Attempt MUST NOT silently change committed Learning semantics.
9. Intermediate/checkpoint state MUST NOT be treated as Learned State solely because it is durable.
10. One Learning produces zero or one primary Learned State under the current concept model.
11. Learning MUST NOT require unavoidable full-corpus driver/local materialization for ordinary enterprise-scale use.
12. Material approximation/sampling semantics MUST remain inspectable when they affect interpretation or reproducibility.
13. A no-network/no-egress Learning MUST NOT silently acquire artifacts or invoke remote services.
14. Learning MUST NOT imply that resulting Learned State is private or safe for release.
15. Learning remains distinct from model-specific `fit`/`train` APIs and from generic Execution.

## Operational principle

A practitioner proposes Learning for a 300-million-row enterprise dataset using an accepted Data Meaning revision, required Constraints, and a locally trained neural Strategy. The Strategy can learn through distributed computation without outbound network access. The Learning binds the source version, meaning, Strategy configuration, Constraint handling, sampling policy, dependency profile, and reproducibility-relevant state before commitment.

Its first Execution Attempt fails after several hours but leaves a checkpoint. A later Attempt resumes the same committed Learning. The checkpoint is recovery material, not yet Learned State. The second Attempt completes operationally; Learning then validates that the intended reusable result is complete and establishes one logical Learned State whose physical representation may be distributed across many files/partitions. Weeks later, Generations can reuse that Learned State independently of the original compute environment.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-01 — Data Meaning revision binding](../synchronizations/core-synchronizations.md#sync-01--data-meaning-revision-binding)
- [SYNC-02 — Strategy selection and compatibility](../synchronizations/core-synchronizations.md#sync-02--strategy-selection-and-compatibility)
- [SYNC-03 — Constraint binding and handling disposition](../synchronizations/core-synchronizations.md#sync-03--constraint-binding-and-handling-disposition)
- [SYNC-04 — Learning operational realization](../synchronizations/core-synchronizations.md#sync-04--learning-operational-realization)
- [SYNC-05 — Learning produces Learned State](../synchronizations/core-synchronizations.md#sync-05--learning-produces-learned-state)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-C does not decide:

- public `fit`/`train` API names;
- Spark ML Estimator mapping;
- PyTorch/TorchDistributor architecture;
- checkpoint/storage format;
- source fingerprint/version implementation;
- execution scheduler/job mapping;
- distributed training algorithm;
- model serialization format;
- exact retry policy;
- user authorization model.

Those representations must preserve this Learning contract rather than redefine it.