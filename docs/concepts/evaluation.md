---
type: Concept
title: Evaluation
status: accepted
---

# Evaluation

## Purpose

Examine explicit [Evaluation Criteria](evaluation-criterion.md) using defined methods, inputs, scope, and uncertainty semantics in order to produce inspectable [Evidence](evidence.md).

Evaluation exists because measurement is an activity with its own commitments, prerequisites, scale behavior, and failure modes. A metric invocation is not automatically a valid examination, and computational success is not enough to establish that the intended Criterion was actually answered.

## Concept boundary

Evaluation is **examination-method and examination-lifecycle authority**.

It owns:

- the committed Evaluation specification;
- bound Criterion revisions;
- method/metric/test identity and configuration;
- input/reference identities;
- logical evaluation scope;
- sampling, coverage, approximation, and uncertainty semantics;
- method assumptions and known limitations;
- semantic lifecycle and outcome;
- association with Evidence.

It does not own:

- the Criterion question itself;
- Constraint or Generation Condition authority;
- durable Evidence semantics after production;
- generic Execution/Attempt state;
- external release/use approval;
- privacy guarantees merely because a privacy-related method was run.

## Evaluation state model

An Evaluation is one logical committed examination and may produce zero or more independently interpretable Evidence records.

### Proposed specification

Before commitment, an actor may define:

- one or more Criteria to be answered where method semantics permit;
- subject/output/Learned State/source/reference inputs;
- method/metric/test selection;
- method configuration;
- scope/population/cohort;
- coverage model;
- sampling design;
- approximation/sketch/bounding semantics;
- uncertainty/confidence semantics;
- deployment/network/dependency requirements;
- reproducibility/randomness intent;
- expected Evidence form.

A representation may expose separate metric requests or grouped Evaluation specifications; no API shape is implied.

### Lifecycle

A materially meaningful distinction must exist among states equivalent to:

- **draft/proposed** — specification still editable;
- **validated/ready** — method and prerequisites are known sufficient enough for commitment;
- **committed** — material Evaluation semantics fixed historically;
- **evaluating** — operational examination in progress;
- **completed** — method executed and produced semantically interpretable Evidence answering the bound Criterion to the strength actually supported;
- **completed with limitations** — Evaluation completed but the Evidence is explicitly limited, approximate, partial, or inconclusive in ways allowed by the committed Evaluation specification;
- **failed** — Evaluation could not validly produce Evidence answering the intended Criterion;
- **cancelled** — examination terminated before semantic completion.

A completed Evaluation may produce Evidence whose substantive answer is negative, violated, poor, risky, or otherwise unfavorable. Evaluation success means the examination was validly performed, **not** that the evaluated subject passed.

## Semantic commitment

At commitment, Evaluation binds the exact material context needed to interpret its result.

Where applicable this includes:

- Criterion revision(s);
- evaluated subject/output/Learned State identity;
- reference/source/baseline identity;
- relevant Data Meaning revision;
- applicable Constraint or Generation Condition revision/reference when those define the question;
- method/metric/test identity and configuration;
- logical scope/population;
- coverage/sampling/approximation semantics;
- randomness/seed intent;
- software/runtime/dependency profile where materially relevant;
- uncertainty/confidence semantics;
- any criterion-specific answer-strength requirement.

After commitment, materially changing these facts creates a new distinguishable Evaluation rather than silently rewriting the existing one.

A retry through Execution is not permission to change the committed Evaluation specification.

## Method compatibility

Before commitment, Evaluation validates that the selected method can legitimately address the bound Criterion under the declared scope.

Compatibility considers at least:

- whether required inputs/references exist and are stably identifiable;
- whether the method measures the property the Criterion asks about;
- whether method coverage can support the Criterion's required claim strength;
- whether sampling/approximation error is acceptable under Criterion semantics;
- whether Data Meaning required for interpretation is available;
- whether deployment/network/dependency policy permits the method;
- whether known scale/resource limitations invalidate the intended scope;
- whether uncertainty can be represented sufficiently for interpretation.

A method MAY be suitable for exploratory Evidence while being insufficient for a Generation-completion claim. Compatibility is therefore Criterion/context specific.

`indeterminate` compatibility MUST NOT silently become sufficient merely because the method can execute.

## Coverage semantics

Evaluation explicitly distinguishes how much of the logical target the method examines or can make claims about.

Conceptually relevant coverage modes include:

### Exhaustive / complete-scope

The method examines or establishes the relevant property across the full logical committed scope.

Exhaustive does not imply driver-local processing. A distributed validation over every relevant partition can be exhaustive while never collecting the corpus centrally.

### Bounded / certificate-backed

The method establishes a property through a deterministic bound, proof, certificate, construction guarantee, or equivalent basis without necessarily materializing a per-row check.

The basis and limitations must remain inspectable.

### Statistical / sampled

The method examines a sample or derives an estimator for a population property.

Evidence must preserve sampling design, sample size/scope, uncertainty/confidence, and assumptions material to extrapolation.

### Approximate / sketch-based

The method uses summaries, sketches, approximations, or bounded error techniques.

Evidence must preserve relevant error bounds, approximation semantics, and unsupported conclusions.

### Diagnostic / partial

The method intentionally examines only a subset or produces investigative observations without claiming population-wide sufficiency.

This may be useful Evidence but cannot silently support stronger claims.

These are conceptual distinctions rather than a required implementation enum.

## Claim-strength rule

The central 002-E Evaluation rule is:

> **The strength of Evidence produced by an Evaluation MUST NOT exceed what its method, scope, coverage, assumptions, and uncertainty can support.**

Examples:

- checking every record distributively can support a universal row-level Constraint claim if the method itself is correct for that property;
- checking 10,000 sampled records and observing no violation supports a sample/statistical observation, not automatically the universal statement "no violations exist anywhere";
- a sketch with a documented error bound can support claims within that bound, not exact equality outside it;
- a downstream-model utility test supports the specified task/use context and does not automatically establish general utility;
- a disclosure-risk attack simulation supports findings under the stated threat model and attacker assumptions, not a universal privacy guarantee.

## Evaluation of Generation Conditions and Constraints

002-D permits Generation completion to depend on post-production Evaluation.

When Evaluation is used for that purpose:

- the exact candidate output identity must be bound;
- the exact mandatory Condition or Constraint revision/semantics must be bound;
- the Criterion must preserve the completion requirement being tested;
- the method must have claim strength sufficient for that requirement;
- Evidence must be available before Generation claims semantic completion;
- a negative or indeterminate result blocks Generation completion when determination/satisfaction is mandatory.

A sampled method may be adequate when the committed requirement itself is statistical or tolerance-based. It is not adequate merely because exhaustive validation is expensive.

## Multiple methods and multiple Evidence records

One Criterion may be examined by several Evaluations, and one Evaluation may produce several independently interpretable Evidence records where its method naturally yields distinct findings.

Different methods may disagree.

SYNGAN MUST preserve that disagreement rather than averaging incompatible Evidence into a single truth value automatically.

A later actor/policy may decide which Evidence is more relevant, but that decision is outside Evaluation unless an explicit Criterion defines a method-combination rule.

## Sampling and approximation

Sampling or approximation is permitted when methodologically appropriate and explicit.

The committed Evaluation must preserve, where material:

- target population;
- selection/sampling design;
- sample size or effective coverage;
- stratification/weighting;
- random seed/policy;
- approximation/sketch algorithm identity;
- error/confidence bounds;
- known bias/representativeness limitations;
- whether the method is suitable for rare-event or tail detection.

A sample that is representative for average distribution fidelity may be poor evidence for extremely rare Constraint violations. Method compatibility must account for the property being sought.

## Reference and baseline semantics

Evaluation may compare synthetic data against source/reference data, historical outputs, baseline models, or other committed references.

Reference identity must be stable enough that later reviewers can determine what comparison was actually made.

A mutable table name or model alias alone is insufficient when underlying contents/behavior can change materially.

Reference data may be too sensitive to preserve directly in Evidence; stable references/provenance can satisfy traceability without copying source records into Evidence.

## Evaluation and privacy/disclosure risk

Privacy-oriented Evaluation must remain scoped to an explicit question and method.

A method may assess, for example, membership-inference risk, nearest-neighbor disclosure, record similarity, attribute inference, or another threat-model-specific concern.

The resulting Evidence must preserve:

- threat model;
- attacker knowledge/assumptions;
- method configuration;
- evaluated subject/input scope;
- limitations and uncertainty.

Such Evidence is not automatically a formal privacy guarantee, anonymization certification, or release authorization.

Mechanism-specific privacy guarantees remain separate future discovery/specification work when independent state/actions exist.

## Evaluation lifecycle and Execution

Evaluation may use [Execution](execution.md) for long-running/distributed work.

Execution owns Attempts, operational progress, retry/resume, and operational failure facts.

Evaluation owns:

- whether the committed examination was realized;
- whether method assumptions remained valid;
- whether the result is interpretable;
- whether Evidence can legitimately be produced;
- Evaluation-level completion/failure/cancellation.

`Execution.completed` does not establish Evaluation completion.

An operationally successful job that used the wrong reference data, missed required scope, violated sampling assumptions, or returned uninterpretable output MUST NOT become a successful Evaluation solely because computation finished.

## Failure and inconclusive semantics

Evaluation failure and unfavorable Evidence are different.

Examples:

- a valid exhaustive check that finds violations is a **successful Evaluation** producing Evidence of violation;
- a method crash with no interpretable result is an Evaluation failure;
- a statistically valid analysis whose confidence interval overlaps a required threshold may be a successful Evaluation producing **indeterminate/inconclusive Evidence**;
- a sampled method discovered after execution to be nonrepresentative for the Criterion may fail semantic validation even if it produced numbers.

This distinction is essential so negative findings are not discarded as failed computations and methodological failures are not mistaken for evidence of success.

## Completion semantics

Evaluation may complete only when:

1. the executed specification matches the committed Evaluation semantics;
2. bound Criterion/input/reference identities remain the ones actually examined;
3. the method was compatible with the Criterion to the claim strength represented;
4. material scope/coverage/sampling/approximation assumptions are known and preserved;
5. the result is interpretable under the method contract;
6. uncertainty/limitations required for interpretation can be stated;
7. one or more Evidence records can be established consistently when the Evaluation is intended to produce durable findings;
8. required provenance can be recorded consistently;
9. no terminal methodological defect invalidates the examination.

`completed with limitations` may preserve useful but bounded/inconclusive Evidence. It MUST NOT misrepresent method insufficiency as criterion satisfaction.

## Reproducibility semantics

Evaluation owns its method-specific reproduction facts, including where material:

- bound Criterion/input/reference identities;
- method/version/configuration;
- scope and coverage semantics;
- sample-selection/randomness policy;
- approximation/sketch semantics;
- software/runtime/dependency identity;
- uncertainty calculation;
- material retry/recovery facts.

002-G will refine cross-cutting reproduction classes and identity requirements.

## Scale semantics

Evaluation must support enterprise-scale examination without requiring full subject/output collection to the driver in the ordinary path.

Different Criteria may legitimately require different scale techniques:

- distributed exhaustive validation;
- aggregations;
- partition-local checks plus global reduction;
- sketches/summaries;
- bounded estimators;
- statistically designed samples;
- task-specific model training/testing.

Scale pressure MUST NOT silently lower claim strength. If only a weaker method is feasible, the resulting Evidence must remain weaker or the Criterion must remain unanswered.

Canonical Evaluation state SHOULD scale with specification, methods, summaries, and Evidence references rather than per-row evaluation details by default.

## Actions

### Define / request

Specify Criterion, method, inputs, scope, and evidence intent.

### Validate prerequisites

Assess method compatibility, reference/input availability, coverage, dependency policy, and claim strength.

### Commit

Freeze material Evaluation semantics historically.

### Initiate

Request operational realization through Execution when required.

### Observe

Track semantic evaluation state without equating operational progress with evidentiary validity.

### Complete

Establish interpretable Evidence when method and semantic completion requirements are satisfied.

### Fail

Terminate when valid Evidence answering the intended Criterion cannot be produced under the committed specification.

### Cancel

Terminate intentionally before semantic completion where permitted.

## Invariants

1. Evaluation owns method; Criterion owns the evaluative question.
2. Evaluation MUST bind exact Criterion and material input/reference identities.
3. Sampling, approximation, coverage, assumptions, and material scope limitations MUST remain visible.
4. Claim strength MUST NOT exceed method/scope/uncertainty support.
5. Execution completion alone MUST NOT establish successful Evaluation.
6. A negative finding may come from a successful Evaluation; pass/fail of the subject is distinct from Evaluation success/failure.
7. Inconclusive/indeterminate Evidence MUST NOT silently become criterion satisfaction.
8. Sampling MUST NOT be treated as universal proof when the Criterion requires exhaustive/universal evidence.
9. Scale limitations MUST NOT silently weaken Criterion semantics.
10. Evaluation MUST NOT become Constraint, Condition, Evidence, privacy-guarantee, or external approval authority.
11. Different valid methods may produce conflicting Evidence; disagreement MUST remain inspectable unless an explicit Criterion defines combination semantics.
12. Evaluation state SHOULD NOT scale linearly with evaluated row count by default.
13. Ordinary enterprise Evaluation MUST NOT require full-corpus/output driver collection.
14. No Evaluation rule may introduce a permanent single-table assumption.

## Operational principle

A Generation has fully materialized 200 million records and is waiting for required validation. One required Constraint states that `quantity >= 0` for every record. Evaluation binds the exact candidate output and Constraint-derived Criterion, performs a distributed exhaustive check across all partitions, reduces only violation counts/diagnostics, and establishes Evidence that is strong enough to support the universal completion requirement without collecting the output to the driver.

A separate fidelity Criterion is evaluated through a statistically designed sample because it asks about population similarity within an explicit tolerance. The resulting Evidence includes confidence and sampling limitations. Both Evaluations are legitimate, but they support different kinds of claims.

## Synchronization

Primary accepted synchronization rules:

- [SYNC-09 — Evaluation Criterion binding](../synchronizations/core-synchronizations.md#sync-09--evaluation-criterion-binding)
- [SYNC-10 — Evaluation method compatibility](../synchronizations/core-synchronizations.md#sync-10--evaluation-method-compatibility)
- [SYNC-11 — Evaluation operational realization](../synchronizations/core-synchronizations.md#sync-11--evaluation-operational-realization)
- [SYNC-12 — Evaluation produces Evidence](../synchronizations/core-synchronizations.md#sync-12--evaluation-produces-evidence)
- [SYNC-14 — Provenance recording](../synchronizations/core-synchronizations.md#sync-14--provenance-recording-at-material-transitions)
- [SYNC-15 — Reproducibility-relevant commitment snapshot](../synchronizations/core-synchronizations.md#sync-15--reproducibility-relevant-commitment-snapshot)

## Representation questions intentionally deferred

Phase 002-E does not decide:

- metrics library/plugin architecture;
- DataFrame API shape;
- statistical package choices;
- distributed validation implementation;
- Evidence serialization/schema;
- report/dashboard form;
- exact privacy attack implementations;
- public Evaluation API names.

Those decisions must preserve the semantic distinction between question, method, and durable finding.