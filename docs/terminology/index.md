---
type: Terminology Index
title: SYNGAN Domain Terminology
status: active
---

# SYNGAN Domain Terminology

This directory is the canonical navigation layer for SYNGAN domain terminology established during Phase 001-C.

Terminology here describes the problem domain. It does not, by itself, establish that a term is an independent software concept, public API type, class, package, storage representation, or execution primitive.

## Canonical documents

- [Domain Lexicon](domain-lexicon.md) — preferred domain terms and canonical meanings.
- [Semantic Distinctions](semantic-distinctions.md) — distinctions that MUST remain visible during concept discovery and later design.
- [Ecosystem Compatibility Vocabulary](ecosystem-compatibility.md) — mappings and collision notes for SDV, Spark, PyTorch, and common synthetic-data vocabulary.
- [Term Status Register](term-status-register.md) — term maturity, ambiguity, and concept-candidate signals without deciding concept boundaries.

## Governing authority

Terminology is governed by [Terminology Policy](../authority/terminology-policy.md).

## Semantic-layer rule

SYNGAN distinguishes four lexical layers:

1. **domain term** — names an idea in the synthetic-data problem space;
2. **candidate concept name** — a hypothesis that a domain idea may deserve an independent concept boundary;
3. **representation term** — names an implementation, storage, framework, runtime, or API representation;
4. **compatibility term** — retained because an external ecosystem or user community commonly uses it.

A word MAY appear in more than one layer, but its meaning MUST be made explicit. Shared spelling does not imply shared semantics.

## Concept-discovery boundary

Phase 001-C may identify that a term appears to carry an independent purpose, state, authority, or lifecycle. Such a signal is recorded as a **concept-candidate signal** only.

Only later concept discovery and review may establish an accepted concept.
