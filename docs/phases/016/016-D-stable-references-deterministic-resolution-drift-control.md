---
type: Phase Work Record
title: 016-D — Stable References, Deterministic Resolution & Drift Control
status: active
---

# 016-D — Stable References, Deterministic Resolution & Drift Control

## Objective

Establish durable logical references for current SYNGAN knowledge so callers can identify an authority independently of its repository path, resolve it exactly and reproducibly, and fail visibly when routing metadata drifts.

## Entry evidence

~~~text
016-C                                 COMPLETE
OKF v0.2 producer profile             COMPLETE
generated knowledge projection        COMPLETE
016-C post-merge Verify #1585         PASS
P16-3 / P16-4 findings                0 / 0
~~~

The user explicitly authorized 016-D.

## Problem

Path-based references are readable but not stable under documentation relocation. Search-based retrieval is discoverable but not deterministic and can elevate historical or generated material by rank.

016-D therefore separates:

~~~text
stable logical identity   != repository path
repository path           != semantic authority
search result             != deterministic resolution
generated route           != current owner
~~~

## Decision direction

Stable references use the reserved repository namespace:

~~~text
syngan://<class>/<logical-name>
~~~

The reference is durable routing identity. The stable-reference registry owns its current path binding.

A path move updates the binding while preserving the stable reference. A retired reference remains reserved and cannot be reused.

Resolution is exact and fail-closed. The resolver MUST NOT guess from titles, basenames, slugs, search rank, or historical similarity.

## Authorized implementation

016-D may add:

- the canonical stable-reference/resolution/drift-control authority;
- a machine-readable reference registry;
- exact forward and reverse resolution tooling;
- validation of uniqueness, coverage, path existence, lifecycle, and authority class;
- OKF manifest/reference integration;
- generated-route stable-reference metadata;
- repository fitness tests and verification integration;
- current status/routing updates required to express the decision.

## Explicit exclusions

016-D does not define agent autonomy or change authority, human approval rules, security/trust policy, context budgets, tool-specific adapters, product/runtime/provider behavior, or a new public product API.

## Exit criteria

016-D may close only when:

- every canonical ownership-map family has exactly one active stable reference;
- active references are unique and active paths resolve to existing current repository resources;
- exact reverse resolution is unambiguous for active bindings;
- malformed, unknown, retired, and ambiguous resolution states fail explicitly without search fallback;
- generated OKF routes bind through stable references rather than owning independent path bindings;
- generated route metadata agrees with registry resolution;
- reference/path/ownership drift is mechanically detected;
- existing authority/portable and C2-C9 verification remain green;
- P16-3/P16-4 findings remain zero;
- no 016-E/016-F agent-policy or adapter scope leaks into 016-D.

## Current state

~~~text
016-D                                 AUTHORIZED / ACTIVE
stable-reference contract             IN PROGRESS
machine-readable registry             IN PROGRESS
deterministic resolver                IN PROGRESS
OKF reference binding                 IN PROGRESS
drift validation                      IN PROGRESS
P16-3 / P16-4                         0 / 0
016-E                                  NOT AUTHORIZED
~~~
