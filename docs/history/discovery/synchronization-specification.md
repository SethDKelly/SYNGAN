---
type: Synchronization Specification
title: SYNGAN Candidate Synchronization Specification
status: provisional
---

# SYNGAN Candidate Synchronization Specification

## Purpose

This document refines Phase 001-D synchronization hypotheses using the reduced and operationally validated concept set produced by 001-E and 001-F.

A synchronization is recorded only when a meaningful state transition in one concept requires coordinated interpretation or action in another. Ordinary references, reads, and compatibility checks are not automatically synchronizations.

This remains provisional until Phase 001-H consolidates the accepted concept catalog.

## Synchronization taxonomy

### Type A — Bind

A concept records the exact identity/revision of another concept state it relies upon.

Binding freezes historical meaning without freezing future evolution of the referenced authority.

### Type B — Validate

A concept checks another concept's authoritative state against activity-specific needs.

Validation is contextual and does not mutate the referenced concept.

### Type C — Produce

Successful semantic completion of one concept establishes or associates a durable result owned elsewhere.

### Type D — Realize

A domain activity is operationally realized through Execution while retaining semantic completion authority.

### Type E — Record provenance

A material transition emits a typed derivation/context fact into Provenance.

### Type F — External handoff

SYNGAN exposes state/evidence to an external actor/system without assuming the external authority itself.

## Core synchronizations

## SYNC-01 — Data Meaning revision binding

**Type:** A / E

**Participants:** Data Meaning → Learning, Generation, Evaluation, Provenance

### Trigger

A Learning, Generation, or Evaluation crosses its semantic commitment boundary using a particular effective Data Meaning revision.

### Rule

The activity MUST bind the relevant Data Meaning revision/identity.

A later Data Meaning revision MUST affect future validation and new activities only. It MUST NOT retroactively reinterpret an already committed activity, existing Learned State, completed Generation, or Evidence.

### Provenance obligation

The binding SHOULD be recorded as a typed provenance relationship sufficient to explain which meaning revision governed the activity.

### Failure avoided

Mutable global metadata silently changing the interpretation of historical work.

---

## SYNC-02 — Strategy selection and compatibility

**Type:** A / B / E

**Participants:** Synthesis Strategy ↔ Data Meaning / Constraint; Synthesis Strategy → Learning / Generation

### Trigger

A Strategy revision/configuration is proposed for Learning or Generation.

### Rule

The activity validates required capabilities against the bound Data Meaning and applicable Constraints.

The Strategy owns its declared capabilities, requirements, configuration, and limitations.

The activity owns the contextual validation result for its intended use.

A validation result MUST NOT be written back as a universal `compatible=true/false` property on the Strategy because compatibility depends on the activity context.

### Provenance obligation

The committed activity records the exact Strategy/configuration revision it used.

### Failure avoided

A hidden compatibility coordinator whose globally mutable state couples Strategy to every dataset and Constraint revision.

---

## SYNC-03 — Constraint binding and handling disposition

**Type:** A / B / E

**Participants:** Constraint → Learning / Generation / Evaluation

### Trigger

A Constraint revision is applicable to the scope of an activity.

### Rule

The activity binds the applicable Constraint revision and records how it intends to handle it where relevant, such as:

- enforce during learning;
- enforce during generation;
- validate after generation;
- unsupported;
- not applicable for the activity method.

The Constraint remains authoritative for the rule itself. The activity owns its handling disposition.

Unsupported required Constraints MUST remain visible; they MUST NOT be silently omitted from the committed activity specification.

### Failure avoided

Strategy-specific or method-specific copies of domain rules drifting away from steward-owned Constraint authority.

---

## SYNC-04 — Learning operational realization

**Type:** D / E

**Participants:** Learning ↔ Execution

### Trigger

A committed Learning requires operational work.

### Direction of control

Learning requests operational realization and may request cancellation according to Learning semantics.

Execution owns:

- logical operational status;
- Attempt history;
- retry/resume mechanics at the concept level;
- operational failure/progress facts.

Learning owns:

- semantic prerequisites;
- whether the intended reusable state was successfully derived;
- Learning-specific completion/failure outcome;
- association with resulting Learned State.

### Terminal-state rule

`Execution.completed` is necessary evidence that physical work finished, but it MUST NOT by itself establish `Learning.completed`.

Learning completion requires domain validation that a valid Learned State result exists or that the selected strategy's Learning semantics have otherwise been satisfied.

### Failure avoided

Treating a Spark/Databricks/PyTorch job success flag as equivalent to successful learning.

---

## SYNC-05 — Learning produces Learned State

**Type:** C / E

**Participants:** Learning → Learned State

### Trigger

Learning reaches successful semantic completion and reusable source-derived information has been established.

### Rule

A new Learned State identity/version is established and linked to the producing Learning.

A failed, cancelled, or semantically incomplete Learning MUST NOT establish usable Learned State.

Learned State MUST preserve enough compatibility/provenance reference to be validated for later use without depending on the original runtime object remaining alive.

### Historical rule

Later retirement/invalidation of Learned State affects future use but MUST NOT rewrite historical Generations that used it while it was valid.

### Failure avoided

Conflating the transient training process with its durable reusable result.

---

## SYNC-06 — Generation commitment and compatibility

**Type:** A / B / E

**Participants:** Generation ↔ Data Meaning / Strategy / Learned State / Constraint

### Trigger

A requested Generation is committed for fulfillment.

### Rule

Generation binds:

- requested intent and Conditions;
- relevant Data Meaning revision;
- applicable Constraint revisions;
- Strategy revision/configuration;
- Learned State identity/version when required;
- reproducibility-relevant request state;
- stable input/output target references where available.

Generation validates that the selected Strategy/Learned State can satisfy the requested semantics/capabilities to the degree claimed.

### Direct-generation rule

If the selected Strategy requires no reusable Learned State, Generation MAY bind the Strategy directly without fabricating Learning/Learned State state.

### Condition rule

Condition remains Generation-owned request state. Constraint remains independently authoritative prescriptive state.

### Failure avoided

Forcing every synthesis method into train-then-sample semantics or making Conditions into globally reusable validity rules.

---

## SYNC-07 — Generation operational realization

**Type:** D / E

**Participants:** Generation ↔ Execution

### Trigger

A committed Generation requires operational work.

### Rule

Execution reports operational progress/failure/completion while Generation owns the semantic outcome.

`Execution.completed` MUST NOT automatically mean the Generation is complete.

Generation completion requires domain confirmation that the intended output is validly associated and that partial/incomplete output is not being represented as the completed synthetic dataset.

### Partial-output rule

Partial materialization MAY exist for recovery/diagnostics, but it MUST remain distinguishable from the successful Generation result.

### Failure avoided

Publishing or returning incomplete distributed output because the underlying job reached a terminal state.

---

## SYNC-08 — Generation produces synthetic output reference

**Type:** C / E

**Participants:** Generation → synthetic dataset/output reference; Generation → Provenance

### Trigger

Generation reaches successful semantic completion.

### Rule

Generation associates a stable logical reference to the completed synthetic output.

Stable output identity/location/version semantics are an integration/representation obligation, not a new generic Artifact or Dataset concept.

Historical provenance records which Generation produced the output and its bound inputs/configuration.

### Failure avoided

Assuming large generated data must be a local return value or creating a generic artifact catalog concept merely to identify output.

---

## SYNC-09 — Evaluation Criterion binding

**Type:** A / E

**Participants:** Evaluation Criterion → Evaluation / Evidence

### Trigger

An Evaluation is committed to answer a specific evaluative question.

### Rule

Evaluation binds the exact Criterion revision it addresses.

Later Criterion revisions MUST NOT reinterpret historical Evidence.

Evidence references the Criterion revision directly or through an immutable evaluation specification so reviewers know exactly what question the result answered.

### Failure avoided

Reusing a historical metric result under a materially different evaluative question.

---

## SYNC-10 — Evaluation method compatibility

**Type:** B / E

**Participants:** Evaluation ↔ Evaluation Criterion / inputs

### Trigger

A measurement method is selected for a Criterion and specified inputs/scope.

### Rule

Evaluation validates that the method is capable of addressing the Criterion under the declared scope.

Sampling, approximation, bounded analysis, or other material methodological limitations belong to Evaluation specification/result context and MUST be visible in resulting Evidence.

The Criterion remains authoritative for the question; Evaluation owns the method.

### Failure avoided

Metric availability silently defining what “quality” means.

---

## SYNC-11 — Evaluation operational realization

**Type:** D / E

**Participants:** Evaluation ↔ Execution

### Trigger

A committed Evaluation requires operational work.

### Rule

Execution owns operational status and Attempt history. Evaluation owns whether the intended examination was semantically completed and whether usable Evidence can be produced.

An operationally successful job that omitted required input scope, failed a methodological validity check, or produced uninterpretable results MUST NOT automatically become a successful Evaluation.

### Failure avoided

Conflating computational completion with evidentiary validity.

---

## SYNC-12 — Evaluation produces Evidence

**Type:** C / E

**Participants:** Evaluation → Evidence

### Trigger

Evaluation produces a result sufficiently interpretable to preserve as Evidence.

### Rule

Evidence records/references at minimum:

- Criterion revision;
- method identity/configuration sufficient for interpretation;
- input references;
- scope;
- result/observation;
- limitations/uncertainty;
- relevant provenance.

A failed Evaluation MAY produce diagnostic records, but they MUST NOT masquerade as Evidence answering the Criterion unless the result is semantically valid for that purpose.

### Historical rule

Newer Evidence may supersede or render earlier Evidence inapplicable for current use, but historical observations MUST NOT be rewritten.

### Failure avoided

Treating ephemeral logs or metric outputs as durable evidence without question/scope/context.

---

## SYNC-13 — Evidence external handoff

**Type:** F

**Participants:** Evidence → external consumer / governance / decision authority

### Trigger

An actor/system uses Evidence to inform a downstream claim, approval, restriction, or release/use decision.

### Rule

SYNGAN exposes Evidence and Provenance without asserting that the Evidence itself constitutes authorization.

External authority MAY reference SYNGAN Evidence, but the current concept model does not import that decision state back into Evidence as though it were part of the observation.

### Failure avoided

`quality score` or `privacy result` silently becoming `approved for use`.

---

## SYNC-14 — Provenance recording at material transitions

**Type:** E

**Participants:** all material concepts → Provenance

### Trigger

A transition materially changes derivation, interpretation, or historical explainability.

Examples include:

- Data Meaning revision accepted/superseded;
- Strategy/configuration bound to an activity;
- Constraint revision bound;
- Learning committed/completed and Learned State established;
- Generation committed/completed and output associated;
- Evaluation committed/completed and Evidence established;
- Execution/Attempt facts materially relevant to reproducibility or failure explanation.

### Rule

Provenance records typed relationships/context using stable references.

Provenance MUST NOT duplicate entire canonical state payloads simply to avoid following references.

### Commit integrity

For transitions where provenance is required by the project's traceability guarantees, the design MUST ensure that a committed domain transition and its required provenance fact cannot silently diverge.

The eventual representation mechanism is deferred; this is a semantic consistency requirement, not a database transaction prescription.

### Failure avoided

A lineage/provenance subsystem that is either incomplete or becomes an all-knowing duplicate state store.

---

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** A / E; cross-cutting contract, not a concept

**Participants:** Learning / Generation / Evaluation / Execution / Provenance

### Trigger

A reproducibility-relevant activity is committed.

### Rule

The activity and related Provenance MUST preserve/refer to enough stable information to state what kind of reproduction/comparison is possible.

Depending on scope, this may include:

- source/output identities or fingerprints;
- Data Meaning revision;
- Strategy/configuration revision;
- Constraint/Criterion revisions;
- Learned State identity;
- seeds/randomness policy;
- software/model implementation identity;
- runtime/environment facts;
- sampling/approximation semantics.

No concept should duplicate all of these fields under a generic `reproducibility` object merely for convenience.

### Failure avoided

A cross-cutting guarantee becoming inconsistent duplicated configuration.

## Non-synchronizations worth preserving

The following are intentionally **not** automatic synchronizations:

### Data Meaning revision → historical Learned State

A new meaning revision does not mutate Learned State. It may cause future compatibility checks to reject or qualify use.

### Constraint revision → historical Generation

A new rule does not retroactively invalidate historical output as though that rule existed at production time. A later Evaluation may assess the old output under the new rule if an actor explicitly asks that question.

### Strategy revision → existing Learned State

A newer strategy version does not rewrite the Strategy identity under which old state was produced. Compatibility with new runtimes/strategies is a separate validation question.

### Criterion revision → historical Evidence

Evidence continues to answer the Criterion revision it originally referenced.

### Learned State retirement → historical Generation

Retirement prevents future selection as appropriate; it does not erase historical derivation.

### Evidence supersession → external historical decision

Evidence can become obsolete for current use, but SYNGAN does not rewrite decisions made by external authorities.

## Synchronization cardinality guidance

The following cardinalities are conceptual expectations, not storage schemas:

- one Data Meaning revision may be bound by many activities;
- one Strategy revision/configuration may be reused by many activities;
- one Learning may produce zero or one primary Learned State result under the current model; strategies needing multiple independently meaningful learned results should trigger later concept review;
- one Learned State may support many Generations;
- one Generation produces one logical synthetic output result, even if physically partitioned into many files/partitions;
- one Criterion may be reused by many Evaluations;
- one Evaluation may produce one or more Evidence records when multiple independently interpretable findings are produced;
- one logical Execution contains one or more Attempts over its lifecycle;
- Provenance contains many typed relationships across all of the above.

## Synchronization economy assessment

The retained set avoids pathological all-to-all synchronization because most relationships are one of:

- stable reference binding;
- local contextual validation;
- one-way result production;
- a narrow activity↔Execution lifecycle pair;
- append/traverse Provenance.

No retained concept currently requires merger due to synchronization burden.

The main design condition is that contextual validation and historical binding remain local to the activity rather than creating a globally mutable compatibility state shared among Strategy, Data Meaning, Constraint, Learned State, and Generation.
