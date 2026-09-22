---
name: resolve-reference
description: Resolve an exact syngan:// stable knowledge reference to its current canonical owner and minimum surrounding context. Use for precise authority lookup. Read-only A1 workflow.
---

# Resolve reference

## Boundary

This is A1 read/review/plan work. It locates current authority and does not create or modify it.

## Workflow

1. Preserve the supplied `syngan://...` reference exactly; do not infer a replacement from title or slug.
2. Run `python tools/resolve_knowledge_ref.py <reference>` when a checkout is available.
3. Read the resolved current owner and only the minimum section/context required by the question.
4. Reverse-resolve a path with `--from-path` only when exact path identity matters.
5. Use `docs/history/` only for an explicit provenance/rationale question; history never competes with current ownership.
6. Distinguish canonical content from generated OKF routes, search results, implementation evidence, examples, memory, and prior summaries.
7. Surface malformed, unknown, retired, missing, or ambiguous resolution explicitly.

## Output

Return the exact stable reference, current path, authority class/owner family when useful, concise application context, and unresolved authority concerns.

## Stop conditions

Do not guess a path, silently redirect a retired reference, use search rank as authority, or edit repository files.
