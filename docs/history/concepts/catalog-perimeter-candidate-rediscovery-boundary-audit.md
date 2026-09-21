---
type: Catalog Design Authority
title: Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit
status: active
---

# Catalog Perimeter Candidate Rediscovery, Missing-Concept & Boundary Audit

## Purpose

Provide the current Phase 008-G authority for the perimeter of SYNGAN's accepted concept catalog.

008-B through 008-F established that the eleven accepted concepts have current purpose justification, state/history, actions/queries, invariants, operational principles, independent boundaries, bounded genericity, familiar-enough names and reuse semantics. 008-G asks the inverse question:

> **What concept, if any, is still missing because an earlier candidate was subordinated, rejected, deferred, externalized or classified as representation — or because later design exposed a candidate that Phase 001 never named?**

The answer is not determined by the existing catalog count. A candidate returns only if current evidence establishes an independently useful Jackson-style concept.

This authority is governed by:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Jackson Methodology Completion Matrix](../authority/jackson-methodology-completion-matrix.md);
- [Current Problem Knowledge](../problem/index.md);
- [Concept-Justification Traceability](../problem/concept-justification-traceability.md);
- [Concept State, Identity, History & Invariant Normalization](state-identity-history-invariant-normalization.md);
- [Concept Action, Query, Preconditions/Postconditions & Lifecycle Normalization](action-query-lifecycle-normalization.md);
- [Operational Principle, Purpose Fulfillment & Counterexample Normalization](operational-principle-purpose-counterexample-normalization.md);
- [Concept Independence, Genericity, Familiarity & Reuse Normalization](independence-genericity-familiarity-reuse-normalization.md);
- historical Phase 001 candidate discovery/disposition records;
- Phase 006 design probes that reopened and re-tested topology, recovery, resource, privacy and governance candidates.

This is concept design only. It does not authorize implementation, architecture revision, API design, schema design, runtime code, privacy mechanisms, schedulers, storage/catalog systems or external governance products.

## Rediscovery rule

008-G deliberately uses a stronger burden than “the idea seems useful.”

A candidate may enter the accepted concept catalog only if it now has all of the following:

1. **distinct product-facing purpose** — a benefit or protection meaningful to a SYNGAN actor, not merely a mechanism needed by implementation;
2. **independent state/history** — state whose meaning is not simply a field, child record, reference or derived view of another concept;
3. **owned actions/queries** — behavior not already naturally owned by an accepted concept or external authority;
4. **operational principle** — an archetypal history that demonstrates the candidate's own purpose;
5. **boundary integrity** — promotion reduces rather than increases ambiguous/shared authority;
6. **appropriate genericity** — the candidate is neither one mechanism instance nor an umbrella over unrelated purposes;
7. **current scope need** — the purpose exists in O1-O16/current product scope rather than only in a hypothetical future product;
8. **synchronization economy** — the independent benefit justifies any new coordination burden introduced by another state owner.

A candidate is **not** promoted merely because:

- architecture has a resource/object/table for it;
- the value needs a stable ID;
- it has a status enum;
- users might see it in a UI;
- it is important for implementation correctness;
- it is a familiar industry noun;
- it can be versioned;
- it appears in provenance;
- it would make the catalog more symmetrical.

## Disposition vocabulary

- **RETAIN SUBORDINATE** — semantically important, but state/actions belong inside an accepted concept.
- **RETAIN CROSS-CUTTING CONTRACT** — constrains multiple concepts but does not have one independent state/action machine.
- **RETAIN REPRESENTATION / INTEGRATION OBLIGATION** — required realization identity or interface, not product functionality.
- **RETAIN SUPPORTING METHOD / OBSERVATION** — useful procedure or derived information serving another concept's purpose.
- **RETAIN EXTERNAL AUTHORITY** — independently purposeful, but outside current SYNGAN product authority.
- **DEFER MECHANISM-SPECIFIC DISCOVERY** — plausible future concept only when a future capability enters scope with independent state/actions.
- **REJECT UMBRELLA / GOD CONCEPT** — familiar aggregation that would erase accepted boundaries.
- **NO STANDALONE CONCEPT** — no current independent concept is justified.

## Current catalog verdict

After rediscovery of the original rejected/deferred candidates, later Phase 006 candidates, and additional missing-candidate probes, **no candidate meets the current promotion burden**.

```text
accepted concepts          11
accepted synchronizations  15
restored concepts           0
newly discovered concepts   0
renamed concepts            0
merged concepts             0
split concepts              0
```

This is a current Phase 008 catalog-perimeter decision, not a claim that SYNGAN can never acquire another concept. New product scope or a later misfit may reopen discovery.

---

# Original Phase 001 candidate rediscovery

## Generation Request

**Current disposition: RETAIN SUBORDINATE TO GENERATION.**

The requested specification is important, but its purpose remains “define this Generation before commitment.” Its editable/withdrawn/validated/committed states are already coherent as Generation's pre-commit lifecycle.

No current requirement establishes reusable request templates, negotiation, approval, delegation or a request lifecycle whose benefit exists apart from one Generation.

Promoting Generation Request would therefore split one actor-requested synthesis outcome into two state owners without independent purpose.

**Promotion trigger:** future product scope in which requests are independently created, exchanged, approved, scheduled/reused or rejected before any Generation exists may require rediscovery.

## Condition

**Current disposition: RETAIN SUBORDINATE TO GENERATION.**

Condition remains semantically distinct from Constraint:

```text
Condition   = what this Generation requests/prefers/requires of its population/result
Constraint  = reusable prescriptive rule governing valid output
```

But current Conditions exist only in the context of a Generation and do not have independent lifecycle/authority.

Reusable cohort/segment/query-definition functionality could create a different future concept, but current O1-O16 does not require such a reusable object.

## Attempt

**Current disposition: RETAIN SUBORDINATE TO EXECUTION.**

Attempt history is essential for failure, retry, recovery and historical explanation. Every Attempt nevertheless exists to realize exactly one Execution and is created/ended under Execution's operational purpose.

The fact that an Attempt may have identity, timing, environment, failure and recovery state does not establish an independent actor purpose. Promoting Attempt would duplicate operational authority and encourage platform-run semantics to leak into concept design.

## Artifact Identity

**Current disposition: RETAIN REPRESENTATION / INTEGRATION OBLIGATION.**

Learned State, Generation output, Evidence, checkpoint/recovery material and other durable objects need stable references appropriate to their owners. That does not create a generic `Artifact` product concept.

A universal Artifact concept would erase differences among semantic result identity, recovery material, external datasets and representation locations. Identity technology remains downstream.

## Reproducibility Contract

**Current disposition: RETAIN CROSS-CUTTING CONTRACT.**

Reproducibility remains a first-class product assurance spanning exact semantic commitments, source/result identity, Strategy/method behavior, dependency/runtime identity, randomness/approximation and Execution/recovery facts.

Its current value is assembled from state owned by several concepts rather than through one independent lifecycle. `Assess reproducibility` is a contextual interpretation/query over those facts, not enough to justify a new canonical state owner.

If future scope introduces independently negotiated or consumable reproducibility commitments with their own lifecycle, rediscovery may be warranted.

## Privacy Objective / Privacy Guarantee

**Current disposition: REJECT GENERIC CANDIDATE; DEFER MECHANISM-SPECIFIC DISCOVERY.**

`Privacy` remains too heterogeneous to form one coherent concept. Disclosure-risk questions, formal mathematical guarantees, confidentiality/access policy and organizational release authority have different purposes, state and actors.

Current empirical disclosure/memorization questions belong to Criterion → Evaluation → Evidence. Synthetic origin and offline operation do not imply privacy.

A future composable differential-privacy capability remains a strong **future mechanism-specific candidate** because reusable privacy-unit/adjacency, allocation, consumption, composition and exhaustion state could outlive one activity. Formal DP is not in the current baseline, so no DP concept is accepted now.

## Dataset Identity

**Current disposition: RETAIN REPRESENTATION / INTEGRATION OBLIGATION.**

Stable source and output identity is necessary for commitment, provenance and reproducibility, but SYNGAN does not own general enterprise dataset cataloging, stewardship, movement or lifecycle.

Source identity is referenced by activities; completed synthetic output identity is part of the Generation result boundary. External catalogs/storage may supply realization identities.

## Relationship

**Current disposition: RETAIN SUBORDINATE DESCRIPTIVE SEMANTICS IN DATA MEANING.**

008-G replays the Phase 006-G result under the now-current O15 topology scope.

Single-table, time-series, multi-table shared-key and composite topology require explicit structural relationship meaning, but the candidate still substantially shares Data Meaning's purpose, authority and lifecycle:

```text
declare descriptive interpretation
review uncertainty/authority
revise/correct
supersede/invalidate
bind exact revision historically
```

Descriptive linkage/order remains Data Meaning. Prescriptive referential/cardinality/temporal validity remains Constraint. Request-specific topology scope/horizon/quantity remains Generation. Strategy owns support/limitations. Evaluation/Evidence owns findings.

No independent Relationship actions remain after those owners are respected, so a standalone Relationship concept would increase synchronization burden without adding purpose.

## Use / Release Decision

**Current disposition: RETAIN EXTERNAL AUTHORITY.**

Use/release governance clearly has an independent organizational purpose, but it is outside the current SYNGAN product boundary. SYNGAN produces Evidence/Provenance and may enforce current technical authorization through downstream security integration; it does not become the organization that approves release/use.

```text
Generation completed != release approved
favorable Evidence    != release approved
technical access      != organizational approval
```

If SYNGAN's product scope later expands into governance decision management, concept discovery must reopen rather than adding `approved` to Generation or Evidence.

## Source Characterization / Profile

**Current disposition: RETAIN SUPPORTING METHOD / OBSERVATION.**

Profiling remains valuable for Data Meaning inference, Strategy/Learning preparation and Evaluation. Its observations must be attributable when materially relied upon.

But the profile has no current independent purpose beyond serving those activities. A persisted profile or summary does not become a concept because it is reusable or expensive to compute.

---

# Later Phase 006 candidate rediscovery

## ControlPlaneIncarnation / AuthorityEpoch

**Current disposition: RETAIN REPRESENTATION / RECOVERY MECHANISM.**

A fresh non-regressing authority generation may be essential to prevent stale writers after regressive restore. Its purpose is enforcement of current authority continuity, not a user/product purpose independent of Execution/security/deployment.

The cross-cutting Operational Authority Continuity contract remains current; no concept is promoted.

## Recovery / Disaster Recovery

**Current disposition: RETAIN EXECUTION-OWNED / DEPLOYMENT BEHAVIOR.**

Recovery is meaningful, but its domain behavior is continuation/reconciliation of existing Execution and result-owner semantics. Backup/restore/quarantine/fencing mechanisms are deployment/architecture concerns.

A generic Recovery concept would create a second owner for Execution's retry/reconcile lifecycle.

## Historical Fork / Reconciliation

**Current disposition: NO STANDALONE CONCEPT.**

Divergence after regressive restore is a condition to classify and reconcile. Known/unknown/adoptable/stale facts remain owned by the relevant concepts plus Provenance/history. There is no separately valuable `Fork` lifecycle.

## Resource / Capacity

**Current disposition: NO STANDALONE DOMAIN CONCEPT.**

Strategy owns reusable requirements/limitations. Execution owns realized operational resource facts. Deployment/admission owns current capacity decisions.

Resource state becomes a concept only if SYNGAN acquires a product purpose to allocate/trade/govern resources independently, which current O1-O16 does not establish.

## Admission / Queue / Backpressure

**Current disposition: RETAIN OPERATIONAL / DEPLOYMENT POLICY.**

These determine when compatible work may proceed. They must not silently alter committed semantics, but they do not own synthesis-domain meaning.

Queue identities/statuses or admission decisions are not concept proof by themselves.

## Approximation

**Current disposition: RETAIN OWNER-SPECIFIC SEMANTICS.**

Approximation has different meanings depending on its owner:

- Learning — source sampling/approximation affecting derivation;
- Generation — allowed tolerance/best-effort completion semantics;
- Evaluation — sampling/sketch/bounded/approximate method and coverage;
- Evidence — resulting claim-strength limitation.

A generic Approximation concept would falsely unify different purposes and authorities.

## Degraded Mode

**Current disposition: REJECT GENERIC CANDIDATE.**

`degraded=true` would hide materially different cases: projection outage, telemetry loss, source/reference unavailability, control persistence failure, dependency loss, storage failure, worker loss or authorization uncertainty.

Degradation remains capability-specific state interpreted by the owning concept/operational boundary.

## Cost / Budget / Quota

**Current disposition: RETAIN EXTERNAL/DEPLOYMENT POLICY FOR CURRENT SCOPE.**

Costs, quotas and capacity budgets affect operation but do not currently have a distinct synthetic-data product lifecycle. A future product that explicitly manages spend/budget allocation could justify rediscovery.

## Disclosure Risk / Memorization

**Current disposition: RETAIN CRITERION / EVALUATION / EVIDENCE SEMANTICS.**

Threat model, subject, method, scope, coverage, uncertainty and result fit the existing evaluation chain. Different disclosure-risk methods intentionally do not collapse into one global score/state.

## Redaction / Disclosure Decision

**Current disposition: RETAIN SECURITY / VIEW SEMANTICS.**

Redaction/withholding changes what a current actor may see; it does not mutate Evidence or Provenance history. Organizational release/use authority remains external.

## TimeSeries / Series / Sequence / Table / DataTopologyMode / GenerationMode

**Current disposition: NO STANDALONE CONCEPT.**

These remain topology vocabulary or interface conveniences. Current topology semantics distribute coherently across Data Meaning, Constraint, Generation, Strategy and Evaluation/Evidence.

A mode selector may choose a workflow preset but cannot replace the actual semantic structure.

---

# Post-Phase-001 missing-candidate probes

008-G also searches beyond candidates explicitly named in earlier phases.

## Synthetic Output / Output

**Current disposition: RETAIN AS GENERATION-OWNED RESULT, NOT A STANDALONE CONCEPT.**

This is the strongest newly explicit missing-candidate challenge.

A completed synthetic output can outlive Generation, be referenced by Evaluation/Provenance and be consumed externally. That resembles Learned State or Evidence superficially.

However, current SYNGAN functionality gives the logical output no independent state-changing lifecycle beyond the Generation result boundary. Generation owns:

- the requested result semantics;
- candidate versus completed status;
- one authoritative logical output association;
- failure/cancellation rules preventing partial material from masquerading as completion.

Availability, location, retention, export permission and storage lifecycle are representation/security/integration concerns. Evaluation observes the output but does not mutate it. External consumption does not create SYNGAN-owned output behavior.

Promoting Output now would therefore split Generation's result state without independent actions. If future SYNGAN scope adds output publication, versioning, retirement, transformation, release governance or independent lifecycle management, `Output` must be rediscovered.

## Source / Source Dataset

**Current disposition: RETAIN EXTERNAL REFERENCED SUBJECT, NOT A STANDALONE CONCEPT.**

Learning/Evaluation may bind exact source state, and Data Meaning may describe it, but SYNGAN does not own source ingestion/catalog/stewardship/lifecycle as an independent product function. Stable references are an integration obligation.

## Dependency / External Artifact / Knowledge Dependency

**Current disposition: RETAIN STRATEGY DECLARATION + EXECUTION/SECURITY RESOLUTION.**

Dependencies matter greatly for offline/no-egress, reproducibility, trust and runtime closure. Strategy owns reusable dependency requirements/limitations; Execution/runtime realizes exact availability; Provenance records material use.

A dependency object, manifest entry or artifact resolver is architecture. No current actor purpose requires SYNGAN to manage generic dependency lifecycle as a domain concept.

## Authorization / Capability / Permission

**Current disposition: RETAIN SECURITY AUTHORITY OUTSIDE THE SYNTHETIC-DATA CONCEPT CATALOG.**

Current permission is necessary for protected actions, especially after recovery or when viewing/exporting sensitive Evidence/history. But authorization purpose, policy sources, credentials and capability grants are security/platform concerns rather than synthetic-data functionality.

Security may synchronize with concept actions at realization/mapping boundaries without becoming a new domain concept. Organizational Use/Release Decision remains separately external.

## Secret / Credential

**Current disposition: RETAIN SECURITY REPRESENTATION / EXTERNAL AUTHORITY.**

Secrets/credentials enable authorized dependency/platform actions and must never become canonical semantic state merely because an Execution uses them.

## Platform Capability / Compatibility

**Current disposition: RETAIN STRATEGY/EXECUTION CONTEXT + ARCHITECTURE MAPPING.**

Platform facts may affect Strategy compatibility and Execution readiness. A provider capability descriptor is not independent product functionality.

## Completion Basis / Promotion / Seal / Candidate

**Current disposition: RETAIN GENERATION/EVALUATION RESULT-ESTABLISHMENT SEMANTICS + ARCHITECTURE MECHANISM.**

The distinction between candidate material and semantic completion is first-class, but `CompletionBasis`, `Seal`, `Promotion` or `Candidate` does not own an independent purpose. Generation/Evaluation/result owners retain authority; manifest/transaction/seal mechanisms are downstream.

## Checkpoint

**Current disposition: RETAIN EXECUTION RECOVERY MATERIAL.**

Checkpoint durability is deliberately not Learned State and not a completed domain result. It exists to continue compatible operational realization. No independent concept is justified.

## Claim / Finding

**Current disposition: RETAIN EVIDENCE STATE.**

Claim strength, finding, uncertainty and limitation are core Evidence semantics. A separate Claim concept would duplicate Evidence unless a future product introduces independently authored/contested claims beyond Evaluation findings.

## Report / View / Export

**Current disposition: RETAIN CONCEPT MAPPING / SECURITY VIEW, NOT CONCEPTS.**

Human/programmatic reports, projections and exports expose concept state. Phase 010 will map them. Their existence does not create domain concepts.

## Text / Tokenizer / Vocabulary / Language Model

**Current disposition: NO STANDALONE CORE CONCEPT.**

Text-bearing structured fields are current O16 scope, but:

- text semantics/roles belong to Data Meaning;
- synthesis capability/dependencies belong to Strategy;
- source-derived reusable state may belong to Learning/Learned State;
- Generation owns requested output;
- Evaluation/Evidence owns fidelity/disclosure findings;
- tokenizer/model artifacts are Strategy/runtime representation/dependencies.

No current text-specific purpose requires a new concept.

## Policy / Quality / Validation / Model / Metadata / Run / Synthesizer / Artifact

**Current disposition: REJECT UMBRELLA / GOD CONCEPTS.**

These remain useful conversational or implementation terms only when their narrower meaning is explicit. They must not replace accepted boundaries:

```text
Metadata     != Data Meaning + Constraint + Provenance + identity
Model        != Strategy + Learned State + artifact representation
Run          != Learning/Generation/Evaluation + Execution + Attempt
Quality      != Criterion + Evaluation + Evidence + approval
Validation   != Constraint + Evaluation + completion
Synthesizer  != Strategy + Learning + Learned State + Generation
Artifact     != every durable result/reference/recovery object
Policy       != Constraint + security + governance + resource rules
```

---

# Missing-purpose sweep against O1-O16

008-G replays all current outcomes against the catalog perimeter after the candidate review.

No outcome requires an unowned independent concept:

- large-data viability and resource responsibility are supported by Strategy/Execution plus downstream architecture;
- Spark continuity/portability remain mapping/architecture obligations around existing semantics;
- data meaning/topology/text semantics remain Data Meaning-led with Strategy/Generation/Evaluation collaborators;
- multiple synthesis approaches remain Strategy plus optional Learning/Learned State and Generation;
- evidence fitness remains Criterion → Evaluation → Evidence;
- privacy non-overstatement remains evaluation/formal-guarantee/external-governance separation, not a generic Privacy concept;
- reproducibility/attribution remains cross-cutting exact commitments plus Provenance;
- long-running recovery/observability remains Execution plus domain activity boundaries;
- governance remains Evidence/Provenance and external release authority;
- extension remains Strategy plus preserved concept/synchronization contracts.

No actor need in the current product requires an additional standalone owner either.

## Hidden-concept test across current synchronizations

008-D already showed SYNC-01 through SYNC-15 can be expressed as coordination of accepted owned actions/queries.

008-G reinterprets that result as catalog-perimeter evidence:

- no synchronization requires an unnamed state owner;
- no synchronization's pre/postconditions depend on a candidate concept being silently implemented;
- topology, recovery, privacy, resource and dependency probes do not require `SYNC-16` under the current catalog.

Phase 009 must still perform the final composition/synchronization/inclusion-dependence closure; 008-G does not pre-empt it.

## Representation-leakage audit

The following remain representation or architecture structures rather than concepts even when durable/typed/versioned:

```text
ResourceRef / HistoricalRef
stable IDs / revisions / hashes
manifests / candidates / seals
ImplementationBindingRef / RuntimeSpiVersion
AttemptEpoch / WriterFence / authority generation
dependency-resolution records
AuthorizationDecision / CapabilityGrant / SecretRef
PlatformCapabilityDescriptor
TelemetryContext / SupportClaim
storage locations / partitions / tables
checkpoint format
report / projection / cache
```

If later design discovers actor-purposeful state/actions around one of these, the correct response is to reopen concept discovery, not to promote it silently through architecture.

## Current catalog completeness verdict

For **current O1-O16 scope**, 008-G finds no missing standalone concept and no incorrectly excluded candidate requiring restoration.

The accepted eleven remain the smallest currently justified set that preserves the intended distinctions without turning representation, cross-cutting policy or external authority into concepts.

This is intentionally qualified:

- future formal composable DP may require mechanism-specific concept discovery;
- future governance/release-management scope may require decision concepts;
- future reusable request/cohort/output-publication functionality may require rediscovery;
- future arbitrary graph/recursive topology may expose a boundary beyond current Data Meaning-owned structural semantics;
- future resource/economic management may create independent concepts if SYNGAN's product purpose expands.

Those are explicit reopen triggers, not current catalog members.

## Methodology disposition

008-G closes for the current individual-concept stage:

- **B1 — divergent candidate concept discovery** → **CURRENTLY CLOSED**;
- **B2 — candidate reduction/merger/subordination/defer/reject disposition** → **CURRENTLY CLOSED**;
- **B5 — missing-concept/god-concept/representation-leakage audit** → **CURRENTLY CLOSED**;
- **C8 — boundaries/non-responsibilities independent of representation** → **CURRENTLY CLOSED**, completing the accepted-concept and catalog-perimeter replay begun in 008-F.

008-G establishes **current catalog completeness evidence**, but Phase 008 does not close until 008-H consolidates all individual-concept obligations and makes the explicit handoff decision.

008-G does not close:

- Jackson inclusion dependence/application family — Phase 009;
- final composition/synchronization/synergy/integrity — Phase 009/011;
- concept mapping — Phase 010;
- final post-mapping design-quality/misfit — Phase 011;
- Jackson concept-design completion — Phase 012;
- architecture reconciliation — Phase 013;
- implementation readiness — Phase 014.

## Implementation hold

No candidate disposition in this document authorizes implementation of the candidate, its realization, or a future trigger.

In particular, the future-DP discovery trigger is **not** permission to add DP parameters/accounting, and the Output/Source/Dependency/Authorization dispositions are **not** architecture decisions.

Until Phase 014 positively passes:

```text
IMPLEMENTATION READINESS   NOT READY
IMPLEMENTATION START       NOT STARTED
IMPLEMENTATION NEXT        NOT YET
```

## 008-G exit state

```text
CATALOG-PERIMETER REDISCOVERY            PASS
ORIGINAL REJECTED/DEFERRED CANDIDATES     REPLAYED
LATER 006 CANDIDATES                      REPLAYED
NEW MISSING-CANDIDATE PROBES              REPLAYED
MISSING CURRENT CONCEPT                   NONE FOUND
RESTORED / NEW CONCEPTS                   0
ACCEPTED CONCEPTS                         11
ACCEPTED SYNCHRONIZATIONS                 15
B1 CANDIDATE DISCOVERY                    CURRENTLY CLOSED
B2 CANDIDATE DISPOSITION                  CURRENTLY CLOSED
B5 MISSING/GOD/REPRESENTATION AUDIT       CURRENTLY CLOSED
C8 BOUNDARY/NON-RESPONSIBILITY            CURRENTLY CLOSED
INDIVIDUAL CONCEPT DESIGN                 AWAITS 008-H CONSOLIDATION
JACKSON CONCEPT DESIGN                    NOT COMPLETE
IMPLEMENTATION READINESS                  NOT READY
IMPLEMENTATION START                      NOT STARTED
IMPLEMENTATION NEXT                       NOT YET
```

The next eligible subgroup is **008-H — Phase 008 Consolidation, Individual-Concept Completeness Decision & Phase 009 Handoff**.