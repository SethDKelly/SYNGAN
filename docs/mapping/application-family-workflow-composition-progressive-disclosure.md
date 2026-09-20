---
type: Concept Mapping Design Authority
title: Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure
status: active
---

# Application-Family Workflow Composition, Optional-Capability Experience & Progressive Disclosure

## Purpose

Establish the Phase 010-F composition authority for how SYNGAN's already-mapped concept actions, inspections, language and physical package/host interactions compose across the valid Phase 009 application family.

010-F answers:

> **Can actors and programmatic consumers use each coherent SYNGAN capability family without being forced through concepts, controls or explanations that do not apply, while still retaining access to the exact semantic, operational, historical and Evidence detail required when those capabilities are present?**

Current answer:

```text
YES — CURRENT APPLICATION-FAMILY COMPOSITIONS ARE EXPERIENCE-COHERENT
```

This is workflow-composition design, not implementation workflow orchestration. `workflow` is explanatory shorthand for an actor/programmatic sequence of mapped concept interactions; it is not a new concept, state owner, service, engine, transaction or product shell.

---

## Current Phase 014 completion note

This document preserves its Phase 010 derivation and original subgroup handoff as historical provenance. Phase 010 F1-F5 are complete; Phase 012 confirmed mapping completion; Phase 013 preserved mapping semantics in architecture; Phase 014-D re-audits the current mapping layer. Current subgroup sequencing is governed by [Phase 014](../phases/014/index.md).

## Governing authority

010-F consumes:

- [Phase 009 Dependence, Application Family & Composition Consolidation](../authority/phase-009-dependence-composition-consolidation.md);
- [Application Family, Valid Concept Subsets & Minimal Coherent Variants](../dependence/application-family-valid-subsets.md);
- [010-B Action Mapping](concept-action-actor-intent-interaction-mapping.md);
- [010-C Inspection Mapping](concept-state-query-history-explanation-inspection-mapping.md);
- [010-D Linguistic Mapping](linguistic-mapping-vocabulary-typed-status-disclosure-semantics.md);
- [010-E Package / Notebook / Automation / Host Interaction Mapping](package-notebook-automation-host-platform-interaction-mapping.md);
- [Problem & Purpose](../problem/problem-purpose.md).

Phase 009 application-family validity remains upstream truth. 010-F may expose a misfit but may not redefine a valid subset merely for interface convenience.

---

## Composition principles

### C1 — capability-driven composition, not full-suite choreography

The eleven accepted concepts do not form one mandatory end-to-end wizard.

Interaction is composed from the capabilities actually present in the valid family member and the actions actually being performed.

```text
concept absent
  -> no required empty step
  -> no fabricated failed/missing state
  -> no mandatory placeholder object
```

If explaining an omitted capability is useful, a surface may say `not applicable` or identify the capability as not present. Omission is not failure.

### C2 — concept inclusion does not imply repeated invocation

A family may include a concept because its authority/result is meaningful even when the current invocation does not perform that concept's state-changing action.

Important example:

```text
learned-state-assisted Generation family
  includes Learning + Learned State

current Generation invocation
  may bind an already-established Learned State
  without performing new Learning
```

The experience must not force a `Learning` step merely because Learning belongs to the family closure.

The same rule applies to reusable Data Meaning, Strategy, Constraint and Criterion authority: actors may select an existing exact revision rather than author a new one.

### C3 — semantic barrier order is preserved without becoming a universal pipeline

Where relevant, actor experience follows the recurring explanatory barriers:

```text
prepare / select / assess
        ↓
semantic commitment
        ↓
operational realization (only when present/material)
        ↓
semantic result / finding / completion
```

These barriers are interaction/comprehension structure, not one global Workflow concept or fixed runtime DAG.

### C4 — package-first interaction remains primary

Primary composition must be expressible through:

```text
P1  Python package / SDK contract
P2  notebook / interactive package use
P3  embedded job / pipeline / automation
```

CLI, report, graphical and host-native representations may improve the experience but cannot be prerequisites for semantic completeness.

### C5 — optional operational detail is orthogonal

Execution-bearing variants add operational realization and Attempt/retry/recovery/cancellation inspection.

They do not replace or own the parent Learning, Generation or Evaluation lifecycle.

A non-Execution family does not show an empty `Execution` stage.

### C6 — Evidence is not approval

Evaluation/Evidence may inform Generation completion when an explicit evidence-gating capability exists, or may simply evaluate an existing subject.

Evidence review never becomes a generic release, privacy or organizational approval step.

### C7 — Provenance is inspectable context, not a workflow gate

Provenance-bearing variants may expose exact relationships and historical explanation throughout interaction. Provenance is not normally a mandatory sequential step the actor must “complete.”

### C8 — progressive disclosure is semantic prioritization

Progressive disclosure determines which already-authoritative facts are foregrounded versus available on demand. It does not change canonical state, disclosure authorization or historical truth.

---

## Progressive-disclosure model

010-F establishes five conceptual disclosure depths. These are mapping levels, not UI screens or API tiers.

### D0 — task intent and immediate next semantic action

Show enough to understand:

- what capability is being used;
- which semantic owner is acting;
- whether the requested action can currently proceed;
- the concise result or reason it cannot proceed.

Examples include selecting a reusable authority revision, assessing Generation readiness, committing Evaluation, or inspecting completed output.

### D1 — material semantic basis

Expose the exact material basis needed for an informed semantic decision:

- bound Data Meaning / Strategy revisions;
- relevant Learned State when used;
- applicable Constraint handling;
- Evaluation Criterion and method basis;
- candidate versus completed Generation state;
- owner-qualified limitations and indeterminacy.

D1 is especially important before commitment.

### D2 — optional capability detail

Reveal capability-specific detail only when present or requested:

- Execution / Attempt summary and actionability;
- Constraint detail;
- Evidence findings / claim strength;
- Provenance relationship summary;
- dependency/runtime capability limitations.

Optional capabilities do not reserve empty space in the baseline interaction.

### D3 — historical and explanatory depth

Provide exact historical bindings, revision differences, reconstructed/partial history quality, Evidence applicability over time, Provenance traversal and explanation of why a current assessment differs from historical fact.

D3 remains bounded/reference-first.

### D4 — distributed / host operational drill-down

Detailed runtime diagnostics, platform logs/metrics/traces, large Evidence support material, distributed data previews or other potentially high-volume information are reached only through explicit bounded drill-down or host-native facilities.

D4 never becomes necessary merely to determine ordinary semantic state.

---

# Application-family workflow replay

## AF-AUTH — authority-only use

Canonical examples:

```text
{ Data Meaning }
{ Synthesis Strategy }
{ Constraint }
{ Evaluation Criterion }
```

### Experience composition

```text
inspect existing revisions
  OR
propose / define / revise authority
  ↓
validate owner-local invariants where applicable
  ↓
establish effective/current-use revision according to owning concept
  ↓
inspect history / current-use status
```

No Learning, Generation, Evaluation, Execution or Provenance activity is implied.

An authority-only package/notebook workflow must not show “next: Generate” merely because generation is a common downstream use.

### Progressive disclosure

D0/D1 foreground the authority itself. Historical revision detail is D3. Consumer-specific compatibility is shown only from the consuming context rather than stored as global authority state.

**Replay result: PASS.**

---

## AF-L — L-KERNEL

```text
{ Data Meaning, Synthesis Strategy, Learning, Learned State }
```

### New Learning sequence

```text
select / establish Data Meaning
select Strategy
  ↓
propose Learning specification
  ↓
contextual readiness / compatibility assessment
  ↓
commit Learning
  ↓
realize work directly or through optional Execution
  ↓
Learning semantic completion
  ↓
establish exact Learned State result
```

Learned State is the durable result authority; Execution success is not sufficient to establish it.

### Reuse/inspection sequence

Actors may inspect or select an existing Learned State without replaying Learning. Historical production Learning remains inspectable when retained/authorized.

### Omitted capabilities

Generation is not shown as a required next step. Evaluation/Evidence, Constraint, Execution and Provenance appear only if the family actually includes those capabilities.

**Replay result: PASS.**

---

## AF-GD — direct G-KERNEL

```text
{ Data Meaning, Synthesis Strategy, Generation }
```

### Experience composition

```text
select / establish Data Meaning
select direct-capable Strategy
  ↓
propose Generation request / Conditions
  ↓
assess readiness / compatibility / limitations
  ↓
commit Generation
  ↓
realize production directly or through optional Execution
  ↓
inspect candidate/non-final material where material
  ↓
Generation establishes completed output when its own completion basis is satisfied
```

### Critical optionality rule

No Learning or Learned State step, placeholder, missing-model warning or empty history lane appears merely because other Strategies can learn.

Direct Generation is a first-class normal composition, not a degraded learned workflow.

**Replay result: PASS.**

---

## AF-GL — learned-state-assisted Generation

Minimum composition:

```text
L-KERNEL + Generation
```

Two legitimate actor workflows exist.

### GL-1 — derive then generate

```text
perform Learning
  ↓
establish Learned State
  ↓
propose Generation
  ↓
assess exact Learned State reuse compatibility
  ↓
commit Generation with exact Learned State basis
  ↓
realize / complete Generation
```

### GL-2 — reuse already-established Learned State

```text
select existing Learned State
  ↓
inspect producing basis/current-use status as needed
  ↓
assess compatibility for this Generation
  ↓
commit Generation with exact Learned State basis
  ↓
realize / complete Generation
```

GL-2 must not force new Learning merely because the family contains Learning.

Later Learned State retirement/supersession does not rewrite the exact historical basis of an already committed Generation.

**Replay result: PASS.**

---

## AF-E — E-KERNEL / evaluation-focused use

```text
{ Evaluation Criterion, Evaluation, Evidence }
```

The evaluated subject may be external or may refer to another included concept in a larger family.

### Experience composition

```text
select / establish Criterion
identify stable evaluation subject/reference
select compatible Evaluation method/scope
  ↓
assess readiness / limitations
  ↓
commit Evaluation
  ↓
realize examination directly or through optional Execution
  ↓
Evaluation completes when interpretable Evidence can be validly established
  ↓
inspect Evidence finding + strength + uncertainty + limitations
```

Generation is not required. `Evaluation completed` is not rendered as `passed` unless an explicit Criterion defines such semantics.

**Replay result: PASS.**

---

## AF-GE — evaluation-gated Generation

Minimum composition:

```text
G-KERNEL + E-KERNEL
```

### Experience composition

```text
Generation committed
  ↓
Generation produces stable candidate identity/material
  ↓
Evaluation examines that candidate under bound Criterion/method
  ↓
Evidence is established
  ↓
Generation consumes the required Evidence as part of its completion basis
  ↓
Generation completes, remains pending/limited, or fails according to its own contract
```

This staged feedback must remain visible enough to avoid the false cycle `Generation must complete before Evaluation can begin`.

Evidence owns the finding. Generation owns its completion decision. A favorable platform job result cannot bypass required Evidence.

### Progressive disclosure

Ordinary Generation interaction may summarize the gate at D0/D1, for example that required Evidence is pending or available. Criterion/method/finding detail is available at D2/D3 without forcing every actor to traverse an Evidence report before seeing Generation state.

**Replay result: PASS.**

---

## AF-C — Constraint-aware variants

Constraint may augment Learning/Generation/Evaluation-related compositions only where reusable prescriptive-rule capability is actually present.

### Experience composition

At the consuming activity, actors can inspect:

```text
bound Constraint revision
applicability
handling = enforced / validated later / unsupported / not applicable
```

If later validation is required, the relevant Evaluation/Evidence or Generation-local completion semantics remain explicit.

Constraint presence must not create one global `constraints passed` stage.

A family without Constraint shows no required Constraint setup panel/step.

**Replay result: PASS.**

---

## AF-X — Execution-bearing versus Execution-light variants

Execution may accompany Learning, Generation and/or Evaluation when durable operational lifecycle capability is claimed.

### Execution-light composition

Without Execution, the semantic activity remains usable through the package contract according to its supported realization. The experience does not fabricate Execution history or show an error that operational tracking is “missing.”

### Execution-bearing composition

```text
parent semantic activity committed
  ↓
Execution prepared / initiated
  ↓
Attempt(s), retry/recovery/cancellation as needed
  ↓
Execution terminal operational state
  ↓
parent concept independently establishes semantic outcome
```

At D0/D1 the package/notebook experience should primarily foreground the parent semantic state plus a compact operational summary when material. Attempt details, platform correlations and diagnostics belong at D2/D4.

Execution completion may coexist with parent semantic pending/failure. Parent semantic completion may not be inferred solely from host job success.

**Replay result: PASS.**

---

## AF-P — Provenance-bearing versus Provenance-light variants

Without Provenance, ordinary concept history and exact bindings remain governed by their owners; no fake `provenance unavailable` failure is required merely because the capability is absent.

With Provenance, typed relationships may be surfaced contextually:

```text
activity bound to authority revision
Learning produced Learned State
Generation used Learned State
Evaluation examined Generation candidate
Evaluation produced Evidence
Execution realized activity
material dependency relationship
```

The normal experience may show a concise trace/relationship summary at D2 and deeper traversal at D3.

Provenance does not become a mandatory final workflow step, a source-fact owner, or a generic lineage graph that every actor must inspect.

**Replay result: PASS.**

---

## AF-FULL — full eleven-concept family member

The full current concept set is coherent, but the experience must **not** render eleven concepts as eleven required sequential stages.

A typical capability-rich composition is instead task-centered:

```text
prepare/select reusable authority as needed
  ↓
perform or reuse Learning only if the Strategy requires Learned State
  ↓
configure/commit Generation
  + bind Constraint only when applicable
  + attach Execution only when durable operational lifecycle is used
  ↓
produce candidate/output
  + perform Evaluation only when requested/required
  + consume Evidence only when relevant to the current decision
  ↓
inspect Provenance/history where useful
```

Existing reusable authority/results are selected rather than recreated. Optional capabilities are attached to the task that needs them rather than occupying permanent empty stages.

**Replay result: PASS.**

---

# Cross-family experience rules

## Existing-resource first

Package/notebook interaction should permit selection of existing valid revisions/results before offering creation of replacements.

This applies to Data Meaning, Strategy, Constraint, Criterion and Learned State.

The design must not imply `create new` merely because an authoring action exists.

## Commitment review

Before committing Learning, Generation or Evaluation, the actor/programmatic consumer must be able to recover the material semantic basis and material limitations relevant to that commitment.

The review may be concise and structured. It does not require a graphical confirmation screen.

Automation may commit using the same semantic basis without simulating human confirmation gestures.

## Optional-capability absence

When a capability is absent from the family:

```text
absent capability != failed capability
absent capability != unknown capability
absent capability != unavailable capability
```

Use `not applicable` only when an explanation is useful; otherwise omit it from the ordinary task surface.

## Current versus historical truth

Current-use warnings may be foregrounded when selecting reusable authority/results. Historical views retain the exact status/bindings relevant at the time of the committed occurrence and may also show current status separately.

## Human versus automation composition

Notebook interaction may provide explanation and rich inspection around the same conceptual actions that automation invokes programmatically.

Human convenience steps such as previews, rich tables or confirmation prompts are never semantic prerequisites unless the upstream concept actually requires the underlying decision/commitment.

## Host integration

Host-native operational UI appears only for host-owned realization facts. SYNGAN may provide correlation/linkage from Execution/Attempt state.

An actor is not required to leave the package/notebook environment for ordinary semantic inspection.

---

# Composition coverage

010-F replays the required Phase 010 family scenarios:

| Family / capability | Result |
|---|---|
| authority-only use | PASS |
| L-KERNEL | PASS |
| direct G-KERNEL | PASS |
| learned-state-assisted Generation | PASS |
| E-KERNEL / evaluation-focused use | PASS |
| evaluation-gated Generation | PASS |
| Constraint-aware variants | PASS |
| Execution-bearing vs Execution-light variants | PASS |
| Provenance-bearing vs Provenance-light variants | PASS |
| full eleven-concept composition | PASS |

Cross-cutting checks:

```text
optional concept rendered as mandatory empty step          NONE FOUND
family membership confused with invocation sequence        NONE FOUND after 010-F rule
forced new Learning for reusable Learned State             REJECTED
forced Evaluation for ordinary Generation                  REJECTED
forced Execution for domain activity                       REJECTED
forced Provenance inspection                               REJECTED
standalone UI/service dependency                           NONE
full-suite wizard requirement                              REJECTED
semantic/operational completion collapse                   NONE FOUND
Evidence/approval collapse                                 NONE FOUND
enterprise-scale local-materialization requirement         NONE FOUND
```

---

# F4 result

010-E completed individual physical interaction responsibility. 010-F now proves that those responsibilities compose coherently across the current application family.

```text
F4  CURRENTLY CLOSED
    package-first physical responsibility mapped
    valid family variants replayed
    optional capabilities remain optional in interaction
    existing-resource reuse does not force authoring/activity replay
    progressive-disclosure model established
    full-suite wizard/application-shell assumption rejected
```

F4 remains subject to 010-G difficult-condition parity/misfit testing and 010-H final Phase 010 revalidation.

---

# Stop / reopen audit

```text
J1 local concept defect                    NONE FOUND
J2 product/purpose/catalog defect           NONE FOUND
J3 dependence/application-family defect     NONE FOUND
new concept                                NO
new synchronization                        NO
new mandatory application-family edge       NO
Workflow concept                            REJECTED
full-suite mandatory workflow               REJECTED
010-F local mapping blocker                 NONE FOUND
```

No current family composition requires reopening Phase 009.

---

# Representation boundary

010-F does not choose:

- Python method/class names;
- builders/fluent APIs;
- notebook widget/rendering technology;
- CLI commands;
- endpoint/service contracts;
- UI pages, wizards or navigation;
- persisted workflow definitions;
- DAG/orchestration engines;
- event/message choreography;
- storage schemas;
- host-specific job integration;
- concrete confirmation/approval mechanisms.

Progressive-disclosure levels are semantic presentation obligations, not UI architecture.

---

# Current next boundary

**010-G — Human/Programmatic Semantic Parity, Degraded/Recovery/Scale & Mapping-Misfit Audit** is next eligible.

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
