---
type: Discovery Knowledge Index
title: SYNGAN Concept Discovery
status: active
---

# Concept Discovery

This directory contains provisional design knowledge produced while discovering SYNGAN concepts.

Discovery artifacts are authoritative for the hypotheses they record, but **they are not accepted concept specifications**. Candidate concepts may be split, merged, renamed, rejected, deferred, or reframed by later Phase 001 work.

## Current artifacts

- [Candidate Concept Catalog](candidate-concept-catalog.md) — purpose-driven concept candidates and current confidence.
- [Boundary Hypotheses](boundary-hypotheses.md) — proposed separations, mergers to resist, and unresolved alternatives.
- [Synchronization Hypotheses](synchronization-hypotheses.md) — coordination needs implied by the candidate set.
- [Purpose / Outcome Coverage](purpose-outcome-coverage.md) — traceability from 001-B needs and outcomes into discovery candidates.

## Authority boundary

Accepted concept specifications will eventually live under `docs/concepts/` after Phase 001 has tested candidate independence, genericity, operational principles, and composition.

No class, package, Spark job, PyTorch object, file format, or API shape may be inferred directly from the candidates in this directory.

## Discovery discipline

A candidate is retained because it appears to have a distinct purpose, meaningful state/lifecycle, independent actor need, or synchronization responsibility—not because a glossary term, external library, or implementation framework exposes an object with the same name.

See [Concept Design Methodology](../authority/design-methodology.md) and [Domain Terminology](../terminology/index.md).
