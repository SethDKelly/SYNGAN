---
type: Implementation Authority
title: Implementation Phase Lifecycle, Gate & Evidence Contract
status: active
---

# Implementation Phase Lifecycle, Gate & Evidence Contract

## Purpose

Define the reusable control structure for SYNGAN implementation phases after Phase 017 planning.

This contract adapts the repository's successful design-phase lifecycle to implementation without
turning implementation phases into narrative checklists or allowing an agent to optimize narrowly
for known tests.

It owns:

- phase-definition stability;
- mandatory start-gate behavior;
- dynamic decomposition into dependency-safe subphases and implementation packages;
- visible normative success obligations;
- evidence planning and evidence-quality rules;
- candidate freeze and independent exit evaluation;
- carry-forward, stop, reopen, and handoff behavior;
- the rule that completing one phase never authorizes the next.

It does not define product semantics, architecture, implementation-package schema details,
provider qualification, release authority, or tool-specific agent behavior. Those remain with their
existing current owners.

## Core lifecycle

Every executable implementation phase follows this structure:

~~~text
human-selected phase
  -> stable phase definition
  -> mandatory start gate
  -> frozen success/evidence contract
  -> dependency-safe implementation subphases/packages
  -> candidate freeze
  -> independent exit evaluation
  -> PASS / PASS WITH CARRY-FORWARD / NOT READY
  -> explicit handoff
  -> STOP
~~~

A successful exit identifies the next eligible phase. It does not start it.

## 1. Phase definition

A high-level implementation phase must declare before execution:

- phase number and name;
- implementation purpose;
- user/system capability or repository outcome it is intended to establish;
- governing current syngan:// authorities;
- prerequisites and incoming handoff;
- explicit included scope;
- explicit exclusions and non-claims;
- dependency assumptions;
- expected durable outputs;
- success intent;
- exit intent;
- known residuals or reopen triggers;
- whether external/provider/scale/release evidence is in or out of scope.

The phase definition is an authority boundary, not an implementation plan.

The start gate may derive the detailed work needed to satisfy it. It may not silently broaden the
phase purpose or remove an obligation because implementation is difficult.

### Phase-definition amendment

After the start gate begins, a material change to phase purpose, included capability, success intent,
or exclusion boundary requires an explicit amendment decision.

If the change affects accepted architecture or product semantics, Class 3/4 and A4 reopen rules
apply. Editing the phase definition cannot launder a higher-class change into ordinary
implementation.

## 2. Mandatory start gate

The first subphase of an executable implementation phase is the start gate, conventionally NNN-A.

The start gate must occur before product implementation in that phase.

It must:

1. verify the incoming phase handoff and current main baseline;
2. verify repository-operational prerequisites such as protected main, required CI, branch hygiene,
   and any phase-specific environment prerequisites;
3. resolve the smallest current authority set using stable references;
4. identify relevant RR/backlog items without treating backlog as authority;
5. classify expected work under Class 0-4 and A1-A4;
6. identify any Class 3/4 conflict that must reopen before implementation;
7. derive dependency-safe substantive subphases;
8. derive material Class 1/2 implementation packages and their dependency order;
9. define one bounded branch/PR objective for each independently mergeable package by default;
10. define the public success/evidence contract before implementation begins;
11. define verification profiles, focused tests, integration/failure/security evidence, and any
    external evidence needed;
12. identify evaluator independence and holdout/challenge-generation requirements;
13. define documentation/traceability/current-owner updates expected from the phase;
14. identify stop conditions and carry-forward destinations;
15. confirm that completion of planned work will not self-authorize the next package or phase.

### Start-gate outcomes

Use exactly one:

- **READY TO BEGIN PHASE IMPLEMENTATION**
- **NOT READY — ENTRY OR AUTHORITY PRECONDITION MISSING**

A start gate may authorize only the bounded implementation program explicitly selected by the human
task/program authority. It cannot grant A3 permission by implication.

## 3. Dynamic subphase and package derivation

The phase definition fixes intent; the start gate derives the work structure.

Do not predeclare a fixed number of subphases for visual regularity. Split work when separation
improves:

- dependency safety;
- merge/review isolation;
- architecture-boundary clarity;
- evidence attribution;
- rollback/recovery;
- agent context size;
- ability to rotate Cursor/Codex implementation and review roles;
- ability to reject one slice without invalidating unrelated completed work.

A subphase may contain one package or a tightly coupled package group. Material Class 1/2
implementation normally receives an IPKG-#### manifest under the existing implementation-package
contract.

A package is never an authorization source. A package may be planned before selection, but it may
become in_progress only when the active phase/start-gate authority and human-selected task permit
that slice.

## 4. Success/evidence contract

Every executable implementation phase must establish a success/evidence contract before product
implementation begins.

The contract contains two layers.

### 4.1 Visible normative success obligations

Implementation agents, reviewers, and humans must be able to see:

- required semantics and invariants;
- required public/internal contract behavior;
- explicit exclusions and non-goals;
- security, authority, identity, recovery, history, and compatibility obligations relevant to the
  phase;
- minimum representative success scenarios;
- minimum failure/negative scenarios;
- required repository verification lanes;
- package traceability obligations;
- evidence required to claim an obligation verified.

These criteria are not hidden. Hiding correctness requirements would create guesswork and increase
contract drift.

### 4.2 Independent challenge layer

The exact challenge set SHOULD remain outside the implementing agent's execution context when
practical.

It may contain:

- adversarial scenario combinations;
- property/fuzz seeds;
- boundary-value selections;
- mutation operators;
- fault orderings and concurrency/interleaving cases;
- holdout fixtures;
- metamorphic probes;
- differential comparisons;
- evaluator-specific review prompts.

The challenge layer may vary how known obligations are tested. It MUST NOT invent a new semantic
requirement after implementation.

Detailed split-visibility, holdout generation, evaluator-independence, contamination, replay, and
anti-gaming mechanics are governed by `syngan://implementation/evaluation-method`.

For a public repository, "holdout" means evaluator independence or fresh generation, not pretending
a checked-in file is secret. Valid mechanisms include fresh evaluator generation from current
authority, randomized seeds captured for replay, or genuinely private CI where separately
available.

## 5. Evidence model

Success is established by a body of evidence, not by a single metric.

The start gate assigns each material obligation the smallest sufficient evidence set from these
dimensions:

### E0 — authority and traceability

Evidence that the implementation obligation is correctly bound to current authority:

- active stable reference;
- section/proposition locator where needed;
- package mapping;
- implementation path;
- verification path;
- limitation/non-claim.

E0 proves routing and accountability, not behavior.

### E1 — static and deterministic correctness

Examples:

- lint/format/type checks;
- schema validation;
- import/dependency fitness;
- deterministic unit tests;
- serialization/round-trip tests;
- generated-artifact drift checks.

### E2 — behavioral and compositional correctness

Examples:

- contract tests;
- integration tests;
- state-transition tests;
- property-based tests;
- cross-component synchronization;
- end-to-end happy-path behavior.

### E3 — negative, failure, security, and recovery correctness

Examples:

- invalid-input rejection;
- stale/fenced writer behavior;
- cancellation/retry/restart;
- authorization/disclosure denial;
- no-egress behavior;
- dependency/runtime failure;
- corruption/partial-completion recovery;
- mutation/adversarial testing.

### E4 — reproducibility, history, compatibility, and candidate qualification

Examples:

- exact historical-read reproduction;
- deterministic/replay evidence where promised;
- migration/compatibility tests;
- package build/install tests;
- clean-environment execution;
- candidate-level workflow replay.

### E5 — external/provider/scale/release qualification

Examples:

- real provider/runtime qualification;
- real enterprise-scale benchmarks;
- current vulnerability/advisory review;
- support-matrix evidence;
- deployment/SLO/SLA evidence;
- license/release/legal decisions.

E5 is required only when the phase claims the corresponding external/support/release property.
A v0.x package MVP may complete without E5 claims when its phase definition explicitly excludes
them.

### Evidence sufficiency rule

No evidence dimension substitutes automatically for another.

In particular:

~~~text
test pass                 != semantic authority
coverage percentage       != behavior completeness
type correctness          != runtime correctness
happy path                != recovery correctness
reference adapter pass    != provider qualification
synthetic benchmark       != enterprise-scale qualification
agent review              != independent verification
~~~

## 6. Success-contract immutability and anti-gaming

Once implementation begins, the success/evidence contract is frozen for ordinary execution.

A criterion may be corrected only when:

- it is internally contradictory;
- it references superseded authority;
- it is impossible for reasons unrelated to implementation quality;
- upstream authority is intentionally changed through the proper reopen path.

The correction must be reviewed as a contract change, not quietly edited in the same branch to make
a failing implementation pass.

Agents must not:

- delete or weaken a failing test merely because it blocks completion;
- rewrite the success criterion to match current code;
- replace a required evidence class with an easier one without authority;
- inspect a holdout evaluator and then tune only to that exact case while claiming independence;
- increase scope merely to accumulate more passing metrics.

## 7. Implementation execution discipline

During substantive implementation:

- work only on the explicitly selected subphase/package;
- use short-lived branches from current verified main;
- keep one bounded independently reviewable objective per branch by default;
- update package traceability from actual code/test evidence;
- keep current authority, code, tests, and documentation synchronized at the smallest owner;
- stop when an A3 action is required without explicit permission;
- stop and reopen on Class 3/4 conflict;
- report adjacent defects without automatically repairing out-of-envelope work;
- do not continue to the next package or subphase solely because current checks are green.

An implementation agent may create tests needed to implement the selected obligation. Those tests
remain first-party implementation evidence and are not, by themselves, the independent exit
evaluation.

## 8. Candidate freeze

Before the final exit evaluation, establish a candidate freeze.

Record:

- exact main/candidate commit;
- completed package IDs;
- package evidence states;
- current success/evidence contract revision;
- known limitations/carry-forwards;
- required deterministic verification results.

During independent evaluation, product changes invalidate the frozen candidate.

A defect fix creates a new candidate and the affected evaluation must be rerun. Reusing unaffected
evidence is allowed only when the evaluator can justify that the change cannot invalidate it.

## 9. Independent exit evaluation

The final phase subphase is a consolidation and exit review.

The evaluator should be independent from the implementation context to the degree practical.
For agent-assisted work, prefer:

- a different tool/model role than the primary implementer; or
- a fresh context with only current authority, success contract, candidate diff/state, and evidence;
- fresh challenge generation after candidate freeze.

Cursor and Codex are interchangeable providers. Neither is inherently the evaluator. Role
separation matters more than brand.

The exit review must examine:

- every public success obligation;
- every package disposition;
- traceability completeness;
- required E0-E5 evidence dimensions;
- independent challenge results;
- unresolved failures;
- compatibility/migration implications;
- documentation/current-owner coherence;
- explicit non-claims;
- whether any success criterion was weakened after failure;
- whether any higher-class conflict was hidden;
- whether the next phase has enough handoff context.

## 10. Exit outcomes

Use exactly one:

### PASS

All blocking success obligations are satisfied with the required evidence. The phase may close.

### PASS WITH CARRY-FORWARD

The phase fulfills its defined purpose, but explicit **non-blocking** issues remain.

Every carry-forward must identify:

- exact unresolved item;
- why it does not invalidate the phase purpose;
- destination phase/package or activation trigger;
- current owner where the unresolved truth remains visible;
- claim that remains prohibited until the item closes.

A failed required success obligation cannot be relabeled carry-forward merely to exit.

### NOT READY TO EXIT

One or more blocking obligations, evidence requirements, authority conflicts, candidate defects, or
documentation-coherence failures remain.

Define the smallest corrective work and rerun affected evaluation.

## 11. Handoff contract

A successful exit records:

- exact completed phase/candidate state;
- durable current owners changed;
- completed/superseded package IDs;
- verification/evaluation evidence;
- explicit limitations and non-claims;
- carried residuals and destinations;
- compatibility/migration state;
- activated or dormant reopen triggers;
- authoritative inputs for the next phase;
- the next **eligible** phase.

The handoff must state:

> Completion establishes eligibility, not authorization.

The next phase begins only after explicit human selection and its own start gate.

## 12. Reopen and stop discipline

Stop ordinary implementation when:

- current authority cannot be resolved;
- the selected package exceeds its authorized envelope;
- an A3 external/destructive/privilege-expanding action becomes necessary without permission;
- a Class 3 architecture conflict appears;
- a Class 4 semantic/product-scope conflict appears;
- evidence reveals the phase definition itself is invalid;
- a required residual becomes blocking for the claim being attempted.

Use the smallest governing reopen. Preserve historical evidence rather than rewriting the prior
phase as though the conflict never occurred.

## 13. Relationship to implementation packages

The phase lifecycle and implementation-package lifecycle are complementary:

~~~text
phase definition       -> purpose / capability boundary
start gate             -> decomposition / authorization plan
IPKG manifest          -> bounded realization + traceability + evidence container
success contract       -> phase-wide normative acceptance obligations
candidate freeze       -> exact evaluation subject
exit review            -> independent phase-level completion decision
~~~

A package can complete while the phase remains incomplete. Phase completion requires successful
composition of all blocking package outcomes and phase-level evidence.

## 14. Relationship to autonomous coding

This contract permits bounded autonomous execution inside an explicitly selected package.

It does not permit:

- unattended roadmap progression;
- self-selection of the next package;
- autonomous phase start;
- tool-driven scope expansion;
- same-context self-certification as the sole exit decision;
- bypass of branch protection, review, CI, A3 permission, or Class 3/4 reopen.

The detailed Cursor/Codex operating model is defined separately by Phase 017-C.

## 15. Minimum artifact set for future executable phases

Each executable phase should normally expose:

~~~text
docs/phases/NNN/
  index.md
  phase-definition.md
  NNN-A-start-gate.md
  success-evidence-contract.md
  ... dynamic substantive subphase records ...
  exit-review.md or exit-review-template.md
~~~

Material implementation packages remain under:

~~~text
docs/implementation/packages/IPKG-####.json
~~~

Phase records are progression evidence. Durable implementation rules belong in current owners under
docs/implementation/, architecture, design, or another natural canonical family.

## Current authorization boundary

This lifecycle contract is planning/process authority established by Phase 017-B.

It does not authorize product implementation, create an active implementation package, authorize
Phase 018, or weaken the post-Phase-016 release/provider/scale residuals.
