---
type: Phase Record
title: 010-B — Concept Action → Actor Intent & Interaction Mapping
status: complete
---

# 010-B — Concept Action → Actor Intent & Interaction Mapping

## Objective

Map every normalized state-changing action across SYNGAN's eleven accepted concepts to actor intent and surface-neutral human/programmatic interaction obligations without selecting implementation APIs, controls, widgets, commands, persistence, services, or runtime mechanisms.

010-B is the primary Phase 010 subgroup for F1.

## Entry baseline

010-B entered after 010-A from `main` at:

```text
27178f4b075704ba75fbf5226b1316263cf08713
```

Entry state:

```text
Phase 010                    ACTIVE
010-A                        COMPLETE
010-B                        NEXT ELIGIBLE
accepted concepts            11
normalized command groups    66
F1                           PARTIAL
F2                           PARTIAL
F3                           PARTIAL TO STRONG
F4                           PARTIAL
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Governing inputs

010-B consumes:

- `docs/mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md`;
- `docs/concepts/action-query-lifecycle-normalization.md`;
- Phase 009 consolidated dependence/composition authority;
- current synchronization authority;
- current actor inventory;
- current semantic distinctions;
- retained Phase 003/006 experience evidence.

## Canonical authority established

010-B creates:

- [Concept Action → Actor Intent & Interaction Mapping](../../mapping/concept-action-actor-intent-interaction-mapping.md)

This becomes the current semantic action-mapping authority used by later Phase 010 subgroups.

## Action inventory mapped

010-B maps all normalized Phase 008-D command headings:

```text
Data Meaning             7
Synthesis Strategy       4
Learning                 8
Learned State            4
Generation              11
Constraint               4
Evaluation Criterion     4
Evaluation               8
Evidence                 3
Execution                11
Provenance               2
                         --
TOTAL                    66
```

Result:

```text
66 / 66 normalized command groups  SEMANTICALLY MAPPED
```

No command group remains `SOURCE IDENTIFIED` only.

Queries and state/history inspection are intentionally not claimed complete here and remain for 010-C.

## Mapping interpretation result

010-B confirms that conceptual command does not mean direct user control.

Examples:

```text
LearnedState.Establish
Evidence.Establish
Execution.RecordAttemptOutcome
Provenance.RecordTypedRelationship
```

may be system-established or synchronization-related transitions that actors/programmatic consumers must be able to observe and understand without a dedicated button/endpoint.

Conversely, actor-triggered actions such as `Generation.Commit` or `Execution.RequestCancellation` may require several physical gestures later rather than one direct control.

## Actor coverage

All seven 010-A actor lenses have legitimate action-mapping coverage:

```text
A1  Data Practitioner
A2  Synthetic Data Consumer
A3  Data Owner / Steward
A4  Privacy / Risk / Governance Reviewer
A5  Platform Operator
A6  Library Maintainer
A7  Synthesizer / Extension Author
```

Coverage does not imply one UI persona, authentication principal, permission role, or product edition per actor.

## Application-family preservation

010-B does not produce one mandatory full-suite action sequence.

### Direct Generation remains direct

A legitimate direct Generation path does not fabricate Learning/Learned State:

```text
propose
  -> validate
  -> commit
  -> fulfill / candidate
  -> completion-basis resolution
  -> complete | fail | cancel
```

### Learned Generation adds only actual learned-state semantics

Learning/Learned State actions appear only when reusable source-informed state is genuinely included. Learned State selection is Generation-owned contextual reuse and does not mutate Learned State.

### Evaluation-focused use remains independent where valid

Criterion/Evaluation/Evidence actions can exist without Generation.

### Evidence-gated Generation preserves staged authority

```text
Generation candidate
  -> Evaluation
  -> Evidence
  -> Generation-owned completion-basis decision
```

Evidence does not acquire Generation completion authority.

### Execution remains conditional

Execution actions exist only where durable operational realization is present. Valid Execution-light workflows do not receive fake Attempt/job lifecycle.

### Provenance remains conditional

Provenance actions exist only where material typed historical relationship capability is present. Concept-local history remains meaningful without Provenance.

## Synchronization mapping result

010-B maps synchronization relevance through the owning concept actions rather than giving synchronizations controls or state.

Key examples:

```text
Learning.Commit                   -> SYNC-01 / 02 / optional 03
Learning.InitiateRealization      -> SYNC-04
Learning.Complete                 -> SYNC-05
Generation.Commit                 -> SYNC-01 / 02 / optional 03 / 06
Generation.InitiateFulfillment    -> SYNC-07
Generation.EvaluateCompletionBasis-> optional SYNC-13
Evaluation.Commit                 -> SYNC-09
Evaluation.ValidateMethodContext  -> SYNC-10
Evaluation.Initiate               -> SYNC-11
Evaluation.Complete               -> SYNC-12
Provenance.RecordTypedRelationship-> SYNC-14
```

`SYNC-08` is not resurrected: candidate/completed synthetic output remains Generation-local lifecycle behavior.

`SYNC-15` remains reclassified under the Reproducibility Contract rather than becoming a mapped action/control.

## Important interaction distinctions retained

010-B preserves:

- semantic commitment versus operational start;
- cancellation request versus terminal cancellation;
- Attempt outcome versus parent semantic outcome;
- candidate output versus completed Generation output;
- Evaluation completion versus favorable Evidence;
- Evidence versus approval/release/privacy guarantee;
- reusable authority effectiveness versus consumer compatibility;
- future-use status changes versus historical bound truth;
- Provenance relationship assertion versus source fact ownership;
- direct versus learned Generation;
- activity-owned validation/readiness rather than global mutable readiness.

## Result-establishment actions

Learning/Evaluation producer-result synchronizations retain two owners:

```text
Learning.Complete   + LearnedState.Establish
Evaluation.Complete + Evidence.Establish
```

The producer owns semantic completion; the result concept owns the established result/finding identity.

This remains visible in mapping and avoids a generic Artifact/Promotion owner.

## Cancellation mapping result

Learning, Generation, Evaluation and Execution preserve request/intent versus resolved terminal state.

A physical surface that reports terminal `cancelled` immediately after a cancellation request would violate current mapping authority.

## Validation/readiness ownership result

No global Validation/Readiness concept is introduced.

```text
Strategy facts      -> Learning / Generation assessment
Constraint facts    -> Learning / Generation / Evaluation handling
Learned State facts -> Generation reuse assessment
Criterion facts     -> Evaluation method sufficiency assessment
Evidence finding    -> Generation completion basis or external decision input
```

Each consuming activity owns its own contextual assessment.

## Coverage advancement

Action subjects advance:

```text
SOURCE IDENTIFIED
    -> SEMANTICALLY MAPPED
```

No action is yet claimed:

```text
LINGUISTICALLY ALIGNED
SURFACE-MAPPED
FAMILY-REPLAYED
PARITY-VALIDATED
```

Those stages remain assigned to 010-D through 010-G.

## F1 disposition

010-B establishes a complete current surface-neutral action mapping:

```text
F1  CURRENTLY CLOSED FOR SEMANTIC ACTION MAPPING
    66 / 66 normalized command groups mapped
    physical interaction remains F4 / 010-E
    final Phase 010 revalidation remains 010-H
```

This does not close F2-F5.

## Stop / reopen audit

010-B finds:

```text
J1 local concept defect                 NONE FOUND
J2 purpose/catalog/boundary defect      NONE FOUND
J3 dependence/composition defect        NONE FOUND
new synchronization                     NONE
hidden coordinator                      NONE
010-B local mapping blocker             NONE FOUND
```

No concept addition/removal/merge/split/rename is justified.

No new synchronization is justified.

No mandatory full-suite workflow emerges from mapping.

## No implementation / architecture change

010-B does not add or modify:

- production code;
- tests or executable verification;
- CI/workflows;
- dependencies/lockfiles;
- package/module topology;
- persistence/data-plane schemas;
- runtime/model/platform/security adapters;
- algorithms/privacy mechanisms;
- architecture ADRs;
- concrete public API/CLI/UI contracts.

## Exit decision

```text
010-B ACTION INVENTORY COVERAGE       PASS — 66 / 66
010-B ACTOR-INTENT MAPPING            PASS
010-B FAMILY OPTIONALITY              PASS
010-B OWNERSHIP / SYNC INTEGRITY      PASS
010-B MAPPING BLOCKER                 NONE FOUND
F1 SEMANTIC ACTION MAPPING            CURRENTLY CLOSED
JACKSON CONCEPT DESIGN                NOT COMPLETE
IMPLEMENTATION READINESS              NOT READY
IMPLEMENTATION START                  NOT STARTED
IMPLEMENTATION NEXT                   NOT YET
```

## Next subgroup

**010-C — Concept State, Query, History & Explanation → Inspection Mapping** is next eligible.
