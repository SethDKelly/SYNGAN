---
type: Experience Specification
title: Generation Request, Condition, Validation & Output Promotion Experience
status: active
---

# Generation Request, Condition, Validation & Output Promotion Experience

## Purpose

Define how human and programmatic actors create, review, commit, observe, validate, complete, and inspect [Generation](../concepts/generation.md) while preserving the distinctions among request intent, Generation-owned Conditions, reusable [Constraints](../concepts/constraint.md), contextual Strategy/Learned-State compatibility, operational [Execution](../concepts/execution.md), candidate materialization, required [Evidence](../concepts/evidence.md), and the final semantic promotion of one completed logical synthetic output.

This experience does not introduce standalone `Generation Request`, `Condition`, `Validation`, `Candidate Dataset`, `Promotion`, `Publication`, or `Output Artifact` concepts.

## Primary experience principle

> **An actor should always be able to tell what output was requested, which requirements are mandatory versus best-effort, what synthesis basis is committed, what data merely exists physically, what completion obligations remain unresolved, and whether one authoritative completed synthetic output has actually been promoted.**

A physically complete table/file set, successful platform job, or finished sampler is not sufficient by itself to establish Generation completion.

## Applicability and entry

Actors may enter the Generation experience from several legitimate contexts:

- a 003-B preparation context ready for direct Generation commitment;
- a [Learned State](../concepts/learned-state.md) selected through 003-C for contextual reuse validation;
- an existing draft/proposed Generation;
- an active committed Generation;
- a Generation with partial or complete candidate materialization;
- a Generation awaiting mandatory post-production validation;
- a failed/cancelled Generation with retained non-final material;
- a completed Generation whose output, Conditions, Evidence, limitations, or Provenance must be inspected historically.

The experience MUST support both the Learned-State path and the direct-generation path. A direct-generation Strategy must not be forced through fabricated Learning/Learned State state simply to fit one user-flow template.

## Generation request experience

### Request is editable before commitment

Before semantic commitment, actors should be able to define and amend Generation intent such as:

- requested quantity/cardinality semantics;
- logical output scope;
- mandatory and best-effort Conditions;
- selected Strategy/configuration;
- selected Learned State where required;
- direct-generation source/input context where Learned State is not required;
- applicable Constraint revisions and expected handling dispositions;
- Data Meaning revision/context;
- material dependency/network/no-egress posture;
- required local/base/pretrained artifact identities;
- accepted approximation/tolerance semantics;
- randomness/reproducibility intent;
- output destination/reference intent where material to actor understanding.

The experience should not imply that every request is simply `N rows`. Quantity semantics may be exact, bounded, minimum/maximum, or tolerance-based where the Strategy/Generation contract supports them.

### Request summary must reflect semantics, not implementation knobs alone

A concise request summary SHOULD prioritize the meaning of the intended output over platform details.

For example:

```text
Generation G-draft

Output quantity
- target: 100,000,000 rows
- tolerance: exact

Conditions
- region = Midwest — mandatory
- premium_customer proportion ~= 20% ± 2% — mandatory
- age distribution preference — best effort

Synthesis basis
- Strategy: Local Neural Tabular v2 / C9
- Learned State: LS17

Constraints
- 6 applicable required
- 4 enforced during generation
- 2 require post-generation validation

Dependencies
- runtime network: none
- local base artifact B3: resolved
```

The future representation may differ, but materially meaningful defaults and hidden orchestration choices must remain inspectable.

## Condition authoring and review

### Condition remains request-specific

The experience MUST continue to distinguish:

```text
Condition: what this Generation is asking for
Constraint: what valid applicable output must obey
```

An identical predicate/expression shape does not merge their semantics.

Examples:

```text
Condition
region = "Midwest"
```

because the actor requests a Midwest-focused output.

```text
Constraint
end_date >= start_date
```

because every applicable valid output must obey the rule.

### Requirement strength must be explicit

Each material Condition should expose whether it is:

- **mandatory** — Generation cannot successfully complete unless fulfillment is sufficiently established; or
- **best-effort/advisory** — Generation may complete with an explicit limitation when the committed contract permits shortfall.

The experience MUST NOT allow an implementation default to silently downgrade a mandatory Condition to best effort.

### Tolerance and target semantics

When a Condition is quantitative or distributional, the actor should be able to understand the committed target and allowed tolerance.

Examples may include:

```text
category A proportion = 40% ± 2%
```

or another Strategy-supported bounded request.

Tolerance is part of the request meaning when material. It must not be introduced only after output is produced to make an unfavorable result appear acceptable.

### Feasibility before commitment

The Generation preparation experience should surface whether each mandatory Condition is:

- supported/feasible sufficiently for commitment;
- supported with explicit limitations;
- incompatible/unsupported;
- indeterminate.

An indeterminate mandatory Condition remains a blocker when the commitment contract requires feasibility to be known.

Condition feasibility is not Condition fulfillment. Successful pre-commit validation only says the proposed synthesis basis can legitimately attempt the committed request.

## Learned-State versus direct-generation basis

### Learned-State path

When Generation uses a Learned State, the actor should be able to inspect the contextual reuse assessment before commitment, including:

- Learned State status: usable/restricted/retired/invalidated;
- producing Strategy/configuration family;
- current Data Meaning compatibility;
- requested Condition support;
- applicable Constraint handling;
- required local/base artifacts;
- runtime/software compatibility where material;
- dependency/network/no-egress posture;
- known intrinsic restrictions/limitations.

`usable` alone is never sufficient to imply Generation compatibility.

### Direct-generation path

When no Learned State is required, the experience should identify the direct input/source/configuration context that materially influences Generation and confirm that it can be historically bound strongly enough for the committed request.

The experience MUST NOT create a fake empty Learned State or no-op Learning merely to normalize the path.

## Pre-commit completion-obligation preview

Before commitment, actors should be able to see not only what will be generated, but also **what must be established after production before Generation can complete**.

The experience should preview obligations such as:

- mandatory Condition fulfillment checks;
- required Constraint satisfaction checks;
- which Constraints are expected to be guaranteed by construction versus validated later;
- quantity/cardinality completion checks;
- required output-integrity/completeness checks;
- required Evidence strength where already known;
- provenance requirements necessary for final promotion;
- dependency/no-egress requirements that remain binding during execution.

For example:

```text
Completion obligations

✓ quantity must equal 100,000,000
✓ region Condition must be fulfilled
? premium-customer proportion requires statistical validation
✓ Constraint C1 covered by construction guarantee
? Constraint C4 requires exhaustive post-generation validation
? Constraint C5 requires exhaustive post-generation validation
✓ no outbound network permitted
✓ final output identity/provenance required before promotion
```

This preview is not an Evaluation configuration interface; 003-E will deepen Criterion/Evaluation/Evidence authoring. It is a Generation-facing statement of what must become known before completion.

## Review-before-commit

Immediately before Generation commitment, the actor should be able to review the material historical facts that will be frozen.

The review should include, where applicable:

- Data Meaning revision;
- Strategy/configuration revision;
- Learned State identity or direct-generation source/input identity;
- applicable Constraint revisions and handling dispositions;
- Conditions and mandatory/best-effort status;
- quantity/scope/tolerance semantics;
- dependency/network/no-egress profile;
- required local/base artifacts;
- randomness/reproducibility intent;
- known completion-validation obligations;
- accepted limitations.

A readiness result from 003-B or Learned State reuse assessment from 003-C can inform this review, but neither is a substitute for Generation commitment.

## Semantic commitment

Generation commitment freezes the material request semantics historically.

After commitment:

- a retry may change operational realization but not the request meaning;
- changing quantity semantics materially creates a new Generation;
- changing a mandatory Condition materially creates a new Generation;
- changing Strategy/configuration materially creates a new Generation;
- substituting Learned State or a direct-generation source/input materially creates a new Generation;
- changing applicable Constraint revisions or required handling materially creates a new Generation;
- enabling network access or substituting a materially different dependency is not a harmless retry.

The experience should make this consequence clear rather than presenting commitment as a generic `generate` button whose request can be edited afterward.

## Generation lifecycle orientation

The experience should preserve a lifecycle orientation equivalent to:

```text
draft / proposed
      ↓
validated / ready
      ↓
committed
      ↓
fulfilling
      ↓
partial materialization
      ↓
complete candidate materialization
      ↓
awaiting required validation
      ↓
┌───────────────────────────┐
│                           │
completed / completed       failed / cancelled
with limitations
      │
      ▼
one authoritative logical output
```

Not every Generation needs every intermediate state, and this is not a required implementation enum.

### Semantic state versus Execution state

The experience MUST preserve distinctions such as:

```text
Generation: fulfilling
Execution: running
Latest Attempt: active
Candidate rows materialized: partial
```

```text
Generation: awaiting required validation
Execution: completed
Latest Attempt: succeeded
Candidate output: physically complete
Completed output: NOT promoted
```

```text
Generation: failed
Execution: completed
Reason: required Constraint C4 violated
Candidate output: retained/quarantined for diagnosis
```

A single `job succeeded` or `generation job finished` message is not an adequate lifecycle interface.

## Materialization progress

### Physical progress is useful but not semantic completion

At enterprise scale the experience MAY expose meaningful materialization progress such as:

- produced logical row count versus requested quantity when interpretable;
- partitions/shards/components materialized;
- output-integrity checks completed;
- current Attempt;
- elapsed time;
- Strategy-defined generation stages;
- candidate destination availability;
- outstanding validation obligations.

The experience MUST NOT equate `100% rows written` with `Generation completed` when mandatory semantic checks remain.

### Quantity semantics must remain faithful

If the request is exact, minimum, maximum, or tolerance-based, progress and completion should use that committed meaning rather than inventing a universal percentage.

For example, `98M / 100M rows` can be meaningful for an exact 100M request. A Strategy-defined bounded or distributional result may require a different progress presentation.

## Partial, candidate, and completed output experience

### Partial materialization

Partial material should be visibly non-final and should not appear in normal completed-output selection.

The experience should expose enough information for recovery/diagnosis without encouraging downstream consumption as if the Generation had succeeded.

### Complete candidate materialization

A complete candidate may have the full requested physical extent while semantic completion remains pending.

The experience should be explicit:

```text
Candidate output: physically complete
Generation status: awaiting required validation
Downstream completed-output status: unavailable
```

A provisional locator may be shown for operational inspection, but it MUST be marked non-final.

### Abandoned/quarantined materialization

Failed or cancelled Generations may retain partial or complete candidate data for diagnosis/recovery according to later storage policy.

Such material must remain distinguishable from a successful result and should not become discoverable through default completed-output flows.

## Required validation experience

### Validation obligations are requirement-specific

The Generation experience should show each mandatory completion obligation independently rather than flattening all checks into one generic `validation passed` value.

For example:

```text
Completion validation

Condition REGION-1
- mandatory
- result: fulfilled
- Evidence: E31

Condition MIX-2
- mandatory
- result: fulfilled within tolerance
- Evidence: E32

Constraint C4
- required
- result: satisfied
- Evidence strength: exhaustive
- Evidence: E33

Constraint C5
- required
- result: indeterminate
- Evidence: E34
- effect: BLOCKS COMPLETION
```

The exact presentation may differ, but the actor must be able to identify what remains unresolved and why it matters.

### Evidence strength must remain visible

When Evidence is consumed for Generation completion, the experience must preserve enough of its strength/coverage to explain whether it is sufficient for the committed requirement.

Examples:

- universal Constraint + exhaustive Evidence → potentially completion-sufficient;
- universal Constraint + sampled diagnostic Evidence → insufficient for universal completion claim;
- tolerance-based mandatory Condition + sufficiently precise statistical Evidence → potentially completion-sufficient;
- indeterminate Evidence when determination is mandatory → blocks completion.

Generation owns the final completion decision. Evidence remains finding authority.

### Evaluation success is not requirement satisfaction

The experience MUST support cases such as:

```text
Evaluation: completed successfully
Evidence: Constraint violated
Generation: cannot complete successfully
```

or:

```text
Evaluation: completed successfully
Evidence: indeterminate at required strength
Generation: awaiting/failed completion depending on committed contract
```

This prevents a green Evaluation job/result badge from being mistaken for a passed requirement.

## Output promotion barrier

### Promotion is semantic

The Generation experience should make the final transition explicit:

```text
partial / candidate physical material
              ↓
all mandatory completion obligations resolved
              ↓
Generation semantic completion
              ↓
SYNC-08 result promotion
              ↓
one authoritative completed logical output
```

Promotion may later be implemented through transactions, manifests, table versions, catalog state, fencing, markers, or other mechanisms. 003-D selects none of them.

### Promotion review

Before the completed-output identity becomes authoritative, the experience should be able to summarize:

- committed request identity;
- candidate output identity;
- quantity/scope completion;
- mandatory Condition fulfillment;
- applicable required Constraint satisfaction basis;
- permitted best-effort/approximation limitations;
- dependency/no-egress compliance;
- required Provenance consistency;
- final logical output reference readiness.

If a mandatory obligation remains violated, unsupported, indeterminate where determination is required, or otherwise unresolved, promotion MUST NOT occur.

### Single semantic promotion

Retries, speculative execution, repeated partition writes, or repeated validation must not result in two authoritative completed outputs for one successful Generation.

The experience should expose one logical completed result even when physical recovery created duplicate/transient material behind the scenes.

003-F will deepen retry/recovery operational experience.

## Completed with limitations

`completed with limitations` should be used narrowly and transparently.

It may represent committed/allowed outcomes such as:

- a best-effort Condition missed its preferred target;
- a declared approximation remained within accepted semantics;
- a non-binding capability limitation remained after all mandatory requirements were satisfied.

It MUST NOT be used to excuse:

- violated required Constraints;
- unsupported required Constraints;
- failed mandatory Conditions;
- required validation that remains indeterminate;
- incomplete output extent;
- forbidden network/egress behavior;
- missing mandatory dependency;
- inconsistent provenance required for completion.

The experience should list each limitation rather than collapsing them into a generic warning icon.

## Completed-output inspection

A completed Generation should expose one logical output identity independently of physical component count/layout.

A normal inspection surface should make available progressively:

- Generation identity;
- completed logical output identity;
- committed quantity/scope;
- Data Meaning revision/context;
- Strategy/configuration;
- Learned State or direct-generation input basis;
- Conditions and fulfillment status;
- applicable Constraints and completion satisfaction basis;
- limitations;
- Evidence used for completion where applicable;
- Provenance/reproducibility availability;
- dependency/no-egress posture;
- physical location/components only to the depth useful for consumption or diagnosis.

Consumers should not need to interpret thousands of partition files to know which logical output is authoritative.

## Post-completion Evaluation boundary

Generation completion does not mean all useful evaluation has already occurred.

Required completion validation may establish only the properties necessary for the committed Generation contract. Actors may later perform additional Evaluations for:

- fidelity;
- downstream utility;
- broader validity questions;
- disclosure/privacy risk;
- comparison against other outputs;
- use-case-specific fitness.

Those later findings do not retroactively change what the Generation requested, although they may affect future governance/use decisions.

003-E will deepen Evaluation/Evidence review experience.

## Failure experience

Generation-related semantic failure should identify the actual blocking reason rather than merely surface a generic job failure.

Examples include:

- mandatory Condition unfulfilled;
- required Constraint violated;
- required Constraint unsupported;
- validation Evidence insufficient/indeterminate;
- requested quantity cannot be fulfilled;
- Learned State/direct-input incompatibility;
- forbidden dependency/network behavior;
- required output integrity cannot be established;
- terminal Execution failure with no valid recovery path;
- required Provenance cannot be made consistent.

A failed Attempt alone does not mean Generation has failed when recovery remains valid.

## Cancellation experience

Before commitment, a Generation request can be withdrawn as editable intent.

After commitment, cancellation should be shown as an operational/domain request whose outcome may race with ongoing work.

The experience should not assume a cancellation request instantly means all work stopped or that an already completed output disappeared.

003-F will deepen cancellation/reconciliation semantics.

## Retry and recovery experience boundary

A retry/resume must continue the same committed Generation semantics.

The Generation experience should show the actor that recovery may reuse partial/candidate material only when the recovery contract can establish its correctness.

Recovery material remains non-final until the same completion obligations are satisfied.

Detailed Attempt/checkpoint/fencing mechanics remain 003-F/downstream architecture work.

## Dependency and offline/no-egress behavior

The Generation experience must preserve the dependency posture selected before commitment throughout fulfillment.

In particular:

- missing local artifacts must be reported explicitly;
- a no-network Generation must not silently download or call a remote service;
- runtime-network-dependent behavior must remain visibly incompatible with a no-network commitment;
- materially different fallback Strategy/configuration requires a new commitment;
- source-derived/synthetic data egress must not occur merely because a dependency becomes unavailable.

## Privacy and release boundary

A promoted completed synthetic output is not automatically:

- anonymous;
- formally private;
- low disclosure risk;
- approved for release;
- appropriate for every downstream use.

The completed-output experience SHOULD avoid celebratory or generic `safe/approved` cues unless an explicit external authority provides such a decision.

Evidence may support later privacy/risk or use decisions without becoming approval authority itself.

## Actor-specific views

### Data Practitioner

Emphasize request semantics, Conditions, synthesis basis, completion obligations, materialization progress, validation blockers, promotion status, limitations, and next legitimate actions.

### Platform Operator

Emphasize Execution/Attempt/output-write/recovery health while retaining the Generation semantic state and candidate-versus-completed distinction.

### Data Owner / Steward

Emphasize bound Data Meaning/Constraints, fulfillment/satisfaction basis, and exact historical output governed by those revisions.

### Privacy / Risk / Governance Reviewer

Emphasize exact output identity, dependency/egress posture, completion Evidence, limitations, Provenance, and distinction between Generation completion and release/privacy approval.

### Synthetic Data Consumer

Default to the authoritative completed logical output and its semantic/limitation/Evidence context; candidate or failed Generation material should not appear equivalent to normal consumable output.

## Programmatic parity

A later SDK/CLI/notebook surface should support direct inspection of:

- editable versus committed request state;
- quantity/scope semantics;
- Conditions and mandatory/best-effort status;
- selected Learned State or direct-generation basis;
- bound Constraints/handling;
- Generation semantic state;
- associated Execution/Attempt summary;
- partial/candidate/completed output distinction;
- outstanding completion obligations;
- Evidence status/strength used for required validation;
- limitation versus blocker distinctions;
- completed logical output identity;
- Provenance/reproducibility references;
- dependency/network/no-egress posture.

A returned DataFrame alone is not an adequate Generation lifecycle contract because it cannot by itself communicate whether the data is candidate or authoritative completed output.

## Enterprise-scale experience

The Generation experience MUST remain usable when output contains hundreds of millions of records and spans many partitions/files/tables/components.

Actor orientation should rely on:

- bounded control-plane status;
- logical output references;
- distributed counts/summaries;
- validation summaries/Evidence;
- selected diagnostic references;
- platform links where useful;

rather than collecting the entire candidate/completed output to the driver/UI process.

Required validation may be exhaustive while remaining distributed. Scale pressure MUST NOT cause the UI/API to quietly downgrade a universal completion requirement to sample-only assurance.

## Next-action guidance

Derived next actions may include:

```text
draft Generation
  → resolve Conditions / compatibility / Constraints
  → review commitment
  → commit

Generation fulfilling
  → observe materialization / Execution

candidate output physically complete
  → perform/await required validation

required Evidence sufficient
  → promote completed output

required Evidence violated/insufficient
  → fail/remediate through a new Generation as appropriate

completed output
  → inspect limitations / Evidence / Provenance
  → perform additional Evaluation

failed recoverable Attempt
  → inspect Execution recovery path
```

Guidance remains derived from canonical state and does not create a generic workflow authority.

## Experience invariants

1. Generation Request and Condition semantics MUST remain subordinate to Generation rather than become standalone domain concepts.
2. Condition MUST remain distinct from Constraint even when representation machinery is shared.
3. Mandatory versus best-effort Condition strength MUST be visible before commitment.
4. Condition tolerance/target semantics MUST be frozen at commitment when material and MUST NOT be retrofitted after unfavorable output.
5. Learned-State reuse compatibility MUST remain contextual to the Generation; `usable` Learned State does not imply universal compatibility.
6. Direct-generation Strategies MUST NOT be forced through fabricated Learning/Learned State experience.
7. Generation commitment MUST visibly freeze the material request/semantic/dependency context.
8. Physical/materialization progress MUST remain distinguishable from semantic Generation completion.
9. Partial, complete candidate, abandoned/quarantined, and completed output states MUST remain distinguishable.
10. A physically complete candidate MUST remain visibly non-final while mandatory completion validation is pending.
11. Required completion validation MUST identify each committed requirement rather than collapse to one opaque pass/fail flag.
12. Evidence claim strength MUST remain visible enough to explain whether it is sufficient for the committed requirement.
13. Evaluation operational success MUST NOT be presented as Condition/Constraint satisfaction automatically.
14. Indeterminate Evidence MUST block completion when the committed requirement requires determination.
15. `completed with limitations` MUST NOT excuse failed mandatory Conditions, violated/unsupported required Constraints, incomplete output, forbidden network behavior, or unresolved mandatory validation.
16. Final output promotion MUST occur only after all mandatory completion obligations are satisfied.
17. One successful Generation establishes zero or one authoritative logical completed output under the current model.
18. Retry/recovery MUST NOT create multiple authoritative outputs or silently change committed Generation semantics.
19. A completed output MUST remain logically identifiable independently of physical partition/file/component layout.
20. Generation completion MUST NOT imply privacy, release approval, or universal downstream fitness.
21. Programmatic and human-facing surfaces MUST preserve equivalent request, candidate, validation, promotion, and limitation distinctions.
22. Ordinary Generation experience MUST NOT require full candidate/completed output collection to driver-local memory.
23. Scale limitations MUST NOT silently weaken committed completion requirements.
24. No experience rule may introduce a permanent single-table assumption.
25. Experience convenience MUST NOT create a generic Validation, Candidate Dataset, Promotion, Publication, Output Artifact, or Run god-concept.

## Representation questions intentionally deferred

003-D does not decide:

- final Generation builder/API shape;
- Condition expression language/editor;
- staging/output table/file format;
- transaction/catalog/publication mechanism;
- output manifest/fencing design;
- exact progress metric representation;
- Validation/Evaluation engine architecture;
- Evidence schema/reporting UI;
- scheduler/job implementation;
- cancellation implementation;
- storage retention/cleanup policy;
- authorization/approval workflow.

Later architecture must preserve the request, Condition, candidate-output, validation, promotion, and completed-output distinctions defined here.
