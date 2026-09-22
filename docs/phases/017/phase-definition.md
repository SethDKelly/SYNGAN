---
type: Phase Definition
title: Phase 017 — Implementation Program Design, Autonomous Delivery Methodology & v0.x/v1 Roadmap
status: active
---

# Phase 017 — Implementation Program Design, Autonomous Delivery Methodology & v0.x/v1 Roadmap

## Role

Phase 017 is a **planning-only implementation-program design phase**. It converts the completed
Phase 016 readiness state into a bounded executable-program roadmap without starting product
implementation.

It defines how future implementation phases will be structured, how Cursor and Codex will be used
without creating unbounded autonomy, how v0.x package-MVP work will be decomposed, how MVP
completion will be independently qualified, and how v1 will be planned at deliberately lower
granularity.

## Governing inputs

Phase 017 is downstream of:

- current repository status and Phase 016 exit;
- current implementation governance and support scope;
- implementation-package / traceability / ADR change control;
- engineering preflight and readiness residuals;
- agent authority and bounded-context/tool-neutral workflow contracts;
- current architecture, concepts, synchronizations, and dormant M8 rediscovery triggers.

The Base phase lifecycle is used as a structural model: phase definition, start gate, dynamically
derived substantive subphases, success/evidence contract, exit review, and explicit handoff.

## Primary questions

Phase 017 must answer:

- What high-level implementation phases are required from the current reference framework through
  an initial v0.x package MVP?
- Which phase boundaries minimize cross-slice interference while preserving end-to-end value?
- What must remain public to implementation agents as normative correctness criteria?
- What should remain holdout/independent evaluation material to reduce metric gaming?
- How should Cursor and Codex divide implementation, review, challenge, and verification roles?
- How should implementation packages map to branches, PRs, evidence, and phase gates?
- What constitutes a package MVP independently of public-release or provider-support claims?
- What testing methodology is strong enough to declare the MVP complete?
- Which v1 themes should be named now without prematurely fixing detailed subphases?

## Expected durable outputs

By exit Phase 017 must establish:

1. a reusable implementation-phase lifecycle contract;
2. a bounded autonomous-coding operating model for Cursor/Codex;
3. a split-visibility success/evaluation model;
4. the v0.x MVP scope and release/non-release boundary;
5. high-level Phase 018+ definitions through MVP qualification;
6. a dependency/order map and version-milestone policy;
7. an independent MVP completion-testing and qualification methodology;
8. a deliberately coarse v1 program definition;
9. entry prerequisites for the first executable implementation phase.

## Explicit exclusions

Phase 017 does **not** authorize:

- product/source implementation beyond planning-supporting repository changes;
- creation of an active implementation package for a delivery slice;
- provider/runtime integration;
- release or deployment;
- public API commitment;
- license selection;
- scale/provider-support claims;
- automatic execution of Phase 018 or later.

## Entry criteria

Phase 017 may begin because:

- Phase 016 is complete at 100/100 repository implementation-program readiness;
- C0-C9 and agentic conformance are passing on main;
- no conceptual blocker or upstream reopen is active;
- the user explicitly requested design of the implementation program and autonomous coding approach.

Repository-admin cleanup is not required to perform planning, but branch cleanup and main protection
are mandatory prerequisites before the first sustained executable implementation phase.

## Exit criteria

Phase 017 may exit only when:

- the v0.x implementation sequence is dependency-safe and bounded;
- each v0.x phase has a clear role, entry/exit intent, and non-goals;
- Cursor/Codex roles prevent unattended self-progression and same-agent self-certification;
- success criteria visibility and holdout evaluation are explicitly separated;
- MVP completion testing includes independent/adversarial/property/failure/reproducibility evidence;
- public-release/provider/scale residuals are not conflated with package-MVP completion;
- v1 is defined at theme/program level without detailed speculative decomposition;
- the first executable phase has explicit operational prerequisites, including protected main and
  cleaned merged branches;
- current documentation/status/indexes are coherent and no product implementation has begun.

## Execution state

~~~text
Phase 017 planning/design          AUTHORIZED
product implementation execution  NOT AUTHORIZED
active implementation packages    0
Phase 018+ execution               NOT AUTHORIZED
~~~
