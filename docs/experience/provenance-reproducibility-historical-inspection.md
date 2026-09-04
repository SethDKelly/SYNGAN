---
type: Experience Specification
title: Provenance, Reproducibility & Historical Inspection Experience
status: active
---

# Provenance, Reproducibility & Historical Inspection Experience

## Purpose

Define how human and programmatic actors inspect, traverse, explain, compare, and assess historical SYNGAN work using [Provenance](../concepts/provenance.md) and the [Reproducibility Contract](../authority/reproducibility-contract.md) without turning Provenance into a copied metadata warehouse or Reproducibility into a standalone state-owning concept.

This experience does not introduce standalone `Lineage`, `History`, `Run Comparison`, `Reproduction`, `Reproducibility Status`, `Manifest`, `Snapshot`, `Metadata Graph`, or `Artifact` concepts.

## Primary experience principle

> **An actor should be able to determine what happened historically, which exact states and dependencies participated, what has changed since, and what level of reproduction or comparison is supportable now—without confusing historical truth, current applicability, and current reproducibility.**

The experience preserves:

```text
canonical concepts own substantive truth
            ↓
Provenance owns typed historical relationships
            ↓
Reproducibility Contract assembles a current claim
            ↓
actor understands what can be reproduced and why
```

Provenance is not the master copy of canonical state, and a reproduction assessment does not rewrite historical bindings.

## Entry modes

Actors may begin historical inspection from:

- a completed synthetic output;
- a candidate/failed/quarantined Generation when investigation is needed;
- a Learned State;
- a Learning, Generation, or Evaluation;
- an Evidence finding;
- an Execution or Attempt history;
- a source snapshot/reference;
- a Strategy/configuration revision;
- a dependency/base/pretrained artifact;
- a historical comparison between two outputs, Learned States, Evaluations, or activities;
- a request to determine whether a historical target can be reproduced now.

Historical inspection MUST NOT require the actor to know the physical storage layout of the underlying source, Learned State, output, or Evidence.

## Three primary historical views

### Explain this result

Starting from a result or finding, the actor should be able to traverse the material path that explains how it came to exist.

For a completed output this may include:

```text
Output O42
  ← produced by Generation G42
  ← bound Strategy/config C9
  ← used Learned State LS17
      ← produced by Learning L12
      ← source snapshot S8
      ← Data Meaning DM4
      ← applicable Constraints C1/C2
  ← Generation Conditions K1/K2
  ← completion Evidence E31/E32/E33
  ← material Execution/Attempt recovery facts
  ← local/base dependencies
```

The experience should progressively disclose this path rather than displaying the entire provenance graph by default.

### Compare two historical paths

Actors should be able to compare two derivations while preserving exact differences in material bindings.

For example:

```text
Output O41                    Output O42
Generation G41               Generation G42
Strategy/config C8           Strategy/config C9
Learned State LS16           Learned State LS17
Source S7                     Source S8
Data Meaning DM4             Data Meaning DM4
Constraint C2 v2             Constraint C2 v3
Base artifact B2             Base artifact B3
Attempt recovery: none       Attempt recovery: checkpoint R1
```

The experience should identify which differences are known to be semantic, operational, dependency-related, or merely representational when that classification is available.

A historical difference does not automatically imply causal explanation or superiority. Evaluation/Evidence is required for claims such as "O42 is better because Strategy C9 changed."

### Assess reproducibility now

Actors should be able to ask what reproduction class is currently supportable for a specific historical target.

The assessment should identify:

- reproduction target;
- preserved historical conditions;
- required dependencies;
- relevant nondeterminism/randomness;
- approximation semantics;
- material Execution/recovery facts where behaviorally relevant;
- missing or mutable context;
- supported equivalence class;
- reasons stronger classes are not supportable.

The experience MUST NOT reduce this to a permanent `reproducible=true/false` field.

## Historical truth versus current state

### Historical bindings remain historical

Opening old work should show the exact state it actually used, even if newer revisions now exist.

For example:

```text
Learning L12 historically used:
- Source S8
- Data Meaning DM4
- Strategy v2 / config C9
- Base artifact B3

Current state:
- source alias now resolves to S12
- Data Meaning current revision is DM6
- Strategy v2 retired
- B3 no longer available
```

The current state may affect future use or reproducibility, but it MUST NOT replace the historical bindings in the inspection view.

### Current lifecycle/applicability remains separate

Historical inspection should distinguish original facts from current statuses such as:

- Learned State now restricted/retired/invalidated;
- Evidence now stale/superseded/inapplicable/invalidated;
- Strategy revision now retired;
- dependency currently unavailable;
- current network/no-egress policy differs;
- source alias now points elsewhere.

A current warning should not visually imply that the original historical record has been rewritten.

## Typed relationship experience

Provenance traversal should preserve relationship meaning rather than showing undifferentiated graph edges.

Actors should be able to distinguish relationships equivalent to:

- bound / governed by;
- derived from / produced by;
- used / depended on;
- evaluated / referenced;
- operationally realized by;
- recovered / resumed from;
- superseded / restricted / retired / invalidated context.

For example, `Generation G42 used Learned State LS17` is semantically different from `Learning L12 produced Learned State LS17`.

A generic `related to` view is insufficient where relationship meaning matters to interpretation.

## Stable identity experience

### Mutable aliases need historical context

When a human-friendly mutable locator is shown, the experience should also expose the historically distinguishing identity used by the committed activity where material.

Example:

```text
Friendly locator:
analytics.customer

Historical identity:
source snapshot/version S8

Current alias target:
S12
```

The same applies to mutable model aliases, URLs, service names, catalog names, or runtime labels.

### Identity strength limitations remain visible

If historical identity is weak or ambiguous, the experience should say so.

For example:

```text
Remote service:
Model API X

Historical endpoint:
api.example.com/model/latest

Stable model/behavior version:
unavailable

Effect:
exact/semantic reproduction may be unsupported
```

The system must not pretend a mutable endpoint is stable historical identity.

## Provenance completeness and gaps

### Required relationships should be inspectable

Where a domain transition required Provenance, actors should be able to determine whether the required historical path is complete enough for the intended explanation.

Examples include:

- Learning → Learned State;
- Generation → completed output;
- Evaluation → Evidence;
- Evidence used by Generation completion.

### Missing context must remain explicit

Historical inspection may reveal:

- missing source version identity;
- lost local/base artifact;
- unknown software/runtime version;
- missing material Attempt/recovery record;
- unresolved provenance correction;
- remote behavior identity unavailable;
- incomplete reference/baseline identity.

Such gaps should be shown as historical/reproducibility limitations rather than silently filled using current state.

The current source alias, latest Strategy version, or newest dependency MUST NOT be substituted merely because the historical identity is unavailable.

## Provenance correction experience

When a provenance assertion is later corrected, the experience should preserve both:

- the corrected/current assertion used for present interpretation; and
- the existence of the earlier assertion where auditability requires it.

For example:

```text
Current provenance assertion:
Generation G42 used base artifact B3

Correction history:
Earlier record stated B2
Corrected after manifest reconciliation
```

A provenance correction does not automatically mutate the underlying Generation, Learning, Evidence, or other concept history.

## Reproducibility assessment experience

### Target must be explicit

The actor must be able to see what is being reproduced:

- Learning derivation;
- Learned State;
- Generation result;
- Evaluation;
- Evidence finding;
- historical comparison.

One workflow may support different reproduction strengths for different targets.

For example, Generation output may support only statistical reproduction while its Evaluation finding is comparatively reproducible against the retained historical reference.

### Supported reproduction classes

The experience should preserve the accepted distinctions:

- **exact deterministic**;
- **semantic**;
- **statistical**;
- **bounded / approximate**;
- **comparative**;
- **not reproducible / insufficient context**.

A future UI may use friendlier labels, but it must not collapse these into one Boolean.

### Assessment explanation

A reproduction assessment should explain why a class is supported.

Example:

```text
Target:
Generation G42 / Output O42

Supported class:
statistical reproduction

Preserved:
✓ source snapshot S8
✓ Data Meaning DM4
✓ Strategy/config C9
✓ Learned State LS17
✓ Conditions and Constraints
✓ base artifact B3 content identity
✓ RNG family and seed policy

Limits:
! GPU kernels are nondeterministic
! distributed update ordering not fixed

Not supported:
exact deterministic reproduction
```

The experience should not require actors to infer the class from raw provenance details manually.

### Seed visibility without determinism inflation

When seeds exist, they may be shown as relevant context, but the experience MUST NOT translate `seed recorded` into `exactly reproducible` unless the complete contract supports that claim.

Material nondeterminism such as worker seed derivation, asynchronous ordering, accelerator kernels, or distributed reduction ordering should remain visible where it constrains the claim.

## Reproduction readiness versus actual reproduction

Historical inspection may assess that sufficient context appears available to attempt a reproduction.

That does not mean the reproduction has already succeeded.

The experience should distinguish:

```text
historical context appears sufficient to attempt statistical reproduction
```

from:

```text
new reproduction activity completed and satisfied the statistical equivalence Criterion
```

An actual reproduction attempt is new Learning/Generation/Evaluation work as appropriate; it does not mutate the historical target.

`Reproduction readiness` remains a derived experience assessment, not a concept.

## Re-execution versus reproduction

The experience should explicitly prevent confusion between rerunning a job and reproducing a historical target.

Example:

```text
Re-execution available:
yes

Historical source preserved:
no — alias now resolves to different data

Reproduction assessment:
insufficient context
```

Likewise, rerunning with the same seed, model family, or endpoint is not proof of reproduction unless the declared equivalence contract is satisfied.

## Dependency loss and reproducibility degradation

A historical result can remain well explained even when it can no longer be reproduced today.

Example:

```text
Historical dependency:
base artifact B3

Historical identity:
recorded and unambiguous

Current availability:
unavailable

Historical provenance:
complete

Current reproducibility:
insufficient context / dependency unavailable
```

The experience should present this as degradation of **current reproduction capability**, not corruption of historical truth.

## Comparison experience

### Difference view

When comparing two historical targets, the experience should organize differences by material category where possible:

- source/input identity;
- Data Meaning;
- Constraint revisions/handling;
- Strategy/configuration;
- Learning/sampling/approximation;
- Learned State;
- Generation Conditions/quantity/scope;
- Evaluation Criteria/methods;
- dependencies/base artifacts;
- software/runtime;
- Execution/Attempt/recovery facts;
- Evidence;
- lifecycle/current-use status.

### Same-looking identifiers require historical resolution

If two activities reference the same mutable alias, the comparison should resolve whether the underlying historical state was actually the same.

For example:

```text
G41 source alias: analytics.customer
G42 source alias: analytics.customer

Historical source:
G41 -> S7
G42 -> S8

Result:
source changed
```

### Difference does not equal causality

The comparison experience must not assert causal explanations merely because a difference is present.

If the actor needs to know whether a Strategy revision caused better utility, that question belongs to explicit Evaluation Criteria and Evidence.

## Evidence and historical review

Historical inspection may traverse from Evidence back through:

- exact Criterion revision;
- Evaluation;
- subject;
- reference/baseline;
- method/configuration;
- coverage/sampling/uncertainty;
- Execution/Attempts where material.

It should also expose current Evidence applicability separately from the original finding.

Evidence that was used in Generation completion should make that exact relationship visible without implying that all later Evidence was part of the original promotion decision.

## Execution history materiality

When operational history is relevant, the actor should be able to inspect material Attempts, recovery, cancellation, unknown-state reconciliation, runtime/dependency changes, and platform references.

The experience should not expand by default into every Spark task, log line, executor metric, or platform event.

A user can drill into platform-native observability when investigation requires lower-level detail.

## Privacy and access boundary

Provenance can reveal sensitive dataset names, model identities, infrastructure details, dependency information, or historical relationships.

The experience therefore must not assume that every actor can see every provenance field simply because traceability exists.

003-H will deepen access, disclosure, sensitive diagnostic, dependency-trust, and no-egress experience.

Until then, 003-G establishes only that access controls/redaction MUST NOT falsify the underlying historical relationship. A restricted actor may see that detail is withheld rather than receive a fabricated substitute.

## Actor-specific historical inspection

### Data Practitioner

Emphasize derivation path, exact bound semantics, changes between outputs/states, Evidence context, and reproduction feasibility.

### Platform Operator

Emphasize material Execution/Attempt/recovery/runtime history while retaining the parent semantic path and avoiding full telemetry duplication.

### Data Owner / Steward

Emphasize source identity, Data Meaning, Constraints, historical revisions, provenance corrections, and current versus historical status.

### Privacy / Risk / Governance Reviewer

Emphasize dependency/egress history, Evidence/threat-model lineage, current applicability, reproducibility limitations, and disclosure-sensitive provenance boundaries.

### Synthetic Data Consumer

Emphasize how the completed output was produced, what semantics/Evidence apply, important current limitations, and relevant reproducibility information without requiring training/runtime internals by default.

## Programmatic parity

A future SDK/CLI/API should allow programmatic users to:

- obtain the material provenance path for a target;
- traverse typed relationships;
- distinguish historical identities from current aliases/state;
- identify provenance gaps/corrections;
- compare two historical derivations;
- inspect exact material differences;
- request a reproducibility assessment for a target;
- inspect supported class, preserved conditions, missing dependencies, and limitations;
- distinguish reproduction readiness from a completed reproduction attempt;
- inspect current applicability/status without rewriting historical facts;
- follow selected platform/dependency references where authorized.

A raw graph dump, dictionary of IDs, or Boolean `reproducible` value alone is not an adequate historical interface.

## Enterprise-scale historical inspection

Historical inspection must remain practical when source/output data contain hundreds of millions of rows, Learned State is distributed, and Execution emitted millions of low-level events.

Canonical inspection should rely on:

- stable concept/result references;
- typed provenance relationships;
- revisions/snapshots/fingerprints/manifests where later architecture supplies them;
- bounded Execution/Attempt summaries;
- dependency identities;
- Evidence summaries;
- selected platform references.

The experience MUST NOT require loading complete source data, synthetic output, Learned State payloads, detailed violation datasets, or all platform telemetry into driver/UI memory merely to explain history or assess reproducibility.

## Next-action guidance

Derived next actions may include:

```text
Historical dependency missing
  → mark current reproduction class as limited/insufficient
  → locate approved historical artifact if available

Mutable alias resolves differently
  → use preserved historical identity for inspection
  → do not substitute current contents

Reproducibility class statistical
  → define a new reproduction attempt and explicit statistical comparison Criterion

Provenance gap discovered
  → investigate/correct provenance assertion if evidence supports correction

Two outputs differ materially
  → inspect categorized derivation differences
  → define Evaluation if causal/quality interpretation is required
```

Guidance remains derived experience behavior rather than a new History/Reproduction workflow authority.

## Experience invariants

1. Provenance MUST remain typed historical relationship authority rather than copied canonical concept state.
2. Historical inspection MUST show the state actually used rather than substituting current revisions/aliases.
3. Current lifecycle/applicability/restriction state MUST remain distinguishable from historical bindings.
4. Mutable aliases alone MUST NOT be presented as sufficient historical identity when underlying state can change materially.
5. Missing/weak historical identity MUST remain explicit rather than being repaired by current-state substitution.
6. Provenance relationship meanings MUST remain distinguishable where material.
7. Provenance corrections MUST preserve auditability and MUST NOT silently rewrite another concept's historical authority.
8. Lineage MUST remain a derivational subset of broader Provenance.
9. Reproducibility MUST remain a cross-cutting assessment/contract rather than a standalone state-owning concept.
10. Reproduction assessment MUST identify target, preserved conditions, and equivalence class.
11. Exact deterministic reproduction MUST NOT be inferred from seed presence alone.
12. Supported reproduction strength MUST NOT exceed unresolved dependency/nondeterminism/identity limitations.
13. `not reproducible / insufficient context` MUST remain a legitimate explicit outcome.
14. Re-execution MUST remain distinguishable from successful reproduction.
15. Reproduction readiness MUST remain distinguishable from an actually completed reproduction attempt.
16. Loss of current dependencies may weaken current reproducibility without rewriting historical provenance.
17. Historical comparison MUST preserve exact revisions/identities and MUST NOT infer causality merely from difference.
18. Evidence used historically for Generation completion MUST remain distinguishable from later Evidence.
19. Material Execution/Attempt history MAY be traversed without copying all platform telemetry.
20. Restricted provenance disclosure MUST indicate withheld detail rather than fabricate alternative history.
21. Programmatic and human-facing inspection MUST preserve equivalent historical/reproducibility distinctions.
22. Ordinary enterprise historical inspection MUST NOT require full payload/log collection to driver-local memory.
23. Experience convenience MUST NOT create generic Lineage, History, Metadata Graph, Reproducibility Status, Run Comparison, Manifest, Snapshot, or Artifact god-concepts.
24. No historical-inspection rule may impose a permanent single-table assumption.

## Representation questions intentionally deferred

003-G does not decide:

- graph database versus relational/event/table provenance storage;
- provenance query language/API shape;
- visualization technology;
- source snapshot/version implementation;
- fingerprint/hash/manifest/content-addressing mechanism;
- OpenLineage/MLflow/catalog integration;
- reproduction orchestration API;
- exact comparison/diff UI;
- provenance retention implementation;
- access-control/redaction implementation;
- software-environment capture technology;
- model/dependency registry technology.

Later architecture must preserve typed references, historical immutability, current-versus-historical distinction, honest reproduction classes, explicit context gaps, and bounded enterprise-scale traversal.