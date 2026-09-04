---
type: Architecture Decision Record
title: ADR-0006 — Typed Canonical Provenance & Derived Historical Projections
status: active
---

# ADR-0006 — Typed Canonical Provenance & Derived Historical Projections

## Decision context

SYNGAN needs efficient historical explanation, lineage-style traversal, comparison, Evidence review, and reproducibility assessment across durable Learning, Generation, Evaluation, Learned State, output, Evidence, Execution, dependency, and revision identities.

A universal metadata/lineage graph that copies all substantive state would simplify some queries but would create a second source of truth, encourage current state to be reconstructed from provenance, and make external lineage systems dangerously authoritative. Conversely, relying only on direct owner repositories without a typed relationship layer would make historical traversal expensive and obscure relationship meaning.

The architecture therefore needs a canonical relationship layer that remains deliberately narrow, plus query-oriented projections that can evolve independently.

## Governing authority

- [Evidence](../concepts/evidence.md)
- [Provenance](../concepts/provenance.md)
- [Reproducibility Contract](../authority/reproducibility-contract.md)
- [Control-Plane Identity, Revision, State, Persistence & Historical Reference Architecture](../architecture/control-plane-identity-revision-state-persistence-historical-reference.md)
- [Execution/Attempt, Checkpoint, Recovery, Fencing, Idempotency & Cancellation Architecture](../architecture/execution-attempt-checkpoint-recovery-fencing-idempotency-cancellation.md)
- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)

## Decision

SYNGAN will persist canonical Provenance as **typed historical relationship assertions over stable references**, while keeping substantive concept/result state in its canonical owner.

Historical navigation/search/adjacency, explain views, comparison views, and reproducibility assessments are derived read/composition layers over those canonical relationships and resource owners.

The architecture therefore separates:

```text
canonical resource state
        +
canonical typed Provenance assertions
        ↓
derived adjacency/search/query projections
        ↓
explain / compare / reproducibility views
```

Derived projections may be eventually consistent and rebuildable. They do not gain canonical mutation authority.

Required Provenance assertions are recorded idempotently and must remain recoverably consistent with the material transition they explain. Provenance correction is append/supersede rather than destructive historical rewrite.

No graph database is mandated. Relational, graph, document, event-oriented, or mixed persistence may comply if typed relationship semantics, stable references, correction, idempotency, and query guarantees are preserved.

## Alternatives considered

### 1. Universal metadata/lineage graph as master state

Rejected because it duplicates concept-owned state, creates competing authority, increases synchronization burden, and violates Provenance's high-fan-in/low-authority-fan-out boundary.

### 2. Reconstruct canonical state from provenance events

Rejected as a universal architecture because Provenance is relationship authority, not the complete event history or payload authority of every concept. Full event sourcing is not required by 004-C.

### 3. No canonical Provenance store; query owners dynamically every time

Rejected because typed historical relationship meaning and correction/idempotency need durable authority, and repeated cross-owner discovery would make historical explanation fragile and expensive.

### 4. External lineage platform as canonical provenance authority

Rejected because external systems observe platform/runtime events under different semantics and may not preserve exact SYNGAN commitment/result identities or relationship types. External lineage remains an integration/projection unless a future explicit authority contract is accepted.

### 5. One denormalized historical table containing copied resource snapshots

Rejected because it creates a shadow metadata warehouse, amplifies migration/staleness problems, and obscures canonical ownership.

### 6. Persist reproducibility as a mutable Boolean/status on every result

Rejected because reproducibility is target- and context-specific, can degrade when dependencies disappear or policy changes, and has multiple accepted equivalence classes.

## Consequences

### Positive

- Provenance remains small, typed, auditable, and semantically meaningful;
- canonical resource ownership stays unambiguous;
- historical query performance can be optimized through rebuildable projections;
- graph technology remains optional rather than architectural destiny;
- external lineage/catalog systems can integrate without becoming semantic authority;
- historical corrections can be retained without rewriting underlying resources;
- reproducibility assessments can change with current availability while historical facts remain immutable;
- query indexes can evolve or be rebuilt without changing domain history.

### Costs

- historical query services must compose several canonical owners rather than read one giant metadata record;
- projection freshness/lag must be represented where relevant;
- required Provenance recording needs explicit idempotency and reconciliation;
- query/index authorization must avoid leaking sensitive identities or relationship existence;
- implementations need stable typed reference contracts across resource owners.

## Compatibility / migration impact

There is no existing implementation to migrate.

Future persistence schemas must avoid treating denormalized search/index copies as canonical state and must reserve stable Provenance assertion identity, relationship type, typed references, qualifiers, correction/supersession status, and originating transition identity.

Historical/reproducibility APIs should be designed so indexes can be rebuilt or replaced without changing resource identities or semantic history.

## Canonical architecture affected

- [Evaluation/Evidence, Provenance, Reproducibility & Historical Query Architecture](../architecture/evaluation-evidence-provenance-reproducibility-historical-query.md)

## Supersession

Supersedes: none.

Superseded by: none.
