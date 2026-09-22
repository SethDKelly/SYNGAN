---
type: Phase Record
title: 010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline
status: complete
---

# 010-A — Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline

## Objective

Establish the canonical control model for Phase 010 before individual concept actions, queries, language, or physical interactions are mapped.

010-A answers:

> **What must every current concept mapping record contain, which actors and surface families must be considered, how application-family conditionality is represented, what counts as mapping coverage, and which retained Phase 003/006 experience evidence remains current versus requiring normalization?**

010-A is design-only.

It does not map all concept actions/queries, select implementation APIs/UI, reconcile architecture, or authorize implementation.

## Entry baseline

010-A entered after Phase 010 decomposition from `main` at:

```text
f607efe61860b5de12a438563fda71086aa6b017
```

Entry state:

```text
Phase 009                    COMPLETE
Phase 010                    ACTIVE
Phase 010 decomposition      COMPLETE
010-A                        NEXT ELIGIBLE
accepted concepts            11
historical SYNC IDs          15
active synchronizations      13
F1                           PARTIAL
F2                           PARTIAL
F3                           PARTIAL TO STRONG
F4                           PARTIAL
F5                           STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
implementation readiness     NOT READY
implementation start         NOT STARTED
implementation next          NOT YET
```

## Governing inputs reviewed

010-A reconciles:

- Phase 008 normalized action/query/lifecycle authority;
- Phase 009 consolidated dependence/application-family/composition authority;
- current Actors & Needs;
- current terminology and semantic distinctions;
- Phase 003 consolidated experience evidence;
- Phase 006 recovery/security/degraded/history/topology experience evidence.

## Canonical authority established

010-A creates:

- [Mapping Authority, Coverage Model, Actor/Surface Taxonomy & Evidence Baseline](../../../mapping/mapping-authority-coverage-actor-surface-evidence-baseline.md)

This becomes the Phase 010 control authority used by 010-B through 010-H.

## Mapping-record schema result

Every current mapping record must be able to represent nineteen fields:

```text
M1   mapping identifier
M2   concept owner
M3   conceptual subject
M4   actor intent / need
M5   interaction / inspection obligation
M6   semantic precondition / guard context
M7   success / result semantics
M8   non-success / uncertainty semantics
M9   application-family applicability
M10  synchronization relevance
M11  temporal orientation
M12  disclosure annotation
M13  historical-knowledge annotation
M14  scale / boundedness annotation
M15  candidate surface families
M16  vocabulary / linguistic risk
M17  evidence source
M18  mapping status
M19  misfit / reopen note
```

The schema is documentation/design authority only. It does not imply a public resource schema, database table, serialized contract, event, endpoint, or class.

## Coverage model result

010-A defines twelve orthogonal coverage dimensions:

```text
COV-A  action coverage
COV-Q  query / observation coverage
COV-S  lifecycle / state distinction coverage
COV-H  historical / exact-binding coverage
COV-X  synchronization visibility
COV-R  actor relevance
COV-L  language coverage
COV-P  physical/surface interaction coverage
COV-F  application-family variant coverage
COV-D  disclosure / uncertainty / history-quality coverage
COV-E  enterprise-scale boundedness
COV-Y  human/programmatic semantic parity
```

A mapping is not complete merely because a concept has an API-shaped operation, workflow step, or UI representation.

## Controlled mapping coverage states

Phase 010 now uses:

```text
SOURCE IDENTIFIED
SEMANTICALLY MAPPED
LINGUISTICALLY ALIGNED
SURFACE-MAPPED
FAMILY-REPLAYED
PARITY-VALIDATED
BLOCKED BY MISFIT
```

These are Phase 010 documentation coverage states, not domain/runtime lifecycle statuses.

## Actor taxonomy

010-A adopts seven current actor roles:

```text
A1  Data Practitioner
A2  Synthetic Data Consumer
A3  Data Owner / Steward
A4  Privacy / Risk / Governance Reviewer
A5  Platform Operator
A6  Library Maintainer
A7  Synthesizer / Extension Author
```

These roles express mapping needs and viewpoints.

They do not establish authentication principals, permissions, organizational roles, approval authority, or implementation personas.

## Surface taxonomy

010-A adopts seven surface families:

```text
S1  SDK / API automation
S2  notebook / interactive analysis
S3  CLI / operational interaction
S4  report / history / review artifact
S5  graphical UI
S6  operator / admin surface
S7  external integration / handoff
```

These are mapping lenses, not mandatory architecture components or product editions.

## Application-family mapping tags

Every conditional mapping may use:

```text
AF-AUTH   authority-only usage
AF-L      L-KERNEL
AF-GD     direct G-KERNEL
AF-GL     learned-state-assisted Generation
AF-E      E-KERNEL / evaluation-focused usage
AF-GE     evidence-gated Generation
AF-C      reusable Constraint relation present
AF-X      durable Execution relation present
AF-P      Provenance relation/history capability present
AF-FULL   full eleven-concept composition
AF-EXT    external handoff/integration boundary
```

These labels preserve Phase 009 optionality and are explicitly not package/SKU/deployment/feature-flag definitions.

## Eleven-concept source coverage

All eleven accepted concepts now have an explicit Phase 010 source row pointing to normalized action/query authority and principal actor/family lenses.

Current 010-A status for each concept is:

```text
SOURCE IDENTIFIED
```

No concept is prematurely marked semantically mapped.

Detailed action mapping remains 010-B; state/query/history mapping remains 010-C.

## Phase 003 evidence replay

010-A retains as current in substance:

- preparation/readiness as contextual rather than global mutable state;
- semantic commitment and exact historical bindings;
- operational realization distinct from semantic lifecycle;
- physical existence distinct from authoritative result;
- review-before-commit;
- retry/resume same-semantics discipline;
- cancellation intent versus resolution;
- Evaluation success versus favorable Evidence;
- Evidence versus external decision authority;
- historical/current separation;
- relational Provenance;
- qualified Reproducibility;
- typed disclosure states;
- enterprise-scale bounded experience;
- anti-god-concept experience rules.

010-A explicitly supersedes or normalizes stale assumptions:

```text
15 historical synchronization IDs != 15 currently active synchronizations
SYNC-08 is not an active output-promotion synchronization
SYNC-15 is not an active reproducibility synchronization
Learning is not universal for Generation
Evaluation/Evidence are not universal for Generation
Execution is not universal for domain activity
Provenance is not universal
Readiness/Validation do not become global concept owners
```

## Phase 006 evidence replay

010-A retains:

- orthogonal semantic/operational/actionability/authority/disclosure/history dimensions;
- queued versus blocked/incompatible/denied/failure distinctions;
- recovery authority-continuity visibility;
- reconstructed versus retained history;
- capability-specific degradation;
- driver versus distributed-worker runtime closure;
- no hidden acquisition/remote fallback where prohibited;
- Evidence/formal-guarantee/release separation;
- inspectable topology semantics;
- whole-result completion distinct from constituent progress.

Architecture-shaped terms remain experience evidence rather than new concept authority.

## Cross-cutting mapping annotations established

Every later mapping must account for relevant instances of:

- semantic versus operational state;
- candidate/intermediate versus authoritative result;
- current versus historical status;
- Evidence versus external decision;
- Provenance relation versus source fact;
- actionability versus domain lifecycle;
- disclosure state;
- historical-knowledge quality;
- enterprise-scale boundedness.

## Completeness ledgers

Phase 010 now requires three completion ledgers:

```text
Ledger A  concept behavior coverage
Ledger B  interaction expression coverage
Ledger C  parity / difficult-condition coverage
```

010-H cannot close F1-F5 while a material coverage hole or `BLOCKED BY MISFIT` mapping remains unresolved.

## Stop/reopen result

010-A finds no upstream blocker.

```text
J1 local concept defect             NONE FOUND
J2 purpose/catalog/boundary defect  NONE FOUND
J3 dependence/composition defect    NONE FOUND
mapping-foundation blocker          NONE FOUND
```

No concept, synchronization, application-family edge, or hidden coordinator is added.

## Methodology disposition

```text
F1  PARTIAL
    mapping schema/coverage exists; action mappings pending 010-B

F2  PARTIAL
    inspection schema/coverage exists; state/query mappings pending 010-C

F3  PARTIAL TO STRONG
    terminology evidence classified; current language mapping pending 010-D

F4  PARTIAL
    surface taxonomy exists; physical interaction mapping pending 010-E

F5  STRONG EVIDENCE / CURRENT REVALIDATION REQUIRED
    parity foundation established; replay pending 010-G
```

## No executable / architecture change

010-A adds no production behavior, tests, CI/workflows, dependencies, lockfiles, package topology, persistence/data-plane schemas, runtime/model/platform/security adapters, APIs, algorithms, privacy mechanisms, architecture ADRs, or public interface contracts.

## Exit assessment

```text
010-A MAPPING AUTHORITY / SCHEMA          PASS
010-A COVERAGE MODEL                      PASS
010-A ACTOR TAXONOMY                      PASS
010-A SURFACE TAXONOMY                    PASS
010-A EVIDENCE BASELINE                   PASS
UPSTREAM J1/J2/J3 BLOCKER                 NONE FOUND
JACKSON CONCEPT DESIGN                    NOT COMPLETE
IMPLEMENTATION READINESS                  NOT READY
IMPLEMENTATION START                      NOT STARTED
IMPLEMENTATION NEXT                       NOT YET
```

## Next subgroup

**010-B — Concept Action → Actor Intent & Interaction Mapping** is next eligible.
