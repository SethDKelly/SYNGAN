---
type: Synchronization Index
title: SYNGAN Accepted Synchronizations
status: complete-current
---

# SYNGAN Accepted Synchronizations

This directory contains current cross-concept coordination authority. Concept specifications own semantic state; synchronization coordinates already-owned behavior and owns no independent canonical state.

## Current canonical synchronization authority

Begin with [Current Cross-Concept Synchronization Contract](current-cross-concept-synchronizations.md).

`core-synchronizations.md` remains retained historical detail and stable anchor material. Where it uses the pre-Phase-009 fifteen-rule interpretation, the current contract controls.

## Current inventory

```text
accepted concepts                       11
historical synchronization IDs          15
active cross-concept synchronizations   13
required-relational                      6
capability/occurrence conditional        7
retired concept-local IDs                1  (SYNC-08)
reclassified contract IDs                1  (SYNC-15)
synchronization-owned canonical state    NONE
```

Required-relational rules remain `SYNC-01`, `SYNC-02`, `SYNC-05`, `SYNC-09`, `SYNC-10`, and `SYNC-12`.

Capability/occurrence-conditional rules remain `SYNC-03`, `SYNC-04`, `SYNC-06`, `SYNC-07`, `SYNC-11`, `SYNC-13`, and `SYNC-14`.

`SYNC-08` is retired as a cross-concept synchronization because candidate/finality/completed-output behavior is Generation-local authority.

`SYNC-15` is historical/reclassified under the cross-cutting Reproducibility Contract. Reproducibility owns no synchronization state.

## Phase 013 result

```text
M6 synchronization drift        CLOSED
historical IDs                  15
active synchronizations         13
SYNC-08                         RETIRED
SYNC-15                         RECLASSIFIED
current-authority ambiguity     0
synchronization reopen          NONE
Phase 013                       COMPLETE
R1                              CURRENTLY CLOSED
```

The Phase 013 Consolidated Architecture Contract preserves singular ownership across representation, persistence, data-plane, runtime/security, Execution/recovery, Evidence/history and platform integration.

## Future synchronization rule

Add a future synchronization only when existing concepts already own the substantive state, a genuinely new relation is required, that relation owns no independent state, and the current inventory cannot express it.

If future scope introduces independent purpose + durable state/history + meaningful actions/lifecycle, concept rediscovery occurs first. M8 triggers do not justify placeholder synchronization IDs.

## Current next boundary

**Phase 014 pre-phase start gate — whole-design/readiness decomposition** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
