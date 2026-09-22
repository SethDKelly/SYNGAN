---
name: resolve-context
description: Resolve the minimum authoritative SYNGAN repository context for a human-selected task. Use when current scope, status, ownership, or governing sources are unclear. Read-only A1 workflow.
---

# Resolve context

## Boundary

This is A1 read/review/plan work. Context retrieval does not authorize edits, scope expansion, or follow-on work.

## Workflow

1. Identify the operative human request, requested action, exclusions, and named phase/task if any.
2. Read root `AGENTS.md`.
3. Read `docs/authority/current-repository-status.md` only when progression or authorization state matters.
4. If an exact `syngan://...` reference is known, resolve it directly with `python tools/resolve_knowledge_ref.py <ref>` and avoid broad discovery.
5. Otherwise use `docs/index.md` and the canonical ownership map to select the smallest current owner.
6. Read only the current owner, tests/evidence, and active work record needed to answer a concrete task question.
7. Use history only for an explicit provenance, rationale, supersession, or reconstruction question.
8. Identify unresolved authority, broken routes, external capability facts, or A3/A4 boundaries explicitly.
9. Return the minimum context set and stop.

## Context rule

Loading another file requires a concrete question it answers. Do not preload the corpus, all architecture documents, all skills, generated OKF routes, or history.

## Output

Report the task/action class, current status if relevant, chosen owner/reference paths and why they are needed, unresolved facts, and stop/escalation conditions.

## Stop conditions

Stop rather than guess when current authority cannot be resolved, a stable reference fails, owners materially conflict, or the request requires A3/A4 authorization.
