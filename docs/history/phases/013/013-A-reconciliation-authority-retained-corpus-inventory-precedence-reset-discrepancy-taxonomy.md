---
type: Phase Record
title: 013-A — Reconciliation Authority, Retained Corpus Inventory, Precedence Reset & Discrepancy Taxonomy
status: active
---

# 013-A — Reconciliation Authority, Retained Corpus Inventory, Precedence Reset & Discrepancy Taxonomy

## Objective

Establish the Phase 013 reconciliation method before any retained architecture is changed.

013-A does not decide whether individual representation, persistence, data-plane, runtime, Execution, Evidence, deployment or ADR decisions survive unchanged. It defines the authority model and classification system that later Phase 013 groups must use.

## Governing inputs

- [Phase 012 Jackson Concept-Design Consolidation](../../authority/phase-012-jackson-concept-design-consolidation.md)
- [Jackson Methodology Completion Matrix](../../authority/jackson-methodology-completion-matrix.md)
- [Jackson Design Completion & Implementation Hold](../../authority/jackson-design-completion-implementation-hold.md)
- [Residual Conceptual Misfit Register](../../authority/residual-conceptual-misfit-register.md)
- [Phase 013 Entry & Decomposition](013-entry-decomposition.md)
- [Representation & Architecture Index](../../architecture/index.md)
- retained Phase 004/006/007 architecture and ADR corpus

Canonical Phase 013 method created by this subgroup:

- [Phase 013 Architecture Reconciliation Authority](../../authority/phase-013-architecture-reconciliation-authority.md)

## Work performed

### 1. Retained corpus inventory

The current reconciliation subject contains:

```text
Phase 004 detailed architecture authorities       9
Phase 004 consolidated architecture               1
Phase 006 reconciliation overlay                  1
Phase 007-D..007-I refined architecture           6
Phase 007-J proof-boundary architecture evidence  1
Phase 007 consolidated architecture               1
---------------------------------------------------
substantive docs/architecture files               19

ADR-0001..ADR-0010                                10
```

`docs/architecture/index.md` is navigation rather than an additional substantive architecture contract.

Phase 005 planning, Phase 007-A..C scaffolding, Phase 007-K readiness history, source and tests are retained as supporting/feasibility evidence rather than architecture authority.

### 2. Precedence reset

Phase 013 now explicitly treats completed concept design as upstream of every retained architecture document, regardless of older `active`, `current`, `canonical`, `implementation-facing`, or `implementation handoff` language.

The working precedence is:

```text
current cross-cutting/method authority
  > Phase 012 completed concept design
  > current concepts
  > current dependence/application family/synchronizations
  > current mapping/experience semantics
  > current Phase 011 quality/residual rules
  > completed Phase 013 reconciliation decisions
  > retained architecture under reconciliation
  > ADR rationale under reconciliation
  > implementation/scaffold/code/test/provider evidence
```

This resolves a methodological ambiguity without yet rewriting every historical document.

### 3. Reconciliation subject statuses

Established:

```text
UNREVIEWED
ALIGNED
ALIGNED-WITH-CLARIFICATION
CONFLICTING
IMPLEMENTATION-ONLY
HISTORICAL-ONLY
UPSTREAM-CONTRADICTION-CANDIDATE
```

These classify the state of retained statements while Phase 013 proceeds.

### 4. Discrepancy taxonomy

Established:

```text
AR-0  aligned architecture
AR-1  terminology / count / identifier drift
AR-2  authority / precedence drift
AR-3  semantic ownership leakage / duplicate authority
AR-4  semantic-strength inflation
AR-5  temporal / recovery / historical-truth distortion
AR-6  application-family / composition distortion
AR-7  architecture over-prescription / implementation leakage
AR-8  unauthorized future-scope reservation
AR-9  genuine upstream semantic contradiction
```

AR-9 is intentionally narrow. Technology inconvenience, implementation cost, provider preference or existing code shape is not sufficient to reopen completed concept design.

### 5. Architecture materiality

Established:

```text
AMAT-0  editorial / historical-only
AMAT-1  bounded architecture clarification
AMAT-2  material architecture defect — must resolve before R1 closes
AMAT-3  architecture blocker / upstream contradiction candidate
```

Class and materiality remain independent.

### 6. Canonical dispositions

Established:

```text
RETAIN
CLARIFY
SUPERSEDE
CORRECT
DEFER
UPSTREAM-REOPEN
```

`UPSTREAM-REOPEN` is valid only for demonstrated AR-9 findings and must use the smallest-authority reopen discipline.

### 7. Propagation/revalidation rule

Each material finding records its owner, upstream basis, affected architecture/ADR surfaces and required blast-radius revalidation.

Phase 013 revalidates the smallest material downstream blast radius rather than replaying all architecture after every wording correction.

If an upstream reopen becomes necessary, affected Phase 013 closure pauses until that authority and its consequences are revalidated.

### 8. Residual architecture register contract

013-I must eventually account for all unresolved AMAT-2/AMAT-3 findings, AR-3..AR-9 findings, supersession ambiguity, ADR changes, M6 drift, implementation-only mandates and any M8 placeholders.

013-J cannot close R1 until:

```text
unresolved AMAT-3 blockers                0
unresolved AMAT-2 defects                 0
unresolved current-authority ambiguity    0
unresolved M6 current ambiguity           0
unjustified M8 placeholders               0
upstream reopen awaiting revalidation     0
```

## Known entry findings

013-A records six initial candidates without pre-empting later subgroup analysis.

| ID | Subject | Class | Materiality | Initial disposition | Upstream reopen |
|---|---|---|---|---|---|
| A13-A-001 | historical `15` synchronization inventory shown as current | AR-1 | AMAT-1 | CLARIFY / SUPERSEDE | NO |
| A13-A-002 | historical SYNC-08 role | AR-1 | AMAT-1 | CLARIFY / SUPERSEDE | NO |
| A13-A-003 | historical SYNC-15 role | AR-1 | AMAT-1 | CLARIFY / SUPERSEDE | NO |
| A13-A-004 | retained Phase 006/007 current/canonical precedence wording | AR-2 | AMAT-1 | CLARIFY; final disposition 013-I | NO |
| A13-A-005 | ADR index says current architecture begins at Phase 007 | AR-2 | AMAT-1 | CLARIFY; final ADR sweep 013-I | NO |
| A13-A-006 | historical implementation-reentry/scaffold assumptions | AR-7 / historical | AMAT-0..1 | DEFER / SUPERSEDE as authority | NO |

No AMAT-2 or AMAT-3 defect is declared by 013-A itself. The purpose of later groups is to determine whether any exists.

## Architecture areas assigned downstream

```text
013-B  representation / public contract / identity / views
013-C  persistence / history / transactions / migration / recovery state
013-D  distributed data / topology / manifest / candidate-seal-promotion
013-E  Strategy/method realization / dependencies / security / runtime closure
013-F  Execution / Attempt / fencing / recovery / admission
013-G  Evaluation / Evidence / Provenance / history / disclosure
013-H  deployment / scale / observability / portability / provider integration
013-I  cross-architecture / ADR / legacy / M6 / residual register
013-J  R1 closure / Phase 014 handoff
```

## Non-goals confirmed

013-A makes no production code or schema changes and selects no:

- package topology;
- public API spelling;
- database or event store;
- graph store;
- scheduler;
- provider adapter implementation;
- fencing mechanism;
- runtime package-distribution mechanism;
- formal privacy/accounting architecture;
- publication/governance/session/resource subsystem.

## Exit review

```text
retained substantive architecture docs       19
retained ADRs                                10
precedence reset                             COMPLETE
subject-state model                         COMPLETE
AR-0..AR-9 taxonomy                         COMPLETE
AMAT-0..AMAT-3 materiality                  COMPLETE
disposition vocabulary                      COMPLETE
propagation/revalidation rules              COMPLETE
residual-register contract                  COMPLETE
known entry candidates                       6
AMAT-2 defects declared by 013-A             0
AMAT-3 blockers declared by 013-A            0
upstream reopen                             NONE
```

Decision:

```text
013-A  COMPLETE
R1     DOWNSTREAM / IN PROGRESS
013-B  NEXT ELIGIBLE
```

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
