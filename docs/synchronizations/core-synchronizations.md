---
type: Synchronization Specification
title: SYNGAN Core Synchronizations
status: accepted
---

# SYNGAN Core Synchronizations

These rules are the canonical cross-concept coordination authority accepted at the end of Phase 001 and refined by later concept-specification phases.

A synchronization rule coordinates concept-owned state; it does not transfer ownership merely because another concept reads, validates, or records that state.

## SYNC-01 — Data Meaning revision binding

**Type:** reference/bind + provenance.

When Learning, Generation, or Evaluation crosses its semantic commitment boundary using [Data Meaning](../concepts/data-meaning.md), it MUST bind the exact relevant effective revision.

The binding freezes historical meaning for that activity without freezing future Data Meaning evolution.

A later meaning revision:

- affects future validation and new work only;
- MUST NOT retroactively reinterpret historical Learning, Generation, Learned State, Evaluation, or Evidence;
- MAY cause future reuse of historical Learned State/output to require new compatibility assessment, without rewriting original history.

Material inferred meaning relied upon by committed work MUST already be inspectable/attributable Data Meaning. An implementation MUST NOT satisfy this synchronization by retaining material semantics solely inside model-private preprocessing state.

If required Data Meaning is unresolved, conflicting, invalidated, or otherwise unavailable, the consuming activity MUST preserve that condition rather than silently inventing an implementation default.

Where required by traceability, Provenance records the exact meaning revision bound.

## SYNC-02 — Strategy selection and compatibility

**Type:** bind + contextual validation + provenance.

Learning or Generation validates the chosen [Synthesis Strategy](../concepts/synthesis-strategy.md) against bound Data Meaning, applicable [Constraints](../concepts/constraint.md), requested capabilities, and the committed deployment/dependency profile where material.

Strategy owns:

- declared capabilities;
- requirements;
- synthesis-relevant configuration;
- declared limitations;
- external artifact/network dependency profile;
- Strategy-specific reproducibility and material resource characteristics.

The activity owns the contextual validation result for its exact intended use.

Compatibility MUST NOT become globally mutable state on Strategy, Data Meaning, Constraint, or Learned State. A prior compatibility result MAY be reused only when the relevant bound revisions/context are demonstrably equivalent under the later specification.

Constraint support and Constraint satisfaction are different claims. Strategy capability may state that a class of rules can be enforced or processed; it does not by itself establish that a particular generated output satisfied a particular Constraint.

Network/dependency compatibility is similarly contextual. A Strategy declared `runtime-network dependent` is incompatible with an activity committed under a no-network profile. A missing local artifact MUST NOT be resolved by an undeclared automatic network call.

Where the activity commits, Provenance records the exact Strategy/configuration revision used and material dependency profile/artifact identity needed to explain or reproduce the activity.

## SYNC-03 — Constraint binding and handling disposition

**Type:** bind + contextual validation + provenance.

An activity determines applicability of [Constraint](../concepts/constraint.md) revisions using the activity scope, bound Data Meaning, and other explicit prerequisites. The Constraint owns its rule, scope, semantic dependencies, and authority; the activity owns the contextual applicability result.

When an applicable Constraint is committed, the activity MUST bind the exact revision and preserve how the rule will be handled where relevant.

Canonical handling dispositions include:

- **enforced** — the activity/method intends to enforce the rule during operation;
- **validated later** — satisfaction is intended to be established in a later validation path;
- **unsupported** — the selected method cannot honor/assess the rule as required;
- **not applicable** — contextual validation establishes that the rule does not apply to the activity scope.

A later phase MAY refine this vocabulary without changing the ownership rule.

Unsupported required Constraints MUST remain visible. They MUST NOT be silently omitted because an implementation lacks support.

Handling disposition MUST NOT be confused with actual satisfaction. In particular:

- `enforced` is not automatically Evidence that every relevant output satisfied the rule;
- `validated later` does not mean satisfied until the required validation has occurred;
- unknown/indeterminate applicability or satisfiability MUST NOT be converted to success.

If required Data Meaning is insufficient to interpret a Constraint, the activity MUST preserve that unresolved dependency rather than fabricate semantics.

Known Constraint conflicts or indeterminate satisfiability remain contextual validation facts and MUST NOT mutate the canonical Constraint definitions.

Where required by traceability, Provenance records the bound rule revisions and material handling disposition.

## SYNC-04 — Learning operational realization

**Type:** operational realization + provenance.

[Learning](../concepts/learning.md) may use [Execution](../concepts/execution.md) for operational work. Execution owns attempts/progress/retry/failure; Learning owns semantic completion. `Execution.completed` MUST NOT by itself establish `Learning.completed`.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version. Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

## SYNC-06 — Generation commitment and compatibility

**Type:** bind + validation + provenance.

At semantic commitment, [Generation](../concepts/generation.md) binds its requested intent/Conditions, relevant Data Meaning, applicable Constraint revisions, Strategy/configuration, Learned State when required, reproducibility-relevant request state, and material Strategy dependency/network requirements.

Constraint applicability and handling MUST be explicit enough that required unsupported or unresolved rules cannot disappear from Generation merely because a Strategy cannot process them.

Condition remains Generation-owned request direction. Constraint remains independent prescriptive authority even if implementation later uses shared predicate/expression machinery.

Strategies requiring no reusable Learned State MAY generate directly without fabricated Learning or Learned State occurrences.

A Generation committed under a no-network/no-egress deployment profile MUST NOT silently invoke a runtime-network-dependent Strategy, fetch an undeclared artifact, or switch to a remote fallback. Any fallback that changes synthesis behavior is an explicit Strategy/configuration choice and must be bound as such.

Phase 002-D will refine how Constraint handling/satisfaction participates in Generation semantic completion while preserving these ownership rules.

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

Constraint-satisfaction Evidence, when produced, records an observation about a specific bound Constraint revision/output/method. It does not become authority for the Constraint definition itself.

## SYNC-13 — Evidence external handoff

**Type:** external handoff.

Evidence may inform claims, restrictions, approvals, or release/use decisions outside SYNGAN. Evidence itself MUST NOT be interpreted as authorization, and external decision authority is not imported into Evidence.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical concept state and MUST NOT duplicate whole state payloads into a shadow source of truth.

Where a transition requires provenance, the committed transition and required provenance fact MUST NOT silently diverge. The representation mechanism remains deferred.

For Data Meaning inference or Constraint applicability/handling, provenance SHOULD preserve the stable references and material context needed to explain the decision without copying row-level source data or full concept payloads.

For Synthesis Strategy, provenance SHOULD preserve the bound Strategy/configuration and material local-artifact/network dependency facts where they affect behavior, reproducibility, or enterprise review. Remote locations alone are not sufficient historical identity when external content may change.

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve or reference enough stable facts to state the supported reproduction/comparison scope. Depending on the activity this may include source/output identity, Data Meaning revision, Strategy/configuration, Constraint/Criterion revisions, Learned State identity, seeds/randomness policy, implementation/software identity, runtime/environment facts, sampling/approximation semantics, external dependency profile, and material local/pretrained artifact identity.

No concept should duplicate these under a generic `reproducibility` state object merely for convenience.

A URL or remote service name alone MUST NOT be treated as sufficient artifact identity for a reproducibility claim when the referenced content/behavior can change.

## Non-synchronizations

The following MUST NOT mutate historical work automatically:

- new Data Meaning → historical Learned State;
- new Constraint → historical Generation;
- new Strategy version → existing Learned State provenance;
- new Criterion revision → historical Evidence;
- Learned State retirement → historical Generation;
- Evidence supersession → external historical decision.

Additional 002-A clarification:

- new inferred Data Meaning MUST NOT overwrite an authoritative declaration automatically;
- a new Data Meaning revision MUST NOT rewrite the semantic prerequisites of historical Constraint bindings;
- a newer Constraint revision MAY be evaluated against historical output as a new Evaluation question, but MUST NOT be represented as having governed the original Generation.

Additional 002-B clarification:

- changed Strategy dependency/network requirements MUST NOT rewrite historical activities;
- a deployment policy change MAY reject future use of an otherwise historical-valid Strategy without changing what earlier work used;
- locally replacing an external artifact with a materially different artifact is a new compatibility/reproducibility context, not silent equivalence.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Constraint revision may be bound by many activities;
- one activity may bind many applicable Constraints;
- one Learning produces zero or one primary Learned State under the current model;
- one Learned State may support many Generations;
- one Generation has one logical completed synthetic-output result, even when physically partitioned;
- one Criterion may serve many Evaluations;
- one Evaluation may produce multiple independently interpretable Evidence records;
- one Execution contains one or more Attempts;
- Provenance contains many typed relationships.

## Synchronization economy assessment

The retained set avoids pathological all-to-all synchronization because most relationships are one of:

- stable revision/reference binding;
- local contextual validation;
- one-way result production;
- a narrow activity↔Execution lifecycle pair;
- append/traverse Provenance.

Data Meaning, Constraint, and Synthesis Strategy remain control-plane authorities. Contextual inference, applicability, compatibility, deployment-profile compatibility, enforcement, and satisfaction results MUST remain with the concepts/activities that produce them instead of creating global mutable coordination hubs.