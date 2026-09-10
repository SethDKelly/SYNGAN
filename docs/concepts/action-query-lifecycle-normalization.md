---
type: Cross-Concept Design Authority
title: Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization
status: active
---

# Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization

## Purpose

Provide the current Phase 008-D normalization of conceptual behavior across SYNGAN's eleven accepted concepts.

This authority builds on [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md) and answers four questions for every accepted concept:

1. which operations actually change concept-owned state;
2. which operations merely observe or derive information from concept-owned state;
3. which contextual assessments belong to a consuming activity rather than the reusable authority being inspected; and
4. what preconditions, effects and postconditions are required for lifecycle transitions to be behaviorally meaningful.

This is concept design. It does not define Python methods, HTTP endpoints, UI controls, Spark jobs, database transactions, event handlers, commands/messages, persistence APIs, status-code enums, scheduler calls or implementation exceptions.

It is governed by:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Jackson Methodology Completion Matrix](../authority/jackson-methodology-completion-matrix.md);
- [Concept-Justification Traceability](../problem/concept-justification-traceability.md);
- [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md);
- the individual accepted concept specifications;
- [Core Synchronizations](../synchronizations/core-synchronizations.md), which coordinate but do not own concept behavior.

## 008-D scope boundary

008-D closes the **individual-concept behavioral specification layer** for the current catalog.

It covers:

- state-changing conceptual actions;
- state-observing/derived conceptual queries;
- contextual assessments and their state owner;
- action preconditions;
- conceptual effects;
- postconditions;
- lifecycle transition ownership;
- blocked/indeterminate outcomes where false success would violate concept semantics;
- the relationship between owned actions and cross-concept synchronizations.

008-D does not close:

- whether each operational principle convincingly demonstrates purpose — 008-E;
- independence, genericity, familiarity or naming — 008-F;
- rejected/deferred candidate rediscovery — 008-G;
- Jackson inclusion dependence or application families — Phase 009;
- final synchronization integrity/composition — Phase 009/011;
- mapping actions/queries to SDK/notebook/CLI/report/UI surfaces — Phase 010;
- implementation or representation architecture.

## Behavioral vocabulary

### Command / state-changing action

A **command** is a conceptual action whose successful occurrence creates, changes, establishes, qualifies or terminates state owned by that concept.

A command specification identifies, where material:

- the owning concept;
- the state on which it operates;
- preconditions that must be established before the transition can succeed;
- the effect on concept-owned state;
- the postcondition that must hold after successful completion;
- whether failure/indeterminacy leaves prior state unchanged or enters an explicit non-success state.

A conceptual command is not necessarily one API call. One command may later map to several physical interactions, and several interface gestures may map to one conceptual command.

### Query / observation

A **query** observes, derives, compares or explains concept state without changing the canonical state merely because the query was asked.

A query:

- may return unresolved, indeterminate, partial or unavailable information;
- must preserve exact historical scope/revision identity where material;
- must not strengthen a claim beyond the underlying state/evidence;
- must not create duplicate mutable authority merely to cache a derived answer;
- may later require expensive or distributed realization, but that does not change its conceptual meaning.

`Inspect`, `review`, `observe`, `compare`, `traverse`, `explain` and similar verbs are therefore queries unless the concept's purpose explicitly makes the observation itself a state-changing fact.

### Contextual assessment

A **contextual assessment** compares reusable declarations/results with the circumstances of a consuming activity.

The key ownership rule is:

> **The source concept owns the facts being consulted; the consuming concept owns the contextual assessment when that assessment controls its own commitment or completion.**

Examples:

- Strategy owns capability/requirement/limitation declarations; Learning or Generation owns whether that Strategy is compatible with the proposed activity.
- Constraint owns rule/scope/prerequisites; Learning, Generation or Evaluation owns applicability/handling in that activity.
- Learned State owns intrinsic restrictions/dependencies; Generation owns whether reuse is compatible with the proposed Generation.
- Criterion owns the question and answer-strength requirement; Evaluation owns whether a selected method can answer it under the proposed scope.
- Evidence owns the historical finding; a later consuming context may assess current applicability without rewriting the finding.

A contextual assessment may itself change the consuming activity's state, for example from proposed to validated/ready, incompatible or indeterminate. It does not create mutable pairwise truth on the reusable concept.

### Synchronization

A synchronization coordinates existing concept-owned actions/queries. It may require actions in more than one concept to occur together or in a constrained order, but it does not create an unnamed state owner.

If a synchronization appears to require behavior that no concept owns, that is a design gap; the behavior must be assigned upstream rather than hidden inside the synchronization mechanism.

### External interaction / handoff

Selecting, reusing, exposing, handing off, displaying or referencing state is not automatically a command on the referenced concept.

Examples:

- a Generation selecting Learned State does not mutate Learned State;
- an Evaluation selecting a Criterion does not mutate the Criterion;
- handing Evidence to an external reviewer does not make Evidence the owner of the reviewer's decision;
- traversing Provenance does not mutate Provenance.

Phase 010 will map such interactions to physical and linguistic surfaces.

## Common action-contract rules

### A1 — Preconditions are semantic, not implementation guards

A precondition states what must already be true for a conceptual transition to be valid. It does not prescribe an `if` statement, database constraint, API validation layer or authorization mechanism.

### A2 — Unestablished preconditions do not become success

If a material precondition is false or cannot be established strongly enough, the command must not silently produce the success postcondition.

Where the concept requires it, the result may remain proposed, blocked, failed, cancelled, indeterminate or otherwise explicitly non-successful.

### A3 — Effects modify only owned state

An action may reference another concept or synchronize with another concept's action. It may not mutate that other concept's canonical state by convenience.

### A4 — Postconditions are the semantic result of success

Successful completion of a command must leave a state from which the promised result can be reasoned about without inferring hidden implementation behavior.

### A5 — Historical commitments are not amended in place

For committed activities and bound reusable revisions, a materially semantic change after commitment creates a new distinguishable revision/activity rather than mutating history.

### A6 — Failure does not erase prior valid history

Failed/cancelled/invalidated transitions may change current/future state but do not erase already established historical facts or earlier Attempts.

### A7 — Query results do not become new authority by repetition

Repeated inspection/comparison may be cached or materialized later, but such representation does not become a new concept-owned truth unless an accepted concept explicitly establishes it.

### A8 — Cross-concept production requires both owners to remain explicit

Where one concept produces another accepted concept's result, the producer owns semantic completion and the result concept owns establishment of the resulting state.

Examples:

```text
Learning.Complete  + LearnedState.Establish
Evaluation.Complete + Evidence.Establish
```

The synchronization preserves both authorities.

## Normalized concept behavior

### Data Meaning

#### Commands

**Create / Declare draft meaning**

- **Precondition:** the logical subject/scope can be distinguished sufficiently for the intended semantic assertion and the declaration source/authority is representable.
- **Effect:** creates or contributes to a draft Data Meaning revision containing explicit declared assertions.
- **Postcondition:** the draft assertion is inspectable and distinguishable from inferred or unresolved state; it is not yet silently treated as effective if effectiveness has not been established.

**Infer meaning**

- **Precondition:** the subject/scope and material inference basis/method can be identified sufficiently for later inspection.
- **Effect:** creates an inferred assertion in draft/effective candidate state with origin and uncertainty preserved.
- **Postcondition:** inference remains distinguishable from declaration and cannot overwrite an authoritative declaration merely because confidence is high.

**Mark unresolved / conflicting / unsupported**

- **Precondition:** the semantic proposition/scope requiring explicit uncertainty can be identified.
- **Effect:** records the non-resolution state rather than selecting a default interpretation.
- **Postcondition:** consumers can determine that the required meaning is unresolved/conflicting/unsupported.

**Correct / Revise**

- **Precondition:** a material correction/new interpretation is proposed for an existing lineage/scope.
- **Effect:** creates a new distinguishable revision; prior bound revisions remain unchanged.
- **Postcondition:** both prior and new historical meanings remain identifiable, with future-use eligibility decided explicitly.

**Make effective**

- **Precondition:** the revision is coherent enough for the scope it claims, material conflicts are either resolved or explicitly represented, and the authority needed for effectiveness is established under the product context.
- **Effect:** changes the revision's current-use status to effective.
- **Postcondition:** new activities may bind this exact revision; unresolved properties remain unresolved rather than being fabricated.

**Supersede**

- **Precondition:** a newer revision is designated for future use.
- **Effect:** prior revision becomes superseded for new selection while remaining historically authoritative where previously bound.
- **Postcondition:** new default/current selection does not rewrite historical bindings.

**Invalidate**

- **Precondition:** a material defect makes the revision unsuitable for new reliance.
- **Effect:** blocks ordinary new commitment against the revision.
- **Postcondition:** invalidation and reason are inspectable; prior historical use remains identifiable.

#### Queries

- inspect one revision and its assertions/origins/uncertainty;
- resolve currently effective meaning for a logical scope, allowing unresolved/conflict as a legitimate answer;
- list unresolved/conflicting semantic assertions;
- compare revisions without declaring later automatically better;
- inspect the exact meaning revision historically bound by an activity.

### Synthesis Strategy

#### Commands

**Define draft Strategy revision**

- **Precondition:** synthesis behavior can be described independently of a concrete implementation class/plugin.
- **Effect:** creates a draft Strategy revision with material capabilities, requirements, limitations, learning/generation mode and dependency profile.
- **Postcondition:** the proposed behavior is inspectable but not yet necessarily eligible for new committed work.

**Configure / Revise material semantics**

- **Precondition:** the configurable behavior or material configuration change can be stated explicitly.
- **Effect:** creates a historically distinguishable configuration/revision when behavior, capability, dependency or reproducibility semantics change materially.
- **Postcondition:** a later activity can bind the exact behavior/configuration used without relying on mutable defaults.

**Make effective**

- **Precondition:** material declarations needed for contextual validation are present and internally coherent enough for selection.
- **Effect:** makes the Strategy revision/configuration eligible for proposed activity validation.
- **Postcondition:** eligibility does not itself establish compatibility with any particular Learning/Generation.

**Supersede / Retire / Invalidate**

- **Precondition:** a future-use status change is justified for the exact Strategy revision/configuration.
- **Effect:** changes selection eligibility without rewriting historical activities.
- **Postcondition:** prior bindings remain exact; invalidation/retirement cannot silently cause fallback to a different Strategy.

#### Queries

- inspect capabilities, requirements, limitations and dependency/network profile;
- describe supported Data Meaning/Constraint/topology/text and Learning/Generation behavior;
- compare Strategies/configurations across actor-relevant dimensions without one universal superiority score;
- inspect historical Strategy/configuration state bound by an activity.

#### Contextual assessment ownership

`Validate proposed use` is **not** a Strategy command. Learning or Generation owns the compatibility assessment against its own proposed context while querying Strategy declarations.

### Learning

#### Commands

**Propose**

- **Precondition:** a learning intent exists for a Strategy that requires or intentionally supports reusable source-informed state.
- **Effect:** creates an editable Learning occurrence/specification.
- **Postcondition:** the occurrence is proposed and not yet historically committed.

**Amend pre-commit specification**

- **Precondition:** Learning has not crossed semantic commitment.
- **Effect:** changes proposed source/scope/bindings/parameters/approximation/dependency/reproducibility intent.
- **Postcondition:** any prior validation that is no longer applicable must not be treated as current.

**Validate prerequisites / context**

- **Precondition:** enough proposed context exists to test required Meaning, Strategy, Constraints, source/dependency/network and material resource prerequisites.
- **Effect:** records Learning-owned contextual assessment state such as ready, ready-with-explicit-limitations, incompatible or indeterminate.
- **Postcondition:** only sufficiently established prerequisites permit normal semantic commitment; material indeterminacy does not become ready by default.

**Commit**

- **Precondition:** required contextual validation is sufficient and exact material source/Meaning/Strategy/Constraint/approximation/dependency/reproducibility semantics can be bound.
- **Effect:** freezes the material Learning specification historically.
- **Postcondition:** retry/resume may realize this same Learning only without semantic mutation.

**Initiate realization / Mark active**

- **Precondition:** Learning is committed and operational realization is required/permitted.
- **Effect:** associates/coordinates with Execution and records the domain fact that realization is underway.
- **Postcondition:** detailed Attempt/progress state remains owned by Execution.

**Request cancellation / Resolve cancellation**

- **Precondition:** Learning is not already irreversibly semantically completed; cancellation is permitted by the current lifecycle.
- **Effect:** records Learning cancellation intent and later resolves the Learning to cancelled only when operational/semantic facts justify that terminal state.
- **Postcondition:** cancellation does not erase commitment/Attempt history and establishes no usable Learned State unless completion preceded cancellation.

**Fail**

- **Precondition:** the committed Learning can no longer validly establish its intended Learned State under the same semantics.
- **Effect:** enters terminal semantic failure.
- **Postcondition:** no primary usable Learned State is established by this failed occurrence; diagnostics/history remain.

**Complete**

- **Precondition:** the committed Learning was realized sufficiently, intended reusable source-informed state is validly established, required result context is available, and required provenance relationships can be made consistent.
- **Effect:** transitions Learning to completed and synchronizes establishment of zero or one primary Learned State.
- **Postcondition:** the resulting Learned State is historically tied to this exact Learning; Execution success alone was not sufficient.

#### Queries

- inspect proposed/committed Learning specification and exact bindings;
- inspect Learning-level lifecycle/outcome;
- inspect contextual validation/limitations;
- inspect associated Execution at the semantic boundary without absorbing Attempt state;
- inspect the primary Learned State identity if established.

### Learned State

#### Commands

**Establish**

- **Precondition:** a Learning has satisfied its semantic completion contract and the result can be distinguished from checkpoint/intermediate state.
- **Effect:** creates one stable logical Learned State result identity with intrinsic requirements/limitations and derivation references.
- **Postcondition:** the established semantic content is historically immutable and independently reusable after producing compute is gone.

**Restrict**

- **Precondition:** a current/future-use limitation is established without necessarily proving the historical Learned State was wrong.
- **Effect:** changes future-use status to restricted with the limitation preserved.
- **Postcondition:** historical derivation/content remains unchanged; Generation must account for the restriction contextually.

**Retire**

- **Precondition:** the state should no longer be ordinarily selected for new use without asserting material historical defect.
- **Effect:** changes future-use status to retired.
- **Postcondition:** prior Generations remain historically attributable.

**Invalidate**

- **Precondition:** a material defect/incompatibility makes the state unsuitable for new reliance.
- **Effect:** blocks future ordinary reuse.
- **Postcondition:** the reason/current status is inspectable; the producing history and prior uses are not rewritten.

#### Queries

- inspect derivation, Strategy/configuration, source/Meaning/Constraint context, dependencies, limitations and current status;
- expose intrinsic compatibility requirements/limitations to a proposed Generation;
- compare Learned States while preserving different derivation contexts;
- inspect producing Learning/history.

#### External/contextual operations

`Select / reuse` is not a Learned State mutation. Generation references the Learned State and owns the contextual reuse decision. Likewise `validate for intended use` is Generation-owned assessment using Learned State queries.

### Generation

#### Commands

**Propose / Request**

- **Precondition:** an actor has a synthesis intent whose logical scope/result can be stated sufficiently to begin design of one Generation occurrence.
- **Effect:** creates editable requested intent including material quantity/scope/Conditions and proposed synthesis basis.
- **Postcondition:** no committed success obligation exists yet.

**Amend / Withdraw pre-commit**

- **Precondition:** semantic commitment has not occurred.
- **Effect:** changes or withdraws proposed intent.
- **Postcondition:** stale validation cannot be treated as current after a material amendment; withdrawal creates no completed Generation.

**Validate proposed Generation**

- **Precondition:** enough proposed state exists to evaluate Meaning, Strategy, Learned-State/direct-input, Constraint, Condition, dependency/network, quantity/scope and material scale prerequisites.
- **Effect:** records Generation-owned compatibility/applicability/handling/feasibility results.
- **Postcondition:** mandatory incompatibility/unsupported/indeterminate conditions remain explicit and block normal commitment where determination is required.

**Commit**

- **Precondition:** material required validation is sufficient and the exact success-defining context can be bound.
- **Effect:** freezes the material Generation specification historically.
- **Postcondition:** retries cannot change Meaning, Strategy, learned/direct basis, Conditions, Constraints, quantity/scope or other committed semantics.

**Initiate fulfillment / Mark fulfilling**

- **Precondition:** Generation is committed and fulfillment is permitted.
- **Effect:** coordinates operational realization where needed and records Generation-level fulfillment state.
- **Postcondition:** Execution owns detailed Attempt/progress state.

**Record partial/candidate result state**

- **Precondition:** fulfillment has produced identifiable material that may contribute to the requested logical output.
- **Effect:** records that the Generation has partial or complete candidate material, explicitly non-final where completion conditions remain open.
- **Postcondition:** consumers cannot treat candidate/partial material as completed output.

**Enter awaiting-required-validation**

- **Precondition:** candidate materialization is sufficient to evaluate outstanding mandatory completion conditions but those conditions are not yet established.
- **Effect:** records that physical production may be complete while semantic completion remains pending.
- **Postcondition:** required Evidence/validation can be associated without implying completion.

**Evaluate completion basis**

- **Precondition:** candidate/result state and all mandatory completion inputs are available to the strength required by the committed specification.
- **Effect:** determines whether Generation's own completion conditions are satisfied, failed or remain indeterminate.
- **Postcondition:** Evidence contributes only to the claims it supports; Evidence does not own the Generation transition.

**Complete / Complete with limitations**

- **Precondition:** all mandatory committed conditions are satisfied; any limitation is explicitly permitted by the committed specification and does not mask mandatory failure.
- **Effect:** establishes zero or one authoritative completed logical output result and terminal semantic state.
- **Postcondition:** completed result is distinguishable from candidate/abandoned material and required provenance is consistent.

**Fail**

- **Precondition:** the committed Generation cannot be validly fulfilled under the same semantics or a mandatory requirement is established as failed with no valid same-Generation recovery path.
- **Effect:** transitions to terminal semantic failure.
- **Postcondition:** partial/candidate material remains non-final; no completed output is promoted.

**Request / Resolve cancellation**

- **Precondition:** cancellation is allowed and semantic completion has not already become controlling.
- **Effect:** records cancellation intent and resolves cancelled only after the semantic/operational race is known sufficiently.
- **Postcondition:** completed-before-cancel remains completed; otherwise cancelled Generation promotes no incomplete candidate as completed.

#### Queries

- inspect requested/committed specification and bound authorities;
- inspect semantic lifecycle and validation state;
- inspect partial/candidate/completed-result references and their finality;
- inspect Condition fulfillment and Constraint completion basis;
- inspect associated Evaluation/Evidence used for completion without copying their authority;
- inspect associated Execution at the semantic boundary.

### Constraint

#### Commands

**Declare draft rule**

- **Precondition:** a prescriptive rule, logical scope, authority/source and material requirement semantics can be stated.
- **Effect:** creates a draft Constraint revision.
- **Postcondition:** the rule remains distinguishable from descriptive Data Meaning and Generation Conditions.

**Revise / Correct**

- **Precondition:** material rule/scope/requirement semantics change.
- **Effect:** creates a new distinguishable Constraint revision rather than editing a bound revision.
- **Postcondition:** prior and new rule histories remain identifiable.

**Make effective**

- **Precondition:** rule meaning/scope/prerequisites are sufficiently coherent for new contextual consideration.
- **Effect:** makes the exact revision eligible to be bound by new activities.
- **Postcondition:** effectiveness does not assert applicability or satisfiability in every context.

**Supersede / Retire / Invalidate**

- **Precondition:** future-use status change is justified for the exact revision.
- **Effect:** changes future selection eligibility.
- **Postcondition:** historical activities remain governed by the revisions they actually bound.

#### Queries

- inspect rule, logical scope, authority, semantic prerequisites and revision history;
- compare revisions;
- expose prerequisites/requirement semantics to a consuming activity;
- inspect the exact historical revision bound by an activity.

#### Contextual assessment ownership

`Determine applicability`, `determine satisfiability` and `associate handling expectations` are not Constraint mutations. Learning, Generation or Evaluation owns the contextual result/handling in its proposed/committed activity while querying the Constraint.

### Evaluation Criterion

#### Commands

**Define draft Criterion**

- **Precondition:** an evaluative question/property, logical scope and material answer interpretation can be stated.
- **Effect:** creates a draft Criterion revision.
- **Postcondition:** the question remains independent of whatever metric/method may later examine it.

**Revise / Correct**

- **Precondition:** the question, scope, reference context, tolerance or answer-sufficiency semantics change materially.
- **Effect:** creates a new distinguishable Criterion revision.
- **Postcondition:** historical Evidence continues to answer the earlier exact revision.

**Make effective**

- **Precondition:** the question/scope/reference/answer-strength semantics are sufficiently coherent for committed Evaluation.
- **Effect:** makes the Criterion eligible for selection by proposed Evaluations.
- **Postcondition:** no Evaluation method is implied or selected by effectiveness alone.

**Supersede / Retire / Invalidate**

- **Precondition:** future-use status change is justified.
- **Effect:** changes selection eligibility without rewriting historical Evidence.
- **Postcondition:** exact historical Criterion bindings remain inspectable.

#### Queries

- inspect the question, scope, reference context and answer-sufficiency/claim-strength requirements;
- compare Criterion revisions;
- inspect the exact historical revision answered by Evidence;
- expose required answer strength to a proposed Evaluation.

#### External/contextual operations

`Select / reuse` is not a Criterion mutation. Evaluation references the Criterion. Method compatibility belongs to Evaluation.

### Evaluation

#### Commands

**Propose**

- **Precondition:** an evaluative intent exists with at least one proposed Criterion/subject/method context sufficient to begin one Evaluation occurrence.
- **Effect:** creates editable Evaluation specification.
- **Postcondition:** no durable Evidence is established merely by proposing the examination.

**Amend pre-commit specification**

- **Precondition:** Evaluation has not crossed semantic commitment.
- **Effect:** changes proposed Criterion/input/reference/method/scope/coverage/approximation/uncertainty semantics.
- **Postcondition:** materially invalidated prior validation is no longer treated as current.

**Validate method/context**

- **Precondition:** enough proposed state exists to assess whether the method can answer the bound Criterion at the represented strength under available subject/reference/dependency/scope conditions.
- **Effect:** records Evaluation-owned contextual compatibility/sufficiency state.
- **Postcondition:** incompatible or materially indeterminate method/scope does not become ready by execution convenience.

**Commit**

- **Precondition:** required method/context validation is sufficient and exact Criterion/input/reference/method/scope/coverage/uncertainty/dependency semantics can be bound.
- **Effect:** freezes the material Evaluation specification historically.
- **Postcondition:** retries cannot silently alter the question, subject/reference, method or claim-strength basis.

**Initiate / Mark evaluating**

- **Precondition:** Evaluation is committed and operational examination is permitted.
- **Effect:** coordinates Execution where needed and records Evaluation-level examination state.
- **Postcondition:** Attempt/progress details remain Execution-owned.

**Request / Resolve cancellation**

- **Precondition:** cancellation is permitted and Evaluation is not already semantically complete.
- **Effect:** records cancellation intent and later resolves terminal cancellation when justified.
- **Postcondition:** partial diagnostics do not become Evidence answering the Criterion merely because they exist.

**Complete / Complete with limitations**

- **Precondition:** the committed examination was realized using the bound subject/reference/method/scope; method assumptions/coverage remain interpretable; claim strength is no stronger than supportable; required finding context can be established; required provenance is consistent.
- **Effect:** enters completed state and synchronizes establishment of zero or more independently interpretable Evidence findings where such findings exist.
- **Postcondition:** Evidence may be favorable, unfavorable or indeterminate; Evaluation success means valid examination, not subject success.

**Fail**

- **Precondition:** the committed Evaluation cannot validly produce interpretable Evidence at the intended/allowed strength under the same semantic specification.
- **Effect:** enters terminal semantic failure.
- **Postcondition:** numbers/diagnostics from the failed examination do not masquerade as valid Evidence answering the Criterion.

#### Queries

- inspect committed Evaluation specification and exact bindings;
- inspect lifecycle/status and contextual validation state;
- inspect method scope/coverage/approximation/uncertainty/limitations;
- inspect established Evidence identities;
- inspect associated Execution without conflating operational and methodological completion.

### Evidence

#### Commands

**Establish**

- **Precondition:** a semantically valid completed Evaluation has an independently interpretable finding whose exact Criterion, subject/reference, method, scope, claim strength, uncertainty and limitations can be retained/referenced sufficiently.
- **Effect:** establishes one immutable historical finding identity.
- **Postcondition:** the Evidence can be interpreted after producing compute is gone and cannot claim more than the Evaluation supports.

**Mark superseded / stale / inapplicable**

- **Precondition:** a future/current decision context establishes that newer Evidence is preferred or the historical finding no longer applies to the requested current context.
- **Effect:** changes current-use/applicability status without editing the finding.
- **Postcondition:** the original observation and producing context remain intact.

**Invalidate**

- **Precondition:** a material methodological/data defect undermines current reliance on the historical finding.
- **Effect:** marks the finding invalid for reliance while preserving that it was previously established/asserted.
- **Postcondition:** the defect and historical finding remain auditable; invalidation does not fabricate a replacement answer.

#### Queries

- inspect finding, Criterion, subject/reference, method, scope, strength, uncertainty, limitations and provenance;
- compare Evidence only while preserving material differences in question/method/scope/time/threat model;
- assess whether the historical finding is applicable to a requested current context, allowing stale/inapplicable/indeterminate;
- expose/hand off the finding to Generation or an external decision maker without transferring Evidence ownership.

### Execution

#### Commands

**Prepare**

- **Precondition:** a committed domain activity requires operational realization and can be associated with one logical Execution.
- **Effect:** establishes prepared operational realization state tied to that exact parent activity.
- **Postcondition:** no platform job/Attempt is yet treated as successful by implication.

**Accept / Queue**

- **Precondition:** prepared Execution is eligible for operational admission/scheduling under the current context.
- **Effect:** enters queued/pending state.
- **Postcondition:** pending remains distinct from actively running.

**Start Attempt**

- **Precondition:** current authority permits work and a distinguishable Attempt can be created under the same committed parent semantics.
- **Effect:** creates subordinate Attempt history and enters running state.
- **Postcondition:** current Attempt identity is distinguishable from prior/future Attempts and platform job identity remains only a mapping/reference.

**Record Attempt outcome**

- **Precondition:** sufficient operational evidence exists to classify the Attempt outcome.
- **Effect:** records succeeded, recoverable failure, terminal-for-attempt failure, cancelled, superseded/abandoned or indeterminate outcome as appropriate.
- **Postcondition:** earlier Attempt history remains; one Attempt outcome does not automatically decide the parent domain result.

**Enter recovery pending**

- **Precondition:** no current Attempt is making progress and same-Execution recovery may still be valid.
- **Effect:** records nonterminal recovery-pending state.
- **Postcondition:** a new Attempt cannot start until retry/resume qualification is established.

**Request cancellation**

- **Precondition:** Execution is not already in a controlling terminal state.
- **Effect:** records cancellation intent separately from terminal cancellation.
- **Postcondition:** subsequent outcome may still be cancelled, completed-before-cancel, failed or indeterminate.

**Retry / Resume by starting a new Attempt**

- **Precondition:** same committed parent semantics are preserved; current authorization/authority is valid; prior side effects are safe/reconciled enough; and for resume, recovery material identity/integrity/compatibility is established.
- **Effect:** creates a new distinguishable Attempt in the same Execution, using validated recovery state only where permitted.
- **Postcondition:** prior Attempts remain historical; retry does not create a new parent Learning/Generation/Evaluation.

**Reconcile indeterminate state**

- **Precondition:** Execution contains unknown/ambiguous operational or side-effect state and sufficient independent evidence can be examined.
- **Effect:** narrows/changes the known operational classification only to the strength supported by evidence.
- **Postcondition:** unresolved ambiguity remains explicit; reconciliation cannot fabricate semantic completion.

**Complete operationally**

- **Precondition:** the operational endpoint assigned to the Execution is reached with no unresolved operational defect under that contract.
- **Effect:** transitions Execution to operationally completed.
- **Postcondition:** Learning/Generation/Evaluation remains responsible for its own semantic completion.

**Fail terminally**

- **Precondition:** no valid same-semantics retry/resume path remains.
- **Effect:** transitions Execution to failed.
- **Postcondition:** parent domain concept receives the operational fact but decides its own terminal semantic state.

**Cancel terminally**

- **Precondition:** cancellation has taken effect sufficiently for terminal operational classification.
- **Effect:** transitions Execution to cancelled.
- **Postcondition:** committed parent history remains; already established domain results are not erased.

#### Queries

- inspect Execution lifecycle/status;
- inspect current and historical Attempts;
- inspect progress/health without equating it to domain completion percentage;
- inspect retry/resume eligibility evidence and recovery basis;
- inspect cancellation and unknown/indeterminate state;
- inspect material operational context needed for diagnosis/provenance.

### Provenance

#### Commands

**Record typed relationship**

- **Precondition:** the relationship meaning and stable historical references are established strongly enough by the owning concepts/external identities; the relationship is material under the provenance contract.
- **Effect:** appends/establishes a distinguishable typed provenance assertion.
- **Postcondition:** the assertion references rather than duplicates canonical concept state and cannot create an upstream fact that the owner has not established.

**Correct / Supersede / Invalidate provenance assertion**

- **Precondition:** a prior provenance assertion is known incomplete, incorrect or unsuitable for current reliance and sufficient corrective information is available.
- **Effect:** records an auditable correction/supersession/invalidation relationship/status rather than destructively erasing history.
- **Postcondition:** the previous assertion and correction remain explainable; another concept's canonical state is unchanged unless that concept separately changes it under its own rules.

#### Queries

- inspect a typed provenance assertion and its material qualifiers;
- traverse derivation/binding/realization/evaluation/dependency relationships;
- explain a result/finding by assembling the material historical path;
- compare derivation paths while preserving revision/dependency/execution/method differences;
- determine whether a relationship is currently known/applicable/corrected/unknown to the strength represented.

## Lifecycle transition closure by state family

### Reusable revisioned authorities

Applies to Data Meaning, Synthesis Strategy, Constraint and Evaluation Criterion.

Canonical transition shape:

```text
new/draft
  │
  ├─ revise/correct ──> new distinguishable draft revision
  │
  └─ make effective ──> effective
                          │
                          ├─ supersede ──> superseded
                          ├─ retire* ────> retired
                          └─ invalidate ─> invalidated
```

`retired` is applicable where the concept currently defines it. No requirement is imposed that every revisioned authority expose identical labels.

The invariant is that a bound revision's semantic content is not edited in place and later status changes affect future selection without rewriting history.

### Committed domain activities

Applies to Learning, Generation and Evaluation.

Canonical transition pattern:

```text
proposed/editable
      │
      ├─ amend ───────────────> proposed/editable
      ├─ validate ────────────> ready / limited / incompatible / indeterminate
      │
      └─ commit (only when sufficient)
              ↓
          committed
              ↓
      realization / semantic resolution
              ↓
      completed | completed-with-limitations* | failed | cancelled
```

Generation additionally has explicit partial/candidate/awaiting-validation semantics. Operational Attempts do not replace this lifecycle.

### Durable established results

Applies to Learned State and Evidence.

```text
producer semantic completion
        ↓
     establish
        ↓
immutable historical result/finding
        +
future-use/applicability status may change
```

No ordinary action revises the established semantic content in place.

### Operational realization

Execution uses subordinate Attempt history and supports recovery/cancellation/unknown state. Retry/resume creates a new Attempt, not a new committed parent activity, only while parent semantics remain unchanged.

### Typed historical relationships

Provenance appends typed assertions. Corrections are also historical facts and therefore do not destructively overwrite the assertion history they correct.

## Synchronization-to-owned-action audit

The fifteen accepted synchronizations can be interpreted without inventing an unnamed coordinator action or new state owner.

| Synchronization | Owned behavior under 008-D |
|---|---|
| **SYNC-01 Data Meaning binding** | `Learning/Generation/Evaluation.Commit` queries and binds an exact eligible Data Meaning revision; Data Meaning is not mutated. |
| **SYNC-02 Strategy selection/compatibility** | `Learning.Validate` or `Generation.Validate` owns contextual compatibility; Strategy supplies queryable declarations. Commitment binds the selected exact revision/configuration. |
| **SYNC-03 Constraint applicability/handling** | consuming `Learning/Generation/Evaluation.Validate` owns applicability/handling; Constraint supplies rule/prerequisites; `Commit` freezes the contextual result where material. |
| **SYNC-04 Learning operational realization** | `Learning.InitiateRealization` coordinates with `Execution.Prepare/StartAttempt`; each retains its own lifecycle. |
| **SYNC-05 Learning produces Learned State** | `Learning.Complete` is coordinated with `LearnedState.Establish`; neither physical checkpoint existence nor Execution completion substitutes for these actions. |
| **SYNC-06 Generation commitment/compatibility** | `Generation.Validate` owns contextual reuse/support decisions; `Generation.Commit` binds exact Meaning/Strategy/Learned-State-or-direct-input/Constraint/Condition context. |
| **SYNC-07 Generation operational realization** | `Generation.InitiateFulfillment` coordinates with `Execution.Prepare/StartAttempt`; retry/resume stays Execution-owned. |
| **SYNC-08 Generation output production** | `Generation.EvaluateCompletionBasis` then `Generation.Complete` establishes/associates one completed logical output; candidate bytes do not perform the transition. |
| **SYNC-09 Criterion binding** | `Evaluation.Commit` queries/binds exact effective Criterion revision; Criterion is not mutated by selection. |
| **SYNC-10 Evaluation method compatibility** | `Evaluation.ValidateMethodContext` owns compatibility/sufficiency; Criterion supplies required question/answer strength. |
| **SYNC-11 Evaluation operational realization** | `Evaluation.Initiate` coordinates with `Execution.Prepare/StartAttempt`; operational success does not call `Evaluation.Complete` automatically. |
| **SYNC-12 Evaluation produces Evidence** | `Evaluation.Complete` coordinates with one or more `Evidence.Establish` actions for independently interpretable findings. |
| **SYNC-13 Evidence handoff** | Evidence is queried/exposed; Generation or an external actor owns any downstream completion/approval/use decision. |
| **SYNC-14 Provenance recording** | material owner transition coordinates with `Provenance.RecordRelationship`; Provenance cannot establish the owner transition by itself. |
| **SYNC-15 Reproducibility-relevant snapshot/history** | owner commitments/results expose exact historical facts; Provenance records required relationships. No standalone Reproducibility mutation is invented. |

No `SYNC-16` is introduced by 008-D.

## Cross-concept behavioral invariants after 008-D

1. Every material lifecycle transition has an accepted concept owner.
2. Queries never mutate canonical concept state merely because they are evaluated.
3. Contextual compatibility/applicability/sufficiency belongs to the consuming activity unless explicitly owned otherwise.
4. Reusable authorities are queried/bound, not mutated by consumers.
5. Material post-commitment changes to Learning, Generation or Evaluation require a new distinguishable activity rather than amendment-in-place.
6. A bound reusable semantic revision is not altered in place; material correction creates a distinguishable revision.
7. Learned State and Evidence establishment requires the producing concept's semantic completion; physical existence is insufficient.
8. Established Learned State semantic content and Evidence findings are not revised in place; future-use/applicability status is separate.
9. Execution retry/resume starts another Attempt only under unchanged parent semantics and sufficient continuation authority/evidence.
10. Execution operational completion does not itself invoke the semantic completion action of Learning, Generation or Evaluation.
11. Candidate/partial Generation material remains non-final until `Generation.Complete` succeeds under the committed completion basis.
12. Negative or indeterminate Evidence can result from a successful Evaluation; subject outcome and Evaluation success remain separate.
13. Evidence handoff does not turn Evidence into approval/release authority.
14. Provenance records established relationships and corrections but does not fabricate or mutate another concept's state.
15. Synchronizations compose owned actions; they do not create hidden state ownership.
16. Unknown/indeterminate preconditions or outcomes remain explicit where choosing success would strengthen a claim or authorize a transition.
17. No command/query definition requires one storage engine, API shape, scheduler, package topology, Spark object, model runtime or platform.
18. Current single-table/time-series/multi-table shared-key/text-bearing scope is expressible through these actions/queries without catalog expansion at 008-D.

## Behavioral gap audit

008-D specifically looked for behavior that existed only in synchronization/architecture prose but lacked an upstream conceptual owner.

### Result establishment

Closed. Learning completion + Learned State establishment, Generation completion/output promotion, and Evaluation completion + Evidence establishment all have explicit owners.

### Contextual compatibility/applicability

Closed. Learning, Generation and Evaluation own their contextual assessments. Strategy, Constraint, Criterion and Learned State expose reusable facts rather than receiving mutable pairwise state.

### Retry/recovery/cancellation

Closed for individual-concept behavior. Execution owns Attempts/retry/resume/reconcile and operational cancellation resolution; Learning/Generation/Evaluation own their semantic terminal states. Detailed cross-concept synchronization integrity remains Phase 009/011 work.

### Historical correction

Closed. Revisioned authorities correct by new revision; established results change future-use status without rewriting content; Provenance correction remains append-preserving.

### Observation/query coverage

Closed for the present individual-concept stage. Every concept has at least one meaningful state observation/query surface and no observation requires inventing mutable shadow state.

### Topology/text behavior

Closed for action/query expressibility only. Current topology/text scope can flow through Meaning declaration/inference, Strategy declaration, Learning/Generation commitment, Constraint handling, Evaluation and Evidence without introducing a new action-owning concept at this stage. 008-G still owns final candidate rediscovery.

## Relationship to older individual `Actions` sections

Several Phase 002 concept documents use `Actions` as a broad heading that includes read-only inspection, comparison, selection/reuse or contextual assessment operations.

Those sections remain useful detailed design evidence. Under the current authority, interpret them as follows:

- true state transitions are **commands**;
- state inspection/comparison is a **query**;
- selection/reuse is normally an action of the consuming concept or a later interaction mapping;
- contextual validation belongs to the consuming activity;
- cross-concept production/coordination is governed by explicit synchronizations of the owning actions.

008-D intentionally avoids rewriting every large Phase 002 file merely to rename headings. This normalization is the current cross-concept authority for behavioral classification; later concept-specific corrections may still reopen an individual document if 008-E–008-G finds a substantive mismatch.

## Current concept-by-concept behavioral verdict

```text
Data Meaning          ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Synthesis Strategy    ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Learning              ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Learned State         ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Generation            ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Constraint            ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Evaluation Criterion  ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Evaluation            ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Evidence              ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Execution             ACTIONS / QUERIES / TRANSITIONS NORMALIZED
Provenance             ACTIONS / QUERIES / TRANSITIONS NORMALIZED
```

No concept is added, removed, merged or renamed by 008-D.

## Methodology disposition

008-D closes for the present individual-concept stage:

- **C4 — conceptual actions**;
- **C5 — conceptual queries/observations**;
- **C6 — preconditions/effects/postconditions sufficient for behavioral reasoning**;
- the transition/action portion of **C7 — invariants, lifecycle/history, unresolved/invalidated states**.

Combined with 008-C, C7 is now currently closed for individual-concept state and lifecycle behavior.

Still open:

- C2 operational-principle revalidation — 008-E;
- C1 naming/familiarity and B3/B4 independence/genericity/familiarity — 008-F;
- B1/B2/B5 and C8 catalog/boundary rediscovery — 008-G/008-F;
- all Jackson inclusion-dependence, composition, mapping, final quality/misfit and completion rows assigned to Phases 009–012.

## Implementation/architecture hold

This authority does not authorize any executable work.

```text
JACKSON CONCEPT DESIGN     NOT COMPLETE
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

No conceptual action in this document implies a method/function/class, database transaction, API endpoint, command bus, state machine library, Spark job, scheduler, event, schema or persistence mechanism.
