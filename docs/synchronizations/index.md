---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: complete-current
---

# SYNGAN Accepted Synchronizations

This directory contains current cross-concept composition authority for SYNGAN. Concept specifications own semantic state; synchronization coordinates already-owned behavior and owns no independent canonical state.

## Current canonical synchronization authority

Begin with:

- [Current Cross-Concept Synchronization Contract](current-cross-concept-synchronizations.md)

`core-synchronizations.md` remains retained historical specification/detail and stable anchor material. Where it uses the pre-Phase-009 fifteen-rule interpretation, the current contract controls.

## Current inventory

```text
accepted concepts                       11
historical synchronization IDs          15
active cross-concept synchronizations   13
required-relational                      6
capability/occurrence conditional        7
retired concept-local IDs                1  (SYNC-08)
reclassified contract IDs                1  (SYNC-15)
new synchronization IDs                  0
synchronization-owned canonical state    NONE
```

Required-relational rules:

```text
SYNC-01  Data Meaning revision binding
SYNC-02  Strategy selection and compatibility
SYNC-05  Learning produces Learned State
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-12  Evaluation produces Evidence
```

Capability/occurrence-conditional rules:

```text
SYNC-03  Constraint binding / handling
SYNC-04  Learning operational realization
SYNC-06  Generation commitment / compatibility
SYNC-07  Generation operational realization
SYNC-11  Evaluation operational realization
SYNC-13  controlled Evidence handoff
SYNC-14  material Provenance recording
```

## Retired / reclassified IDs

`SYNC-08` is retired as a cross-concept synchronization. Candidate/finality/completed-output behavior is Generation-local authority.

`SYNC-15` is historical/reclassified under the cross-cutting [Reproducibility Contract](../authority/reproducibility-contract.md). Reproducibility owns no synchronization state.

Historical IDs are never renumbered or reused.

## Canonical ownership

```text
consumer exact bindings / contextual assessments  -> owning activity
producing Learning identity                       -> Learned State
producing Evaluation identity                     -> Evidence
Execution parent binding + Attempts/recovery       -> Execution
Generation candidate/output/completion             -> Generation
Provenance typed relationships                     -> Provenance
synchronization-owned canonical state              -> NONE
```

## Phase 013 result

Phase 013 closed architecture reconciliation while preserving singular ownership and application-family optionality. M6 synchronization drift is closed; no synchronization reopen occurred.

## Phase 014 boundary

Phase 014 must retest these rules only as part of whole-design composition. It must detect any downstream mapping/architecture interaction that would force a hidden coordinator, universal workflow, duplicate owner or invalid synchronization assumption.

The whole-design audit may reopen synchronization authority only if current cross-layer evidence actually contradicts this inventory/ownership model.

## Current phase state

```text
Phase 009 synchronization authority       COMPLETE
13 / 13 singular ownership                PASS
M6                                        CLOSED
synchronization reopen                    NONE
Jackson concept design                    COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013                                 COMPLETE
R1                                        CURRENTLY CLOSED
Phase 014                                 ACTIVE
Phase 014 subgroup sequencing       SEE docs/phases/014/index.md
R2                                        OPEN
R3                                        OPEN
```

## Future synchronization rule

Add a future synchronization only when existing concepts already own the substantive state, a genuinely new relation is required, that relation owns no independent state, and the current inventory cannot express it.

If future scope introduces independent purpose + durable state/history + meaningful actions/lifecycle, concept rediscovery occurs first. M8 triggers do not justify placeholder synchronization IDs.

## Current next boundary

Current Phase 014 subgroup sequencing is governed by [`docs/phases/014/index.md`](../phases/014/index.md).

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
