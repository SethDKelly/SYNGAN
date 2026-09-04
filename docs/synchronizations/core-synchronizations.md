---
type: Synchronization Specification
title: SYNGAN Core Synchronizations
status: accepted
---

# SYNGAN Core Synchronizations

These rules are the canonical cross-concept coordination authority accepted at the end of Phase 001.

## SYNC-01 — Data Meaning revision binding

**Type:** reference/bind + provenance.

When Learning, Generation, or Evaluation commits using Data Meaning, it MUST bind the exact relevant revision. Later meaning changes affect future work only and MUST NOT retroactively reinterpret historical Learned State, Generation, or Evidence.

## SYNC-02 — Strategy selection and compatibility

**Type:** bind + contextual validation + provenance.

Learning or Generation validates the chosen [Synthesis Strategy](../concepts/synthesis-strategy.md) against bound Data Meaning, applicable Constraints, and requested capabilities. Strategy owns declared capabilities/configuration; the activity owns its contextual validation result. Global mutable compatibility state is prohibited.

## SYNC-03 — Constraint binding and handling disposition

**Type:** bind + contextual validation + provenance.

An activity binds applicable [Constraint](../concepts/constraint.md) revisions and records how each will be handled where relevant: enforced, validated later, unsupported, or not applicable. Unsupported required Constraints MUST remain visible.

## SYNC-04 — Learning operational realization

**Type:** operational realization + provenance.

[Learning](../concepts/learning.md) may use [Execution](../concepts/execution.md) for operational work. Execution owns attempts/progress/retry/failure; Learning owns semantic completion. `Execution.completed` MUST NOT by itself establish `Learning.completed`.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version. Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

## SYNC-06 — Generation commitment and compatibility

**Type:** bind + validation + provenance.

At semantic commitment, [Generation](../concepts/generation.md) binds its requested intent/Conditions, relevant Data Meaning, Constraints, Strategy/configuration, Learned State when required, and reproducibility-relevant request state. Strategies requiring no reusable Learned State MAY generate directly without fabricated Learning.

## SYNC-07 — Generation operational realization

**Type:** operational realization + provenance.

Generation may use Execution for operational work. Execution owns operational status; Generation owns whether valid requested output was fulfilled. Partial/incomplete output MUST remain distinguishable from completed output.

## SYNC-08 — Generation produces synthetic output reference

**Type:** production + provenance.

Successful Generation associates a stable logical reference to completed synthetic output. Stable physical identity/location/version mechanics are representation/integration obligations and MUST NOT create a generic Artifact/Dataset concept by implication.

## SYNC-09 — Evaluation Criterion binding

**Type:** bind + provenance.

[Evaluation](../concepts/evaluation.md) MUST bind the exact [Evaluation Criterion](../concepts/evaluation-criterion.md) revision it answers. Later Criterion revisions MUST NOT reinterpret historical Evidence.

## SYNC-10 — Evaluation method compatibility

**Type:** validation + provenance.

Evaluation validates that its method can address the bound Criterion under the declared scope. Sampling, approximation, bounded analysis, or other material methodological limits MUST remain visible in resulting Evidence.

## SYNC-11 — Evaluation operational realization

**Type:** operational realization + provenance.

Evaluation may use Execution for operational work. Execution completion MUST NOT automatically establish a successful Evaluation; Evaluation owns methodological/domain validity.

## SYNC-12 — Evaluation produces Evidence

**Type:** production + provenance.

A semantically valid Evaluation result establishes [Evidence](../concepts/evidence.md) containing/referencing the Criterion, method, inputs, scope, result, limitations/uncertainty, and relevant provenance. Diagnostic output from a failed Evaluation MUST NOT masquerade as Evidence answering the Criterion.

## SYNC-13 — Evidence external handoff

**Type:** external handoff.

Evidence may inform claims, restrictions, approvals, or release/use decisions outside SYNGAN. Evidence itself MUST NOT be interpreted as authorization, and external decision authority is not imported into Evidence.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical concept state and MUST NOT duplicate whole state payloads into a shadow source of truth.

Where a transition requires provenance, the committed transition and required provenance fact MUST NOT silently diverge. The representation mechanism remains deferred.

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve or reference enough stable facts to state the supported reproduction/comparison scope. Depending on the activity this may include source/output identity, Data Meaning, Strategy/configuration, Constraint/Criterion revisions, Learned State identity, seeds/randomness policy, implementation/software identity, runtime/environment facts, and sampling/approximation semantics.

No concept should duplicate these under a generic `reproducibility` state object merely for convenience.

## Non-synchronizations

The following MUST NOT mutate historical work automatically:

- new Data Meaning → historical Learned State;
- new Constraint → historical Generation;
- new Strategy version → existing Learned State provenance;
- new Criterion revision → historical Evidence;
- Learned State retirement → historical Generation;
- Evidence supersession → external historical decision.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Learning produces zero or one primary Learned State under the current model;
- one Learned State may support many Generations;
- one Generation has one logical completed synthetic-output result, even when physically partitioned;
- one Criterion may serve many Evaluations;
- one Evaluation may produce multiple independently interpretable Evidence records;
- one Execution contains one or more Attempts;
- Provenance contains many typed relationships.
