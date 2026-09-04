---
type: Terminology Authority
title: Terminology Policy
status: active
---

# Terminology Policy

## Purpose

SYNGAN terminology is part of the design contract. Terms MUST be stable enough for humans, agents, tests, APIs, and architecture documents to refer to the same ideas without semantic drift.

## Rules

1. A durable domain term MUST have one canonical definition.
2. Definitions SHOULD live with the concept or authority that owns the term rather than in a global glossary when ownership is clear.
3. A glossary or terminology index MAY aggregate links, but SHOULD NOT become a second source of truth.
4. Synonyms MAY be recorded for discovery and compatibility, but one preferred term SHOULD be identified.
5. Implementation names MUST NOT redefine domain meaning.
6. Vendor terminology MAY be referenced for compatibility, but MUST NOT be adopted merely because a dependency uses it.
7. New terms SHOULD be introduced only when they distinguish a materially different purpose, state, relationship, guarantee, or responsibility.
8. A change to an established term that changes meaning MUST be treated as a design change, not an editorial cleanup.

## Concept naming

Candidate concept names are hypotheses until the concept boundary and purpose are accepted.

Concept names SHOULD:

- name a stable domain idea rather than a UI screen, class, package, job, or storage representation;
- remain intelligible without knowing the chosen implementation stack;
- avoid embedding one model family when the concept is intended to support many;
- distinguish an enduring capability from an incidental workflow step.

## SYNGAN naming constraint

`SYNGAN` is the project/package brand. The project name MUST NOT be interpreted as making GANs or CTGAN the conceptual boundary of the framework.

CTGAN, GANs, VAEs, diffusion models, statistical generators, and future approaches MAY become synthesis strategies or implementations if later concept and architecture work supports them.

## Provisional terms

Until Phase 001-C and later concept discovery resolve them, terms such as `dataset`, `metadata`, `synthesizer`, `model`, `training`, `generation`, `constraint`, `evaluation`, `privacy`, and `artifact` MUST be treated as provisional domain vocabulary rather than accepted concept names.

## Definition changes

When a term changes materially:

- update its canonical definition;
- identify affected concepts, synchronizations, APIs, architecture, tests, and documentation;
- preserve historical aliases only where they aid migration or comprehension;
- do not leave two active definitions with different meanings.
