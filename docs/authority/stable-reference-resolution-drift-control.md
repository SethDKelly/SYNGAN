---
type: Documentation Authority
title: Stable References, Deterministic Resolution & Drift Control
status: active
---

# Stable References, Deterministic Resolution & Drift Control

## Purpose

Define durable logical knowledge references for SYNGAN and the exact rules used to resolve them to current repository resources without relying on path stability, search ranking, or generated-document authority.

This document owns stable-reference syntax, lifecycle, resolution, reverse resolution, retrieval failure behavior, and reference-routing drift control.

## Stable reference form

Stable references use the repository namespace:

~~~text
syngan://<class>/<logical-name>
~~~

Allowed classes are:

- `authority`
- `design`
- `implementation`
- `program`
- `history`

The logical name uses lower-case ASCII letters, digits, and hyphens with optional additional slash-delimited segments.

Examples:

~~~text
syngan://authority/repository-status
syngan://design/concepts
syngan://implementation/support-scope
syngan://program/phase-016
syngan://history/documentation
~~~

A stable reference is a routing identity. It is not a file path, URL to an external service, content hash, semantic identifier for a product concept, or public product API.

## Canonical registry

`docs/authority/stable-reference-registry.json` is the machine-readable registry.

Each active entry binds exactly one stable reference to exactly one current repository path and records its authority class and canonical ownership family.

The registry is routing metadata downstream of the canonical owner. It does not acquire the semantic authority of the document it locates.

## Identity and move rules

1. A stable reference MUST NOT be derived at runtime from the current file path.
2. Renaming or moving the bound file does not by itself change the stable reference.
3. A path move MUST update the stable-reference registry and the canonical ownership map in the same change when that owner path is represented there.
4. An active path MUST have no more than one active stable reference.
5. A stable reference MUST never be reassigned to a different logical owner merely because the old path disappeared.
6. Reference spelling changes are identity changes, not cosmetic path changes.

## Lifecycle

Registry entries use:

- `active` — resolves to one current repository path;
- `retired` — permanently reserved and no longer resolves to a current path.

A retired reference:

- MUST remain reserved;
- MUST NOT be reused;
- MAY identify a `replacement_ref`;
- MUST NOT automatically redirect during exact resolution.

Automatic redirects are intentionally prohibited because they can conceal authority replacement or semantic change.

## Deterministic resolution

Forward resolution is:

~~~text
stable reference
  -> exact registry lookup
  -> active entry
  -> exact current repository path
~~~

Reverse resolution is:

~~~text
current repository path
  -> exact active path lookup
  -> exactly one stable reference
~~~

Resolution MUST NOT:

- search by title;
- infer from basename or slug;
- fall back to repository search;
- choose the highest-ranked or newest document;
- traverse history looking for a similar owner;
- silently follow a retired reference to a replacement.

## Failure discipline

Resolution fails explicitly when:

- syntax is malformed;
- the reference is unknown;
- the reference is retired;
- the active target path is missing;
- reverse resolution has no binding;
- reverse resolution is ambiguous;
- the registry conflicts with canonical ownership;
- a generated OKF route declares a stable reference whose resolved path differs from its generated resource path.

Failure is preferable to heuristic substitution.

## Authority classes

The registry records one of:

- `current` — current durable authority/routing owner;
- `current-program` — current active program authority/work routing;
- `future-non-authoritative` — future-work routing only;
- `history-provenance` — historical evidence/provenance routing only.

The class is retrieval metadata. It does not change documentation authority order.

## OKF integration

Generated OKF route concepts MUST carry `syngan_ref`.

The OKF projection manifest identifies routes by stable reference rather than storing an independent canonical path.

Projection generation resolves the stable reference through the registry and emits the resolved relative `resource` path.

Therefore:

~~~text
OKF route ref
  -> stable-reference registry
  -> current docs path
~~~

The generated `knowledge/` tree remains projection-only and non-authoritative.

## Drift control

Repository validation MUST detect:

- duplicate stable references;
- duplicate active path bindings;
- malformed references;
- missing active paths;
- active bindings outside `docs/`;
- owner-family bindings that differ from the canonical ownership map;
- ownership-map families without exactly one active stable reference;
- OKF manifest references that are unknown or retired;
- generated `syngan_ref` metadata that disagrees with registry resolution;
- generated resource paths that disagree with the stable reference binding.

Content edits do not create drift merely because document bytes change. This control is about identity/routing consistency, not content hashing.

## Change discipline

Stable-reference and resolver changes are P16-2 when they affect routing/process behavior only.

If a proposed reference change would redefine accepted semantics or architecture, stop and reopen the smallest owning authority under P16-3/P16-4 instead of encoding semantic change in routing metadata.

## Explicit exclusions

This contract does not define agent autonomy, authorization to modify files, human approval rules, security/trust policy, task context budgets, portable skills, tool adapters, or product/runtime/provider behavior. Those are owned by later Phase 016 groups or existing product authorities.
