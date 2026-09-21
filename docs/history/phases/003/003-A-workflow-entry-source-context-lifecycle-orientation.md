---
type: Phase Record
title: 003-A — Workflow Entry, Source Context & Lifecycle Orientation
status: complete
---

# 003-A — Workflow Entry, Source Context & Lifecycle Orientation

## Objective

Establish the first canonical experience layer for SYNGAN by defining how actors/programmatic users enter new or existing work, orient around source/result context, understand editable versus committed lifecycle state, and distinguish semantic activity status from operational Execution state.

003-A translates Phase 002 semantics into experience obligations without selecting final UI/API/package architecture.

## Governing authority

- [Phase 002 Exit](../002/002-H-cross-concept-invariant-synchronization-consolidation-review.md)
- [Accepted Concepts](../../concepts/index.md)
- [Accepted Synchronizations](../../synchronizations/index.md)
- [Design Authority](../../authority/index.md)
- [Reproducibility Contract](../../authority/reproducibility-contract.md)
- [Actors & Needs](../../problem/actors.md)

## Canonical experience authority created

003-A establishes:

- [Experience & Workflow Design Index](../../experience/index.md)
- [Workflow Entry, Source Context & Lifecycle Orientation](../../experience/workflow-entry-source-context-lifecycle-orientation.md)

## Main decisions

### 1. Entry is intent-oriented rather than one mandatory wizard

Legitimate entry includes:

- new source/direct-input synthesis preparation;
- continuation of draft/prepared work;
- observation/recovery of committed work;
- Learned State reuse;
- Evaluation/review of an existing subject;
- historical/provenance/reproducibility inspection.

No one linear workflow is mandatory for all actors or strategies.

### 2. Workflow orientation is an experience composition, not a concept

A composed orientation view may summarize source/result identity, Data Meaning, Constraints, Strategy, domain activity, lifecycle, Execution/Attempt state, dependencies, blockers, Evidence, Provenance, and reproducibility availability.

It does not own any of those states and does not create a generic `Workflow`, `Session`, `Project`, or `Dataset Context` concept.

### 3. Source context remains composed

`Source context` is experience language, not a new domain concept.

It may compose:

- human-usable locator/alias;
- stable historical identity/version/fingerprint when known;
- schema/scale summaries;
- Data Meaning readiness;
- Constraint context;
- access/dependency facts;
- prior-use provenance.

A mutable locator alone is insufficient to imply historical/reproducible identity.

### 4. Mutable source and committed source are visibly different

Before commitment, a mutable source may be refreshed/re-resolved and draft preparation updated.

After commitment, Learning/Generation/Evaluation remain bound to the exact source/context actually used.

Opening historical work defaults to historical bindings rather than silently substituting today's source contents/configuration.

### 5. Commitment is a visible experience boundary

The experience distinguishes:

```text
editable/proposed -> validated/ready -> committed
```

After commitment, material semantic changes create a new distinguishable domain activity rather than a hidden retry mutation.

Commitment should therefore be reviewable/consequential rather than presented as an undifferentiated generic `run` action.

### 6. Semantic and operational state remain separate

Experience surfaces may summarize them together but must preserve distinctions such as:

```text
Generation: awaiting required validation
Execution: completed
Latest Attempt: succeeded
```

or:

```text
Learning: committed / deriving
Execution: recovery pending
Latest Attempt: failed, recoverable
```

Platform success/failure does not replace domain lifecycle semantics.

### 7. Candidate and authoritative results remain visually/programmatically distinct

The experience must distinguish:

- checkpoint/intermediate material from Learned State;
- partial/candidate output from completed Generation output;
- diagnostic method output from durable Evidence;
- historical valid result from current preferred/usable status.

### 8. Indeterminate state is preserved

Unknown/unresolved/indeterminate state cannot be flattened into generic pass/fail for presentation convenience.

Blockers, permitted limitations, warnings, and operational incidents should remain distinguishable.

### 9. Actor orientation differs without changing semantics

Practitioner, Steward, Platform Operator, Governance Reviewer, and Synthetic Data Consumer may receive different emphasis, but all views reference the same canonical state.

### 10. Human/programmatic parity is required

Later APIs, CLI, notebooks, or UI surfaces may differ ergonomically, but all must make material commitment, lifecycle, blockers/limitations, candidate/result, dependency, Execution, and provenance distinctions inspectable.

### 11. No hidden network/dependency behavior at entry

Material dependency/no-egress requirements should be visible before commitment. Missing dependencies cannot silently trigger download/acquisition or remote fallback.

### 12. Large-data orientation remains distributed

Entry/orientation may use schema, catalog metadata, stable references, distributed summaries/counts, bounded profiles, and representative diagnostics.

It does not require full source/output driver collection.

## Lifecycle orientation pattern

003-A adopts a common actor-orientation pattern where applicable:

```text
editable / proposed
      ↓
validated / ready
      ↓
semantic commitment
      ↓
realization / fulfillment / examination
      ↓
possible pending semantic checks
      ↓
semantic terminal outcome
```

This is explicitly not a universal concept lifecycle enum.

## Next-action guidance

Experience surfaces should help actors understand legitimate next actions from canonical state rather than invent transitions through a generic workflow engine.

Examples include:

- draft Generation → resolve incompatibility → review Conditions → commit;
- failed recoverable Attempt → inspect → retry/resume;
- candidate output awaiting validation → perform/await Evaluation;
- completed output → evaluate / inspect Evidence / inspect Provenance.

## No new concept result

003-A does not require new standalone concepts for:

- Workflow;
- Source Context;
- Dataset;
- Session;
- Project;
- Run;
- Status;
- Validation;
- Next Action.

These remain experience compositions, subordinate state, representation choices, or derived guidance.

## Deferred to later Phase 003 groups

### 003-B

Deepen preparation/review of Data Meaning, Constraints, and Strategy compatibility before commitment.

### 003-C

Deepen Learning initiation, observation, Learned State inspection/reuse/restriction/retirement experiences.

### 003-D

Deepen Generation request/Condition editing, validation, candidate-output and promotion experiences.

### 003-E

Deepen Criterion/Evaluation/Evidence selection, interpretation, comparison, and review.

### 003-F

Deepen Execution/Attempt monitoring, failure diagnosis, recovery, retry, cancellation, and unknown-state experiences.

### 003-G

Deepen Provenance traversal, reproduction assessment, historical comparison, and dependency-history inspection.

### 003-H

Deepen enterprise dependency, no-egress, sensitive-state, and safety experiences.

## Representation questions intentionally deferred

003-A does not choose:

- web UI versus notebook versus CLI versus SDK;
- final public API names;
- workflow/session Python object;
- source-reference schema;
- database/persistence technology;
- dashboard visual design;
- orchestration engine;
- auth/access-control implementation.

## Exit criteria

- [x] actor/programmatic entry modes defined;
- [x] source context composition defined without new Dataset concept;
- [x] mutable alias versus historical identity exposed;
- [x] source refresh before commitment distinguished from committed history;
- [x] editable/validated/committed orientation defined;
- [x] semantic versus operational status separation preserved;
- [x] candidate/intermediate versus authoritative result distinction preserved;
- [x] unknown/indeterminate status preserved;
- [x] blocker/limitation/warning/incident distinction established;
- [x] actor-specific emphasis defined;
- [x] human/programmatic parity established;
- [x] offline/no-egress dependencies visible before commitment;
- [x] enterprise-scale entry avoids mandatory driver collection;
- [x] no new god-concept introduced;
- [x] representation architecture remains deferred.

## Exit assessment

**Status: complete.**

SYNGAN now has a canonical entry/orientation experience that exposes the Phase 002 semantic system without collapsing it into a generic workflow or platform-run abstraction.

## Next phase

**003-B — Data Meaning, Constraint & Strategy Preparation Experience**
