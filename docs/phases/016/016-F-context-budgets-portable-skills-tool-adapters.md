---
type: Phase Work Record
title: 016-F — Context Budgets, Portable Skills, Tool Adapters
status: complete
---

# 016-F — Context Budgets, Portable Skills, Tool Adapters

## Objective

Make the 016-E human-directed operating model practical across supported coding-agent tools without growing persistent context, duplicating repository semantics, or binding SYNGAN correctness to one provider.

## Entry evidence

~~~text
016-E                                 COMPLETE
agent authority stable ref            syngan://authority/agent-development-policy
016-E closure Verify #1601            PASS
016-E post-merge Verify #1602         PASS
P16-3 / P16-4 findings                0 / 0
~~~

The user explicitly authorized 016-F.

## Design direction

016-F uses three layers:

~~~text
persistent shared authority     -> small root AGENTS / tiny tool bridge
on-demand portable workflows    -> .agents/skills/<name>/SKILL.md
canonical detailed truth        -> docs owners reached only when needed
~~~

Context budgets are measured in UTF-8 bytes because repository bytes are deterministic. Provider token accounting may be observed later but is not a repository correctness primitive.

Portable skills describe how to execute bounded tasks. They do not own product semantics, task selection, current phase status, A3 authorization, or A4 reopen authority.

Tool adapters are compatibility mechanics. They may route/import the shared policy and canonical skills, but cannot carry an independent semantic or security rulebook.

## Authorized implementation

016-F may add canonical context-budget/workflow/tool-adapter authority, machine-readable budgets, portable repository skills, minimal Claude compatibility bridges, documented tool-discovery mapping and manual fallback, a deterministic budget measurement helper, and bounded fitness checks.

## Explicit exclusions

016-F does not add autonomous work queues, subagent orchestration, MCP servers, external credentials, unattended deployment, provider-runtime certification, agentic CI negative-control fixtures, implementation-package/ADR rules, or product/runtime/provider integration.

## Exit criteria

- persistent and on-demand context surfaces have deterministic byte budgets;
- context discovery begins with the smallest current route and expands only for a concrete question;
- known stable references bypass unnecessary broad discovery;
- portable skills use one common frontmatter subset and remain task-bounded;
- Cursor and Codex use shared AGENTS plus `.agents/skills/` without duplicate semantic adapters;
- Claude uses a thin compatibility bridge rather than a copied policy/workflow corpus;
- loss of native skill discovery has a manual repository fallback;
- tool switching requires no semantic/status migration;
- documented compatibility is distinguished from provider-runtime verification;
- canonical ownership, stable-reference routing, and OKF projection include the new authority;
- repository fitness/budget checks pass without creating the 016-G conformance program;
- existing portable and C2-C9 verification remain green;
- P16-3/P16-4 findings remain zero.

## Closure evidence

~~~text
016-F                                 COMPLETE
change class                          P16-2
candidate head                        3e1dca16fadfd382bf9f7c504a462a2c63a58988
pull request                          #5
candidate Verify                      35688409580 / #1603
candidate Verify result               PASS
context budget unit                   UTF-8 BYTES
budget measurement                    PASS
canonical portable skills             5 / PASS
Claude project bridge                 PASS
Claude command bridges                5 / PASS
Cursor documented adapter             AGENTS + .agents/skills
Codex documented adapter              AGENTS + .agents/skills
provider runtime evidence             UNVERIFIED / NOT CLAIMED
manual fallback                       PASS
stable-reference registry             24 ACTIVE
canonical owner-family coverage       24 / 24
OKF projection                        26 FILES / PASS
portable                              PASS
C2..C9                                PASS
P16-3 / P16-4                         0 / 0
product/runtime/provider behavior     UNCHANGED
~~~

## Exit decision

Every 016-F exit criterion is satisfied.

016-F is **COMPLETE**.

SYNGAN now has bounded progressive context retrieval, provider-neutral canonical workflows, and thin provider adapters whose failure degrades ergonomics rather than repository correctness. Documented provider capability remains separate from runtime certification, and no tool-specific surface may fork task authority or product semantics.

**016-G — Agentic Conformance, Negative Controls, Drift Detection & CI** is **NEXT ELIGIBLE / NOT AUTHORIZED** pending explicit proceed.
