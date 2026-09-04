---
type: Experience Specification
title: Workflow Entry, Source Context & Lifecycle Orientation
status: active
---

# Workflow Entry, Source Context & Lifecycle Orientation

## Purpose

Define how human and programmatic actors enter SYNGAN work, identify the source/result context they are operating against, choose whether they are creating, continuing, inspecting, or comparing work, and remain oriented to the correct semantic lifecycle without confusing domain state with platform execution state.

This experience is intentionally composed from existing concepts. It does not introduce a standalone `Workflow`, `Project`, `Dataset`, `Session`, `Run`, or `Source Context` concept.

## Primary experience principle

> **An actor should know what they are working on, which exact historical state governs it, what remains editable, what has been committed, what result—if any—is authoritative, and what is happening operationally without needing to reconstruct those facts from Spark/platform internals.**

## Entry modes

SYNGAN should support several legitimate entry intents without forcing every user through one linear wizard.

### Start new synthesis work

Typical practitioner entry begins from a source or direct-generation context and proceeds toward Data Meaning/Constraint/Strategy preparation before Learning or Generation commitment.

The experience should make clear:

- what source/current input is being considered;
- whether its historical identity is already stable enough for commitment;
- what semantic preparation is incomplete;
- whether the intended path expects Learning first or can generate directly;
- which dependency/network profile applies.

### Continue prepared but uncommitted work

An actor may return to draft/proposed Learning, Generation, or Evaluation state.

The experience must show that material semantics remain editable and that historical commitment has **not** yet occurred.

### Observe or recover committed work

An actor may enter through an active Learning, Generation, or Evaluation.

The orientation surface should show both:

- the domain activity's semantic state; and
- associated Execution/Attempt operational state where present.

These statuses must not be flattened into one generic `running/succeeded/failed` field.

### Reuse a Learned State

An actor may begin from an existing Learned State rather than a source-preparation flow.

The experience should expose enough intrinsic state to decide whether new Generation is worth preparing, including status/restrictions, producing context, Strategy/dependency requirements, and relevant historical identity without forcing full provenance traversal immediately.

### Evaluate or review an existing subject

An actor may start from completed/candidate synthetic output, Learned State, Evidence, or another evaluable subject.

The experience should make the subject identity and whether it is candidate, completed, retired, invalidated, or otherwise historically qualified explicit before Evaluation is configured.

### Inspect or compare historical work

A reviewer/practitioner may enter through a completed output, Evidence finding, Learned State, Generation, Evaluation, or Execution and navigate backward/forward through Provenance.

The experience should preserve the distinction between historical truth and current usability/reproducibility.

## Workflow orientation view

A workflow-orientation view is an **experience composition**, not a new concept.

Depending on context it may summarize:

- current entry subject/source/result reference;
- exact historical identity where known;
- current mutable alias/location separately from historical identity;
- relevant Data Meaning revision/status;
- applicable Constraint readiness/known issues;
- selected or candidate Synthesis Strategy;
- intended/committed domain activity type and identity;
- semantic lifecycle state;
- associated Learned State/output/Evidence result status;
- associated Execution operational state and latest Attempt summary;
- dependency/network/no-egress posture;
- unresolved blockers, limitations, or indeterminacy;
- provenance/reproducibility availability.

This view MUST reference canonical state rather than become the owner of copied state.

## Source context experience

### Source context is composed, not owned

`Source context` is experience language for the collection of facts needed to understand which source/input state a workflow is considering.

It may include:

- source locator/alias for human usability;
- stable snapshot/version/fingerprint/reference where available;
- structural schema/shape summaries;
- Data Meaning readiness and unresolved semantics;
- relevant Constraints;
- size/scale indicators needed for planning;
- dependency/access availability;
- source-sensitive handling warnings where known;
- provenance references to prior use.

No generic Dataset concept is created by this experience.

### Mutable alias versus historical identity

The experience MUST visibly distinguish:

```text
Current locator: analytics.customer
Historical identity: source snapshot/version/fingerprint used by committed work
```

when those differ or when the locator can mutate.

A mutable alias alone may be sufficient for exploration before commitment, but the experience MUST NOT imply reproducible/historical binding until the source can be distinguished strongly enough for the relevant activity contract.

### Source changes during preparation

Before commitment, a practitioner may refresh/re-resolve a mutable source and update draft preparation.

The experience should surface when that refresh changes material source facts such as:

- schema/shape;
- source identity;
- Data Meaning inference/declarations;
- Constraint applicability;
- Strategy compatibility;
- row-count/scale characteristics.

It MUST NOT silently rewrite a committed Learning, Generation, or Evaluation.

### Large-source orientation

Entry should not require full source collection to the driver merely to orient the actor.

Useful orientation MAY be built from:

- schema/catalog metadata;
- stable source references;
- distributed counts/aggregates;
- bounded profiles/summaries;
- representative diagnostics;
- previously recorded Data Meaning/Provenance.

Any sampled/approximate source characterization must remain labeled as such and must not become hidden semantic authority.

## Lifecycle orientation model

Different domain concepts have different lifecycle details, but the experience should preserve a common orientation pattern where applicable:

```text
editable / proposed
      ↓
validated / ready
      ↓
semantic commitment
      ↓
realization / fulfillment / examination
      ↓
possible pending semantic checks
      ↓
semantic terminal outcome
```

This is an experience orientation, **not** a universal lifecycle enum.

### Editable versus committed

The commitment boundary must be especially visible.

Before commitment:

- material specifications may be amended;
- source/context may be refreshed;
- compatibility may be reevaluated;
- the actor should understand that no immutable historical activity has yet been fixed.

After commitment:

- bound material semantics are historical;
- retry/recovery may continue the same work only under those semantics;
- material changes require a new distinguishable domain activity.

The experience SHOULD make a commitment action consequential and reviewable rather than presenting it as an indistinguishable `run` button.

### Semantic state versus operational state

For committed work, users need two related but separate status channels.

Example:

```text
Generation: awaiting required validation
Execution: completed
Latest Attempt: succeeded
```

or:

```text
Learning: committed / deriving
Execution: recovery pending
Latest Attempt: failed, recoverable
```

The UI/API MAY summarize these together for convenience, but the underlying distinctions MUST remain inspectable.

### Candidate versus authoritative result

The experience MUST distinguish:

- checkpoint/intermediate state from Learned State;
- partial/candidate Generation material from completed output;
- diagnostic Evaluation output from Evidence;
- historical result from current preferred/usable status.

Physical existence or platform success must never make candidate material look authoritative by default.

## Status communication principles

### Prefer semantic labels over generic pass/fail

A status should answer the actor's actual question.

For example:

- `constraint validation pending` is better than generic `processing` when it is the semantic blocker;
- `Execution failed; retry available` is better than `Generation failed` when Generation has not terminally failed;
- `Evidence indeterminate at required claim strength` is better than `validation failed` when the Evaluation itself completed validly.

### Preserve indeterminacy

Unknown, indeterminate, unresolved, or partially known states must remain visible.

The experience MUST NOT automatically map:

```text
unknown → failed
unknown → success
indeterminate Evidence → pass
```

for presentation simplicity.

### Show blockers separately from warnings

Actors should be able to distinguish:

- **blocking requirements** — prevent commitment/completion;
- **permitted limitations** — may allow completion with limitations;
- **informational warnings** — useful but non-binding;
- **operational incidents** — may be recoverable without semantic failure.

This classification is an experience presentation of canonical semantics, not new policy authority.

## Actor-specific orientation

### Data Practitioner

Default orientation should emphasize:

- source/current input;
- semantic preparation readiness;
- chosen synthesis path;
- editable versus committed state;
- semantic blockers;
- result/output status;
- recoverability and next legitimate action.

### Data Owner / Steward

Orientation should emphasize:

- source identity;
- Data Meaning declarations/inference status;
- Constraint authority/revisions;
- which committed work bound those revisions;
- meaningful changes requiring review.

### Platform Operator

Orientation should emphasize Execution health, Attempt history, resources, failure/recovery state, and platform references while retaining the associated domain activity/commitment for context.

The operator view MUST NOT imply operational success equals semantic success.

### Privacy / Risk / Governance Reviewer

Orientation should emphasize:

- exact subject identity;
- relevant Evidence and claim strength;
- Provenance/history;
- dependency/egress posture;
- known limitations;
- current reproducibility status;
- explicit absence of automatic release/privacy authority.

### Synthetic Data Consumer

Orientation around completed output should emphasize:

- completed logical output identity;
- Data Meaning/schema interpretation relevant to use;
- known limitations;
- Evaluation/Evidence appropriate to the intended use;
- provenance/reproducibility availability;
- distinction between completion and organizational approval.

## Programmatic experience parity

Programmatic users need the same semantic distinctions even if they do not see a UI.

A later API should make it possible to inspect, rather than infer from exceptions/log strings:

- editable versus committed state;
- current semantic lifecycle state;
- associated Execution/Attempt state;
- blocker/limitation information;
- stable historical bindings;
- candidate versus completed results;
- dependency/network requirements;
- relevant Evidence/Provenance references.

Convenience methods MAY orchestrate several steps, but they MUST NOT hide a material commitment boundary or silently weaken requirements.

## Navigation and next-action guidance

The experience SHOULD help an actor identify legitimate next actions based on state, for example:

```text
draft Generation
  → resolve Strategy incompatibility
  → review mandatory Conditions
  → commit

committed Generation + failed recoverable Attempt
  → inspect failure
  → retry/resume

candidate output + validation pending
  → inspect required Evaluation
  → await/run validation

completed output
  → evaluate
  → inspect Evidence
  → inspect Provenance/reproducibility
```

Next-action guidance must be derived from canonical lifecycle semantics rather than an independent workflow engine inventing transitions.

## Entry safety and dependency visibility

Before an actor commits work, the orientation experience should expose material dependency posture such as:

- fully local/self-contained;
- locally provisioned artifact dependency;
- acquisition dependency;
- runtime network dependency;
- no-egress policy incompatibility;
- unresolved dependency identity.

A missing dependency MUST NOT result in hidden model acquisition or remote fallback from the entry experience.

003-H will deepen enterprise safety/dependency presentation.

## Historical inspection entry

Entry into historical work should default to the **historical committed context**, not silently substitute current configuration.

For example, opening Generation G4 should show:

- the Strategy/configuration G4 actually used;
- the Data Meaning/Constraints G4 actually bound;
- the Learned State or direct input G4 actually used;
- its Execution/Attempt history;
- its completed/candidate outcome;
- Evidence used for completion where applicable.

The experience MAY separately show current compatibility or newer revisions, but MUST label them as current comparison context rather than historical truth.

## No hidden orchestration semantics

An implementation may later provide a one-call convenience experience such as "synthesize this DataFrame".

If so, the experience contract still requires material hidden steps to be inspectable when they affect meaning, for example:

- inferred Data Meaning relied upon;
- selected/default Strategy;
- generated/selected Constraints;
- whether Learning occurred;
- committed Generation request/Conditions;
- required validation;
- network/dependency use;
- resulting Evidence/Provenance.

Convenience is permitted; invisible semantic authority is not.

## Experience invariants

1. Workflow/source-context views MUST remain compositions over canonical concept state rather than new semantic owners.
2. Actors MUST be able to distinguish editable/pre-commit state from committed historical work.
3. A mutable source alias MUST remain distinguishable from the historical source identity used by committed work.
4. Semantic activity state MUST remain distinguishable from Execution/Attempt/platform state.
5. Candidate/partial/checkpoint/diagnostic material MUST remain distinguishable from authoritative domain results.
6. Indeterminate/unknown/unresolved state MUST remain visible when material.
7. Blocking requirements, permitted limitations, warnings, and operational incidents SHOULD remain distinguishable.
8. Historical inspection MUST default to the state actually bound at commitment rather than current mutable state.
9. Programmatic and human-facing surfaces MUST preserve equivalent semantic distinctions.
10. Entry/orientation MUST NOT require full source/output collection to driver-local memory in the ordinary enterprise path.
11. Dependency/network requirements MUST be inspectable before commitment.
12. Experience convenience MUST NOT silently create a Dataset, Workflow, Run, Validation, Quality, or other god-concept.
13. Experience presentation MUST NOT imply synthetic output is private, approved, or fit for all uses merely because Generation completed.
14. No experience rule may impose a permanent single-table model.

## Representation questions intentionally deferred

003-A does not decide:

- notebook versus CLI versus web UI versus SDK entry surface;
- final Python method names;
- a universal workflow/session object;
- source-reference storage format;
- dashboard/card/layout design;
- notification system;
- authorization implementation;
- orchestration technology;
- persistence/database model.

Later representation architecture must preserve the entry, source-history, lifecycle, and status distinctions defined here.
