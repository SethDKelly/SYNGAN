---
type: Provenance Authority
title: Source and Provenance Policy
status: active
---

# Source and Provenance Policy

## Purpose

SYNGAN design decisions should remain explainable: readers must be able to distinguish external facts, local requirements, hypotheses, decisions, and implementation evidence.

## Source classes

Use the following source classes when provenance matters:

- **Project requirement** — an explicit SYNGAN goal or constraint accepted by the project.
- **Method authority** — Daniel Jackson concept-design material or another explicitly adopted methodology source.
- **Specification authority** — normative external specifications such as OKF.
- **Platform authority** — official documentation for Spark, PySpark, PyTorch, Python, storage systems, or execution environments.
- **Research evidence** — peer-reviewed papers, preprints, benchmarks, or other technical research.
- **Comparative implementation** — existing products/libraries such as SDV used for comparison or compatibility analysis.
- **Project decision** — a conclusion accepted within SYNGAN after analysis.
- **Hypothesis** — an unverified or provisional proposition requiring later resolution.

## Evidence discipline

External claims that materially constrain the design SHOULD cite an authoritative source.

Preference order is generally:

1. normative specification or primary source;
2. official project/platform documentation;
3. original research;
4. high-quality secondary material;
5. informal commentary.

Comparative implementations are evidence of one possible design, not authority over SYNGAN's concept model.

## Provenance versus duplication

A citation does not make copied text canonical. External sources support local reasoning; local rules MUST be stated in a local canonical authority when they become SYNGAN requirements.

Where a local rule is derived from an external source, record both:

- the local normative conclusion; and
- the external source or rationale that supports it.

## Time sensitivity

Version-sensitive facts MUST identify the relevant version or retrieval context when changes could affect the decision. This is particularly important for Spark, PyTorch, Python, OKF, SDV, platform integrations, and model/runtime compatibility.

## Uncertainty

Unknowns MUST remain explicit. Documentation SHOULD distinguish:

- observed fact;
- external claim;
- inference;
- architectural hypothesis;
- accepted project decision.

Absence of evidence MUST NOT be silently converted into a design guarantee.

## References

External references MAY be collected under `docs/references/` when a durable project note is useful. Reference notes SHOULD summarize why the source matters and link back to the canonical decision or concept that uses it rather than duplicating the source.
