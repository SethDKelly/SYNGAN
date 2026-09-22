---
type: Documentation Authority
title: OKF v0.2 Producer Profile, Generated Knowledge Projection & Conformance
status: active
---

# OKF v0.2 Producer Profile, Generated Knowledge Projection & Conformance

## Purpose

Define how SYNGAN produces and validates an externally compatible Open Knowledge Format v0.2 bundle without turning a generated interchange surface into a second authority plane.

This document owns the OKF producer/projection/conformance contract. Product semantics remain owned by their existing current authorities.

## External specification baseline

016-C audited the Open Knowledge Format v0.2 specification in `GoogleCloudPlatform/knowledge-catalog` at repository commit `22efaa5402775a7c4d4c37f89e41258daaf3cb65` (`okf/SPEC.md` blob `c06e3eede0c910d0ecf12524c34204156f8795ac`).

The external conformance minimum is intentionally small:

- every non-reserved Markdown concept has parseable YAML frontmatter;
- every concept has a non-empty `type`;
- `index.md` and `log.md` are reserved structural filenames;
- only the bundle-root `index.md` may carry frontmatter, for the optional `okf_version` declaration;
- optional metadata families must not be treated as mandatory merely because a producer chooses to use them.

SYNGAN adopts a stricter producer profile for its generated routes while preserving that permissive external model.

## Authority topology

~~~text
AUTHORED CURRENT AUTHORITY
docs/
  |
  | deterministic projection
  v
GENERATED COMPATIBILITY / ROUTING
knowledge/
~~~

Rules:

1. `docs/` remains the authored current knowledge and authority surface.
2. `knowledge/` is generated, disposable, and reproducible from repository-owned sources.
3. `knowledge/` MUST NOT be hand-edited.
4. A generated route MUST NOT create, strengthen, weaken, reinterpret, or supersede a proposition.
5. Search rank, OKF metadata, generated lifecycle status, or generated prose MUST NOT outrank the canonical owner under `docs/`.
6. A semantic change is made in the smallest current owner and only then reflected by regeneration when routing is affected.

## Bundle root and reserved files

The generated bundle root is `knowledge/`.

The root `knowledge/index.md`:

- MUST declare only `okf_version: "0.2"` in frontmatter;
- MUST identify the bundle as a generated compatibility projection in its body;
- MUST route progressively to group indexes and the authored `docs/` root.

Group `index.md` files:

- MUST contain no YAML frontmatter;
- MUST list only their generated child routes;
- MUST remain routing surfaces rather than semantic summaries.

016-C does not require `log.md`. Git history and canonical source documents retain change history and provenance.

## SYNGAN route-concept profile

Every non-reserved generated Markdown document MUST contain:

~~~yaml
type: "SYNGAN Knowledge Route"
title: "<display title>"
description: "<one-sentence routing description>"
syngan_ref: "syngan://<class>/<logical-name>"
resource: "<resolved relative path to canonical docs owner>"
tags: ["syngan", "<group>", "generated", "routing"]
status: "stable"
syngan_authority: "projection-only"
~~~

Additional constraints:

- `syngan_ref` MUST resolve exactly through the canonical stable-reference registry;
- `resource` MUST equal the current path resolved from `syngan_ref` and resolve to an existing path under `docs/`;
- local Markdown links MUST resolve even though external OKF v0.2 consumers are required to tolerate broken links;
- `status` uses the external OKF v0.2 lifecycle vocabulary for the projection, not the richer authored-document lifecycle;
- `generated` and `verified` trust metadata are intentionally omitted from this routing profile because a generated route does not independently verify the truth of its target;
- output MUST be deterministic: no wall-clock timestamps, random identifiers, or environment-dependent ordering.

## Projection manifest

`docs/authority/okf-projection-manifest.json` is the machine-readable projection source.

It defines the authored discovery root, generated root, producer-profile owner, projection-only authority classification, and route groups keyed by stable `syngan://...` references. Canonical paths are resolved from the stable-reference registry during generation rather than duplicated in the manifest.

The manifest is not a semantic owner. It is deterministic input governed by this profile.

## Generation and conformance

`tools/generate_okf_projection.py` owns deterministic rendering.

- `--write` recreates the generated `knowledge/` tree from the manifest.
- `--check` compares the committed tree with a fresh in-memory rendering and fails on missing, unexpected, or drifted files.

`tools/validate_okf_projection.py` validates both external OKF v0.2 structural conformance and the stricter SYNGAN producer profile above.

The existing repository authority/portable verification path MUST run projection generation drift checks and conformance validation. 016-C does not establish the broader agentic negative-control/CI program reserved for 016-G.

## Change discipline

A change to this producer contract is P16-2 while it remains a compatibility/process decision with no accepted product or architecture impact.

If an OKF requirement would force a change to accepted semantics or architecture, stop and reopen the smallest owning authority under P16-3/P16-4 rather than changing canonical meaning for format convenience.

## Explicit exclusions

Phase 016-D owns stable-reference identity and exact deterministic routing for the generated projection. This profile still does not authorize agent action/change/context-budget/tool-adapter policy, product/runtime/provider behavior, new public product APIs, or external service dependencies merely to validate documentation.

Those remaining boundaries are owned by later Phase 016 groups.

## Conformance claim

SYNGAN may claim OKF v0.2 conformance only for the generated `knowledge/` projection after both deterministic generation check and producer-profile validation pass.

The authored `docs/` tree MUST NOT be described as the externally conformant OKF bundle.
