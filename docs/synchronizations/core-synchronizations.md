---
type: Synchronization Specification
title: SYNGAN Core Synchronizations
status: accepted
---

# SYNGAN Core Synchronizations

These rules are the canonical cross-concept coordination authority accepted at the end of Phase 001 and refined by later concept-specification phases.

A synchronization coordinates concept-owned state; it does not transfer ownership merely because another concept reads, validates, or records that state.

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

Learning owns semantic commitment/outcome and association with Learned State. Execution owns operational state, Attempts, progress, retry/resume, and operational failures.

One committed Learning MAY span multiple Attempts. Retry/resume MUST NOT alter committed Learning semantics.

`Execution.completed` MUST NOT by itself establish `Learning.completed`.

Checkpoint/intermediate material MUST NOT become Learned State unless Learning semantically validates/promotes it as the successful result.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version.

Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

Under the current model one Learning produces zero or one primary logical Learned State even when its physical representation contains many components.

Learned State retains stable references sufficient to trace producing Learning, source context, Data Meaning, Strategy/configuration, applicable Constraint context, material sampling/approximation, and dependency/artifact facts without duplicating all upstream state.

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

Generation may use Execution for long-running/distributed work.

Generation owns committed request semantics, semantic progress/result, fulfillment of mandatory Conditions/Constraints, promotion of candidate data, terminal domain outcome, and completed output association.

Execution owns operational state, Attempts, progress, retry/resume/cancellation realization, and operational failures.

One committed Generation MAY span multiple Attempts; retries MUST NOT alter committed semantics.

`Execution.completed` MUST NOT by itself establish `Generation.completed`.

Partial materialization, complete candidate materialization, completed output, and abandoned/quarantined materialization remain distinct.

## SYNC-08 — Generation produces synthetic output reference

**Type:** production + provenance.

A successful Generation establishes one logical completed synthetic-output result, even when physically distributed across many files/objects/tables/partitions.

A stable completed-output reference may be associated only when the Generation completion contract is satisfied. Candidate/provisional references must remain explicitly non-final.

Successful completion requires, where applicable, committed-specification consistency, compatible synthesis basis, no forbidden dependency behavior, materially complete quantity/scope, fulfilled mandatory Conditions, completion-sufficient satisfaction basis for every applicable required Constraint, no mandatory indeterminacy/violation, clear non-partial identity, consistent provenance, and no terminal semantic defect.

`completed with limitations` may cover only explicitly permitted best-effort/approximate limitations and MUST NOT override mandatory failures.

## SYNC-09 — Evaluation Criterion binding

**Type:** bind + provenance.

[Evaluation](../concepts/evaluation.md) MUST bind the exact [Evaluation Criterion](../concepts/evaluation-criterion.md) revision it answers.

The binding includes the Criterion's material question, subject/scope, reference context, and answer-sufficiency/claim-strength semantics where those affect interpretation.

Later Criterion revisions MUST NOT reinterpret historical Evidence.

When a Criterion is derived from a Constraint or Generation Condition, the Evaluation also binds the exact originating rule/request semantics needed to preserve what was actually tested. Criterion does not take ownership of the Constraint or Condition.

## SYNC-10 — Evaluation method compatibility

**Type:** contextual validation + provenance.

Evaluation validates that its selected method can legitimately address the bound Criterion under the declared inputs, logical scope, coverage, sampling/approximation model, assumptions, and uncertainty semantics.

The Criterion owns the question and required answer strength. Evaluation owns the method and contextual compatibility assessment.

Method compatibility MUST account for claim strength. In particular:

- exhaustive/universal Criteria require a method capable of supporting that scope unless the Criterion itself permits bounded/statistical assurance;
- sample-based methods MUST NOT silently answer a universal Criterion as though the full population was proven;
- approximation/sketch methods may support only claims within their preserved bounds;
- task-specific utility methods support the stated task/use context, not universal utility;
- disclosure-risk methods support the stated threat model/attacker assumptions, not universal privacy.

Sampling, approximation, coverage, and methodological limitations MUST remain visible in resulting Evidence.

For Generation-required validation, method strength must be sufficient for the exact committed Condition/Constraint completion requirement. A method that can only produce weaker or indeterminate Evidence does not satisfy that completion requirement merely because it executed successfully.

## SYNC-11 — Evaluation operational realization

**Type:** operational realization + provenance.

Evaluation may use Execution for long-running/distributed work.

### Evaluation owns

- committed Criterion/method/input/scope semantics;
- methodological validity;
- whether assumptions/coverage remained sufficient;
- whether result is interpretable;
- Evaluation-level completion/failure/cancellation;
- association with Evidence.

### Execution owns

- operational state;
- Attempt history;
- progress/health;
- retry/resume/cancellation realization;
- operational failure facts.

One committed Evaluation MAY span multiple Attempts. Retry/resume MUST NOT silently alter Criterion, subject/reference inputs, method/configuration, sampling design, coverage, uncertainty semantics, or other material Evaluation commitments.

`Execution.completed` MUST NOT automatically establish successful Evaluation.

A valid Evaluation that establishes an unfavorable result is still a successful Evaluation. A computationally completed method with invalid scope, broken assumptions, wrong references, or uninterpretable output is not successful Evaluation merely because it produced numbers.

## SYNC-12 — Evaluation produces Evidence

**Type:** production + provenance.

A semantically valid Evaluation establishes one or more [Evidence](../concepts/evidence.md) records when independently interpretable findings exist.

Evidence MUST preserve/reference enough information to identify:

- exact Criterion revision;
- producing Evaluation;
- evaluated subject/candidate output/Learned State identity;
- reference/baseline identity where applicable;
- observed finding/result;
- logical scope/population;
- method/configuration;
- coverage model;
- sampling/approximation semantics;
- uncertainty/error/confidence where applicable;
- assumptions and limitations;
- claim-strength/applicability boundary;
- relevant provenance.

Diagnostic output from a failed Evaluation MUST NOT masquerade as Evidence answering the Criterion.

### Claim-strength rule

Evidence strength MUST NOT exceed what the Evaluation's method, scope, coverage, assumptions, and uncertainty support.

Relevant forms include exhaustive/universal, deterministic bounded/certificate, statistical, approximate/sketch, and diagnostic/partial Evidence. These are conceptual distinctions rather than a required API enum.

### Constraint/Condition completion use

Constraint-satisfaction Evidence records an observation about a specific bound Constraint revision, exact candidate output, and method. It does not become Constraint authority or global satisfaction state.

Condition-fulfillment Evidence similarly remains tied to the exact committed Generation Condition.

When Generation completion depends on post-production validation:

- Evidence must refer to the exact candidate output being promoted;
- Evidence must answer the exact committed completion requirement;
- its claim strength must be sufficient for that requirement;
- negative Evidence blocks completion when satisfaction is mandatory;
- indeterminate Evidence blocks completion when determination is mandatory;
- sample-only Evidence cannot support universal satisfaction unless the committed Criterion/rule explicitly defines statistical assurance as sufficient.

Generation, not Evidence, owns the final completion-state transition.

## SYNC-13 — Evidence external and Generation handoff

**Type:** controlled handoff.

Evidence may be consumed by Generation completion logic or by external actors/systems making claims, restrictions, approvals, release/use decisions, or remediation decisions.

Evidence remains observation authority only.

It MUST NOT be interpreted by itself as:

- release/use authorization;
- formal privacy guarantee;
- anonymization certification;
- universal downstream fitness;
- automatic Generation completion independent of Generation's contract.

The same Evidence may legitimately produce different external decisions under different policies.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical state and MUST NOT duplicate full payloads into a shadow source of truth.

For Evaluation/Evidence, provenance SHOULD preserve stable references sufficient to explain:

- Criterion revision and authority;
- evaluated subject and reference/baseline identities;
- method/configuration/version;
- logical scope/coverage;
- sampling/approximation/randomness semantics;
- material Data Meaning/Constraint/Condition context;
- dependency/network/software/runtime facts where behaviorally material;
- Execution/Attempt facts required for failure/reproducibility explanation;
- Evaluation → Evidence production;
- Evidence supersession/staleness/invalidation where material;
- Generation completion use where Evidence formed part of the promotion basis.

Provenance MUST NOT copy source/synthetic rows, complete detailed validation output, or full model/state payloads merely to satisfy traceability.

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve/reference enough stable facts to state supported reproduction/comparison scope.

For Learning this includes source/semantic/Strategy/Constraint/sampling/randomness/dependency facts where material.

For Generation this includes Data Meaning, Strategy/configuration, Learned State or direct input/source identity, Constraints, Conditions, quantity/scope, randomness, software/runtime/dependencies, partition/distribution semantics, retry/recovery facts, and approximation/tolerance semantics where material.

For Evaluation this may include Criterion revision, subject/reference identity, method/version/configuration, logical scope/coverage, sampling design, randomness, approximation/error semantics, software/runtime/dependency identity, and uncertainty calculation.

For Evidence, the effective reproduction story MUST preserve enough producing context to state whether the finding is exactly reproducible, statistically reproducible, approximately recomputable within bounds, only qualitatively comparable, or not meaningfully reproducible.

No concept should duplicate all such facts under a generic `reproducibility` object merely for convenience.

Mutable table names, aliases, URLs, or service names alone MUST NOT be treated as sufficient identity when underlying content/behavior can change materially.

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
- newer validation policy → historical Generation unless explicitly evaluated as a new question.

Further accepted refinements:

- new inferred Data Meaning MUST NOT overwrite an authoritative declaration automatically;
- newer Constraint revisions MAY be evaluated against old output but MUST NOT be represented as governing original production;
- changed Strategy dependency/network requirements MUST NOT rewrite historical activities;
- deployment-policy changes MAY reject future use without changing prior history;
- materially different pretrained/base artifacts create new compatibility/reproducibility context;
- retrying Learning, Generation, or Evaluation is not permission to change committed semantic specifications;
- physical relocation/reserialization of Learned State/completed output may preserve logical identity only when later representation contracts guarantee semantic equivalence;
- new Evidence may supersede an older finding for current use but MUST NOT rewrite what the older Evaluation observed.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Constraint revision may be bound by many activities;
- one activity may bind many applicable Constraints;
- one Learning produces zero or one primary logical Learned State;
- one Learned State may contain many physical components and support many Generations;
- one Generation produces zero or one successful logical completed output result;
- one completed output may have many physical partitions/components;
- one Criterion may serve many Evaluations;
- one Evaluation may bind one or more compatible Criteria where method semantics support that grouping;
- one Evaluation may produce zero or more independently interpretable Evidence records;
- one Evidence record represents one durable interpretable finding;
- one Execution contains one or more Attempts;
- Provenance contains many typed relationships.

## Synchronization economy assessment

The retained model continues to avoid pathological all-to-all synchronization. Most relationships are stable reference binding, contextual validation, one-way result production, a narrow activity↔Execution pair, or append/traverse Provenance.

Data Meaning, Constraint, Synthesis Strategy, and Evaluation Criterion remain declarative authorities. Learning owns derivation semantics. Learned State owns reusable state. Generation owns request/Condition semantics and output completion. Evaluation owns examination method/lifecycle. Evidence owns durable findings and claim-strength limits. Execution owns operational realization. Provenance explains history without becoming duplicate authority.