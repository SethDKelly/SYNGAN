---
type: Phase Record
title: 002-D — Generation Specification, Request/Condition Semantics & Output Completion
status: complete
---

# 002-D — Generation Specification, Request/Condition Semantics & Output Completion

## Objective

Deepen the accepted [Generation](../../concepts/generation.md) concept into precise request, Condition, commitment, compatibility, output-materialization, completion, failure, cancellation, and enterprise-scale semantics.

The phase resolves when physical synthetic output is merely candidate materialization versus when one logical output may legitimately be associated as the completed result of a committed Generation.

## Governing authority

002-D is governed by:

- [Concept Design Methodology](../../authority/design-methodology.md)
- [Documentation Governance](../../authority/documentation-governance.md)
- [Terminology Policy](../../authority/terminology-policy.md)
- [Network and External Dependency Policy](../../authority/network-external-dependency-policy.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Phase 001 Exit](../001/001-H-phase-001-consolidation-initial-concept-catalog.md)
- [002-A — Data Meaning & Constraint Specification](002-A-data-meaning-constraint-specification.md)
- [002-B — Synthesis Strategy Specification & Capability Semantics](002-B-synthesis-strategy-capability-semantics.md)
- [002-C — Learning & Learned State Specification](002-C-learning-learned-state-specification.md)

Canonical concept authority remains under `docs/concepts/`; this record preserves the refinement history and handoff.

## Scope

002-D specifies:

- Generation requested-intent semantics;
- request lifecycle before/after commitment;
- quantity/cardinality and logical scope semantics;
- Condition meaning, strength, feasibility, and fulfillment;
- Condition versus Constraint boundary;
- direct-generation versus Learned-State generation paths;
- Learned State reuse/restriction/non-mutation;
- deployment/network/dependency compatibility;
- required Constraint handling in Generation;
- enforced versus validated-later completion implications;
- candidate/partial/completed output distinctions;
- stable logical completed-output association;
- semantic completion criteria;
- completed-with-limitations boundary;
- failure/cancellation/retry semantics;
- privacy/release boundary;
- enterprise-scale output/control-plane semantics;
- synchronization refinements to SYNC-02, SYNC-03, SYNC-06, SYNC-07, SYNC-08, SYNC-10, SYNC-12, SYNC-13, SYNC-14, and SYNC-15.

## Non-goals

002-D does not select:

- Python `sample`/`generate` APIs;
- request object/class design;
- Condition expression language;
- output file/table/storage format;
- Spark partitioning strategy;
- transactional publication mechanism;
- orchestration implementation;
- exact retry/cancellation race implementation;
- output registry/catalog technology;
- validation implementation;
- formal privacy mechanism;
- exact Evidence taxonomy or statistical confidence semantics.

Those remain later specification or representation work.

## Canonical authority refined

002-D directly deepens:

1. [Generation](../../concepts/generation.md)
2. [Core Synchronizations](../../synchronizations/core-synchronizations.md)

No new standalone concept is introduced.

## Principal Generation decisions

### 1. Generation is more than data production

Generation owns both the requested synthesis outcome and whether that outcome was semantically fulfilled.

Physical rows being written is not enough to establish success.

### 2. Generation Request remains subordinate state

The request can exist in editable/validated form before semantic commitment, but that lifecycle does not justify restoring Generation Request as an independent concept.

The request is the pre-commitment/requested portion of Generation state.

### 3. Generation has a semantic commitment boundary

At commitment Generation binds the exact material semantics under which success will later be judged.

Where applicable these include:

- Data Meaning;
- Strategy/configuration;
- Learned State or direct-generation source/input identity;
- Constraints and handling dispositions;
- Conditions and requirement strength/tolerance;
- requested quantity/cardinality;
- output scope;
- dependency/network/no-egress profile;
- base/local artifact identities;
- reproducibility/randomness intent;
- material approximation semantics.

After commitment a material change requires a new distinguishable Generation rather than mutation of historical meaning.

### 4. Quantity need not universally mean exact row count

Generation supports conceptually distinct quantity contracts such as exact, minimum, maximum, or target-with-tolerance semantics.

Physical partition/file/task count is not output quantity.

### 5. Condition is request direction

Condition states characteristics this particular Generation is asked to produce.

A Condition can express predicates, cohorts, distributions, quotas, mixtures, ranges, or other directed-generation semantics supported by Strategy.

It remains separate from reusable prescriptive Constraint authority.

### 6. Conditions can be mandatory or explicitly best-effort

A mandatory Condition must be fulfilled sufficiently for Generation success.

A best-effort/advisory Condition may allow completion with an explicit limitation when the committed request authorizes that behavior.

Making a Condition mandatory does not transform it into a Constraint.

### 7. Indeterminate mandatory Condition feasibility is not success

Before commitment, the Strategy/Learned State/direct-generation basis must be assessed for requested Condition support.

If feasibility is indeterminate and the Condition is mandatory, the system cannot silently assume compatibility.

### 8. Direct generation remains first-class

A Strategy requiring no reusable Learned State may generate directly.

When direct inputs/source state materially affect output, Generation binds sufficient stable identity for provenance/reproducibility.

No fabricated Learning or Learned State is required.

### 9. Learned State reuse is contextual and non-mutating

Generation owns the exact reuse compatibility decision for its context.

Restriction may require explicit qualification; invalidated state cannot be used for new Generation.

Ordinary Generation does not fine-tune or mutate Learned State. Material adaptation requires explicit Learning/derived-state semantics.

### 10. Deployment compatibility participates before expensive work

A Strategy can be semantically appropriate yet incompatible with the committed enterprise deployment profile due to network, egress, artifact, runtime, resource, or other known requirements.

No hidden automatic download or remote fallback is allowed.

## Constraint completion decisions

### Unsupported required Constraints

An applicable required Constraint known to be unsupported prevents normal semantic commitment as successfully fulfillable under that Strategy/specification.

Preflight/diagnostic exploration may exist later, but cannot be promoted to successful completed Generation under an unsupported required rule.

### Enforced Constraints

`enforced` describes intended handling, not automatically proof of actual output satisfaction.

An enforcement claim is sufficient for Generation completion only where the committed Strategy/Constraint contract gives a strong explicit output-level guarantee for that rule and no contrary result exists.

Otherwise output-specific validation is required.

### Validated-later Constraints

The key 002-D rule is:

> **`validated later` means later than production, not later than successful Generation completion.**

A complete candidate output may exist while Generation remains semantically incomplete pending required validation.

### Violation and indeterminate satisfaction

A required Constraint established as violated blocks successful completion.

An indeterminate result also blocks completion when the committed contract requires satisfaction to be established.

A new request with different semantics is a new Generation, not reinterpretation of the failed/incomplete one.

## Output-state decisions

002-D distinguishes:

1. **partial materialization** — incomplete logical output;
2. **complete candidate materialization** — output appears materially complete but required semantic validation/checks are pending;
3. **completed output** — all mandatory completion conditions are satisfied;
4. **abandoned/quarantined materialization** — retained output from failed/cancelled/incomplete work that is explicitly non-final.

The representation mechanism is deferred, but the completed/non-final distinction is conceptually mandatory.

## Logical output result

One successful Generation produces one logical completed synthetic-output result under the current model.

The result may be physically partitioned into many files/tables/objects/partitions.

Logical cardinality does not imply one local object or driver-returned DataFrame.

If provisional references exist before completion, they remain explicitly non-final.

## Completion contract

Generation can claim `completed` only when all mandatory committed conditions are satisfied.

Where applicable, this means:

1. committed semantics match what was actually executed;
2. Strategy/Learned State/direct inputs were sufficiently compatible;
3. no forbidden/undeclared network/dependency behavior was used;
4. operational work is sufficient for semantic completion;
5. requested logical output extent is materially complete;
6. quantity/cardinality contract is satisfied;
7. mandatory Conditions are fulfilled within committed tolerance;
8. every applicable required Constraint has a completion-sufficient satisfaction basis;
9. no required Constraint is violated, unsupported, or impermissibly indeterminate;
10. output is distinguishable from candidate/partial/recovery material;
11. one stable logical completed-output reference can be associated;
12. required provenance can be recorded consistently;
13. no terminal defect materially invalidates the result.

## Completed with limitations

A `completed with limitations` result is permitted only where mandatory requirements remain satisfied and the limitation was explicitly allowable at commitment.

Examples may include:

- best-effort Condition shortfall;
- declared approximation within an accepted tolerance;
- documented non-mandatory limitation.

It cannot be used to hide:

- violated required Constraints;
- unsupported required Constraints;
- failed mandatory Conditions;
- incomplete output;
- forbidden network/egress;
- missing mandatory dependencies.

## Execution boundary

One Generation may span several Attempts.

A failed Attempt is not automatically a failed Generation when valid retry/recovery remains possible.

Execution owns operational progress/retry mechanics; Generation owns semantic fulfillment.

`Execution.completed` remains insufficient to establish `Generation.completed`.

## Cancellation

Before commitment, a request can be withdrawn.

After commitment, cancellation becomes domain intent realized operationally through Execution when applicable.

Cancellation does not erase history and cannot retroactively cancel a Generation that already completed before cancellation was validly accepted.

Cancelled/failed partial output remains non-final.

Detailed race/terminal-state behavior is handed to 002-F.

## Privacy/release boundary

Generation completion means the committed synthesis request was fulfilled under its completion contract.

It does not mean the output is:

- anonymous;
- formally private;
- low disclosure risk;
- safe for arbitrary release;
- approved for use;
- useful for every downstream task.

Those require explicit mechanisms, Evaluation/Evidence, or external governance authority.

## Enterprise-scale conclusions

Generation control-plane state must not grow linearly with output row count merely because the output is large.

The output may contain hundreds of millions of records and remain distributed.

Completion, validation, identity, and publication must not require ordinary full-output driver collection.

Distributed validation, guarantees, summaries, or accepted approximation may support completion where their semantics are explicit.

## Synchronization refinements

### SYNC-02

Generation compatibility now explicitly includes mandatory Condition support, quantity/scope semantics, Learned State/direct-input compatibility, and material deployment/scale requirements.

### SYNC-03

Generation now defines completion implications for `unsupported`, `enforced`, and `validated later` required Constraints.

### SYNC-06

Generation commitment now binds the full request semantics, including Condition strength/tolerance and direct-generation source/input identity where required.

### SYNC-07

Generation ↔ Execution now includes retry invariance, candidate-output states, and cancellation boundaries.

### SYNC-08

Generation production now defines the actual semantic completion contract and stable logical output association.

### SYNC-10 / SYNC-12

A post-production Evaluation used to satisfy Generation completion must be capable of answering the exact required Condition/Constraint question for the exact candidate output. 002-E will refine Evidence strength and uncertainty.

### SYNC-13

Generation completion is explicitly separated from external release/use authority and privacy approval.

### SYNC-14 / SYNC-15

Committed request semantics, Conditions, quantity/scope, validation basis, output status, retry/recovery, and direct-generation inputs are now part of the Generation provenance/reproducibility story where material.

## Invariant set added/refined

1. Generation Request/Condition remain subordinate to Generation.
2. committed Generation semantics are immutable historically.
3. mandatory Conditions are required for success but do not become reusable Constraints.
4. best-effort Conditions can permit limited completion only when explicitly allowed.
5. direct-generation paths do not fabricate Learning/Learned State.
6. Learned State reuse is contextual and non-mutating.
7. unsupported applicable required Constraints block normal successful commitment/completion.
8. `validated later` required rules must be validated before Generation completion.
9. handling is not automatically satisfaction.
10. partial/candidate data is not completed output.
11. Execution completion is not Generation completion.
12. one successful Generation has one logical output result independent of physical partitioning.
13. retries do not change committed semantics.
14. failed/cancelled output remains non-final.
15. network/dependency policy cannot be silently bypassed.
16. completed-with-limitations cannot weaken mandatory requirements.
17. completion is not privacy/release approval.
18. output completion must remain viable without full-output driver collection.
19. no permanent single-table invariant is introduced.

## Deferred questions handed forward

### To 002-E — Evaluation Criterion, Evaluation & Evidence

- exact Evidence forms for mandatory Condition fulfillment;
- Constraint-satisfaction Evidence and uncertainty/approximation semantics;
- what evidence strength is sufficient for a Generation completion dependency;
- how `indeterminate`, statistical confidence, bounded approximation, and sampling affect completion;
- Evidence for fidelity/utility/privacy remains separate from basic Generation completion.

### To 002-F — Execution

- detailed Attempt/retry/resume/cancellation lifecycle;
- cancellation/completion race rules;
- partial-output cleanup/recovery realization;
- progress/status mapping without redefining Generation semantic state.

### To 002-G — Provenance / Reproducibility

- exact output/source identity/fingerprint requirements;
- required reproduction facts for Conditions and direct-generation inputs;
- how retries/partitioning/randomness affect reproducibility classes;
- historical retention of candidate/failed output references where appropriate.

## Exit criteria

002-D is complete when:

- [x] request state remains subordinate to Generation;
- [x] Generation semantic commitment is explicit;
- [x] quantity/scope semantics are model-neutral;
- [x] Condition meaning and strength are specified;
- [x] Condition remains separate from Constraint;
- [x] direct-generation and Learned-State paths are explicit;
- [x] Learned State reuse is contextual/non-mutating;
- [x] deployment/network compatibility is preserved;
- [x] required Constraint handling has explicit completion consequences;
- [x] validated-later semantics are resolved;
- [x] partial/candidate/completed output are distinguished;
- [x] stable logical output result semantics are explicit;
- [x] completion contract is defined;
- [x] completed-with-limitations cannot weaken mandatory rules;
- [x] failure/cancellation/retry semantics preserve domain/Execution boundary;
- [x] privacy/release boundary is explicit;
- [x] enterprise-scale output semantics avoid full driver collection;
- [x] canonical synchronization IDs are refined rather than duplicated;
- [x] no representation architecture is selected prematurely.

## Exit assessment

**Status: complete.**

Generation is now sufficiently specified for Phase 002-E to define Evaluation Criterion, Evaluation, and Evidence semantics that can support both independent quality/risk questions and the narrower mandatory validation dependencies required before a Generation may legitimately complete.

## Next phase

**002-E — Evaluation Criterion, Evaluation & Evidence Specification**

002-E should define criterion purpose/scope/revision, Evaluation method/specification/lifecycle, Evidence identity/strength/uncertainty/applicability, sampling/approximation semantics, Constraint/Condition validation evidence, supersession, and the boundary between Evidence and external decisions.