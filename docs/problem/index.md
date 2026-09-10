---
type: Problem Knowledge Index
title: SYNGAN Problem Knowledge
status: active
---

# Problem Knowledge

This directory contains canonical knowledge about why SYNGAN exists, who needs it, what outcomes matter, and the scale envelope the design must satisfy.

It describes the problem space and its trace to concept purposes without selecting implementation architecture.

## Canonical documents

- [Problem & Purpose](problem-purpose.md) — motivating problem, current product purpose, scope and non-goals.
- [Actors & Needs](actors.md) — actor roles and needs that motivate functionality.
- [Desired Outcomes](outcomes.md) — sixteen current observable outcomes the design should make possible.
- [Enterprise Scale Envelope](enterprise-scale-envelope.md) — multidimensional scale conditions including topology, sequence and text-bearing structured-data pressures.
- [Concept-Justification Traceability](concept-justification-traceability.md) — current problem/actor/outcome → accepted-concept purpose mapping established by 008-B.

## Current scope clarification

The current structured-data target includes:

```text
single-table generation
time-series generation
multi-table shared-key generation
```

with legitimate composite topology remaining representable.

The supported baseline also includes at least one self-contained source-derived/local synthesis path for free-form/source-language text fields inside structured data without mandatory public pretrained models, hidden first-use downloads, or runtime inference services.

General unstructured/free-standing text generation and arbitrary recursive/cyclic graph synthesis are not implied by those commitments.

## Authority boundary

These documents are authoritative for the problem statements, actors, outcomes, scale conditions, and purpose traceability they own.

They MUST NOT be read as authorization for a particular class hierarchy, model family, algorithm, database, distributed runtime, persistence format, package topology, public API, or implementation.

Accepted concept purpose/state/action authority lives under [`docs/concepts/`](../concepts/index.md). The traceability document explains why those concepts are currently justified; it does not determine Jackson inclusion dependence or require every concept in every reduced application.

Implementation remains downstream of the complete design program under [Design Methodology](../authority/design-methodology.md) and the [Jackson Design Completion & Implementation Hold](../authority/jackson-design-completion-implementation-hold.md).