---
type: Phase Record
title: 003-D — Generation Request, Condition, Validation & Output Promotion Experience
status: complete
---

# 003-D — Generation Request, Condition, Validation & Output Promotion Experience

## Objective

Translate the accepted Generation, Condition, Constraint, Learned State/direct-generation, Evaluation/Evidence, Execution, dependency/no-egress, and output-promotion semantics into a coherent actor-visible and programmatic Generation experience.

003-D focuses on making request intent, commitment, candidate materialization, validation obligations, and final output promotion inspectable without creating standalone Generation Request, Condition, Validation, Candidate Dataset, Promotion, Publication, or Output Artifact concepts.

## Governing authority

- [003-A — Workflow Entry, Source Context & Lifecycle Orientation](003-A-workflow-entry-source-context-lifecycle-orientation.md)
- [003-B — Data Meaning, Constraint & Strategy Preparation Experience](003-B-data-meaning-constraint-strategy-preparation-experience.md)
- [003-C — Learning & Learned State Lifecycle Experience](003-C-learning-learned-state-lifecycle-experience.md)
- [Generation](../../concepts/generation.md)
- [Constraint](../../concepts/constraint.md)
- [Learned State](../../concepts/learned-state.md)
- [Evidence](../../concepts/evidence.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)

## Canonical experience authority created

- [Generation Request, Condition, Validation & Output Promotion](../../experience/generation-request-condition-validation-output-promotion.md)

## Main decisions

### 1. Generation experience begins with request semantics, not a sampler call

Before commitment, actors can inspect and amend material request intent including quantity/scope, Conditions, Strategy/configuration, Learned State or direct-generation basis, Constraints, dependency posture, tolerances, reproducibility intent, and known completion obligations.

The experience does not assume every request means exactly `N rows`.

### 2. Condition remains Generation-owned and distinct from Constraint

The experience preserves:

```text
Condition -> what this Generation requests
Constraint -> what valid applicable output must obey
```

Shared expression/predicate representation later cannot collapse the distinction.

### 3. Mandatory versus best-effort Condition strength is explicit

A mandatory Condition can block successful Generation completion.

A best-effort Condition may permit `completed with limitations` only when such shortfall was allowed at commitment.

The experience cannot silently downgrade mandatory intent for convenience.

### 4. Condition target/tolerance is part of commitment

Quantitative/distributional Conditions expose material targets/tolerances before commitment.

Tolerances cannot be retrofitted after output exists simply to make an unfavorable result acceptable.

### 5. Learned-State and direct-generation paths remain equally legitimate

Learned-State reuse receives contextual Generation compatibility validation.

Direct-generation Strategies bind the stable direct input/source/configuration context they actually use without fabricated Learning/Learned State lifecycle.

### 6. Generation preview includes completion obligations

Before commitment, the actor should know not just what will be generated, but what must later be established before the result can be promoted.

Possible obligations include:

- quantity/scope completion;
- mandatory Condition fulfillment;
- required Constraint satisfaction;
- post-production validation for rules marked `validated later`;
- completion-sufficient Evidence strength;
- output integrity/identity;
- required Provenance;
- dependency/no-egress compliance.

003-D does not yet design the full Evaluation/Evidence authoring experience; 003-E will do that.

### 7. Commitment visibly freezes request semantics

After Generation commitment, material changes to Conditions, quantity/scope, Strategy/configuration, Learned State/direct input, Constraint revisions/handling, dependencies, or no-egress posture require a new distinguishable Generation rather than an edited retry.

### 8. Production completion and Generation completion are distinct

The experience preserves cases such as:

```text
Execution: completed
Candidate output: physically complete
Generation: awaiting required validation
Completed output: not promoted
```

A successful Spark/Databricks/PyTorch job or fully written table does not by itself establish Generation success.

### 9. Output state is intentionally graduated

The experience distinguishes:

- partial materialization;
- complete candidate materialization;
- abandoned/quarantined materialization;
- authoritative completed output.

Candidate/failed material cannot appear equivalent to normal completed output merely because a locator exists.

### 10. Validation is requirement-specific

The Generation experience shows mandatory completion obligations separately rather than reducing them to one opaque `validation=true` field.

Actors can understand which Condition/Constraint is fulfilled, violated, pending, or indeterminate and which Evidence supports that state.

### 11. Evidence strength participates visibly in completion

Completion-facing Evidence must expose enough coverage/claim strength to explain whether the exact committed requirement is satisfied.

For example:

- exhaustive Evidence may support a universal Constraint;
- sampled diagnostic Evidence ordinarily cannot prove a universal rule;
- statistical Evidence may satisfy a tolerance-based Condition when sufficiently precise;
- indeterminate Evidence blocks completion when determination is mandatory.

Evidence remains finding authority; Generation owns the completion decision.

### 12. Evaluation success does not mean requirement satisfaction

A successful Evaluation can produce Evidence that a required Constraint was violated or remains indeterminate.

The Generation experience must not map `Evaluation completed` to `validation passed` automatically.

### 13. Candidate-to-completed promotion is semantic

003-D establishes the actor-visible promotion barrier:

```text
candidate material
      ↓
mandatory completion obligations satisfied
      ↓
Generation semantic completion
      ↓
one authoritative logical completed output
```

The physical implementation of promotion remains downstream architecture work.

### 14. Single semantic promotion is preserved

Retries, repeated partition writes, speculative execution, and repeated validation must not produce multiple authoritative outputs for one successful Generation.

One successful Generation has zero or one authoritative logical completed output under the current model.

### 15. `Completed with limitations` remains narrow

It may describe allowed best-effort or approximation limitations after mandatory requirements pass.

It cannot excuse violated/unsupported required Constraints, failed mandatory Conditions, incomplete output, forbidden network behavior, missing dependencies, or unresolved mandatory validation.

### 16. Completed-output inspection is logical, not file-oriented

Actors inspect one logical output identity with request/semantic/Strategy/Condition/Constraint/Evidence/Provenance context while physical partitions/files/components remain progressive drill-down.

A user does not need to inspect physical layout to determine which output is authoritative.

### 17. Completion validation is not the end of Evaluation

Additional post-completion Evaluation for fidelity, utility, disclosure risk, comparison, or use-case fitness remains legitimate and does not redefine the original Generation request.

### 18. Offline/no-egress posture persists through fulfillment

Committed dependency/network policy remains binding during Generation.

Missing artifacts or failed local resources cannot cause hidden downloads, remote fallback, or source/synthetic data egress.

### 19. A returned DataFrame is not a complete lifecycle contract

Programmatic users must be able to determine whether output is partial, candidate, completed, failed/quarantined, and which validation/promotion obligations remain.

Returning tabular data alone cannot safely communicate that distinction.

## Generation orientation example

```text
Generation G42

Request
- exact 100,000,000 rows
- Condition REGION-1: mandatory
- Condition MIX-2: mandatory, 20% ± 2%
- Condition AGE-3: best effort

Synthesis basis
- Strategy v2 / config C9
- Learned State LS17
- no outbound network

Production
- candidate rows: 100,000,000 / 100,000,000
- Execution: completed

Completion validation
- REGION-1: fulfilled / Evidence E31
- MIX-2: fulfilled within tolerance / Evidence E32
- Constraint C4: satisfied exhaustive / Evidence E33
- Constraint C5: indeterminate / Evidence E34

Generation
- status: awaiting required validation / cannot promote while C5 remains indeterminate

Completed logical output
- not established
```

This is an experience example, not a required UI layout or API schema.

## Actor experience conclusions

### Data Practitioner

Needs inspectable request semantics, mandatory/best-effort Conditions, synthesis basis, materialization progress, completion obligations, validation blockers, promotion state, limitations, and legitimate next actions.

### Platform Operator

Needs operational output/Execution detail while retaining candidate-versus-completed semantic context.

### Data Owner / Steward

Needs exact Data Meaning/Constraint revisions and the Evidence basis used to establish output validity where required.

### Privacy / Risk / Governance Reviewer

Needs exact output identity, dependency/egress posture, completion Evidence, limitations, Provenance, and clear separation between Generation completion and release/privacy approval.

### Synthetic Data Consumer

Should encounter the authoritative completed logical output by default, not candidate/failed material presented as equivalent data.

## Enterprise-scale conclusions

Generation lifecycle and promotion remain distributed-first.

The experience may use logical output references, distributed counts, validation summaries, Evidence, diagnostic references, and selected platform links without collecting the full candidate/completed output into driver-local memory.

A scale limitation does not authorize silently weakening a universal completion requirement to sample-only assurance.

## No new concept result

003-D does not require standalone concepts for:

- Generation Request;
- Condition;
- Candidate Dataset;
- Candidate Output;
- Validation;
- Completion Obligation;
- Promotion;
- Publication;
- Output Artifact;
- Generation Result;
- Run.

These remain Generation-owned subordinate semantics, derived experience state, representation mechanisms, or rejected umbrella terms.

## Deferred to later Phase 003 groups

### 003-E

Deepen Evaluation Criterion selection, Evaluation configuration, Evidence interpretation/strength, comparison, and review beyond Generation-facing completion obligations.

### 003-F

Deepen Execution/Attempt monitoring, repeated writes, recovery, cancellation races, unknown state, and operational reconciliation.

### 003-G

Deepen completed-output Provenance, historical traversal, reproduction assessment, and comparison.

### 003-H

Deepen sensitive output/dependency/access/egress and enterprise safety experience.

## Representation questions intentionally deferred

003-D does not select:

- final Generation API/builder;
- Condition expression editor/language;
- output/staging storage format;
- catalog/transaction/promotion/fencing mechanism;
- output manifest format;
- Evaluation engine;
- Evidence reporting schema/UI;
- scheduler/Execution architecture;
- cancellation implementation;
- retention/cleanup policy;
- authorization/release approval flow.

## Exit criteria

- [x] Generation request semantics defined as actor-visible pre-commit intent;
- [x] Condition kept distinct from Constraint;
- [x] mandatory/best-effort Condition strength exposed;
- [x] Condition target/tolerance commitment semantics defined;
- [x] Learned-State and direct-generation paths preserved;
- [x] pre-commit completion obligations exposed;
- [x] Generation commitment consequence defined;
- [x] semantic versus operational state preserved;
- [x] production completion versus Generation completion distinguished;
- [x] partial/candidate/quarantined/completed output distinctions defined;
- [x] required validation presented per requirement;
- [x] Evidence claim-strength sufficiency exposed;
- [x] Evaluation success kept separate from requirement satisfaction;
- [x] semantic output-promotion barrier defined;
- [x] single semantic promotion preserved;
- [x] completed-with-limitations boundary constrained;
- [x] completed logical output inspection defined independently of physical layout;
- [x] additional post-completion Evaluation preserved;
- [x] offline/no-egress posture preserved throughout fulfillment;
- [x] programmatic/human parity preserved;
- [x] enterprise-scale Generation avoids mandatory full driver collection;
- [x] no representation architecture selected prematurely.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical Generation experience that makes request intent and completion obligations visible, keeps distributed candidate material non-authoritative until required validation succeeds, and promotes exactly one logical completed output only at semantic Generation completion.

## Next phase

**003-E — Evaluation, Evidence & Review Experience**
