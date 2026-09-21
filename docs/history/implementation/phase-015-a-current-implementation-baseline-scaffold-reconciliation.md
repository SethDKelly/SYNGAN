
---
type: Implementation Authority
title: 015-A — Current Implementation Baseline, Repository/Toolchain & Scaffold Reconciliation
status: complete-current
---

# 015-A — Current Implementation Baseline, Repository/Toolchain & Scaffold Reconciliation

## Purpose

Consume the Phase 015 start-gate authorization and establish a trustworthy current repository baseline without implementing domain behavior.

015-A reconciles:

- current implementation authority discovery;
- repository/build/toolchain bootstrap;
- Phase 007 scaffold residue;
- architecture-fitness constraints;
- executable phase/status gates;
- package/build verification assumptions.

## Authorized scope

015-A was limited to:

~~~text
authority/documentation reconciliation
repository/toolchain reconciliation
scaffold/test retain-revise-remove decisions
obsolete phase-state fitness removal/rewrite
architecture-fitness normalization
no-domain bootstrap corrections
~~~

It did not authorize concept/domain behavior, persistence, distributed data, runtime, Execution/recovery, Evaluation/Evidence/Provenance, security/provider behavior, or scale claims.

## Baseline reconciliation performed

### Repository/toolchain retained

The current baseline retains:

~~~text
one syngan distribution
src/ layout
py.typed
Python >= 3.11
pyproject.toml
uv
Hatchling
pytest
Hypothesis availability
Ruff
mypy
Import Linter availability
coverage diagnostics
portable-core external-network-denied capability
empty base runtime dependency set
optional/provider dependency isolation
general inward-dependency intent
~~~

No production runtime dependency was added.

### Exact package topology de-authorized

The prior fitness test requiring exactly seven top-level packages was removed as a permanent constraint.

Current fitness now checks only durable baseline properties:

- no generic hidden-owner packages;
- root package does not eagerly import outer/provider integrations;
- production source does not import test support;
- package root and typing marker exist.

The existing seven scaffold packages remain present as feasibility structure; their exact set is no longer an architecture invariant.

### Import Linter normalized

The historical exact layered graph was replaced with two current baseline contracts:

~~~text
semantic-core-stays-inward
portable-core-no-outer-integration
~~~

These protect durable responsibility boundaries without requiring the historical seven-package graph to remain the final physical topology.

015-B may refine current architecture-fitness coverage from Phase 013/014 authority.

### Phase 007 executable status gates removed

The obsolete test that asserted Phase 007 progression, 007-D lock state, and 007-C authority wording was deleted.

A current Phase 015 authority fitness test replaced it.

The new test protects:

- current Phase 015 authority discoverability;
- current slice-bounded authorization;
- locked later slices;
- agent guidance consistency;
- continued scaffold presence.

### Bootstrap metadata tests reconciled

Bootstrap tests now assert:

- retained Python/build/packaging choices;
- empty base runtime dependencies during 015-A;
- only reauthorized bootstrap tool families;
- deferred runtime/provider dependencies remain absent;
- current normalized Import Linter contracts.

They no longer describe the state as "007-C".

### Package verification made topology-neutral

Repository package verification no longer hard-codes the seven historical subpackages.

It discovers current top-level Python subpackages from the source tree, imports those packages, and verifies that the built wheel contains the package paths actually present in the current scaffold.

This allows future authorized topology evolution without weakening package integrity.

### Current authority paths normalized

The repository bootstrap verifier now requires the Phase 015 implementation authority and start-gate record rather than Phase 007 implementation-lock documents.

The adapter scaffold wording was also normalized from 007-C to the current 015-A boundary.

## Historical implementation disposition after 015-A

~~~text
Phase 005 plans        historical planning evidence
Phase 006 overlay      historical planning refinement
Phase 007 source       reconciled feasibility scaffold
Phase 007 phase locks  removed from current executable verification
Phase 007 exact tree   not current architecture authority
Phase 015 start gate   current implementation authority source
015-A                  current completed baseline authority
~~~

Named persistence/provider/runtime choices remain deferred to their owning later slices.

## Domain-implementation check

~~~text
concept/domain behavior         NONE
persistence implementation      NONE
distributed data behavior       NONE
Strategy/runtime behavior       NONE
Execution/recovery behavior     NONE
Evidence/Provenance behavior    NONE
security/provider behavior      NONE
base runtime dependencies       []
~~~

015-A therefore remains a no-domain implementation-baseline slice.

## Verification evidence

The repository-owned Verify workflow passed on the completed executable 015-A baseline:

~~~text
commit     e24553b5f7302392c6fd8081e107a7c8fac2e922
workflow   Verify
run        35556553627
result     SUCCESS
~~~

The successful run exercised:

- lockfile check;
- Ruff lint;
- Ruff format;
- mypy;
- unit tests;
- Import Linter architecture checks;
- fitness tests;
- package import/build verification.

## Readiness-risk disposition

### RR-01 — historical implementation-plan re-baselining

015-A establishes current precedence and removes historical implementation plans from executable authority.

Status:

~~~text
INITIAL CONTROL COMPLETE
final historical-residue closure remains 015-J
~~~

### RR-02 — historical scaffold / fitness-test reauthorization

015-A reconciles the existing scaffold and removes obsolete Phase 007 executable gates.

Status:

~~~text
SCAFFOLD RECONCILIATION COMPLETE
current verification-harness expansion continues in 015-B
~~~

No other Phase 014 readiness risk is claimed closed by 015-A.

## 015-A exit criteria

~~~text
current implementation authority discoverable   PASS
historical Phase 007 executable lock removed     PASS
exact seven-package permanence removed           PASS
durable inner/outer fitness retained             PASS
toolchain retained without new runtime deps       PASS
package verification topology-neutral             PASS
domain implementation absent                      PASS
full repository Verify workflow                   PASS
architecture/design reopen required               NO
~~~

## 015-A result

~~~text
015-A                                  COMPLETE
ICLASS-3 findings                      0
ICLASS-4 findings                      0
upstream reopen                        NONE
IMPLEMENTATION READINESS               READY
IMPLEMENTATION START                   NOT STARTED
015-B                                  NEXT ELIGIBLE / NOT AUTHORIZED
015-C..015-J                           NOT AUTHORIZED
~~~

015-A does not authorize 015-B automatically.

## Current next boundary

**015-B — Current Verification Harness, Architecture-Fitness & Evidence-Gate Foundation** is next eligible but remains **NOT AUTHORIZED** pending explicit proceed.
