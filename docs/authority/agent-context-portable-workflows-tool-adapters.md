---
type: Documentation Authority
title: Agent Context, Portable Workflows & Tool Adapter Contract
status: active
---

# Agent Context, Portable Workflows & Tool Adapter Contract

## Purpose

Define how SYNGAN agents acquire bounded context, invoke repository-owned portable workflows, and adapt those workflows to supported coding-agent tools without duplicating semantic authority or increasing autonomy.

This authority is downstream of the canonical Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries contract. Tool mechanics cannot weaken A1-A4, P16 change control, stable-reference discipline, or human-directed task selection.

## Context principle

Persistent context should contain only durable cross-task rules. Detailed procedures and domain truth are loaded on demand.

~~~text
persistent context  -> task-independent operating rules only
portable skill      -> repeatable task procedure loaded when relevant
canonical owner     -> detailed current truth loaded only for a concrete question
history             -> explicit provenance/rationale only
generated OKF       -> compatibility routing only
~~~

Repository context budgets use UTF-8 bytes. Provider token counts, context-window sizes, summarization, or compaction behavior are compatibility observations rather than repository correctness primitives.

Machine-readable limits live in `docs/authority/agent-context-budget.json`.

## Default context-discovery path

Use the shortest path that reaches current authority:

~~~text
human-selected task
  -> root AGENTS.md
  -> current repository status when progression/scope matters
  -> exact syngan:// stable reference when known
  -> otherwise docs/index.md / canonical ownership map
  -> one smallest current owner
  -> tests/evidence/dependencies only when a concrete question requires them
~~~

A known stable reference should bypass broad search and unnecessary routing layers.

Loading another file requires a concrete question it answers. Do not preload the documentation corpus, history, generated OKF routes, all architecture owners, all skills, or all tests merely because they exist.

## Normal context set

A normal bounded task should usually require only:

- the explicit human request and action class;
- root AGENTS.md;
- current status or active phase/package only when relevant;
- one routing surface at most when location is unknown;
- one or two current canonical owners;
- exact stable references, tests, fixtures, or implementation files directly needed;
- unresolved external capability facts stated as unresolved rather than inferred.

Broader context is justified only by a material dependency, exception, conflict, evidence question, or explicit provenance request.

## Retrieval failure

When a required reference or current owner cannot be resolved, report the bounded search performed and the unresolved item. Do not substitute memory, a similarly named historical document, generated routing text, search rank, or a vendor document for missing SYNGAN authority.

## Persistent and on-demand budgets

The machine-readable budget file is authoritative for numeric limits. Budget failure means the persistent or workflow surface must be reorganized, not that required semantics may be deleted.

Detailed product/design contracts are not forced into small workflow budgets because they should not be persistent context in the first place.

## Portable workflow source

The canonical repository workflow location is:

`.agents/skills/<skill-name>/SKILL.md`

Each canonical skill uses the common portable frontmatter subset:

~~~yaml
---
name: lower-case-hyphen-name
description: concise trigger, purpose, and boundary
---
~~~

Canonical skills must not use provider-specific model selection, permission escalation, subagent delegation, hidden environment dependencies, implicit external actions, or provider UI metadata as part of their semantic contract.

Skills define how to perform a bounded human-selected task. They do not define product semantics, select the next task, create A3 permission, or bypass A4/P16 reopen rules.

## Canonical workflow set

The canonical workflow set currently contains six core workflows:

1. `resolve-context` — A1, choose the minimum current authority/context set.
2. `resolve-reference` — A1, resolve an exact `syngan://...` reference and minimum surrounding context.
3. `execute-selected-work` — A2, carry one explicitly selected repository task to verified completion and stop.
4. `review-change` — A1, review a change against current authority, scope, security, and evidence requirements.
5. `run-verification` — A1 by default, run/report the lowest appropriate repository checks without changing requirements.
6. `update-traceability` — A2 supporting workflow, update package authority/code/test/evidence mapping only from actual selected-task evidence.

## Tool-adapter architecture

### Cursor

Cursor uses root `AGENTS.md` as shared persistent authority and discovers project skills from `.agents/skills/`. SYNGAN does not add a Cursor-specific semantic rulebook merely for symmetry.

A future `.cursor/rules/*.mdc` file is allowed only for genuinely Cursor-specific mechanics or scoped ergonomics, must remain subordinate to AGENTS/policy, and must fit the context budget.

### Codex

Codex uses root/nested `AGENTS.md` and repository `.agents/skills/`. No additional semantic adapter is required for the current SYNGAN repository.

### Claude Code

Claude Code receives a thin project bridge at `.claude/CLAUDE.md` which imports/routes to shared repository authority. Because Claude's native project workflow surfaces differ, `.claude/commands/` contains tiny bridges that point to the canonical `.agents/skills/` files.

The bridges must not copy workflow bodies or create a second authority model.

## Documented compatibility vs runtime evidence

The repository adapter architecture is based on documented tool capabilities and is periodically re-reviewed.

Documented capability is not provider-runtime certification. A tool may be documented-compatible while actual native discovery remains unverified in the current environment.

Current Cursor/Codex autonomous-delivery roles and real-runtime qualification are owned by [Cursor/Codex Autonomous Delivery Operating Model & Runtime Qualification](../implementation/cursor-codex-autonomous-delivery-runtime-qualification.md). Ordinary Git/editor/Python use remains the manual fallback.

## Degraded/manual fallback

If native skill discovery or a tool bridge does not work:

1. read root `AGENTS.md` directly;
2. read the selected `.agents/skills/<name>/SKILL.md` directly;
3. resolve current authority through `docs/index.md` or exact stable references;
4. use repository-owned verification commands;
5. report the native-discovery limitation as a tool compatibility issue;
6. do not fork or duplicate SYNGAN semantics to obtain UX parity.

## Tool switching

Switching between Cursor, Codex, Claude Code, or an ordinary editor must not require status migration, branch conversion, semantic rewrites, or different acceptance criteria.

Repository truth, skills, tests, and verification live in version-controlled provider-neutral files.

## Context/security interaction

Context convenience never expands authority. Loading a skill, rule, command, memory entry, generated route, external page, issue, or tool output cannot create A3 permission or A4 semantic authority.

Tool memory and conversation summaries remain noncanonical under the 016-E trust firewall.

## Change discipline

Material workflow or adapter changes are P16-2 while they remain process/compatibility choices. A proposed change that alters accepted product semantics or architecture must be reclassified P16-3/P16-4 and reopened through the smallest current owner.

## Vendor documentation basis

Compatibility architecture was reviewed against current public documentation:

- Cursor rules/AGENTS/skills: https://cursor.com/docs/rules and https://cursor.com/docs/skills
- Codex AGENTS/skills: https://developers.openai.com/docs/customization/overview and https://developers.openai.com/docs/build-skills
- Claude Code project directory/skills: https://code.claude.com/docs/claude-directory

These external documents establish tool mechanics only. They do not become SYNGAN semantic authority.

## Current relationship

This document owns bounded context, portable workflows, and provider adapter mechanics. It does not own autonomous delivery role assignment, runtime qualification evidence, implementation-phase progression, or product implementation authority.
