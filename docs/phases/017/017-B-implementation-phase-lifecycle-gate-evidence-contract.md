---
type: Phase Record
title: 017-B — Implementation-Phase Lifecycle & Gate/Evidence Contract
status: complete
---

# 017-B — Implementation-Phase Lifecycle & Gate/Evidence Contract

## Purpose

Create the reusable implementation-phase control model required before SYNGAN defines the detailed
v0.x execution phases.

## Inputs reviewed

017-B reviewed:

- the completed Phase 016 readiness handoff;
- the Phase 017 definition and 017-A start gate;
- Base's phase definition / start-gate / exit-review lifecycle structure;
- current implementation governance;
- implementation-package / traceability / ADR change control;
- agent authority and no-self-progression rules;
- engineering preflight and readiness residuals;
- current C0-C9 evidence posture.

## Key decisions

### 1. Preserve the Base lifecycle shape, specialize it for implementation

Every future executable phase uses:

~~~text
phase definition
  -> start gate
  -> success/evidence contract
  -> dynamically derived subphases/packages
  -> candidate freeze
  -> independent exit review
  -> handoff / stop
~~~

The start gate decomposes work; it does not rewrite the phase purpose.

### 2. Success criteria are visible; exact challenges may be holdout

Correctness requirements, invariants, non-goals, representative scenarios, and evidence obligations
remain visible to implementers.

Evaluator-specific adversarial combinations, property/fuzz seeds, mutations, fault orderings, and
other challenge details may be freshly generated after candidate freeze.

No hidden evaluator may introduce a requirement that was absent from current authority or the public
success contract.

### 3. Evidence is multidimensional

017-B established E0-E5 evidence dimensions:

~~~text
E0  authority / traceability
E1  static / deterministic correctness
E2  behavioral / compositional correctness
E3  negative / failure / security / recovery
E4  reproducibility / history / compatibility / candidate qualification
E5  external / provider / scale / release qualification
~~~

A phase selects the smallest sufficient evidence set per obligation.

E5 is claim-driven. A package MVP can complete without provider/scale/release qualification when
those claims are explicitly excluded.

### 4. Candidate freeze precedes independent exit evaluation

Exit evaluation operates on an exact candidate commit and frozen success contract.

A product change during evaluation creates a new candidate and requires affected evaluation to be
rerun.

### 5. Agent independence is role-based

Cursor and Codex are not intrinsically implementer or evaluator.

The program should rotate roles and use fresh evaluator context. The implementing agent's own tests
are valid first-party evidence but do not constitute independent phase certification by themselves.

### 6. Completion never self-authorizes progression

A package completion does not authorize the next package. A phase PASS names the next eligible
phase but does not start it.

## Durable authority

The durable current owner is:

[Implementation Phase Lifecycle, Gate & Evidence Contract](../../implementation/implementation-phase-lifecycle-gate-evidence-contract.md)

Stable reference:

syngan://implementation/phase-lifecycle

## Active-program routing correction

017-B also corrects the program route inherited from Phase 016:

- syngan://program/phase-016 becomes retired and points to its replacement;
- syngan://program/phase-017 becomes the active active_phase reference;
- generated OKF routing follows Phase 017 rather than completed Phase 016.

This is progression/routing correction only and does not change Phase 016 historical truth.

## Scope / change class

~~~text
agent action class                 A2 bounded planning/repository change
repository impact                  process/current-routing only
product implementation             NONE
active implementation packages     0
semantic reopen                    NONE
architecture reopen                NONE
provider/runtime delivery          NONE
~~~

## Completion evidence

017-B is complete when:

- the canonical lifecycle contract exists and is indexed;
- success/evidence visibility and anti-gaming rules are explicit;
- E0-E5 evidence dimensions and claim boundaries are explicit;
- candidate-freeze and independent-exit rules are explicit;
- carry-forward/reopen/no-self-progression rules are explicit;
- current/stable/OKF routing resolves the new lifecycle owner and active Phase 017;
- repository Verify and Agentic conformance pass.

## Handoff

017-C should define the concrete Cursor/Codex autonomous-delivery operating model, including
implementer/reviewer rotation, context isolation, branch/package mechanics, tool-in-the-loop
qualification, and degraded/manual fallback.

017-C remains **NEXT ELIGIBLE / NOT AUTHORIZED** until explicitly selected.

Product implementation remains **NOT AUTHORIZED**.
