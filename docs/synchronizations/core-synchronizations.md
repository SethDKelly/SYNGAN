---
type: Synchronization Specification
title: SYNGAN Core Synchronizations
status: accepted
---

# SYNGAN Core Synchronizations

These rules are the canonical cross-concept coordination authority accepted at the end of Phase 001 and refined by later concept-specification phases.

A synchronization coordinates concept-owned state; it does not transfer ownership merely because another concept reads, validates, records, or operationally realizes that state.

## SYNC-01 — Data Meaning revision binding

**Type:** reference/bind + provenance.

When Learning, Generation, or Evaluation crosses semantic commitment using [Data Meaning](../concepts/data-meaning.md), it MUST bind the exact relevant effective revision.

Later meaning revisions affect future validation/new work only and MUST NOT retroactively reinterpret historical Learning, Learned State, Generation, Evaluation, or Evidence.

Material inferred meaning relied upon by committed work MUST already be inspectable/attributable Data Meaning. Required unresolved/conflicting/invalidated meaning remains explicit rather than becoming an implementation default.

## SYNC-02 — Strategy selection and compatibility

**Type:** bind + contextual validation + provenance.

Learning or Generation validates the chosen [Synthesis Strategy](../concepts/synthesis-strategy.md) against bound Data Meaning, applicable [Constraints](../concepts/constraint.md), requested capabilities, Learned State when applicable, and committed deployment/dependency profile.

Strategy owns reusable capability/requirement/configuration/limitation/dependency declarations. The activity owns the exact contextual compatibility result.

Compatibility MUST NOT become globally mutable state on Strategy, Data Meaning, Constraint, or Learned State.

Constraint support is not proof of Constraint satisfaction. A runtime-network-dependent Strategy is incompatible with a no-network committed activity, and missing local artifacts MUST NOT trigger undeclared network acquisition.

For Generation, compatibility also includes mandatory Condition support, requested quantity/scope, Learned State/direct-input suitability, and known deployment/scale requirements material to commitment.

## SYNC-03 — Constraint binding and handling disposition

**Type:** bind + contextual validation + provenance.

An activity determines applicability of [Constraint](../concepts/constraint.md) revisions using activity scope, bound Data Meaning, and explicit prerequisites. Constraint owns rule/scope/semantic dependencies/authority; the activity owns contextual applicability and handling.

Canonical handling dispositions remain:

- **enforced**;
- **validated later**;
- **unsupported**;
- **not applicable**.

Unsupported required Constraints remain visible. Handling is not satisfaction.

For Generation:

- known unsupported required Constraints prevent normal commitment as successfully fulfillable;
- `validated later` means after production but before successful Generation completion when satisfaction is mandatory;
- `enforced` alone is not automatically output-level Evidence;
- a required Constraint established as violated, or indeterminate where determination is mandatory, blocks successful Generation completion.

## SYNC-04 — Learning operational realization

**Type:** operational realization + provenance.

[Learning](../concepts/learning.md) may use [Execution](../concepts/execution.md) for long-running/distributed work.

### Ownership

Learning owns:

- semantic commitment and bound Learning specification;
- whether reusable state was validly derived;
- Learning-level completion/failure/cancellation;
- association with Learned State.

Execution owns:

- one stable logical operational identity for the realization;
- Attempt history;
- operational progress/health;
- retry/resume/cancellation realization;
- checkpoint/recovery associations;
- operational failure/unknown-state facts.

### Attempt and retry rule

One committed Learning MAY span multiple Attempts. A new Attempt remains part of the same Execution only when it preserves the committed Learning semantics.

Retry/resume MUST NOT silently change source identity, Data Meaning, Strategy/configuration, Constraints/handling, learning scope, sampling/approximation, dependency profile, base/pretrained artifact identity, or materially behavior-changing reproducibility state.

A failed Attempt does not automatically fail Learning while a valid retry/recovery path remains.

### Checkpoint rule

Checkpoint/intermediate material MUST NOT become Learned State merely because it is durable or reusable for recovery.

Resume may use checkpoint state only after establishing that the state belongs to the same committed Learning/Execution context, remains sufficiently intact, and preserves required Strategy/runtime/dependency semantics.

### Completion rule

`Execution.completed` MUST NOT by itself establish `Learning.completed`.

Learning may establish Learned State only through its semantic completion contract under SYNC-05.

### Cancellation/unknown rule

Execution cancellation or unknown platform state does not erase the committed Learning. Learning resolves its own terminal state from Execution facts plus its semantic contract.

If operational state is indeterminate, SYNGAN MUST NOT assume Learning success merely because partial/checkpoint material exists.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version.

Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

Under the current model one Learning produces zero or one primary logical Learned State even when its physical representation contains many components.

Learned State retains stable references sufficient to trace producing Learning, source context, Data Meaning, Strategy/configuration, applicable Constraint context, material sampling/approximation, dependency/artifact facts, and operational history required to explain derivation without duplicating all upstream state.

Repeated Attempts/recomputation MUST NOT create multiple ambiguous primary Learned States for the same committed Learning. Later representation must enforce single semantic promotion even when physical computation is repeated.

## SYNC-06 — Generation commitment and compatibility

**Type:** bind + validation + provenance.

At semantic commitment, [Generation](../concepts/generation.md) binds the material specification by which success will be judged, including where applicable quantity/scope, Conditions and their requirement strength/tolerance, Data Meaning, Constraints/handling, Strategy/configuration, Learned State or direct-generation input/source identity, deployment/network profile, dependency artifacts, randomness/reproducibility intent, and material approximation/partition semantics.

Generation owns contextual Learned State reuse compatibility. Ordinary Generation MUST NOT silently mutate/adapt Learned State.

Condition is Generation-owned request direction and remains distinct from Constraint.

Strategies requiring no reusable Learned State MAY generate directly without fabricated Learning/Learned State occurrences.

A no-network/no-egress Generation MUST NOT silently fetch dependencies, invoke remote fallback, substitute materially different base artifacts, or enable undeclared egress.

Material post-commitment request changes require a new Generation.

## SYNC-07 — Generation operational realization

**Type:** operational realization + provenance.

Generation may use [Execution](../concepts/execution.md) for long-running/distributed work.

### Ownership

Generation owns:

- committed request semantics;
- semantic progress/result state;
- fulfillment of mandatory Conditions/Constraints;
- promotion of candidate data;
- Generation-level completion/failure/cancellation;
- completed output association.

Execution owns:

- logical operational state;
- Attempt history;
- operational progress/health;
- retry/resume/cancellation realization;
- checkpoint/partial-output recovery associations;
- operational failure/unknown-state facts.

### Retry/resume rule

One committed Generation MAY span multiple Attempts. Retry/resume MUST preserve Data Meaning, Strategy/configuration, Learned State/direct-generation basis, Conditions, Constraints, quantity/scope, deployment/dependency profile, and other material request semantics.

Recovery may reuse partial materialization only when identity, scope, integrity, and committed-context compatibility can be established sufficiently. Recomputing or duplicating physical partitions is allowed; duplicate physical work MUST NOT create multiple authoritative completed outputs.

### Candidate-output rule

Generation may have partial materialization, complete candidate materialization awaiting semantic validation, completed output, or abandoned/quarantined materialization.

Execution/Attempt success or complete physical materialization is insufficient to promote candidate data.

Single semantic promotion is required: one committed Generation produces zero or one successful logical completed-output result even if Attempts generate overlapping/repeated physical data.

### Cancellation/unknown rule

Cancellation is a request first. Execution may report cancellation accepted, operational completion before cancellation took effect, failure while cancelling, or indeterminate state requiring reconciliation.

Generation determines its terminal semantic state. Cancellation MUST NOT erase committed history or retroactively cancel a Generation already semantically completed.

Unknown operational state MUST NOT result in candidate output being treated as completed until side-effect/output state is reconciled or safely fenced.

### Completion rule

`Execution.completed` MUST NOT by itself establish `Generation.completed`.

Generation applies its completion barrier under SYNC-08, including required validation/Evidence where applicable.

## SYNC-08 — Generation produces synthetic output reference

**Type:** production + provenance.

A successful Generation establishes one logical completed synthetic-output result, even when physically distributed across many files/objects/tables/partitions.

A stable completed-output reference may be associated only when the Generation completion contract is satisfied. Candidate/provisional references must remain explicitly non-final.

Successful completion requires, where applicable, committed-specification consistency, compatible synthesis basis, no forbidden dependency behavior, materially complete quantity/scope, fulfilled mandatory Conditions, completion-sufficient satisfaction basis for every applicable required Constraint, no mandatory indeterminacy/violation, clear non-partial identity, consistent provenance, and no terminal semantic defect.

`completed with limitations` may cover only explicitly permitted best-effort/approximate limitations and MUST NOT override mandatory failures.

Retry/recovery MUST NOT permit multiple completed-output references to be promoted ambiguously for the same committed Generation.

## SYNC-09 — Evaluation Criterion binding

**Type:** bind + provenance.

[Evaluation](../concepts/evaluation.md) MUST bind the exact [Evaluation Criterion](../concepts/evaluation-criterion.md) revision it answers.

The binding includes material question, subject/scope, reference context, and answer-sufficiency/claim-strength semantics where those affect interpretation.

Later Criterion revisions MUST NOT reinterpret historical Evidence.

When a Criterion derives from a Constraint or Generation Condition, Evaluation also binds the exact originating rule/request semantics needed to preserve what was tested. Criterion does not take ownership of Constraint or Condition.

## SYNC-10 — Evaluation method compatibility

**Type:** contextual validation + provenance.

Evaluation validates that its selected method can legitimately address the bound Criterion under declared inputs, logical scope, coverage, sampling/approximation model, assumptions, and uncertainty semantics.

Criterion owns the question/required answer strength. Evaluation owns method and contextual compatibility.

Evidence strength MUST NOT exceed method/scope/coverage/assumption/uncertainty support.

Sample-based methods MUST NOT silently answer universal Criteria as though full population were proven. Approximate/sketch methods support only claims within preserved bounds. Utility remains task-scoped and disclosure-risk evidence remains threat-model scoped.

For Generation-required validation, method strength must be sufficient for the exact completion requirement.

## SYNC-11 — Evaluation operational realization

**Type:** operational realization + provenance.

Evaluation may use [Execution](../concepts/execution.md) for long-running/distributed work.

### Ownership

Evaluation owns:

- committed Criterion/method/input/scope semantics;
- methodological validity;
- coverage/assumption sufficiency;
- interpretability;
- Evaluation-level completion/failure/cancellation;
- association with Evidence.

Execution owns:

- logical operational state;
- Attempt history;
- operational progress/health;
- retry/resume/cancellation realization;
- partial examination/recovery associations;
- operational failure/unknown-state facts.

### Retry/resume rule

One committed Evaluation MAY span multiple Attempts. Retry/resume MUST NOT silently alter Criterion, subject/reference identity, method/configuration, sampling design, coverage, uncertainty semantics, or other material commitments.

For exhaustive/distributed validation, completed partitions or summaries may be reused only when the recovery contract can establish their identity, integrity, coverage, and compatibility with the same Evaluation.

A retried partition or repeated method execution MUST NOT cause duplicate observations to be counted twice unless the Evaluation method explicitly defines that behavior.

### Completion rule

`Execution.completed` MUST NOT automatically establish successful Evaluation.

A valid Evaluation that establishes an unfavorable result is successful Evaluation. Computational completion with invalid scope, broken assumptions, wrong reference, missing coverage, or uninterpretable output is not successful Evaluation merely because it produced numbers.

### Cancellation/unknown rule

Cancellation or unknown operational state may leave partial diagnostics but MUST NOT create Evidence answering the Criterion unless Evaluation can still establish a semantically valid result at the represented claim strength.

When Evaluation is required by a pending Generation completion barrier, unresolved Execution/Evaluation state leaves Generation pending rather than converting uncertainty to success.

## SYNC-12 — Evaluation produces Evidence

**Type:** production + provenance.

A semantically valid Evaluation establishes one or more [Evidence](../concepts/evidence.md) records when independently interpretable findings exist.

Evidence MUST preserve/reference exact Criterion revision, producing Evaluation, evaluated subject/reference identity, finding, logical scope, method/configuration, coverage, sampling/approximation, uncertainty/error/confidence, assumptions/limitations, claim-strength/applicability boundary, and relevant provenance.

Diagnostic output from failed/incomplete Evaluation MUST NOT masquerade as Evidence answering the Criterion.

### Claim-strength rule

Evidence strength MUST NOT exceed what the Evaluation method, scope, coverage, assumptions, and uncertainty support.

### Constraint/Condition completion use

When Generation completion depends on post-production validation:

- Evidence must refer to the exact candidate output;
- Evidence must answer the exact committed completion requirement;
- its claim strength must be sufficient;
- negative Evidence blocks completion when satisfaction is mandatory;
- indeterminate Evidence blocks completion when determination is mandatory;
- sample-only Evidence cannot support universal satisfaction unless the committed Criterion/rule explicitly defines statistical assurance as sufficient.

Generation, not Evidence, owns the completion-state transition.

Repeated Attempts/recovery MUST NOT create ambiguous duplicate authoritative Evidence for one semantic finding; physical recomputation may occur, but durable finding identity/history must remain coherent.

## SYNC-13 — Evidence external and Generation handoff

**Type:** controlled handoff.

Evidence may be consumed by Generation completion logic or external actors/systems making claims, restrictions, approvals, release/use decisions, or remediation decisions.

Evidence remains observation authority only and MUST NOT by itself become release/use authorization, formal privacy guarantee, anonymization certification, universal downstream fitness, or automatic Generation completion.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical state and MUST NOT duplicate full payloads or platform logs into a shadow source of truth.

For Execution/Attempt history, provenance SHOULD preserve stable references sufficient to explain, where material:

- associated domain activity identity;
- Execution identity and terminal operational outcome;
- Attempt identities/order/outcomes;
- platform job/run references without making them logical authority;
- retry/resume/checkpoint/recovery relationships;
- material resource/runtime/dependency context;
- cancellation request/outcome;
- indeterminate/lost-state reconciliation;
- operational failures material to domain outcome or reproducibility;
- promotion/use of recovered partial state where relevant.

Provenance should retain summarized typed facts/references rather than copying all task-level telemetry, logs, checkpoints, source rows, generated rows, or model payloads.

Domain-specific provenance requirements from prior phases remain in force, including Learning → Learned State derivation, Generation completion/promotion basis, Evaluation → Evidence production, and Evidence applicability history.

## SYNC-15 — Reproducibility-relevant commitment and operational history

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve/reference enough stable facts to state supported reproduction/comparison scope.

Learning, Generation, and Evaluation retain their previously specified source/semantic/Strategy/Constraint/Condition/Criterion/method/randomness/dependency facts where material.

002-F adds that operational history MAY also be reproduction-relevant when behavior can depend on:

- Attempt/retry count or ordering;
- checkpoint/resume point;
- partial recomputation;
- worker/partition topology;
- runtime/resource substitution;
- nondeterministic failure/recovery timing;
- external dependency/service behavior;
- duplicate physical execution and fencing/promotion decisions.

Execution MUST preserve/refer to those operational facts when they materially affect the supported reproduction/comparison claim, without turning every platform log into canonical reproducibility state.

Exactly-once physical execution is not assumed. Reproducibility claims must distinguish semantic equivalence from identical operational history where relevant.

No concept should duplicate all such facts under a generic `reproducibility` object solely for convenience.

## Non-synchronizations

The following MUST NOT mutate historical work automatically:

- new Data Meaning → historical Learned State, Generation, Evaluation, or Evidence;
- new Constraint → historical Learning, Generation, or Evidence;
- new Strategy version → existing Learned State or Generation provenance;
- source mutation → existing Learning/Learned State/direct-generation history;
- new Criterion revision → historical Evaluation or Evidence;
- newer Evaluation/Evidence → earlier Evidence observation;
- Learned State restriction/retirement/invalidation → historical Generation;
- Evidence supersession/staleness → external historical decision;
- later Condition/request changes → committed Generation;
- newer validation policy → historical Generation unless explicitly evaluated as a new question;
- new Attempt → committed domain semantics;
- platform-native retry/run numbering → SYNGAN logical Execution/Attempt identity;
- checkpoint existence → domain result existence;
- Execution completion → Learning/Generation/Evaluation completion;
- cancellation request → automatic domain cancellation;
- unknown platform state → assumed success or failure.

Further accepted refinements:

- retrying Learning, Generation, or Evaluation is not permission to change committed semantic specifications;
- materially different recovery inputs/artifacts/runtime behavior create a new semantic/compatibility question when they affect domain meaning;
- physical relocation/reserialization may preserve logical identity only when later representation contracts guarantee semantic equivalence;
- duplicate physical work is acceptable only when canonical promotion/side effects remain unambiguous;
- new Evidence may supersede an older finding for current use but MUST NOT rewrite what the older Evaluation observed.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Constraint revision may be bound by many activities;
- one Learning produces zero or one primary logical Learned State;
- one Learned State may contain many physical components and support many Generations;
- one Generation produces zero or one successful logical completed output result;
- one Criterion may serve many Evaluations;
- one Evaluation may produce zero or more independently interpretable Evidence records;
- one Evidence record represents one durable interpretable finding;
- one domain activity requiring operational realization has one primary logical Execution under the current model;
- one Execution contains one or more Attempts over its active history;
- one Attempt may map to one or many physical platform jobs/tasks/processes;
- one platform job is not assumed to equal one Attempt;
- Provenance contains many typed relationships.

## Synchronization economy assessment

The model continues to avoid pathological all-to-all coordination. Domain concepts own semantic commitment and completion. Execution owns operational realization. Attempt remains subordinate history. Retry/resume preserve semantics rather than creating new compatibility authority. Provenance records typed history without becoming duplicate platform telemetry. Exactly-once physical work is not required; single semantic promotion prevents duplicate authoritative domain results.