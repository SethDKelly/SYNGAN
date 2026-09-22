---
type: Implementation Authority
title: Implementation Package, Traceability & ADR Change Control
status: active
---

# Implementation Package, Traceability & ADR Change Control

## Purpose

Define the prospective package, traceability, evidence, and architecture-decision change-control contract for material SYNGAN implementation work.

This contract refines the existing [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](implementation-authority-delivery-governance-toolchain-repository-enforcement.md). It does not replace the existing Class 0–4 model, architecture authority, current support scope, or human-directed agent authority.

## Core invariant

> An implementation package is a bounded scope/evidence container. It is never an authorization source and never a semantic or architecture owner.

Package creation, a package status change, code existence, a passing test, or an ADR cannot independently authorize implementation or redefine upstream meaning.

## Applicability

A material Class 1 or Class 2 implementation slice SHOULD have one package manifest under `docs/implementation/packages/` once that slice is explicitly selected for implementation.

Class 0 maintenance MAY omit a package when existing review/test evidence is sufficient.

Class 3 and Class 4 conflicts MUST NOT proceed as ordinary implementation packages. They stop the affected work and reopen the smallest upstream architecture or semantic owner. After that upstream change is accepted, downstream implementation resumes against the new current authority as an appropriate Class 1/2 realization.

016-H creates no active package instance. Completed Phase 015 work remains historical implementation evidence and is not retroactively repackaged merely to satisfy this format.

## Package identity and lifecycle

Material implementation packages use immutable logical IDs:

~~~text
IPKG-0001
IPKG-0002
...
~~~

The ID identifies the delivery/evidence package, not a product concept, runtime job, PR, branch, architecture decision, or deployment.

Allowed lifecycle states are:

- `planned` — package defined but not claimed started;
- `in_progress` — explicitly selected work is being realized;
- `blocked` — material conflict/dependency prevents ordinary completion;
- `complete` — all mandatory package obligations and evidence are satisfied;
- `superseded` — package replaced by a named successor while history remains preserved.

Lifecycle does not convey authorization. A package that is not backed by an explicit human-selected task remains descriptive only.

## Required package manifest

The machine-readable profile is `implementation-package-profile.json`. Package manifests live under `docs/implementation/packages/IPKG-####.json`.

A package records at least:

- immutable package ID and title;
- lifecycle status and Class 0–4 impact classification;
- explicit authorization basis supplied by the selected task/program authority;
- current stable `syngan://...` authority references;
- bounded included implementation scope and explicit exclusions;
- obligation-level mapping from authority to implementation paths and verification paths;
- verification commands/evidence actually available;
- compatibility/migration assessment for Class 2 changes;
- referenced architecture ADR rationale, when relevant;
- unresolved/blocking items;
- explicit non-claims and deferred work.

Manifest metadata is evidence/routing. It must reference current authority rather than copy large semantic or architecture passages.

## Authority reference rule

Every material obligation uses an active stable `syngan://...` reference. When a package needs precision below the document level, it also records the current section heading or local proposition locator.

Stable-reference resolution proves identity/routing only. It does not prove implementation.

History may be cited for rationale/provenance but cannot satisfy the current-authority field.

## Obligation-to-code/test/evidence mapping

Each material package obligation records:

~~~text
obligation ID
current authority ref
section / proposition locator
implementation paths
verification paths
evidence state
notes / limitation
~~~

Allowed evidence states are:

- `planned` — realization/evidence not yet established;
- `implemented` — implementation exists but mandatory verification is not yet established;
- `verified` — required repository evidence supports the obligation;
- `blocked` — obligation cannot currently progress under ordinary implementation authority;
- `not_applicable` — explicitly justified as outside the package's bounded scope.

`verified` requires both implementation and verification evidence appropriate to the obligation. A canonical locator, prose assertion, model confidence, one-off notebook success, or unrelated passing gate is not implementation proof.

## Completion rule

A package may be `complete` only when:

- every material obligation is `verified` or justified `not_applicable`;
- referenced implementation and verification paths exist;
- required package-level verification evidence is recorded;
- blocking/unresolved items are empty;
- compatibility/migration obligations are assessed when Class 2 applies;
- no Class 3/4 conflict remains hidden inside the package;
- non-claims remain explicit where evidence does not establish broader support.

Package completion never authorizes the next package, phase, backlog item, release, deployment, or provider integration.

## Class 0–4 interaction

The existing implementation classification remains controlling:

- **Class 0** — local/non-contractual maintenance;
- **Class 1** — implementation realization decision;
- **Class 2** — public/persisted/compatibility contract change;
- **Class 3** — architecture-affecting conflict/change;
- **Class 4** — semantic/experience conflict/change.

Class 2 packages must record explicit compatibility and migration assessments even when the result is `no impact`.

Class 3/4 findings are stop/reopen conditions. A package may record the blocked conflict and affected refs, but it must not claim `in_progress` or `complete` while that higher-layer conflict is unresolved.

## Implementation decisions vs architecture ADRs

Ordinary implementation realization decisions belong in `docs/implementation/` or the selected package evidence when they do not change architecture.

`docs/decisions/ADR-*` remains an **architecture rationale** surface. An implementation package may reference an active ADR, but it may not use the ADR as permission to change current architecture.

Adding, materially changing, superseding, or retiring an architecture ADR requires an explicitly authorized architecture change/reopen. The corresponding canonical architecture owner MUST be updated first or in the same change. The ADR records durable rationale and supersession consequences; it never becomes the sole current rule.

Class 0–2 implementation work MUST NOT modify architecture ADR meaning as a convenience mechanism. If such a modification appears necessary, reclassify and stop under Class 3.

## ADR supersession discipline

When architecture genuinely changes:

1. identify the smallest current architecture owner and upstream requirement;
2. establish explicit architecture-change authorization;
3. update the canonical architecture rule;
4. update or add ADR rationale as a downstream consequence when durable alternatives/rationale are useful;
5. identify superseded ADRs explicitly rather than rewriting history;
6. re-evaluate affected implementation packages/tests;
7. resume implementation only against the new accepted authority.

An ADR must not be edited merely to make existing code appear conformant.

## Traceability maintenance

Traceability SHOULD be updated in the same selected A2 task that changes material implementation behavior.

Updates must preserve the distinction between:

~~~text
authority identity
implementation realization
verification evidence
support/qualification claim
~~~

Resolving an authority ref proves only the first item.

The canonical `update-traceability` workflow may update package evidence only when actual code/test/CI evidence exists. It cannot create behavior, authorization, or a completion claim from documentation alone.

## Pull-request/review contract

A material implementation PR should identify:

- package ID or explain why no package is required;
- selected task/authorization basis;
- Class 0–4 classification;
- upstream stable authority refs;
- implementation and verification changes;
- compatibility/migration, dependency, network/egress, security, and scale impacts as applicable;
- ADR references and whether an architecture reopen is required;
- unresolved/deferred work and explicit non-claims.

The repository PR template operationalizes this review contract but remains below canonical authority.

## Package history and supersession

Completed/superseded package manifests are retained as implementation evidence. They must not be rewritten to imply evidence that did not exist at the time.

If a package is superseded, record its successor and preserve both histories. A successor package does not retroactively make the predecessor complete.

## Validation

`tools/validate_implementation_packages.py` checks the package profile, prospective package manifests, active stable-reference use, path/evidence consistency, Class 2 assessment requirements, Class 3/4 stop behavior, and ADR-reference validity.

016-H fixtures and seeded negative controls exercise the validator without creating a real implementation package.

## Phase boundary

016-H does not define dependency/supply-chain/secrets review, benchmark qualification, support-matrix versioning, or API/version-release policy reserved for 016-I.

016-H does not authorize a post-Phase-016 implementation program.
