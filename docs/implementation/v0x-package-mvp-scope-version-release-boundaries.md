---
type: Implementation Authority
title: v0.x Package MVP Scope, Capability/Version Milestones & Release Boundaries
status: active
---

# v0.x Package MVP Scope, Capability/Version Milestones & Release Boundaries

## Purpose

Define the bounded capability that SYNGAN must establish before the initial v0.x package may be
called an MVP, define capability milestones without turning phase numbers into package versions,
and keep package-MVP completion separate from public release, provider support, and scale claims.

This authority is downstream of the current phase lifecycle, evaluation method, implementation
governance, package contract, engineering preflight, readiness authority, and current design and
architecture authority.

It defines a future implementation target. It does not claim that target is already implemented.

## Core definition

The initial v0.x MVP is a **qualified Python package capability**, not a public release.

A package-MVP decision answers:

> Can a Python developer use one coherent, intentionally exposed SYNGAN package surface to execute
> the bounded synthetic-data workflow promised by the current design, with required evidence,
> history, failure/recovery, security, and distributed-capability behavior demonstrated at the
> explicitly supported v0.x boundary?

It does not answer whether the package may be publicly distributed, whether a production provider
is supported, whether enterprise-scale performance is qualified, whether long-term public
compatibility is guaranteed, or whether operational SLO/SLA commitments exist.

## MVP minimization principle

v0.x should productize the smallest coherent vertical capability that exercises the accepted design.

The MVP MUST NOT become a catalog-completeness project merely because more strategies, adapters,
providers, or convenience APIs could be implemented.

Prefer:

- one intentional public composition path over exporting internal implementation surfaces;
- the minimum strategy realizations needed to exercise required behavioral distinctions;
- the minimum baseline topology set already selected by the implementation roadmap;
- bounded provider-neutral capability evidence over premature production-provider claims;
- explicit non-claims over speculative compatibility/support promises.

## Required v0.x capability surface

### MVP-C01 — installable Python package and intentional public composition surface

The package must be buildable/installable in its verified environment and expose an intentional
Python-facing entry/composition surface.

The public surface should represent current domain/experience semantics rather than mirror internal
module structure.

MVP-C01 does not freeze a 1.0 API or require every current internal contract to become public.

### MVP-C02 — complete minimal end-to-end workflow

At least one supported workflow must compose the current lifecycle through:

~~~text
input / preparation
  -> durable intent / control state
  -> execution
  -> generation
  -> evaluation / evidence
  -> provenance / history
  -> result access
  -> recovery / reconstruction when applicable
~~~

The workflow must use real package composition rather than a test-only orchestration shortcut.

### MVP-C03 — baseline structured-data and strategy coverage

The MVP must cover the baseline roadmap topology set:

- single-table structured data;
- time-series structured data;
- multi-table shared-key structured data.

It must preserve the designed distinction among direct/reuse behavior and
Learning/Learned-State-assisted behavior.

Only the smallest strategy/algorithm set needed to make those distinctions useful is required.
A complete Strategy or algorithm catalog is explicitly outside v0.x MVP scope.

### MVP-C04 — bounded Spark-capable distributed realization

The MVP must include a provider-neutral Spark-capable source/output/runtime path sufficient to
demonstrate distributed identity, materialization/promotion, fencing, no-hidden-collect,
failure/recovery, and portability obligations selected for Phase 022.

This is a **capability requirement**, not a production-support claim.

The exact Spark runtime/profile used for v0.x must be recorded with executed evidence. Passing this
capability does not establish production Databricks support, enterprise-scale qualification,
provider HA/DR certification, or a general production Spark support statement.

### MVP-C05 — integrated security, recovery, reproducibility, and failure behavior

The composed v0.x path must exercise relevant authorization/disclosure, no-egress, dependency
failure, stale-writer/fencing, retry/cancellation/restart, partial-completion recovery,
reproducibility, and historical-read obligations.

The MVP is not complete if these behaviors exist only as disconnected foundations that the public
workflow bypasses.

### MVP-C06 — evidence, provenance, history, and result access

A completed workflow must produce and expose the evidence/provenance/history needed to understand
what ran, what result was produced, how it was evaluated, and what historical state is being read.

The MVP must preserve current evidence-strength/non-claim discipline.

### MVP-C07 — candidate productization

Before candidate freeze the package must have:

- coherent build/install behavior;
- developer-facing API/error/result ergonomics appropriate to the selected v0.x surface;
- bounded examples/documentation for the supported workflow and topology set;
- explicit current compatibility/migration posture;
- explicit support/non-claim statements;
- deterministic package and repository verification;
- exact candidate identity.

This does not require public release metadata to be complete.

### MVP-C08 — independent qualification

The frozen package-MVP candidate must pass the Phase 025 independent qualification method derived
from the canonical evaluation method.

Qualification must include required public success obligations plus independently selected or
generated challenge realization for applicable boundary, property, mutation, failure/recovery,
reproducibility, and authority/security families.

## Explicitly outside package-MVP completion

The following are not required to declare the bounded v0.x package MVP complete:

- public distribution or publication;
- distribution-license selection;
- public-release-candidate status;
- current release-candidate vulnerability/advisory clearance;
- a long-term public compatibility window;
- executed support for Python versions beyond 3.11;
- production Databricks/provider qualification;
- general production Spark support certification;
- enterprise-scale benchmark/support qualification;
- deployment/IaC;
- SLO/SLA or production-operations readiness;
- a complete Strategy/algorithm/Evaluation catalog;
- dormant M8 future-capability groups unless separately reactivated through design authority.

An excluded claim must remain visibly unclaimed. Exclusion is not permission to imply support.

## Minimum v0.x support posture

The intended MVP qualification boundary is:

~~~text
package form                    installable Python package
verified Python baseline        3.11
portable/reference path         required
baseline topology set           single-table / time-series / multi-table shared-key
direct/reuse distinction        required
Learning/Learned-State path     required
Spark-capable bounded path      required
production provider support     not required / not implied
enterprise-scale support        not required / not implied
public distribution             separate authorization
~~~

Future Phase 018-025 start gates may refine implementation mechanics and exact test profiles, but
they may not silently remove these blocking MVP capabilities. A genuine conflict requires an
explicit scope/authority amendment.

## Capability milestones

Capability milestones describe program maturity. They are not package versions.

| Milestone | Expected state | Primary roadmap boundary |
|---|---|---|
| MVP-M0 | verified reference/framework baseline; planning only | current / pre-018 |
| MVP-M1 | intentional installable package/public composition surface | Phase 019 exit |
| MVP-M2 | one complete minimal vertical workflow | Phase 020 exit |
| MVP-M3 | baseline topology and strategy distinctions complete | Phase 021 exit |
| MVP-M4 | bounded provider-neutral Spark-capable path complete | Phase 022 exit |
| MVP-M5 | integrated security/recovery/reproducibility hardening complete | Phase 023 exit |
| MVP-M6 | productized package-MVP candidate frozen | Phase 024 exit |
| MVP-M7 | independent v0.x package-MVP qualification decision complete | Phase 025 exit |

Passing a milestone does not authorize the next phase.

## Package-version policy

### 1. Phase numbers are not versions

Do not mechanically map Phase 019 to 0.1.0, Phase 020 to 0.2.0, and so on.

Implementation phases organize dependency-safe work. Package versions identify package artifacts and
compatibility/release intent. They answer different questions.

### 2. 0.0.0 remains the placeholder baseline

The current 0.0.0 project version remains valid while the repository is in planning/reference
development and no intentionally versioned package candidate has been selected.

Changing it during Phase 017 would imply progress that has not occurred.

### 3. First non-placeholder version follows package-surface evidence

A non-placeholder v0.x development version MAY be selected after MVP-M1 when an intentional package
surface exists and an executable phase has a concrete artifact-identity need.

It MUST be selected no later than MVP-M6 candidate freeze.

The selected version must be explicit in package evidence. Version selection alone proves no
capability.

### 4. Exact v0.x numbering is deliberately deferred

Phase 017 does not fix whether the first meaningful artifact is 0.1.0, another 0.N.0, or a
pre-release/development form.

Phase 024 selects the MVP-candidate version after the public package boundary, compatibility posture,
and completed capability evidence are known.

### 5. Pre-1.0 does not remove change-control discipline

No SemVer stability promise is inferred merely from a 0.x number.

Class 2 compatibility/migration assessment remains required for public or persisted contract
changes. The package must state its actual compatibility posture rather than relying on folklore
about pre-1.0 versions.

## Package-MVP state model

Use these states distinctly:

~~~text
development baseline
  -> capability milestones
  -> package-MVP candidate
  -> qualified package MVP
  -/-> public release candidate
  -/-> published release
~~~

The -/-> notation means there is no automatic transition.

### Package-MVP candidate

A package-MVP candidate is the exact frozen Phase 024 subject for Phase 025 evaluation.

It requires MVP-C01 through MVP-C07 complete, an exact commit/build identity, a selected
non-placeholder v0.x version, explicit limitations/non-claims, and no unresolved blocking Class 3/4
conflict.

It is **not** a release candidate merely because the package version is non-placeholder.

### Qualified package MVP

A candidate becomes a qualified package MVP only through a successful Phase 025 decision under the
phase lifecycle.

A qualified package MVP may remain entirely unpublished.

Its existence does not authorize distribution, deployment, provider support, scale claims, or v1
execution.

## Public release boundary

The term **release candidate** is reserved for an artifact actually being considered for public
distribution/release.

Promotion from qualified package MVP to public release candidate is separate work and requires
applicable engineering-preflight evidence, including:

- a deliberate non-placeholder release version;
- distribution-license decision and metadata;
- explicit public compatibility/readability/migration windows for the release scope;
- current vulnerability/advisory review of the resolved release set;
- package build/install evidence;
- support/provider/scale claims restricted to exact evidence;
- human release authorization.

A public release does not require provider or enterprise-scale qualification when those claims are
explicitly excluded. It may not imply them.

Publication itself remains an explicit human-authorized action after release-candidate qualification.

## Residual-risk mapping

| Residual | Package MVP | Public release/provider/scale boundary |
|---|---|---|
| RR-016-01 license | non-blocking; distribution remains prohibited | blocks public release/distribution |
| RR-016-02 vulnerability review | non-blocking for bounded unpublished MVP | blocks public release candidate |
| RR-016-03 public compatibility windows | no public window required; current posture must be explicit | blocks public release/public compatibility promise |
| RR-016-04 Python >3.11 | non-blocking; v0.x verified claim stays at Python 3.11 | blocks broader Python support claim |
| RR-016-05 enterprise benchmark | non-blocking; enterprise scale stays unclaimed | blocks enterprise-scale/performance support claim |
| RR-016-06 production provider qualification | non-blocking; bounded Spark capability is not provider support | blocks production provider/support claim |

No residual may be marked resolved merely because it does not block package-MVP completion.

## Package-MVP completion decision

The v0.x MVP is complete only when:

1. MVP-C01 through MVP-C08 are satisfied;
2. Phase 025 reaches a lifecycle-allowed successful exit outcome;
3. all blocking package/phase obligations are closed;
4. the exact candidate commit/build/version is recorded;
5. required support-scope/current-owner documentation reflects only executed evidence;
6. all RR-016 residuals remain correctly resolved or carried as non-claims;
7. no active Class 3/4 conflict or semantic/architecture reopen remains;
8. public-release/provider/scale state is not overstated;
9. completion identifies the next eligible work without authorizing it.

A large amount of foundation code or a high verification count cannot substitute for a missing
blocking MVP capability.

## Relationship to current support scope

The current support-scope authority continues to own what is actually implemented and supported at
the current repository head.

This document owns the future v0.x target boundary.

During Phases 018-025, support claims may move only when executed evidence justifies updating the
current support owner. This roadmap document never promotes a planned capability into current
support by itself.

## Current authorization boundary

This authority is planning/program scope established by Phase 017-E.

It does not authorize product implementation, change pyproject.toml from 0.0.0, select a public
license, create an active implementation package, authorize Phase 018, create a release candidate,
or publish/distribute an artifact.
