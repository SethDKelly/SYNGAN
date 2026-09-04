---
type: Experience Specification
title: Learning & Learned State Lifecycle Experience
status: active
---

# Learning & Learned State Lifecycle Experience

## Purpose

Define how human and programmatic actors commit, observe, recover, complete, inspect, reuse, compare, restrict, retire, and invalidate [Learning](../concepts/learning.md) and [Learned State](../concepts/learned-state.md) while preserving the distinction between semantic derivation, operational [Execution](../concepts/execution.md), recovery material, and durable reusable state.

This experience does not introduce a standalone `Training Session`, `Model`, `Model Registry`, `Checkpoint`, `Fit Result`, or `Artifact` concept.

## Primary experience principle

> **An actor should always be able to tell whether reusable state is merely being derived, recoverable intermediate material exists, semantic Learning has actually completed, and a durable Learned State is validly established for future use.**

Physical files, checkpoints, successful platform jobs, or a completed optimizer loop are not enough by themselves to establish Learned State.

## Applicability and entry

The Learning experience exists only when the selected [Synthesis Strategy](../concepts/synthesis-strategy.md) requires or intentionally supports reusable source-derived state.

Strategies that generate directly without Learned State should bypass this lifecycle rather than showing a fake `training skipped/completed` stage.

Actors may enter the Learning/Learned State lifecycle from:

- a 003-B preparation context ready for Learning commitment;
- an existing proposed/validated Learning;
- an active committed Learning;
- a failed/recoverable Execution Attempt;
- a completed Learning whose Learned State must be inspected;
- an existing Learned State selected for later Generation;
- a historical Learned State requiring comparison, restriction, retirement, or invalidation review.

## Learning pre-commit review

Before semantic commitment, the experience should summarize the material facts that will become historical if Learning is committed.

A review should make inspectable, where applicable:

- stable source identity/version/snapshot/fingerprint basis;
- Data Meaning revision;
- Strategy revision/configuration;
- applicable Constraint revisions and Learning handling dispositions;
- learning scope;
- sampling, filtering, weighting, approximation, or summarization semantics;
- material Strategy-specific parameters;
- local/base/pretrained artifact identities;
- dependency/network/no-egress posture;
- resource prerequisites known to be commitment-relevant;
- randomness/reproducibility intent;
- expected Learned State result semantics;
- explicit limitations accepted at commitment.

This review should build on 003-B readiness rather than duplicate authority.

### Commitment consequence

The experience MUST make clear that committing Learning freezes these material semantics historically.

After commitment:

- a retry may change operational realization but not the committed Learning semantics;
- a materially different source, Strategy configuration, Constraint set, sampling design, dependency, or semantic revision requires a new distinguishable Learning;
- a current source/table alias must not silently replace the historical source identity.

The commitment action may later be represented by a method, command, form submission, or orchestration step, but the semantic consequence must remain inspectable.

## Learning lifecycle orientation

The experience should preserve Learning states equivalent to:

```text
proposed
   ↓
validated / ready
   ↓
committed
   ↓
active / being realized
   ↓
┌───────────────┬──────────────┬──────────────┐
│               │              │              │
completed      failed        cancelled      recovery/attempt activity
   │
   ▼
Learned State established
```

This diagram is an orientation aid, not a required universal enum or platform state machine.

### Semantic state versus operational state

The Learning view MUST keep semantic and operational status distinct.

Examples:

```text
Learning: active
Execution: running
Latest Attempt: active
Checkpoint: available
```

```text
Learning: active
Execution: recovery pending
Latest Attempt: failed, recoverable
Checkpoint: available and candidate for resume
```

```text
Learning: validating result for semantic completion
Execution: completed
Latest Attempt: succeeded
Learned State: not established yet
```

```text
Learning: completed
Execution: completed
Learned State: LS-17 usable
```

A single generic `training_status = succeeded` is insufficient when it hides these distinctions.

## Progress experience

### Progress should be meaningful, not fabricated

Different Strategies may provide different meaningful progress signals.

The experience MAY expose, where semantically or operationally useful:

- Strategy-defined learning stages;
- epochs/iterations when meaningful to the Strategy;
- processed source partitions/segments;
- sampled scope completed;
- checkpoint creation;
- elapsed time;
- current Attempt;
- resource/worker status;
- diagnostics/losses/fit indicators with correct interpretation;
- outstanding post-run semantic checks.

The experience MUST NOT imply that all Learning has a meaningful universal percentage-complete measure.

For example, `73% complete` should not be derived merely from elapsed time, epoch count, or processed partitions unless the Strategy contract actually makes that measure interpretable.

### Metrics are not completion authority

Training loss, convergence metrics, elapsed time, checkpoint count, or resource utilization MAY inform an actor, but none independently establishes Learning semantic completion.

A Strategy-specific stopping criterion may participate in Learning semantics when explicitly committed; the experience should expose that relationship rather than converting every metric into a generic success score.

## Execution and Attempt drill-down

Learning should present a concise semantic view by default while allowing drill-down into Execution when operational detail is needed.

The actor should be able to inspect:

- logical Execution identity;
- current/latest Attempt;
- recoverable versus terminal operational failure;
- cancellation state;
- checkpoint/recovery basis;
- relevant platform job/run references;
- material resource/runtime incidents.

The Learning view should not copy all Spark/Databricks/Kubernetes/PyTorch task telemetry into canonical SYNGAN state.

003-F will deepen monitoring/recovery presentation.

## Checkpoint and intermediate-material experience

### Recovery material must remain visibly non-final

The experience MUST distinguish intermediate/recovery material from Learned State.

Possible labels may vary, but an actor must be able to see distinctions equivalent to:

```text
Checkpoint / recovery material
- exists
- created by Attempt A2
- may support resume
- NOT a Learned State
- NOT available for ordinary Generation use
```

A checkpoint cannot appear in normal Learned State selection merely because it is durable.

### Resume qualification

When a checkpoint is eligible for resume consideration, the experience should expose whether its committed-context compatibility has been established, is pending, failed, or indeterminate.

A checkpoint from another Learning, another Strategy configuration, another materially different source context, or otherwise incompatible activity must not be presented as safely resumable by default.

### Intermediate material after failure/cancellation

Failed or cancelled Learning may leave useful diagnostics or recovery material.

The experience should make retained material clearly non-authoritative and support later cleanup/retention policy without implying deletion is required immediately.

Retention/storage controls are representation/governance concerns and remain deferred.

## Learning completion and Learned State promotion

### Promotion barrier

The experience should make the transition from Learning to Learned State explicit:

```text
Execution/Attempts produce physical/intermediate material
                    ↓
Learning verifies semantic completion requirements
                    ↓
SYNC-05 promotion
                    ↓
Learned State logical identity established
```

There may be little or no physical copying at promotion time; the important distinction is semantic authority.

### Completion review

Before or at completion, the experience should be able to show whether:

- committed Learning semantics were actually realized;
- no terminal semantic defect invalidates the result;
- output is distinguishable from checkpoints/incomplete state;
- required Learned State identity/components are resolvable;
- material compatibility/dependency facts are available;
- required Provenance can be recorded consistently;
- restrictions/limitations known at establishment are visible.

Operational success alone does not satisfy this review.

### Failed semantic completion after operational success

If Execution succeeds but Learning cannot establish a valid reusable result, the experience should say so directly.

For example:

```text
Execution: completed successfully
Learning: failed semantic completion
Reason: required learned component missing/inconsistent
Learned State: not established
```

This must not be presented as a successful trained model with a warning.

## Learned State inspection experience

A Learned State should be inspectable as one logical reusable result even when its physical representation is distributed/composite.

A normal inspection surface should make available, progressively rather than all at once:

- logical identity/version;
- current future-use status: usable/restricted/retired/invalidated;
- producing Learning identity;
- Strategy/configuration identity;
- source and Data Meaning provenance references;
- relevant Constraint/sampling/approximation context;
- required local/base/pretrained dependencies;
- whether the state is self-contained for Generation or dependency-bound;
- known intrinsic limitations/restrictions;
- reproducibility characteristics/availability;
- sensitivity/privacy warning posture;
- physical component references only to the depth useful for operation/diagnosis.

The experience should not require users to understand raw serialization layout merely to identify or reuse the logical Learned State.

## Learned State usability and status

### Usable

`usable` means eligible for contextual Generation validation. It does not mean compatible with every Generation.

### Restricted

The experience should show:

- the restriction itself;
- why it exists when known;
- any scope/conditions for permitted future use;
- when/who/what authority established the restriction where applicable;
- historical uses unaffected by the new restriction.

A restricted Learned State may still be selectable only where the proposed Generation can satisfy the restriction and policy allows the use.

### Retired

Retirement should normally remove the state from preferred/default new selection while keeping it discoverable historically.

The experience should distinguish retirement from invalidation:

```text
retired = no longer preferred/ordinarily selected
invalidated = known unsuitable for new reliance
```

Historical Generations continue to reference the retired state they actually used.

### Invalidated

Invalidation should be visually/programmatically strong enough that normal future Generation cannot accidentally treat the state as usable.

The experience should expose the reason/material defect where available and should not imply that historical Generations are retroactively rewritten.

## Learned State reuse entry

A practitioner may begin new Generation from Learned State rather than from source preparation.

The reuse entry should expose enough information before Generation preparation to answer:

- is the state currently usable/restricted/retired/invalidated?;
- what Strategy/configuration family produced it?;
- what source/Data Meaning context informed it?;
- what required local/base artifacts must still be present?;
- what intrinsic limitations are known?;
- is there a no-egress/network dependency issue?;
- what current changes may require compatibility reevaluation?;

The experience should then hand off contextual reuse validation to Generation rather than displaying a permanent global `compatible=true` state on Learned State.

003-D will deepen Generation compatibility and request experience.

## Historical versus current status

Opening an old Learned State should distinguish:

- what was true when it was established;
- its original producing context;
- its current future-use status;
- current dependency availability;
- current compatibility/reproducibility assessment where available.

For example:

```text
Established: usable under Strategy v2 + base artifact B3
Current status: restricted
Current issue: B3 security advisory / replacement required
Historical Generations: unchanged
```

Current restrictions do not rewrite original history.

## Learned State comparison

Actors may compare Learned States to understand materially relevant differences without inventing a universal `best model` ranking.

Useful comparison dimensions may include:

- producing source revision;
- Data Meaning revision;
- Strategy/configuration;
- Constraints/learning handling;
- sampling/approximation;
- dependency/base artifacts;
- reproducibility class/limitations;
- lifecycle status/restrictions;
- relevant Evaluation/Evidence when available;
- production time/resource characteristics when decision-relevant.

Comparing two states does not establish equivalence or superiority automatically.

Later Evaluation experience may supply Evidence for specific comparison questions.

## Restrict, retire, and invalidate actions

These lifecycle actions should be consequential and reviewable because they affect future selection.

The experience should preserve:

- target Learned State identity;
- action type;
- reason/context;
- effective future-use impact;
- provenance/audit record where required;
- distinction between future-use change and historical truth.

The experience MUST NOT use destructive editing of the producing Learning to represent these changes.

## Learned State sensitivity experience

Because Learned State is source-derived, the experience should avoid visual or programmatic cues that imply it is automatically safe to export/share.

Where relevant, actors should be able to understand that Learned State may:

- memorize source information;
- contain source-derived distributions/encodings;
- depend on sensitive local artifacts;
- require separate privacy/disclosure-risk Evaluation;
- be subject to access/egress restrictions distinct from generated output.

A label such as `synthetic model` or `trained model` MUST NOT imply anonymity or release approval.

003-H will deepen enterprise safety/access/egress experience.

## Dependency and offline/no-egress behavior

For active Learning and Learned State inspection/reuse, the experience should keep visible material external dependency facts established under the Network and External Dependency Policy.

In particular:

- a missing required artifact must be reported explicitly;
- a no-network Learning cannot silently acquire missing artifacts;
- a Learned State dependent on a base artifact must not appear self-contained;
- remote/network requirements must remain visible on later reuse;
- artifact/version substitution must not appear as the same historical context when materially different.

## Actor-specific views

### Data Practitioner

Emphasize commitment summary, semantic progress, Execution recovery status, checkpoint availability, completion/promotion, Learned State identity/status, reuse readiness inputs, and next legitimate action.

### Platform Operator

Emphasize Execution/Attempt/resource/recovery detail while retaining Learning identity and semantic state. Operational fixes must not silently change Learning semantics.

### Data Owner / Steward

Emphasize source/Data Meaning/Constraint lineage of the Learned State and later restriction/invalidation consequences.

### Privacy / Risk / Governance Reviewer

Emphasize source-derived sensitivity, dependencies/egress, Provenance, current restrictions, and relevant Evidence without treating Learned State existence as release approval.

### Synthetic Data Consumer

Typically should encounter Learned State only when relevant to provenance/reproducibility or production context, not be forced to understand training internals to use completed synthetic output.

## Programmatic parity

A later SDK/CLI/notebook surface should support inspection of the same distinctions without requiring log parsing or implementation-specific object introspection.

Programmatic users should be able to determine:

- Learning semantic state;
- committed specification identity/references;
- associated Execution and latest Attempt summary;
- checkpoint/intermediate availability and non-final status;
- whether Learned State has actually been established;
- Learned State logical identity/components/dependencies;
- usable/restricted/retired/invalidated status;
- intrinsic restrictions/limitations;
- provenance/reproducibility references;
- sensitivity/dependency warnings;
- legitimate next actions.

A returned Python/PyTorch/Spark object alone is not an adequate semantic lifecycle interface.

## Enterprise-scale experience

The Learning/Learned State experience MUST remain usable when:

- source data contains hundreds of millions of rows;
- Learning runs for hours/days;
- Learned State spans many physical components;
- Execution contains multiple Attempts;
- detailed telemetry remains in platform-native systems.

Actor orientation should rely on bounded control-plane state, summaries, stable references, diagnostics, and selected platform links rather than collecting source data, model payloads, or all telemetry into the driver/UI process.

The experience should not require loading the entire Learned State merely to inspect identity/status/history.

## Next-action guidance

Derived next actions may include:

```text
Learning proposed
  → review commitment
  → commit

Learning active + Attempt failed recoverably
  → inspect recovery basis
  → retry/resume

Execution completed + Learning result validation pending
  → inspect semantic completion checks

Learning completed
  → inspect Learned State
  → prepare Generation
  → evaluate Learned State where appropriate

Learned State restricted
  → inspect restriction
  → prepare Generation only if allowed/compatible

Learned State retired
  → prefer newer state / inspect history

Learned State invalidated
  → do not use for new Generation
  → inspect reason / perform new Learning if needed
```

Guidance remains derived experience behavior, not a new workflow authority.

## Experience invariants

1. Learning and Learned State MUST remain distinct in all experience surfaces.
2. Strategies requiring no reusable state MUST NOT be shown a fabricated Learning lifecycle.
3. Learning commitment MUST make material historical bindings reviewable and consequential.
4. Semantic Learning state MUST remain distinguishable from Execution/Attempt/platform state.
5. Progress presentation MUST NOT invent universal percentage/completion semantics unsupported by the Strategy.
6. Checkpoint/intermediate material MUST remain visibly non-final and unavailable as ordinary Learned State until semantic promotion.
7. Execution success MUST NOT be presented as Learned State establishment unless Learning completion succeeds.
8. Failed/cancelled/incomplete Learning MUST NOT expose intermediate material as a usable Learned State.
9. One successful Learning establishes zero or one primary logical Learned State under the current model.
10. Learned State inspection MUST present logical identity independently of physical component count/layout.
11. Usable MUST mean eligible for contextual validation, not globally compatible.
12. Restricted, retired, and invalidated statuses MUST remain semantically distinct.
13. Future-use status changes MUST NOT rewrite producing Learning or historical Generation provenance.
14. Ordinary Learned State reuse MUST NOT mutate/adapt the state invisibly.
15. Contextual compatibility for reuse belongs to Generation, not global Learned State state.
16. Required local/base/pretrained dependencies MUST remain visible; dependent states MUST NOT falsely appear self-contained.
17. Missing dependencies MUST NOT trigger undeclared network acquisition or remote fallback.
18. Learned State MUST NOT be presented as anonymous/private/release-approved merely because it is source-derived.
19. Programmatic and human-facing surfaces MUST preserve equivalent lifecycle/result distinctions.
20. Enterprise-scale inspection MUST NOT require full source, Learned State, or telemetry collection to driver-local memory.
21. No lifecycle experience may imply one file/object is universally identical to Learned State.
22. Experience convenience MUST NOT create a Training Session, Model Registry, Checkpoint, Fit Result, Model, Artifact, or Run god-concept.
23. No experience rule may impose a permanent single-table assumption.

## Representation questions intentionally deferred

003-C does not decide:

- final `fit`/`train` method names;
- notebook/CLI/web lifecycle presentation;
- progress-bar implementation;
- checkpoint storage/selection mechanics;
- model registry technology;
- Learned State manifest/schema;
- Spark ML or PyTorch object mapping;
- distributed state loading architecture;
- retention/garbage-collection policy;
- exact lifecycle API enums;
- authorization for restrict/retire/invalidate actions;
- notification system.

Later representation architecture must preserve the Learning, Execution, checkpoint, promotion, Learned State, reuse, lifecycle-status, and historical distinctions defined here.
