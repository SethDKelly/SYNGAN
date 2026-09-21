---
type: Cross-Concept Design Authority
title: Concept State, Identity, History & Invariant Normalization
status: active
---

# Concept State, Identity, History & Invariant Normalization

## Purpose

Provide the current Phase 008-C normalization of conceptual state, logical identity, history, lifecycle distinctions, uncertainty and invariants across SYNGAN's eleven accepted concepts.

This authority is conceptual. It does not define classes, tables, schemas, IDs, manifests, event stores, databases, APIs, persistence mechanisms, Spark objects, package boundaries or runtime protocols.

It is governed by:

- [Concept Design Methodology](../authority/design-methodology.md);
- [Jackson Methodology Completion Matrix](../authority/jackson-methodology-completion-matrix.md);
- [Problem & Purpose](../problem/problem-purpose.md);
- [Concept-Justification Traceability](../problem/concept-justification-traceability.md);
- the individual accepted concept specifications in this directory.

Where older concept wording still describes relational/time-series support as merely future, the current Phase 008-B problem/outcome authority and this normalization supersede that stale scope qualifier. This does not select a physical topology representation.

## 008-C scope boundary

008-C answers:

- what kind of conceptual state each concept owns;
- what constitutes its logical identity or historical distinguishability;
- what may change versus what must remain historically fixed;
- which lifecycle/status distinctions are conceptually meaningful;
- how correction, supersession, invalidation, uncertainty and history behave;
- which cross-concept invariants must hold independent of representation.

008-C does **not** finish:

- the complete action/query catalog;
- precise action preconditions/effects/postconditions;
- operational-principle revalidation;
- independence/genericity/familiarity;
- rejected/deferred candidate rediscovery;
- Jackson inclusion dependence/application families;
- synchronizations or concept mapping;
- representation architecture or implementation.

Those remain assigned to later groups/phases.

## Shared normalization rules

### N1 — Logical identity is conceptual distinguishability, not an ID technology

When a concept requires stable identity, the requirement means actors and other concepts must be able to distinguish the same logical subject/history from another one where that distinction affects behavior or interpretation.

No UUID, database key, URI, hash, catalog handle, object identity or serialization format is implied.

### N2 — Identity, revision, occurrence, result and current-use status are not synonyms

The concept model distinguishes as applicable:

- **lineage identity** — a reusable authority that can have materially different revisions;
- **revision** — a historically distinguishable semantic version of that authority;
- **occurrence identity** — one committed domain activity or operational realization;
- **result identity** — one established reusable/finding/output result;
- **current-use status** — whether an already established thing is currently eligible/relevant for future use.

Concepts use only the distinctions their purpose requires. 008-C does not impose revisions on immutable result concepts merely for uniformity.

### N3 — Material historical meaning is non-destructive

Once committed/established state has participated materially in historical work, later correction, supersession, restriction, retirement or invalidation must not make the historical record pretend a different state was originally used.

A later state may affect future eligibility or current interpretation without rewriting the earlier fact.

### N4 — Current eligibility is separate from historical validity

`effective`, `usable`, `restricted`, `retired`, `superseded`, `stale`, `inapplicable` and `invalidated` are future/current-reliance distinctions where applicable. They do not erase historical identity or automatically declare every past use invalid.

The exact vocabulary is concept-specific.

### N5 — Unknown/indeterminate state must remain representable where false certainty would change behavior

When the design cannot safely establish a material fact—such as semantic interpretation, compatibility, evaluation result, operational outcome or historical continuity—it must preserve an explicit unresolved/unknown/indeterminate condition rather than silently choose the favorable/default interpretation.

Not every concept needs a universal `unknown` lifecycle state. The requirement applies only where uncertainty is semantically material to that concept.

### N6 — Contextual judgments do not become global mutable truth on reusable authorities

Examples include:

- Strategy compatibility with one activity;
- Constraint applicability/satisfiability for one activity;
- Learned State compatibility with one Generation;
- Evidence applicability to a new decision context.

The reusable concept owns intrinsic state; the consuming context owns the contextual assessment unless the concept's own purpose explicitly includes current-use applicability.

### N7 — Concept state is not bulk payload by default

Canonical concept state should scale with semantic/control complexity rather than source rows, generated rows, every Spark task, every metric point or full payload content unless a concept purpose genuinely requires otherwise.

Large/distributed subjects may be referenced without being copied into concept state.

### N8 — Physical persistence does not create semantic state

A file, checkpoint, table, object, platform run, manifest, cache or log does not become Learned State, completed Generation output, Evidence, Execution completion or Provenance truth merely because it exists durably.

The owning concept's semantic establishment/completion rules still apply.

### N9 — Cross-concept references do not transfer ownership

A concept may bind/reference another concept's exact historical state. It must not copy that state and then become a second authority for it.

### N10 — Regressive representation recovery cannot rewrite conceptual history

A restored older persistence projection may represent historical knowledge, but it cannot make superseded/cancelled/invalidated conceptual state current merely by being restored.

If current truth cannot be established after a regressive recovery, the relevant concept/history remains explicitly unresolved until sufficient evidence supports reconciliation. The concrete fencing/recovery mechanism is downstream architecture.

### N11 — Current topology scope is structural, not a new universal lifecycle

Data Meaning, Constraint, Strategy, Generation, Evaluation and Evidence must be able to describe/operate over the current structured-data capability target:

```text
single-table
time-series
multi-table shared-key
legitimate composite structured topology
```

No standalone `Table`, `Series`, `TimeSeries`, `Relationship`, `Dataset` or `DataTopology` concept is introduced by this state requirement.

### N12 — Text-bearing structured data does not create a separate state model

Free-form/source-language text inside structured data is represented through ordinary Data Meaning plus Strategy/Learning/Learned State/Generation/Evaluation/Evidence state where applicable. It does not require a `Text`, `Tokenizer` or `LanguageModel` concept.

## Concept state-shape families

The eleven concepts intentionally do not share one generic lifecycle.

### Family A — reusable revisioned authorities

- Data Meaning
- Synthesis Strategy
- Constraint
- Evaluation Criterion

These concepts define reusable semantic authority that may change materially over time. They therefore need stable lineage/revision distinguishability and historical binding.

### Family B — committed domain activities

- Learning
- Generation
- Evaluation

These concepts describe one logical activity occurrence with editable/proposed state before commitment, an immutable historical commitment after commitment, a semantic lifecycle, and a terminal/nonterminal result distinction.

### Family C — durable established results

- Learned State
- Evidence

These concepts represent a result/finding established by another concept. Their established semantic content is historically immutable. Later future-use/applicability status can change without revising what the original result/finding was.

Generation's completed synthetic output is Generation-owned result state under the current catalog rather than a separate accepted `Dataset`/`Artifact` concept.

### Family D — operational realization

- Execution

Execution has one stable logical realization identity and subordinate Attempt history. Its state includes operational progress, recovery/cancellation and explicit unknown/indeterminate conditions without becoming the semantic success owner of Learning, Generation or Evaluation.

### Family E — typed historical relationships

- Provenance

Provenance is append-preserving relationship/history authority. Individual provenance assertions can be corrected/superseded for current reliance, but correction preserves auditability and does not rewrite the referenced concept's canonical state.

## Normalized concept-by-concept state model

| Concept | Conceptual identity/state unit | Historically fixed material state | Current/evolving state | Explicit uncertainty/correction requirement | 008-C verdict |
|---|---|---|---|---|---|
| **Data Meaning** | Logical semantic scope/lineage with distinguishable revisions containing semantic assertions | Meaning of any revision bound by committed work; assertion origin/authority and declared-vs-inferred character | Draft/effective/superseded/invalidated eligibility; unresolved/conflicting assertions; later revisions | Unknown/unresolved/conflicting meaning must remain explicit; correction creates a later revision | **NORMALIZED** |
| **Synthesis Strategy** | Reusable Strategy lineage/revision plus historically distinguishable material configuration | Bound synthesis semantics, capabilities, requirements, limitations, learning/generation mode, dependency/network and material configuration | Draft/effective/superseded/retired/invalidated selection eligibility; new revisions/configurations | Contextual compatibility may be compatible/limited/incompatible/indeterminate but belongs to the activity | **NORMALIZED** |
| **Learning** | One logical Learning occurrence with one committed semantic specification | Source identity, Meaning/Strategy/Constraint bindings, learning scope, material approximation/sampling/dependency/reproducibility commitments | Proposed/validated/committed/active/completed/failed/cancelled semantic lifecycle | Failed Attempt does not imply failed Learning; unresolved prerequisites cannot become commitment success | **NORMALIZED** |
| **Learned State** | One established logical reusable result identity produced by successful Learning | Learned semantic content/identity and producing Learning/Strategy/source context | Usable/restricted/retired/invalidated future-use status | Later incompatibility or discovered defect changes future reliance, not producing history; material adaptation creates a new result | **NORMALIZED** |
| **Generation** | One logical Generation occurrence with one committed requested outcome and zero/one successful logical output result | Committed scope/quantity/Conditions/Meaning/Strategy/Learned-State-or-direct-input/Constraint/dependency/reproducibility semantics; completed result identity | Draft/validated/committed/fulfilling/awaiting-validation/completed/completed-with-limitations/failed/cancelled | Partial/candidate output remains non-final; indeterminate mandatory fulfillment cannot become completed | **NORMALIZED** |
| **Constraint** | Logical prescriptive rule lineage with distinguishable revisions | Meaning, scope, authority and requirement semantics of bound rule revision | Draft/effective/superseded/retired/invalidated revision eligibility; later revisions | Applicability/satisfiability may be indeterminate and belongs contextually to consuming activity; correction creates new revision | **NORMALIZED** |
| **Evaluation Criterion** | Reusable evaluative-question lineage with distinguishable revisions | Bound question, scope, reference context and answer-sufficiency semantics | Draft/effective/superseded/retired/invalidated selection eligibility; later revisions | Ambiguous/insufficient question cannot be repaired by available metric; later revision does not reinterpret historical Evidence | **NORMALIZED** |
| **Evaluation** | One logical Evaluation occurrence with one committed examination specification | Criterion/input/reference/method/scope/coverage/approximation/uncertainty/dependency commitments | Draft/validated/committed/evaluating/completed/completed-with-limitations/failed/cancelled | Negative or inconclusive finding may come from successful Evaluation; method insufficiency must remain distinct from subject failure | **NORMALIZED** |
| **Evidence** | One independently interpretable established finding identity | Observed finding plus exact Criterion, subject, method, scope, claim strength, uncertainty and limitation context | Applicable/current, superseded, stale/obsolete, inapplicable or invalidated future-reliance status | Finding is not rewritten when applicability changes; invalidation records a defect without fabricating a different historical result | **NORMALIZED** |
| **Execution** | One stable logical operational realization identity with subordinate distinguishable Attempts | Associated committed domain activity; Attempt history; material operational outcomes/recovery facts | Prepared/queued/running/recovery-pending/cancellation-requested/completed/failed/cancelled/indeterminate current lifecycle | Unknown/lost state remains explicit; historical/restored Attempt state cannot by itself become current authority; retry preserves parent semantics | **NORMALIZED** |
| **Provenance** | Distinguishable typed historical relationship assertions among stable references | What relationship was asserted, between which historical states, with material type/context | Current applicability/validity of an assertion may be corrected/superseded while original assertion remains auditable | Missing history remains unknown where it cannot be reconstructed; correction does not rewrite another concept's authority | **NORMALIZED** |

## Identity normalization by concept

### Data Meaning

The durable conceptual identity is the **semantic lineage/scope plus exact revision used**. A physical schema, field ID, table name or catalog object may help identify the subject later but is not itself Data Meaning identity.

Structural relationship and temporal/order semantics required by O15 are current Data Meaning state where descriptive. They are no longer merely hypothetical future relational state.

### Synthesis Strategy

Strategy identity distinguishes a reusable synthesis behavior lineage from materially different revisions/configurations. A plugin/class/package/model endpoint is implementation identity, not Strategy identity.

Changing a material capability, requirement, limitation, learning requirement, generation behavior, topology/text capability, external-knowledge dependency or reproducibility behavior must remain historically distinguishable.

### Learning

A Learning occurrence is one committed derivation intent, not one training process or Attempt. Its occurrence identity survives valid retry/resume of the same committed semantics.

A materially changed source, meaning, Strategy, Constraint handling or learning semantics is a new distinguishable Learning rather than mutation of the old occurrence.

### Learned State

Learned State is not a revisioned mutable model object. Once established, its learned semantic content is immutable for historical purposes.

Restriction, retirement and invalidation are future-use states. A material transformation/adaptation that changes learned behavior produces a new distinguishable Learned State through an explicitly owned derivation rather than silently revising the old one.

### Generation

Generation identity belongs to the requested/committed synthesis outcome, not a Spark job or destination table. A valid operational retry remains the same Generation if its committed semantics remain unchanged.

The completed logical output is Generation-owned result state. Many physical components may realize one result. Candidate/partial material is not promoted to completed result by existence alone.

### Constraint

Constraint identity is the rule lineage plus exact revision. Similar predicate syntax does not make two semantically different requirements the same Constraint, and shared expression machinery does not merge Constraint with Generation Condition.

### Evaluation Criterion

Criterion identity follows the evaluative question. A material change to question, scope, reference, tolerance or answer-sufficiency semantics is a new revision even if the same metric could be used.

### Evaluation

Evaluation identity follows one committed examination, not one metric invocation or distributed job. Operational retry under unchanged examination semantics remains the same Evaluation.

Changing the Criterion, subject/reference, method, scope/coverage, approximation or uncertainty semantics materially creates a new distinguishable Evaluation.

### Evidence

Evidence identity denotes one established finding. The finding's historical content is immutable after valid establishment.

Current applicability may change because the decision context, Criterion, threat model, subject or newer Evidence changes. Those changes qualify future reliance; they do not edit the original observation.

008-C therefore normalizes older shorthand such as `Evidence identity/version` to mean stable finding identity plus any explicit history/applicability assertion—not arbitrary in-place revision of the finding.

### Execution

Execution identity survives worker/process/job replacement and valid Attempts under the same committed parent activity.

Attempt identity is subordinate history. Attempt currentness/authority is not historical existence. A restored old projection cannot make a superseded Attempt conceptually current merely because its old state reappears.

### Provenance

Provenance does not require a single global graph revision. Its fundamental state unit is a typed historical assertion with stable distinguishability and references.

If an assertion is later found wrong or incomplete, correction is represented through auditable supersession/invalidation/correction history rather than destructive replacement.

## History normalization

### Revisioned-authority history

For Data Meaning, Strategy, Constraint and Criterion:

```text
lineage
  ├─ revision A — historical/bound where used
  └─ revision B — later effective/current where applicable
```

Revision B does not rewrite work bound to A.

### Activity history

For Learning, Generation and Evaluation:

```text
proposed → validated → committed → realization/result resolution → terminal/nonterminal semantic state
```

The exact action transition rules remain 008-D work. 008-C establishes that commitment freezes material semantic context and that operational retries do not rewrite it.

### Durable-result history

For Learned State and Evidence:

```text
established immutable semantic result/finding
        +
future-use/applicability status may later change
```

Changing current reliance does not create a different historical result unless a genuinely new result/finding is established.

### Execution history

Execution preserves one logical operational history containing distinguishable Attempts and enough current lifecycle state to avoid confusing past success/failure/currentness.

Unknown operational history or continuity must remain explicit rather than inferred from a restored snapshot or surviving bytes.

### Provenance history

Provenance history is append-preserving. The system may discover that a relationship assertion is wrong or missing, but any accepted correction/reconstruction must itself remain historically explainable.

## Cross-concept invariant set after 008-C

The following invariant spine is current conceptual authority:

1. A material historical binding must continue to identify the exact conceptual state originally used.
2. Later revisions/status changes must not retroactively rewrite committed Learning, Generation, Evaluation, Learned State, Evidence, Execution or Provenance history.
3. Descriptive meaning, prescriptive rule, requested outcome, evaluative question, examination, finding, operational realization and historical relationship remain separately owned state.
4. Contextual compatibility/applicability/sufficiency results must not become global mutable truth on reusable concepts unless explicitly owned by that concept.
5. Unknown/indeterminate material state must remain explicit where choosing a default would strengthen a claim, authorize progress or rewrite history.
6. Physical existence/durability is insufficient to establish a semantic result or lifecycle transition.
7. Operational completion is insufficient to establish Learning/Generation/Evaluation semantic completion.
8. Retry/resume may preserve one activity/Execution identity only while the committed semantic context remains unchanged.
9. Candidate, partial, checkpoint and recovery material must remain distinguishable from established Learned State, completed Generation output and Evidence.
10. Established Learned State and Evidence content is historically immutable; future-use/applicability status may change separately.
11. Provenance references canonical states and must not become their duplicate current-state owner.
12. Regressive persistence recovery cannot resurrect superseded conceptual authority or erase later possible history.
13. Canonical concept state must not require whole source/output/task payloads in driver-local memory as a semantic prerequisite for enterprise-scale use.
14. Current topology breadth and text-bearing structured-data scope must be expressible through the existing concept state model without fabricating new implementation-shaped concepts.
15. No concept's state model may make one algorithm, platform, runtime, storage mechanism, API, schema or object model universal SYNGAN semantics.

## Topology and text state closure

008-C confirms the existing concept-state model can represent O15/O16 without catalog expansion at this stage:

- **Data Meaning** owns field/group/record/relationship/temporal/text semantic interpretation;
- **Constraint** owns prescriptive row/cross-field/cross-record/temporal/cross-scope rules;
- **Strategy** owns topology/text capability, requirements and limitations;
- **Learning/Learned State** own reusable source-derived state where required;
- **Generation** owns requested logical output scope/topology/conditions and completed-result state;
- **Criterion/Evaluation/Evidence** own topology/text-related evaluative questions, examinations and findings;
- **Execution** owns operational realization independent of topology payload size;
- **Provenance** relates exact states/results without copying topology payloads.

This is a state-model sufficiency finding only. 008-G still reopens rejected/deferred candidate discovery deliberately, and Phase 009 still determines inclusion dependence.

## Representation leakage audit

The following are explicitly non-conceptual representation choices despite appearing in older/later documents:

- UUID/content hash/version-column formats;
- Spark schema/partition/file/table identity;
- object/class/dataclass identity;
- database/event-store lifecycle representation;
- checkpoint/manifest storage layout;
- API/CLI status enum names;
- package/module boundaries;
- scheduler/platform job/run identity;
- transaction/fencing/CAS implementation;
- graph-database representation of Provenance.

They may later realize the normalized state but do not define it.

## 008-C completion assessment

```text
CONCEPT STATE SHAPES                    NORMALIZED
LOGICAL IDENTITY DISTINCTIONS           NORMALIZED
HISTORICAL IMMUTABILITY                 NORMALIZED
CURRENT-USE/APPLICABILITY DISTINCTION   NORMALIZED
UNKNOWN/INDETERMINATE STATE             NORMALIZED WHERE MATERIAL
TOPOLOGY/TEXT STATE SUFFICIENCY         PASS FOR CURRENT CATALOG
CROSS-CONCEPT INVARIANT SPINE           ESTABLISHED
ACTION/QUERY TRANSITION CLOSURE         NOT YET — 008-D
OPERATIONAL PRINCIPLE CLOSURE           NOT YET — 008-E
CATALOG/INDEPENDENCE FINALITY           NOT YET — 008-F/008-G
JACKSON CONCEPT DESIGN                  NOT COMPLETE
IMPLEMENTATION READINESS                NOT READY
IMPLEMENTATION START                    NOT STARTED
IMPLEMENTATION NEXT                     NOT YET
```

Any later Phase 008-D through 012 finding may reopen this authority under the J0-J7 discipline.