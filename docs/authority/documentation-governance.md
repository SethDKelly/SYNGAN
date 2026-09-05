---
type: Documentation Authority
title: Documentation Governance and Anti-Drift Rules
status: active
---

# Documentation Governance and Anti-Drift Rules

## Purpose

This document defines how SYNGAN documentation remains authoritative, navigable, reviewable, and resistant to semantic drift as the project grows.

## Canonical authority

Every durable fact, definition, requirement, invariant, policy, design decision, or implementation rule MUST have one canonical home.

Other documents SHOULD reference that canonical authority rather than reproduce it.

Repetition is permitted only when one of the following applies:

- local comprehension would otherwise be materially impaired;
- a document must remain independently auditable;
- an explicitly labeled summary or derived view is useful;
- a temporary migration requires duplicated text while authority is being moved.

Repeated text MUST NOT create a competing source of truth. Where duplicated material can age independently, the document MUST identify the canonical source.

## Documentation authority order

Unless a later explicit decision overrides this order, interpret conflicting material using the following precedence:

1. `docs/authority/` — methodology, terminology, documentation, provenance, network/dependency, and cross-cutting policy/contract rules.
2. `docs/concepts/` and `docs/synchronizations/` — accepted semantic ownership and cross-concept coordination.
3. `docs/experience/` — accepted actor-visible/programmatic workflow and experience contracts downstream of semantics.
4. `docs/architecture/` — accepted representation and architecture rules downstream of experience; accepted ADRs under `docs/decisions/` preserve architecture decision rationale/supersession history but MUST NOT override upstream authority or newer canonical architecture.
5. `docs/implementation/` — accepted implementation-planning and delivery authority downstream of architecture. Implementation choices may select concrete realization mechanisms but MUST NOT weaken/redefine architecture for convenience.
6. Current phase deliverables and exit reviews — execution/planning history and consolidation evidence, not a substitute for promoted canonical authority.
7. Source code, deployment/configuration, generated artifacts, examples, tutorials, and agent-oriented navigation aids — executable or derived realizations that MUST conform to the accepted authority above them.
8. Backlog and exploratory notes.

A lower-authority document or code artifact MUST NOT silently override a higher-authority one.

Architecture that discovers an upstream infeasibility or contradiction MUST surface the conflict explicitly and request an upstream design revision rather than redefining the upstream contract inside `docs/architecture/`.

Implementation that discovers an architecture infeasibility or contradiction MUST surface the conflict explicitly and request an architecture revision rather than redefining the contract inside `docs/implementation/` or code.

## OKF 0.2 profile

`docs/` is an OKF 0.2 knowledge bundle under the current project-specific profile.

The bundle root MUST be `docs/index.md` and MUST declare `okf_version: "0.2"`.

All durable knowledge documents MUST contain YAML frontmatter with at least:

```yaml
---
type: <project-specific type>
title: <human-readable title>
status: <status>
---
```

Additional metadata MAY be added when useful for provenance, lifecycle, verification, relationships, or automation.

Project-specific `type` values are allowed and SHOULD describe the semantic role of the document rather than its file format.

The separate question of strict conformance to external OKF 0.2 reserved-file/frontmatter conventions remains subject to an explicit external-authority audit; repository text MUST NOT imply that separate normalization question has been completed merely because the project uses this profile.

## Progressive disclosure

Every durable documentation area SHOULD have an `index.md` when the area contains multiple documents or when an agent would otherwise need to scan the directory to understand it.

Indexes SHOULD:

- explain the area's purpose;
- link to the smallest set of canonical child documents needed to navigate it;
- avoid restating child-document content;
- indicate current authority and lifecycle status where useful.

The root and section indexes form the primary agent-navigation surface.

For implementation work, agents and humans SHOULD normally begin with `docs/index.md`, the consolidated architecture contract, and `docs/implementation/index.md`, then follow only the detailed authorities needed for the active slice.

## Status vocabulary

Until superseded, use these lifecycle states:

- `draft` — under active development and not yet authoritative;
- `proposed` — coherent and reviewable, but not yet accepted;
- `active` — current canonical authority;
- `deprecated` — retained for compatibility or historical context but no longer preferred;
- `superseded` — replaced by explicitly identified newer authority;
- `archived` — historical and not part of current design authority.

Phase work MAY use additional progress markers in prose, but the frontmatter `status` SHOULD use this vocabulary.

## Phase documentation

Phase documents SHOULD record:

- objective;
- scope;
- non-goals;
- inputs and governing authorities;
- questions to resolve;
- decisions and findings;
- created or changed canonical authorities;
- unresolved items;
- exit criteria;
- completion status.

A phase document is a work record, not automatically the long-term canonical home of every decision it contains. Durable conclusions MUST be promoted into the appropriate canonical authority when needed.

## Change discipline

When changing an established rule:

1. locate its canonical source;
2. update that source first or in the same change;
3. update inbound references only where required;
4. do not patch multiple copied statements independently;
5. record material compatibility or migration consequences;
6. mark obsolete authority as superseded or deprecated rather than leaving contradictory text active.

Implementation-specific change classification and delivery evidence are governed by [Implementation Authority, Delivery Governance, Toolchain & Repository Enforcement](../implementation/implementation-authority-delivery-governance-toolchain-repository-enforcement.md).

## Agent authoring rules

Human and automated contributors MUST follow the same authority model.

Agents SHOULD begin from `docs/index.md`, then follow indexes and direct references. They SHOULD NOT load the entire documentation corpus unless the task genuinely requires it.

For implementation tasks, the root [`AGENTS.md`](../../AGENTS.md) provides concise repository-wide execution rules but remains a navigation/enforcement aid below canonical documentation authority.

Agents MUST NOT:

- infer a rule from repeated examples when a canonical specification exists;
- invent new terminology when canonical terminology is available;
- convert an architectural hypothesis into an accepted concept implicitly;
- resolve contradictions by choosing whichever document/code artifact was encountered first;
- copy large canonical sections into new documents merely for convenience;
- treat existing code or tests as permission to override accepted design/architecture;
- add implementation dependencies or hidden runtime/network behavior solely for generation convenience.

If an agent finds conflicting active authorities, it SHOULD flag the conflict and resolve it explicitly rather than silently choosing one.

## Documentation quality rules

Durable documents SHOULD be:

- concise enough for targeted retrieval;
- complete enough to explain their own authority;
- link-rich rather than repetition-heavy;
- explicit about uncertainty;
- explicit about normative strength using MUST, SHOULD, MAY where appropriate;
- free from implementation detail unless the document's layer requires it.

## Repository README

The repository `README.md` is an orientation surface, not the complete design or implementation authority. It SHOULD point readers to `docs/index.md` for canonical knowledge.

## Anti-drift review

Every phase exit SHOULD check:

- whether new durable rules were left only in phase notes/code;
- whether concepts or terms now have multiple definitions;
- whether superseded assumptions remain labeled active;
- whether indexes still lead to current authority;
- whether architecture text has leaked into concept authority without justification;
- whether implementation has silently weakened architecture;
- whether code/tests/examples have become undocumented de facto contracts;
- whether copied text should be replaced with cross-references.
