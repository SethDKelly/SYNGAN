---
type: Phase Work Record
title: 016-C — OKF v0.2 Producer Profile, Generated Knowledge Projection & Conformance
status: complete
---

# 016-C — OKF v0.2 Producer Profile, Generated Knowledge Projection & Conformance

## Objective

Establish one externally grounded OKF v0.2 producer contract and a deterministic compatibility projection that improves exchange and agent discovery without duplicating SYNGAN semantic authority.

## Entry evidence

~~~text
016-B                                COMPLETE
current/history separation            COMPLETE
canonical ownership map               COMPLETE
progressive-disclosure routing        COMPLETE
repository-local Markdown links       PASS
C0-C9                                 PASS
P16-3 / P16-4 findings                0 / 0
~~~

The user explicitly authorized 016-C after the audited 016-B closure.

## External-authority audit

The current Open Knowledge Format v0.2 specification was reviewed from `GoogleCloudPlatform/knowledge-catalog` at commit `22efaa5402775a7c4d4c37f89e41258daaf3cb65`.

The audit confirmed that strict OKF v0.2 has different structural rules from SYNGAN's authored docs convention, especially around reserved `index.md`/`log.md` files and the minimal required `type` field on concept documents.

Therefore 016-C does not force authored current authorities into the transport format.

## Decision

~~~text
docs/       AUTHORED CURRENT AUTHORITY
knowledge/  GENERATED OKF v0.2 COMPATIBILITY / ROUTING
~~~

The generated projection is downstream, deterministic, disposable, and non-authoritative.

This is a P16-2 compatibility/process decision. No semantic or architecture reopen is required.

## Authorized implementation

016-C may add a canonical producer-profile authority, a machine-readable projection manifest, deterministic generator/checker, dependency-free conformance validator, generated `knowledge/` routing bundle, repository fitness checks integrated into existing authority/portable verification, and current-status/routing updates required to express this decision.

## Explicit exclusions

016-C does not add stable IDs or stable-reference resolution, a general deterministic context resolver, agent authority/action/change policy, context-budget/tool-adapter rules, a separate agentic negative-control CI lane, or product/runtime/provider behavior.

Those remain reserved for 016-D through 016-G or later authorized work.

## Exit criteria

016-C may close only when:

- external OKF v0.2 minimum conformance is accurately represented;
- the SYNGAN producer profile is canonical and explicit;
- `docs/` remains the only authored authority plane;
- `knowledge/` is generated deterministically from repository-owned input;
- generated drift is mechanically detectable;
- committed projection passes external-structure and project-profile validation;
- local projection resources/links resolve;
- existing repository verification remains green;
- P16-3/P16-4 findings remain zero;
- no stable-reference or agent-governance scope leaks into 016-C.

## Closure evidence

~~~text
016-C                                 COMPLETE
change class                          P16-2
candidate head                        a3a35aec0de1a6b243d2a4d461e845319a17fd41
pull request                          #2
candidate Verify                      35684468631 / #1581
candidate Verify result               PASS
portable                              PASS
control/data/runtime/execution        PASS
evidence/security/platform            PASS
cross-slice                           PASS
generated projection files            23
generation drift check                PASS
OKF v0.2 + SYNGAN profile             PASS
P16-3 / P16-4                         0 / 0
product/runtime/provider behavior     UNCHANGED
~~~

## Exit decision

Every 016-C exit criterion is satisfied.

016-C is **COMPLETE**.

The authored `docs/` tree remains the only semantic/current-authority plane. The generated `knowledge/` tree is deterministic compatibility/routing only.

**016-D — Stable References, Deterministic Resolution & Drift Control** is **NEXT ELIGIBLE / NOT AUTHORIZED** pending explicit proceed.
