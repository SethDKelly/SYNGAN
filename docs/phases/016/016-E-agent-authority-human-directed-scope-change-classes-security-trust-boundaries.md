---
type: Phase Work Record
title: 016-E — Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries
status: complete
---

# 016-E — Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries

## Objective

Define the durable, tool-neutral operating authority for human-directed agent-assisted development in SYNGAN without granting autonomous work selection, weakening canonical design authority, or turning agent tooling into a new security or semantic authority plane.

## Entry evidence

~~~text
016-D                                 COMPLETE
stable-reference owner coverage       22 / 22
016-D candidate Verify #1594          PASS
016-D post-merge Verify #1595         PASS
P16-3 / P16-4 findings                0 / 0
~~~

The user explicitly authorized 016-E.

## Problem

SYNGAN now has deterministic knowledge routing, but deterministic retrieval alone does not define what an agent is allowed to do with the retrieved authority.

Without a shared operating contract, different tools or sessions could independently infer:

- whether a review request permits edits;
- how far supporting changes may extend;
- whether passing validation authorizes the next phase;
- whether a human implementation request silently changes accepted semantics;
- whether external/destructive actions are implied;
- whether retrieved text, generated output, memory, or tool privilege constitutes authority.

016-E closes those governance gaps before portable skills/adapters are introduced.

## Design direction

016-E separates two independent dimensions:

~~~text
A1-A4   = action / consequence authority
P16-0..P16-4 = change impact / repository escalation class
~~~

An apparently ordinary edit cannot use a lower action label to bypass a higher-impact P16 classification.

Human-selected work defines the task envelope. Canonical owners define current product/design meaning. Tool/runtime permissions control what can technically execute. None of those roles silently substitutes for another.

## Authorized implementation

016-E may add:

- one canonical agent authority/scope/security/trust contract;
- current root-agent guidance derived from that contract;
- canonical ownership and stable-reference routing for the new authority;
- generated OKF routing required by current projection rules;
- bounded repository fitness checks proving the authority is present and routed;
- status and closure evidence.

## Explicit exclusions

016-E does not define context budgets, skills, provider/tool adapters, vendor compatibility matrices, autonomous task queues, multi-agent orchestration, agentic CI/negative-control fixtures, implementation-package/ADR governance, provider/runtime integration, deployment, or production permissions.

## Exit criteria

016-E may close only when:

- task-selection authority and semantic authority are explicitly distinguished;
- A1 review, A2 bounded change, A3 consequential/external/destructive/scope-expanding action, and A4 semantic/architecture reopen behavior are defined;
- necessary supporting changes are bounded and cannot authorize unrelated cleanup or the next work item;
- A1-A4 and P16-0..P16-4 interaction is explicit;
- review-only and completion/no-self-progression invariants are explicit;
- least-privilege, sensitive-data/secrets, untrusted-content, memory, generated-output, and external-action trust boundaries are explicit;
- root AGENTS routes to the canonical policy rather than duplicating a second policy plane;
- canonical ownership, stable-reference routing, and OKF projection include the new authority without drift;
- existing portable and C2-C9 verification remain green;
- P16-3/P16-4 findings remain zero;
- 016-F/016-G implementation scope does not leak into 016-E.

## Closure evidence

~~~text
016-E                                 COMPLETE
change class                          P16-2
candidate head                        4d7bda7e9387d852b366059a78647686ccacf64c
pull request                          #4
candidate Verify                      35686993647 / #1597
candidate Verify result               PASS
canonical agent authority             COMPLETE
A1 review-only boundary               COMPLETE
A2 bounded repository work            COMPLETE
A3 consequential action boundary      COMPLETE
A4 semantic/architecture reopen       COMPLETE
A1-A4 / P16 orthogonality             COMPLETE
review-only invariant                 COMPLETE
completion/no-self-progression        COMPLETE
least privilege                       COMPLETE
secret/sensitive-data boundary        COMPLETE
untrusted-content trust boundary      COMPLETE
memory/generated-output trust         COMPLETE
stable-reference registry             23 ACTIVE
canonical owner-family coverage       23 / 23
OKF projection                        25 FILES / PASS
portable                              PASS
C2..C9                                PASS
P16-3 / P16-4                         0 / 0
product/runtime/provider behavior     UNCHANGED
~~~

## Exit decision

Every 016-E exit criterion is satisfied.

016-E is **COMPLETE**.

Human-selected work now defines the bounded task envelope without silently redefining current SYNGAN meaning. A1–A4 governs action/consequence authority, P16-0–P16-4 governs Phase 016 change impact, technical privilege is not treated as authorization, and passing validation cannot self-authorize subsequent work.

**016-F — Context Budgets, Portable Skills, Tool Adapters** is **NEXT ELIGIBLE / NOT AUTHORIZED** pending explicit proceed.
