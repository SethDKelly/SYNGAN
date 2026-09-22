---
type: Phase Start Gate
title: 017-A — Implementation Program Intent, Autonomous Delivery Boundaries & Subphase Planning
status: complete
---

# 017-A — Implementation Program Intent, Autonomous Delivery Boundaries & Subphase Planning

## Purpose

Validate the Phase 017 planning mandate, reconcile the Phase 016 handoff, establish the planning
coverage needed for a robust implementation program, and derive dependency-safe Phase 017
subphases.

## 1. Handoff/readiness assessment

~~~text
Phase 016                           COMPLETE
repository implementation readiness 100 / 100
C0-C9                               ACTIVE / PASS
current conceptual blockers         0
current upstream reopens            0
active implementation packages      0
product implementation execution    NOT AUTHORIZED
~~~

The current codebase is not an empty scaffold: it already contains verified domain/application
foundations, reference persistence/recovery/platform adapters, security and evidence/history
machinery, and C0-C9 cross-slice evidence. The public package/API and composition surfaces remain
intentionally sparse.

Therefore the next program should **productize and complete vertical capability**, not rebuild
already verified foundations.

## 2. Administrative prerequisite finding

The GitHub connector available to this planning run can verify but cannot mutate branch protection
or delete refs.

The ten non-main branches are verified as unchanged heads of merged PRs and are safe cleanup
candidates. Main remains unprotected.

These are not blockers to Phase 017 planning, but they are **hard entry prerequisites for the first
executable implementation phase**:

- delete the ten merged branches;
- protect `main`;
- require the repository Verify and Agentic conformance checks for merge;
- prefer the documented short-lived branch + squash-merge workflow;
- enable automatic deletion of merged head branches when practical.

No implementation execution start gate may pass while these prerequisites remain unconfirmed.

## 3. Autonomous coding operating principle

Cursor and Codex are interchangeable tool providers below repository authority. Neither receives
semantic privilege.

The implementation program will use **role-separated bounded autonomy**:

~~~text
human/start gate
  -> selects phase and bounded package
  -> implementation agent executes one authorized package
  -> independent review agent reviews authority/diff/evidence
  -> independent exit evaluator challenges frozen candidate
  -> repository CI proves deterministic gates
  -> human/program authority selects next work
~~~

Rules:

- one implementation package / bounded slice per working branch by default;
- no agent selects the next package merely because the current one passes;
- the implementing agent must not be the sole completion evaluator;
- Cursor and Codex should rotate implementer/reviewer roles across packages to reduce correlated
  blind spots;
- review agents should receive a fresh bounded context centered on authority + package + diff rather
  than the implementer's conversational history;
- generated tests from the implementing agent are evidence, not independent acceptance;
- branch/PR/CI state remains repository-owned and tool-neutral.

## 4. Success-metric visibility decision

**Do not blind normative success criteria.**

Implementation agents must see:

- required semantics/invariants;
- explicit scope and exclusions;
- public compatibility/security/recovery obligations;
- minimum acceptance scenarios;
- required deterministic/fitness/integration gates;
- evidence needed to claim a package obligation verified.

Hiding these would turn implementation into guesswork and increase accidental contract violations.

**Blind or independently generate challenge details.**

The exit process should withhold from the implementer, or generate after candidate freeze:

- exact adversarial scenario combinations;
- mutation operators;
- fuzz/property seeds and boundary-value selections;
- holdout fixtures;
- failure-order/interleaving cases;
- evaluator-specific review prompts;
- selected metamorphic and differential probes.

This is **split visibility**, not secret requirements.

The public contract says *what correctness means*. The holdout layer varies *how correctness is
challenged*.

Because the repository is public, durable hidden tests should not be stored as pretend-secret files.
Use fresh evaluator generation from canonical authority, runtime-randomized seeds with recorded
replay artifacts, or genuinely private CI only when an external system explicitly provides it.
After an evaluation cycle, challenge evidence may be disclosed while the next cycle rotates the
holdout set.

## 5. High-level implementation roadmap candidate

The Phase 017 work will refine, not blindly freeze, this sequence:

### Phase 018 — Implementation Execution Start Gate & Autonomous Delivery Qualification

Purpose: authorize sustained coding only after repository-admin prerequisites, tool-in-the-loop
Cursor/Codex qualification, package/branch/CI operating rules, and the first bounded implementation
packages are ready.

No product implementation begins before the Phase 018 start gate passes.

### Phase 019 — Public Python Package Surface, Composition & Installable Foundation

Purpose: turn the verified internal/reference framework into a coherent installable Python package
with intentional public representation/composition boundaries, without overcommitting provider or
v1 compatibility.

### Phase 020 — Complete Minimal End-to-End Vertical Workflow

Purpose: deliver one fully composed, useful v0.x workflow through preparation/commit, execution,
generation, evaluation/evidence, provenance/history, recovery, and result access using the smallest
self-contained supported path.

### Phase 021 — Baseline Structured-Data & Strategy Coverage

Purpose: complete the minimum baseline topology/strategy set required by current design, including
single-table, time-series, and multi-table shared-key paths, while preserving direct/reuse and
Learning/Learned-State distinctions.

### Phase 022 — Spark-Capable Distributed Realization

Purpose: add provider-neutral Spark-capable source/output/runtime realization with distributed
identity, fencing, promotion, no-hidden-collect, failure/recovery, and portability evidence.

This phase does not by itself claim production Databricks/provider qualification or enterprise-scale
support.

### Phase 023 — Security, Recovery, Reproducibility & Failure-Mode Hardening

Purpose: deliberately challenge the integrated v0.x system under authorization/disclosure,
no-egress, dependency failure, restart/recovery, stale writers, partial execution, reproducibility,
historical reads, and cross-slice fault interactions.

### Phase 024 — v0.x Package Productization, Compatibility & Candidate Freeze

Purpose: complete packaging/version semantics, developer-facing API/error/result ergonomics,
documentation/examples, migration/compatibility policy, build/install evidence, support non-claims,
and freeze an MVP candidate.

Public distribution remains separately gated by license/vulnerability/release residuals.

### Phase 025 — v0.x MVP Independent Qualification & Completion Decision

Purpose: run the independent MVP completion methodology against the frozen candidate, including
holdout/adversarial/property/mutation/failure/reproducibility checks and requirement traceability.

Outcome: PASS, PASS WITH CARRY-FORWARD, or NOT READY TO EXIT.

### Phase 026 — v1 High-Level Program Design

Purpose: define v1 themes, sequencing constraints, qualification targets, and rediscovery/reopen
triggers at intentionally lower granularity.

Likely v1 themes may include production provider qualification, enterprise-scale evidence, broader
Strategy/Evaluation catalogs, operationalization/SLOs, stronger compatibility guarantees, and
public-release hardening, but Phase 026 must not prematurely decompose these into detailed packages
before v0.x evidence exists.

## 6. Version-milestone principle

Do not bind every implementation phase to an exact semantic package version yet.

Phase 017 will define a version-milestone policy in which intermediate v0.x versions may identify
coherent capability checkpoints, while the exact `0.N.0` mapping is selected only after the
package/API boundary and dependency order are validated.

The current `0.0.0` metadata remains appropriate during Phase 017 planning.

## 7. Phase 017 subphase plan

~~~text
017-A  program intent / handoff / autonomy boundaries / decomposition       COMPLETE
017-B  implementation-phase lifecycle & gate/evidence contract              NEXT ELIGIBLE
017-C  Cursor/Codex autonomous delivery operating model & runtime proof      PLANNED
017-D  success visibility, holdout evaluation & anti-gaming methodology     PLANNED
017-E  v0.x MVP scope, capability/version milestones & release boundaries   PLANNED
017-F  Phase 018-025 definitions, dependency graph & package strategy       PLANNED
017-G  MVP completion testing, qualification & independent exit method      PLANNED
017-H  v1 coarse program design, deferrals & rediscovery triggers           PLANNED
017-I  consolidation, documentation audit, exit decision & Phase 018 handoff PLANNED
~~~

## 8. Completion evidence by subphase

- **017-B:** reusable phase lifecycle contract with start gate, success/evidence contract, exit
  review, carry-forward, reopen, and canonical-promotion rules.
- **017-C:** concrete Cursor/Codex role model, branch/package workflow, context boundaries, reviewer
  independence, runtime qualification requirements, and no-self-progression controls.
- **017-D:** public vs holdout criteria matrix, challenge-generation method, anti-gaming controls,
  evaluator independence, replay/evidence rules.
- **017-E:** explicit v0.x MVP included/excluded capability surface, version milestone policy,
  release-vs-package distinction, residual-risk mapping.
- **017-F:** durable high-level definitions for Phases 018-025 with dependency/order and package
  decomposition guidance.
- **017-G:** MVP qualification protocol with test layers, scenario families, mutation/property/fuzz
  disciplines, acceptance evidence, and decision outcomes.
- **017-H:** v1 themes and boundaries without detailed speculative subphases.
- **017-I:** current-knowledge reconciliation, duplication/staleness audit, unresolved-item register,
  exit decision, and explicit Phase 018 authorization boundary.

## 9. Gate outcome

**READY TO BEGIN PHASE 017 SUBPHASES.**

Only 017-A is complete. 017-B is **NEXT ELIGIBLE / NOT AUTHORIZED** until explicitly selected.

Product implementation execution remains **NOT AUTHORIZED**.
