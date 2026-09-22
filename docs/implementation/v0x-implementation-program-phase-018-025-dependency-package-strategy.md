---
type: Implementation Program Authority
title: v0.x Implementation Program — Phase 018-025 Dependency & Package Strategy
status: active
---

# v0.x Implementation Program — Phase 018-025 Dependency & Package Strategy

## Purpose

Define the durable high-level execution sequence from implementation entry through qualified v0.x
package-MVP completion, including phase dependencies, phase roles, package-decomposition rules,
candidate-freeze behavior, repair routing, and no-self-progression boundaries.

This authority is downstream of the implementation phase lifecycle, autonomous delivery model,
evaluation method, v0.x MVP boundary, implementation-package contract, engineering preflight, and
current design/architecture authorities.

It is a program plan. It does not authorize Phase 018 or any product implementation.

## Program invariant

The v0.x implementation program is phase-sequential and package-bounded:

~~~text
Phase 017 planning complete
  -> explicit human selection
  -> Phase 018 execution start gate / operational qualification
  -> explicit human selection
  -> Phase 019 / MVP-M1
  -> Phase 020 / MVP-M2
  -> Phase 021 / MVP-M3
  -> Phase 022 / MVP-M4
  -> Phase 023 / MVP-M5
  -> Phase 024 / MVP-M6 candidate freeze
  -> Phase 025 / MVP-M7 independent qualification
~~~

A passed phase makes its successor eligible. It never authorizes the successor.

Phase-level ordering is strict for the initial v0.x program because each later phase evaluates or
extends an integrated capability produced by its predecessor.

Within one authorized phase, bounded implementation packages may form a dependency DAG when the
start gate proves that package scopes are genuinely independent.

Cross-phase implementation concurrency is not part of the v0.x program.

## Phase 018 — Implementation Execution Start Gate & Autonomous Delivery Qualification

### Role

Convert Phase 017 planning into an executable-program entry decision without implementing product
capability.

### Required entry conditions

Phase 018 cannot pass its start gate until:

- Phase 017 is complete;
- Phase 018 is explicitly selected by a human;
- leftover planning branches are reconciled against current main and obsolete branches are safely removed;
- main branch protection is confirmed;
- required Verify and Agentic conformance checks are enforced for merge;
- the selected branch/PR workflow is operational;
- Cursor and Codex tool-in-loop runtime qualification satisfies the autonomous-delivery profile;
- current repository verification is passing;
- no Class 3/4 conflict or upstream reopen is active.

### Outputs

Phase 018 establishes:

- executable-program authority boundaries;
- verified repository-admin controls;
- actual runtime qualification evidence for the selected agent tools;
- the Phase 019 start-gate inputs;
- the first prospective package-family decomposition for Phase 019;
- confirmation that no implementation package self-authorizes execution.

### Non-goals

Phase 018 does not implement MVP-C01..MVP-C08, create provider/runtime capability, bump the package
version, or automatically start Phase 019.

MVP milestone remains MVP-M0.

## Phase 019 — Public Python Package Surface, Composition & Installable Foundation

### Role

Productize the verified framework into an intentional installable Python package surface without
exporting internal implementation structure as accidental public API.

### Required outcome

Phase 019 reaches MVP-M1 only when the package has an intentional Python-facing composition entry,
coherent build/install behavior, bounded public representations, and package-level errors/results
sufficient for the next vertical workflow phase.

### Prospective package families

The start gate should derive actual packages from the then-current repository, using these planning
families as a guide:

- public contract and representation boundary;
- composition/bootstrap entry;
- package build/install and import surface;
- public error/result ergonomics and focused compatibility assessment.

These are not package IDs and are not pre-authorized work.

### Non-goals

No complete end-to-end workflow claim, Spark capability, production provider claim, broad strategy
catalog, public release, or 1.0 stability promise.

## Phase 020 — Complete Minimal End-to-End Vertical Workflow

### Role

Produce one useful, fully composed package workflow through the smallest supported reference path.

### Required outcome

Phase 020 reaches MVP-M2 only when one package-level flow composes preparation/control, execution,
generation, evaluation/evidence, provenance/history, result access, and bounded reconstruction or
recovery where applicable.

### Prospective package families

Prefer vertical increments rather than disconnected horizontal subsystems:

- minimal successful reference workflow;
- durable result/evidence/history reconstruction;
- explicit failure/retry/recovery path;
- public workflow integration evidence.

### Non-goals

No topology catalog completion, distributed Spark realization, or public-release claim.

## Phase 021 — Baseline Structured-Data & Strategy Coverage

### Role

Extend the vertical workflow to the minimum structured-data topology and strategy distinctions
required by the v0.x MVP.

### Required outcome

Phase 021 reaches MVP-M3 only when the supported package path covers:

- single-table structured data;
- time-series structured data;
- multi-table shared-key structured data;
- direct/reuse behavior;
- Learning/Learned-State-assisted behavior.

The minimum useful strategy realizations are sufficient. Catalog breadth is not the target.

### Prospective package families

The start gate should prefer topology-bounded packages and shared strategy contracts over one
cross-cutting mega-package:

- shared topology/strategy integration contract;
- single-table capability increment where still needed;
- time-series capability increment;
- multi-table shared-key capability increment;
- cross-topology direct/reuse and Learned-State evidence.

### Non-goals

No complete algorithm catalog, production provider support, or scale qualification.

## Phase 022 — Spark-Capable Distributed Realization

### Role

Add the bounded provider-neutral Spark-capable realization required by MVP-C04 while preserving the
portable core and explicit support non-claims.

### Required outcome

Phase 022 reaches MVP-M4 only when executed evidence demonstrates the selected Spark-capable path
for source/output/runtime interaction, distributed identity, materialization/promotion, fencing,
no-hidden-collect, failure/recovery, and portability behavior.

### Prospective package families

- Spark runtime/source/output boundary;
- distributed identity and materialization;
- fencing/promotion/recovery behavior;
- no-hidden-collect and portability integration;
- bounded Spark-capability evidence.

### Non-goals

Phase 022 does not establish production Databricks support, general production Spark certification,
provider-specific HA/DR certification, or enterprise-scale qualification.

## Phase 023 — Security, Recovery, Reproducibility & Failure-Mode Hardening

### Role

Challenge the integrated MVP path after distributed capability exists and close implementation
defects that prevent trustworthy package-MVP qualification.

### Required outcome

Phase 023 reaches MVP-M5 only when the integrated path withstands the applicable authorization,
disclosure, no-egress, dependency-failure, stale-writer, retry/cancellation, partial-completion,
restart/recovery, reproducibility, historical-read, and cross-slice fault obligations.

### Prospective package families

- authorization/disclosure/no-egress hardening;
- failure/retry/recovery/stale-writer hardening;
- reproducibility/history reconstruction hardening;
- integrated cross-slice adversarial repairs.

Hardening packages must trace to existing visible obligations. This phase cannot invent hidden
requirements.

### Non-goals

No public release, provider support, enterprise-scale claim, or candidate freeze until all blocking
hardening obligations close.

## Phase 024 — v0.x Package Productization, Compatibility & Candidate Freeze

### Role

Turn the completed capability into an exact, reviewable package-MVP candidate for independent
qualification.

### Required outcome

Phase 024 reaches MVP-M6 only when:

- package/API/error/result ergonomics are coherent for the selected v0.x surface;
- build/install evidence is complete;
- examples and developer documentation cover the supported boundary;
- compatibility/migration posture and support non-claims are explicit;
- the exact non-placeholder v0.x candidate version is selected;
- the exact candidate commit/build identity is frozen;
- applicable public success obligations are frozen for Phase 025;
- no blocking Class 3/4 conflict remains.

### Prospective package families

- API/error/result productization;
- examples and developer documentation;
- compatibility/migration and version selection;
- build/install/candidate evidence consolidation;
- final candidate-freeze reconciliation.

### Non-goals

A Phase 024 package-MVP candidate is not automatically a public release candidate. Distribution,
license selection, release vulnerability clearance, provider support, and scale qualification
remain separately gated.

## Phase 025 — v0.x MVP Independent Qualification & Completion Decision

### Role

Independently evaluate the exact frozen Phase 024 candidate against the v0.x MVP contract.

### Evaluation-only rule

Phase 025 does not contain product implementation packages.

The evaluator must not repair the frozen candidate while certifying it.

### Required outcome

Phase 025 reaches MVP-M7 only through an allowed lifecycle exit decision based on independent
qualification evidence.

The evaluation portfolio is defined by Phase 017-G and the canonical evaluation method.

### Defect routing

When Phase 025 exposes a candidate defect:

1. record the failing challenge, visible obligation mapping, and contamination state;
2. classify the candidate as NOT READY for the affected qualification;
3. do not modify the frozen candidate in the evaluator role;
4. route repair to the smallest owning implementation phase/package under explicit human
   authorization;
5. apply Class 3/4 reopen rules when architecture or semantics are implicated;
6. create and freeze a new candidate after repair;
7. rerun affected regression evidence;
8. use fresh holdout realization for renewed independent evaluation.

A Phase 025 failure never authorizes its own repair cycle.

## Dependency graph

The initial v0.x phase graph is:

~~~text
017
 |
 v
018  start gate / execution qualification
 |
 v
019  MVP-M1 package surface
 |
 v
020  MVP-M2 minimal vertical workflow
 |
 v
021  MVP-M3 baseline topology/strategy coverage
 |
 v
022  MVP-M4 Spark-capable realization
 |
 v
023  MVP-M5 integrated hardening
 |
 v
024  MVP-M6 package-MVP candidate freeze
 |
 v
025  MVP-M7 independent qualification
~~~

No edge is an authorization edge.

A phase may be reopened when downstream evidence invalidates one of its accepted obligations. Such
re-entry is explicit and evidence-preserving rather than an informal backward edit.

## Implementation-package strategy

### Package is smaller than phase

A phase is a program boundary. An implementation package is a bounded review/evidence unit.

Do not create one package that means "implement Phase 021" or another whole phase.

A package should normally have:

- one primary capability or integration seam;
- a bounded authority set;
- one dominant Class 0-2 change classification;
- independently reviewable implementation and tests;
- explicit non-claims;
- a dependency position that can be explained without broad repository archaeology.

### Actual packages are derived at the start gate

The package families in this authority are planning guidance only.

For each selected phase, its start gate must inspect current repository state and derive the
smallest sufficient package set. Actual manifests continue to use the existing IPKG-#### contract.

Creating a manifest does not authorize work.

### Branch and PR default

The default execution unit is:

~~~text
one selected implementation package
  -> one short-lived branch
  -> one implementation agent role
  -> focused verification
  -> independent reviewer role
  -> reviewable PR
  -> required repository CI
  -> merge only after package obligations are satisfied
~~~

Exceptions require explicit justification.

### Package dependency control

Package dependencies are owned by the selected phase start-gate plan.

Do not add an ad hoc dependency field to the current IPKG schema merely for convenience. If
per-package dependency metadata later proves necessary as a durable contract, change the package
authority/schema explicitly under its normal change-control discipline.

Default package execution is serialized.

Concurrent package execution is allowed only when the start gate explicitly establishes that:

- scopes are dependency-independent;
- they do not modify the same public/persisted contract;
- they do not share an unresolved architecture decision;
- evidence from one is not a prerequisite for the other;
- merge ordering and rebase/revalidation obligations are explicit.

### No cross-phase mega-packages

An implementation package belongs to one selected phase execution context.

If a package discovers work owned by a later phase, record/defer it.

If it discovers a prerequisite owned by an earlier phase, stop and reopen/repair the smallest owner
rather than silently broadening the package.

### Package completion and phase completion are different

A package may complete while its phase remains incomplete.

A phase may exit only after:

- all blocking selected packages are complete or validly dispositioned;
- integration evidence across those packages exists;
- the phase success/evidence contract is satisfied;
- the candidate state for that phase is frozen where required;
- independent exit review reaches an allowed outcome.

Neither package nor phase completion authorizes subsequent work.

## Change and reopen discipline

Class 0-2 work may proceed inside an authorized package.

Class 3 architecture conflicts and Class 4 semantic/experience conflicts stop ordinary
implementation and reopen the smallest governing authority.

Do not widen a package to absorb a reopen merely to preserve schedule or phase numbering.

## Version interaction

MVP-M1..MVP-M7 are capability milestones, not package versions.

Phase 019 may make a non-placeholder development version possible, but version change is
evidence-driven rather than mandatory at that phase.

Phase 024 must select the exact non-placeholder candidate version before MVP-M6 freeze.

Phase 025 evaluates that exact identity and never changes it.

## Public-release boundary

Phases 018-025 target a qualified package MVP.

They do not automatically perform public distribution, production-provider qualification,
enterprise-scale qualification, deployment/IaC, or SLO/SLA work.

Those claims/actions remain governed by the v0.x MVP boundary and engineering preflight.

## Current authorization boundary

Phase 017-F establishes this roadmap only.

Phase 018 through Phase 025 remain NOT AUTHORIZED for execution. No active implementation package is
created by this roadmap. The current project version remains 0.0.0.
