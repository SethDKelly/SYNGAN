---
type: Phase Work Record
title: 016-G — Agentic Conformance, Negative Controls, Drift Detection & CI
status: complete
---

# 016-G — Agentic Conformance, Negative Controls, Drift Detection & CI

## Objective

Make the agentic-development foundation mechanically enforceable through repository-owned deterministic checks and seeded negative controls without conflating repository configuration conformance with product health or provider runtime certification.

## Entry evidence

~~~text
016-F                                 COMPLETE
context workflow stable ref           syngan://authority/agent-context-workflows
016-F closure Verify #1607            PASS
016-F post-merge Verify #1608         PASS
P16-3 / P16-4 findings                0 / 0
~~~

The user explicitly authorized 016-G.

## Design direction

016-G adds an independent conformance plane for repository agentic/documentation configuration:

~~~text
agentic policy / adapters / skills / routing / budgets
  -> deterministic validators
  -> isolated seeded negative controls
  -> one conformance report
  -> dedicated CI job
~~~

This plane does not replace C0-C9 and does not claim provider runtime, product behavior, production readiness, or external security certification.

## Authorized implementation

016-G may add a canonical conformance authority, focused dependency-free validators, one unified runner/report, isolated temporary-copy negative controls, a dedicated GitHub Actions workflow, and bounded repository tests proving the conformance surface remains wired.

## Explicit exclusions

016-G does not install or exercise coding-agent runtimes, external services, MCP servers, credentials, production systems, deployment, implementation-package/ADR policy, supply-chain/secrets preflight, or product/provider integration.

## Exit criteria

- one canonical safe/non-destructive agentic conformance command exists;
- adapters/skills/status/compatibility drift have deterministic owning validators;
- stable-reference, OKF, context-budget, and current-document link validation are included;
- seeded negative controls mutate only a temporary copy and prove representative defects are rejected;
- negative controls cover status self-progression, stable-reference drift, OKF drift, context overflow, skill metadata/scope drift, adapter authority drift, and fabricated provider-runtime support;
- the report explicitly states non-product-health and non-runtime-certification semantics;
- dedicated CI runs the canonical command with checkout + Python only;
- conformance remains independent from C0-C9 while the normal Verify workflow remains green;
- canonical ownership, stable-reference routing, and OKF projection include the conformance authority;
- P16-3/P16-4 findings remain zero;
- 016-H/016-I scope does not leak into 016-G.

## Closure evidence

~~~text
016-G                                 COMPLETE
change class                          P16-2
candidate head                        39b76e8249b76c85178c1f595f7855ed66c8d3b8
pull request                          #6
agentic conformance                   35690366584 / #6 / PASS
candidate Verify                      35690366586 / #1614 / PASS
positive validators                   8 / PASS
seeded negative controls              8 / 8 PASS
status self-progression guard         PASS
stable-reference drift guard          PASS
generated OKF drift guard             PASS
context-budget overflow guard         PASS
portable-skill metadata guard         PASS
Claude authority-import guard         PASS
fabricated runtime-support guard      PASS
broken current-link guard             PASS
stable-reference registry             25 ACTIVE
canonical owner-family coverage       25 / 25
OKF projection                        27 FILES / PASS
provider runtime evidence             UNVERIFIED / NOT CLAIMED
portable                              PASS
C2..C9                                PASS
P16-3 / P16-4                         0 / 0
product/runtime/provider behavior     UNCHANGED
~~~

## Exit decision

Every 016-G exit criterion is satisfied.

016-G is **COMPLETE**.

SYNGAN now has a dedicated repository-owned agentic conformance lane whose positive checks and seeded negative controls mechanically enforce status, routing, workflow, adapter, stable-reference, OKF, and context-budget invariants. PASS remains explicitly limited to repository configuration conformance and cannot self-authorize later work or stand in for product/provider/runtime evidence.

**016-H — Implementation Package Contract, Design-to-Code Traceability & ADR Change Control** is **NEXT ELIGIBLE / NOT AUTHORIZED** pending explicit proceed.
