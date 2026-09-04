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

Later meaning revisions affect future validation/new work only and MUST NOT retroactively reinterpret historical Learning, Learned State, Generation, Evaluation, or Evidence.

Material inferred meaning relied upon by committed work MUST already be inspectable/attributable Data Meaning. Required unresolved/conflicting/invalidated meaning MUST remain explicit rather than being replaced by an implementation default.

Where required by traceability, Provenance records the exact meaning revision bound.

## SYNC-02 — Strategy selection and compatibility

**Type:** bind + contextual validation + provenance.

Learning or Generation validates the chosen [Synthesis Strategy](../concepts/synthesis-strategy.md) against bound Data Meaning, applicable [Constraints](../concepts/constraint.md), requested capabilities, Learned State when applicable, and the committed deployment/dependency profile.

Strategy owns declared capabilities, requirements, synthesis-relevant configuration, limitations, external artifact/network dependency profile, Strategy-specific reproducibility facts, and material resource characteristics.

The activity owns the contextual compatibility result for its exact intended use.

Compatibility MUST NOT become globally mutable state on Strategy, Data Meaning, Constraint, or Learned State. Prior compatibility MAY be reused only when the relevant context/revisions are materially equivalent.

Constraint support is not proof of Constraint satisfaction. Network/dependency compatibility is likewise contextual: a runtime-network-dependent Strategy is incompatible with a no-network committed activity, and a missing local artifact MUST NOT trigger undeclared network acquisition.

Where the activity commits, Provenance records the exact Strategy/configuration and material dependency/artifact identity needed to explain the activity.

## SYNC-03 — Constraint binding and handling disposition

**Type:** bind + contextual validation + provenance.

An activity determines applicability of [Constraint](../concepts/constraint.md) revisions using its scope, bound Data Meaning, and explicit prerequisites. Constraint owns rule/scope/semantic dependencies/authority; the activity owns contextual applicability and handling.

When an applicable Constraint is committed, the activity MUST bind the exact revision and preserve handling where relevant. Canonical dispositions include:

- **enforced**;
- **validated later**;
- **unsupported**;
- **not applicable**.

Unsupported required Constraints MUST remain visible. Handling MUST NOT be confused with satisfaction; unknown/indeterminate applicability or satisfiability MUST NOT be converted to success.

If required Data Meaning is insufficient to interpret a Constraint, the unresolved dependency remains explicit. Known conflicts or indeterminate satisfiability remain contextual facts and do not mutate Constraint authority.

Where required by traceability, Provenance records the bound revisions and material handling disposition.

## SYNC-04 — Learning operational realization

**Type:** operational realization + provenance.

[Learning](../concepts/learning.md) may use [Execution](../concepts/execution.md) for long-running/distributed work.

### Learning owns

- semantic commitment and bound Learning specification;
- whether the intended reusable state was validly derived;
- Learning-level completion/failure/cancellation;
- association with the resulting Learned State.

### Execution owns

- logical operational state;
- Attempt history;
- progress/health;
- retry/resume/cancellation realization;
- operational failure facts.

One committed Learning MAY span multiple Attempts. Retry/resume MUST NOT silently alter committed source, Data Meaning, Strategy/configuration, Constraint handling, sampling/approximation, dependency profile, or other material Learning semantics.

A failed Attempt does not automatically fail Learning if valid retry/resume remains possible.

`Execution.completed` MUST NOT by itself establish `Learning.completed`.

Checkpoint/intermediate material produced by Execution/Attempts MUST NOT be interpreted as Learned State unless Learning later semantically validates/promotes it as the successful reusable result.

## SYNC-05 — Learning produces Learned State

**Type:** production + provenance.

Successful semantic Learning establishes a new [Learned State](../concepts/learned-state.md) identity/version.

Learning may establish Learned State only when:

- the committed Learning specification was realized sufficiently under Strategy semantics;
- the result is distinguishable from partial/checkpoint/recovery state;
- no unresolved terminal defect invalidates the reusable result;
- a stable logical Learned State identity can be created;
- intrinsic reuse requirements/limitations/dependencies are available enough for later validation;
- required provenance can be recorded consistently.

Failed, cancelled, or incomplete Learning MUST NOT establish usable Learned State.

Under the current model one Learning produces zero or one **primary logical Learned State**, even if the physical representation contains many files, partitions, tensors, tables, statistics, encoders, or other components.

Learned State MUST retain stable references sufficient to trace its producing Learning, source context, Data Meaning, Strategy/configuration, applicable Constraint context, material sampling/approximation, and dependency/artifact facts without duplicating every upstream authority payload.

Later retirement/restriction/invalidation affects future use and MUST NOT rewrite the historical Learning or Generations that legitimately used the state.

## SYNC-06 — Generation commitment and compatibility

**Type:** bind + validation + provenance.

At semantic commitment, [Generation](../concepts/generation.md) binds requested intent/Conditions, relevant Data Meaning, applicable Constraints, Strategy/configuration, Learned State when required, reproducibility-relevant request state, and material Strategy dependency/network requirements.

When Learned State is used, Generation performs contextual reuse validation against the requested context. Learned State owns intrinsic requirements/limitations/status; Generation owns the compatibility result.

Validation may consider:

- Strategy/configuration compatibility;
- semantic/Data Meaning requirements;
- Conditions/request semantics;
- applicable Constraints;
- Learned State restriction/retirement/invalidation status;
- required base/pretrained artifact identity;
- runtime/software compatibility where material;
- deployment/network policy.

A later Data Meaning/Constraint/Strategy revision MUST NOT mutate Learned State history. It creates a new future-use compatibility question.

Ordinary Generation reuse MUST NOT silently mutate/adapt Learned State. Material adaptation must produce an explicitly distinguishable new result/activity rather than altering the historical Learned State identity.

Strategies requiring no reusable Learned State MAY generate directly without fabricated Learning/Learned State occurrences.

A no-network/no-egress Generation MUST NOT silently fetch missing Learned State dependencies, invoke a remote fallback, or replace a required base artifact with materially different content.

Phase 002-D refines Generation completion and Constraint satisfaction while preserving these ownership rules.

## SYNC-07 — Generation operational realization

**Type:** operational realization + provenance.

Generation may use Execution for operational work. Execution owns operational state; Generation owns whether the requested synthetic output was semantically fulfilled. Partial/incomplete output MUST remain distinguishable from completed output.

## SYNC-08 — Generation produces synthetic output reference

**Type:** production + provenance.

Successful Generation associates a stable logical reference to completed synthetic output. Stable physical location/version mechanics are representation/integration obligations and MUST NOT imply a generic Artifact/Dataset concept.

## SYNC-09 — Evaluation Criterion binding

**Type:** bind + provenance.

[Evaluation](../concepts/evaluation.md) MUST bind the exact [Evaluation Criterion](../concepts/evaluation-criterion.md) revision it answers. Later Criterion revisions MUST NOT reinterpret historical Evidence.

## SYNC-10 — Evaluation method compatibility

**Type:** validation + provenance.

Evaluation validates that its method can address the bound Criterion under the declared scope. Sampling, approximation, bounded analysis, or other material methodological limitations MUST remain visible in Evidence.

## SYNC-11 — Evaluation operational realization

**Type:** operational realization + provenance.

Evaluation may use Execution for operational work. Execution completion MUST NOT automatically establish successful Evaluation; Evaluation owns methodological/domain validity.

## SYNC-12 — Evaluation produces Evidence

**Type:** production + provenance.

A semantically valid Evaluation result establishes [Evidence](../concepts/evidence.md) containing/referencing Criterion, method, inputs, scope, result, limitations/uncertainty, and relevant provenance.

Diagnostic output from failed Evaluation MUST NOT masquerade as Evidence answering the Criterion.

Constraint-satisfaction Evidence records an observation about a specific bound Constraint revision/output/method and does not become Constraint authority.

## SYNC-13 — Evidence external handoff

**Type:** external handoff.

Evidence may inform claims, restrictions, approvals, or release/use decisions outside SYNGAN. Evidence itself MUST NOT be interpreted as authorization, and external decision authority is not imported into Evidence.

## SYNC-14 — Provenance recording at material transitions

**Type:** historical/provenance.

Material committed transitions MUST record typed derivation/context relationships when required by SYNGAN traceability guarantees. [Provenance](../concepts/provenance.md) references canonical concept state and MUST NOT duplicate full state payloads into a shadow source of truth.

Where a transition requires provenance, the committed transition and required provenance fact MUST NOT silently diverge.

Material Learning/Learned State provenance SHOULD preserve stable references sufficient to explain:

- source state/version/fingerprint context;
- Data Meaning revision;
- Strategy/configuration;
- applicable Constraint revisions/handling;
- material sampling/approximation choices;
- dependency/network profile and base/pretrained artifact identity;
- Learning → Learned State production;
- material Execution/Attempt facts required for failure explanation or reproducibility;
- Learned State restriction/retirement/invalidation history where material.

Provenance MUST NOT copy source rows or entire model/state payloads merely to satisfy traceability.

## SYNC-15 — Reproducibility-relevant commitment snapshot

**Type:** cross-cutting bind + provenance; not a concept.

At reproducibility-relevant commitment, activities MUST preserve/reference enough stable facts to state the supported reproduction/comparison scope.

For Learning this may include source identity/version/fingerprint semantics, Data Meaning, Strategy/configuration, Constraints, sampling/approximation, seeds/randomness policy, implementation/software identity, runtime/environment facts, dependency profile, and local/pretrained artifact identity.

For Learned State, the effective reproducibility story MUST preserve how the state was derived and any base/runtime artifacts required for reuse.

No concept should duplicate these facts under a generic `reproducibility` object solely for convenience.

A mutable table name, URL, or remote service name alone MUST NOT be treated as sufficient historical identity when underlying data/content/behavior can change materially.

## Non-synchronizations

The following MUST NOT mutate historical work automatically:

- new Data Meaning → historical Learned State;
- new Constraint → historical Learning or Generation;
- new Strategy version → existing Learned State provenance;
- source mutation → existing Learning/Learned State source history;
- new Criterion revision → historical Evidence;
- Learned State retirement/restriction/invalidation → historical Generation;
- Evidence supersession → external historical decision.

Additional refinements:

- new inferred Data Meaning MUST NOT overwrite an authoritative declaration automatically;
- newer Constraint revisions MAY be evaluated against old output but MUST NOT be represented as governing original production;
- changed Strategy dependency/network requirements MUST NOT rewrite historical activities;
- deployment policy changes MAY reject future Strategy/Learned State use without changing prior history;
- replacing a required pretrained/base artifact with materially different content is a new compatibility/reproducibility context, not silent equivalence;
- retrying Learning via a new Attempt is not permission to change committed Learning semantics;
- physical relocation/reserialization of Learned State is not a semantic state change when logical identity/behavior are preserved by the later representation contract.

## Cardinality guidance

These are conceptual expectations, not storage schemas:

- one Data Meaning revision may serve many activities;
- one Strategy configuration may serve many activities;
- one Constraint revision may be bound by many activities;
- one activity may bind many applicable Constraints;
- one committed Learning binds one material source/semantic/Strategy context;
- one Learning produces zero or one primary logical Learned State under the current model;
- one Learned State may contain many physical components;
- one Learned State may support many Generations;
- one Generation has one logical completed synthetic-output result even when physically partitioned;
- one Criterion may serve many Evaluations;
- one Evaluation may produce multiple independently interpretable Evidence records;
- one Execution contains one or more Attempts;
- Provenance contains many typed relationships.

## Synchronization economy assessment

The retained set avoids pathological all-to-all synchronization because most relationships remain stable revision/reference binding, contextual validation, one-way result production, a narrow activity↔Execution lifecycle pair, or append/traverse Provenance.

Data Meaning, Constraint, and Synthesis Strategy remain declarative control-plane authorities. Learning owns its committed derivation context and semantic outcome. Learned State owns the durable logical result and intrinsic reuse requirements. Generation owns contextual reuse compatibility. Execution owns operational realization. Provenance explains relationships without becoming duplicate authority.