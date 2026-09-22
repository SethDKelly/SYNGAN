---
type: Phase Work Record
title: 016-E — Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries
status: active
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

## Current state

~~~text
016-E                                 AUTHORIZED / ACTIVE
canonical authority contract           IN PROGRESS
root AGENTS derivation                 IN PROGRESS
ownership/reference/OKF routing        IN PROGRESS
bounded fitness evidence               IN PROGRESS
P16-3 / P16-4                         0 / 0
016-F                                  NOT AUTHORIZED
~~~
