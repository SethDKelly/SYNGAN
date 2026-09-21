---
type: Architecture Reconciliation Authority
title: Phase 013-G — Evaluation, Evidence, Provenance, Historical Query, Reproducibility, Disclosure & External-Governance Boundary Reconciliation
status: active
---

# Phase 013-G — Evaluation, Evidence, Provenance, Historical Query, Reproducibility, Disclosure & External-Governance Boundary Reconciliation

## Purpose

Reconcile SYNGAN's retained Evaluation-result, Evidence, Provenance, historical-query, reproducibility, disclosure and external-governance architecture against the completed concept design and Phase 013-B through 013-F baselines.

013-G asks:

> **Can SYNGAN establish durable findings, explain exact historical derivation, qualify reproducibility, and disclose or hand off those facts safely without turning metrics, metadata graphs, caches, privacy scores, policy decisions, lineage systems or release approvals into stronger semantic authority than the accepted concepts permit?**

Current answer:

```text
YES — THE EVALUATION / EVIDENCE / PROVENANCE / HISTORY / DISCLOSURE SPINE
      REMAINS SOUND WITH BOUNDED CLARIFICATIONS.
NO AMAT-2 DEFECT IS FOUND.
NO AMAT-3 BLOCKER OR AR-9 UPSTREAM CONTRADICTION IS FOUND.
```

This authority is downstream of the completed Phase 012 concept design, current Phase 009/010 authority, 013-A reconciliation method, and completed 013-B through 013-F reconciliation decisions.

---

## 1. Reconciliation subjects

Primary retained subjects reviewed here are:

- `evaluation-evidence-provenance-reproducibility-historical-query.md`;
- `phase-007-i-evaluation-evidence-provenance-historical-query-reproducibility-disclosure-foundation.md`;
- accepted `Evaluation`, `Evidence` and `Provenance` concepts;
- `reproducibility-contract.md` as corrected in 013-E;
- `privacy-disclosure-formal-guarantee-release-boundary-contract.md`;
- security/redaction/history-query boundaries in `dependency-resolution-offline-no-egress-authorization-redaction-enterprise-security.md`;
- 013-F Execution/Attempt/recovery history;
- ADR-0006 as primary rationale input, with ADR-0002/0007/0009 relevant to state, security and recovery.

Deployment/provider-specific observability, external lineage integration guarantees and platform support claims remain 013-H. Final legacy/ADR/status/synchronization-reference cleanup remains 013-I.

---

## 2. Governing evidence/history rule

> **Evaluation owns whether the committed examination was semantically valid; Evidence owns the durable finding established by that valid examination; Provenance owns typed historical relationships; historical query composes those owners without becoming an owner; Reproducibility is a qualified derived assessment; disclosure governs the current actor-visible view; external governance owns release/use decisions outside SYNGAN.**

The responsibility chain is therefore:

```text
committed Evaluation
        ↓
013-F Execution / Attempts when operational work is required
        ↓
non-final method/runtime observations
        ↓
Evaluation semantic validation
        ↓
zero or more durable Evidence findings as legitimately established
        ↓
required typed Provenance relationships
        ↓
exact historical query / explain / compare composition
        ↓
qualified Reproducibility assessment
        ↓
current actor-safe disclosure projection
        ↓
optional controlled handoff to external governance
```

No downstream layer may strengthen an upstream claim merely because it is convenient to store, cache, display, export or approve.

---

## 3. Evaluation result remains non-final until semantic validation

Platform/runtime success, a metric value, readable diagnostic bytes or completion of all physical tasks is not Evidence.

Evaluation validates the exact committed examination, including where material:

- exact Evaluation and Criterion revision;
- exact subject/reference/baseline identities;
- method/configuration and executable realization;
- logical scope/topology/coverage;
- sampling/approximation semantics;
- assumptions and limitations;
- uncertainty/error semantics;
- retry/recovery contribution semantics;
- required diagnostic/support facts;
- claim strength supportable by the actual examination.

A method that ran successfully over the wrong revision, wrong scope, invalid assumptions or insufficient coverage does not become successful Evaluation merely because computation succeeded.

A successful Evaluation may establish negative, unfavorable, risky or indeterminate Evidence. Subject outcome and Evaluation validity remain independent.

---

## 4. Evidence establishment, multiplicity and identity

Evidence remains durable finding authority.

One Evaluation may have zero or more Evidence records over its lifecycle. Architecture must preserve an important qualification:

- failed, cancelled, incomplete or semantically uninterpretable Evaluation may establish no Evidence;
- a valid Evaluation establishes only the independently interpretable findings its committed method/result actually supports;
- when successful Evaluation completion requires durable Evidence under its committed contract, that completion cannot be reported while the required Evidence establishment remains absent or irreconcilably pending.

This preserves the catalog cardinality without inventing `Evidence Set` or making every Evaluation fabricate a finding.

### Finding identity

Repeated normalization/retry must not duplicate one semantic finding.

A stable finding identity/slot is scoped strongly enough to the exact Evaluation result contract, conceptually including:

```text
exact Evaluation
+ logical finding role/slot
+ exact subject/scope/result-role identity where needed
```

Equivalent replay resolves idempotently. Materially conflicting replay for the same logical finding is a consistency defect requiring reconciliation, not overwrite.

### Multiple findings

“At-most-one authoritative semantic result” in operational architecture means retry-safe authoritative owner transitions. It does **not** mean one Evidence resource per Evaluation.

A valid Evaluation may establish several independently interpretable Evidence findings. Physical replay must not manufacture duplicate/conflicting establishment of the same finding.

---

## 5. Immutable Evidence finding and mutable applicability remain separate

Evidence preserves immutable historical finding semantics, including enough exact context to interpret what was established.

Current reliance may later become:

```text
applicable / current
superseded
stale / obsolete
inapplicable
invalidated
```

Those future-use states do not rewrite the original finding.

Newer Evidence may disagree with older Evidence. The framework preserves Criterion, method, scope, baseline, time, threat model, uncertainty and other material differences rather than averaging incompatible findings into one global score.

No generic `quality`, `safe`, `private`, `approved` or `passed` field may erase that heterogeneity.

---

## 6. Claim strength and diagnostics remain bounded

Evidence claim strength cannot exceed the producing Evaluation's method, scope, coverage, assumptions, approximation and uncertainty.

The architecture retains distinctions such as:

```text
exhaustive / universal
deterministic bounded / certificate-backed
statistical
approximate / sketch
diagnostic / partial
indeterminate
```

These are interpretive roles, not a required public enum.

Large violation sets, attack traces, nearest-neighbor examples, row-level observations, prediction outputs or other diagnostics remain separately referenced distributed material by default.

Readable diagnostics do not become Evidence merely through existence.

---

## 7. Generation completion basis remains Generation-owned

Where Generation completion depends on Evidence, Generation preserves an immutable bounded completion basis identifying the exact candidate, committed requirement, Criterion, Evidence identities and sufficiency determination actually used.

Evidence may inform that decision but does not own the Generation transition.

Later Evidence may relate historically to the completed output but cannot retroactively enter the original completion basis.

Negative or indeterminate Evidence remains valid Evidence and may prevent Generation completion when the committed requirement demands satisfaction or determination.

---

## 8. Provenance remains typed relationship authority with low authority fan-out

Canonical Provenance stores typed historical relationship assertions over exact stable references.

It does not copy canonical concept payloads into a metadata graph and does not reconstruct current domain truth as its own state.

Material relationship meanings remain distinguishable, including roles equivalent to:

- bound / governed by;
- derived / produced by;
- used / depended on;
- evaluated / referenced;
- operationally realized by;
- recovered / resumed from;
- superseded / restricted / retired / invalidated context;
- reconstructed / adopted after recovery where material.

A generic `related_to` edge is insufficient when relationship meaning affects interpretation.

### Required Provenance and transition completion

Required Provenance may be a completion invariant for a material transition without becoming the owner of that transition.

Where owner transition and required Provenance cannot share one atomic boundary, architecture may use durable intent, idempotent completion, a recoverable pending condition or reconciliation. Permanent silent divergence is prohibited; a universal distributed transaction is not required.

The semantic owner still decides whether its own transition is valid and complete.

### Correction/reconstruction

Provenance correction is append/supersede/invalidate or equivalent audit-preserving representation. It cannot rewrite another concept's history.

After recovery, reconstructed Provenance is legitimate only to the strength independent retained evidence establishes. Reconstructed status/basis remains inspectable where material.

---

## 9. Historical truth requires two independent axes

Historical query must not collapse **what is known about occurrence** with **whether the referenced object can currently be resolved/disclosed**.

### Historical knowledge basis

A fact/relationship may be:

```text
directly retained canonical fact
reconstructed from sufficient independent evidence
partially known
unknown / occurrence not establishable
```

### Current object-resolution / disclosure state

A referenced object/detail may independently be:

```text
resolved
absent because it did not exist
known identity but payload unavailable
unknown / indeterminate
invalid / integrity-defective
withheld / redacted / non-disclosing outwardly
```

A reconstructed relationship can therefore point to a currently unavailable dependency. A canonically known relationship can be withheld from one actor. These conditions are not contradictory and must remain composable.

A recovery gap is not proof that nothing happened during the gap.

---

## 10. Historical query is read composition, not history ownership

Explain/traverse/compare services compose exact canonical owners, Provenance, Evidence applicability, material Execution history and derived indexes.

Derived adjacency/search/report/warehouse projections remain rebuildable and non-authoritative.

Therefore:

```text
projection miss != historical absence
stale projection != canonical truth
current alias != exact historical binding
```

A correctness-sensitive query can resolve back to canonical authorities rather than trusting a stale cache.

### Query consistency qualification

A query may combine immutable historical facts with current applicability, availability and disclosure observations made at different versions/times.

It must not imply one global atomic snapshot unless that guarantee actually exists.

### Comparison boundary

Historical comparison may report structural/material differences. Difference does not establish causality, superiority or quality; those claims require explicit Evaluation/Evidence.

---

## 11. Reproducibility remains derived and multi-axis

013-G retains the corrected 013-E Reproducibility model: historical `SYNC-15` is not active synchronization authority and there is no canonical `Reproducibility` resource/lifecycle.

At minimum three independent axes must remain distinguishable.

### Historical supportability

What reproduction/comparison class can the retained historical record defensibly support?

Accepted classes remain conceptually:

```text
exact deterministic
semantic
statistical
bounded / approximate
comparative
not reproducible / insufficient historical context
```

The strongest-defensible-class rule applies. Seed presence alone never proves exact determinism.

### Current feasibility

Can an authorized deployment attempt the reproduction now under current availability, trust, network, runtime, security and admission conditions?

A historically strong reproduction contract may be infeasible now because an exact artifact is unavailable or current policy blocks a dependency.

### Actor-visible assessability

What may the current actor inspect about the basis, limitations and reasons?

Disclosure restrictions may hide a dependency identity or limiting reason without making the canonical historical fact absent.

Caching any of these assessments does not make the cache authority.

### Reproduction success

Readiness/feasibility is not success. Actual reproduction is new domain work and, where equivalence is not guaranteed by construction, is established through explicit Evaluation/Evidence against the declared equivalence Criterion.

The historical target is never overwritten by the reproduction attempt.

---

## 12. Disclosure remains current view authority

Disclosure/redaction determines what a current actor may observe or traverse. It does not mutate canonical Evidence, Provenance or history.

Protection may apply to more than field values, including:

- resource existence;
- relationship existence and graph shape;
- endpoint identities;
- relationship qualifiers;
- diagnostics;
- source/dependency/runtime identities;
- counts/cardinality/pagination shape;
- reverse traversal;
- comparison fields;
- reproducibility reason text.

When existence itself is protected, outward responses may intentionally avoid distinguishing absence from forbidden/withheld. Internal canonical/security state remains precise where policy permits.

An authorized summary is a derived view, not the original value. Redaction must not fabricate replacement facts.

Disclosure is contextual and non-transitive: permission to inspect one Evidence summary does not imply permission to inspect its diagnostics, source, reverse Provenance path or provider logs.

---

## 13. Privacy Evidence, formal guarantees and external governance remain distinct

The current architecture preserves four independent responsibilities:

```text
privacy / disclosure-risk question
    -> Criterion / Evaluation / Evidence

formal mechanism guarantee/accounting
    -> future mechanism-specific authority if accepted through renewed concept discovery

current disclosure/redaction permission
    -> security / authorization view authority

release / use decision
    -> external organizational governance authority
```

Synthetic origin, local/offline execution, successful Generation or favorable privacy-related Evidence does not imply anonymization, formal privacy, certification or release approval.

Formal composable privacy mechanisms remain an M8 rediscovery trigger. No generic privacy-budget/accounting state is introduced by architecture.

### External governance handoff

Current active `SYNC-13` permits controlled Evidence handoff to Generation completion logic or external decision authorities.

The external system/actor owns its release/use/policy decision. SYNGAN may:

- provide exact authorized Evidence/Provenance/history context;
- retain an external decision/reference in audit/integration context when materially required;
- enforce current action authorization derived from configured governance/security integration.

SYNGAN must not create hidden domain state such as:

```text
output.approved = true
evidence.safe_to_release = true
provenance.certified = true
```

The same Evidence may legitimately lead to different release/use outcomes under different external policies.

Historical approval does not create permanent future export permission.

---

## 14. External lineage/metadata integrations remain evidence/projections

External lineage collectors, catalogs, registries, warehouses and observability systems may receive or expose SYNGAN references.

Their observations may support correlation, search or recovery reconstruction, but an external edge/event does not automatically become canonical SYNGAN Provenance or Evidence.

Deletion/mutation of an external record does not rewrite canonical SYNGAN history.

013-H will reconcile the provider/platform guarantee side of these integrations.

---

## 15. Regressive-recovery composition

After potentially regressive recovery:

```text
fresh non-regressing authority frontier
        ↓
reconcile surviving operational / physical / provider facts
        ↓
reconstruct or adopt only where normal owner proof is sufficient
        ↓
record recovery / reconstruction relationships
        ↓
historical query identifies direct vs reconstructed vs partial / unknown
        ↓
Reproducibility uses strongest defensible retained history
```

Surviving output does not prove Generation promotion. Surviving diagnostic bytes do not prove Evidence establishment. External lineage does not prove canonical Provenance. Missing restored rows do not prove that later transitions never happened.

---

## 16. Scale and boundedness

Evidence/Provenance/history control state scales with material findings, relationships, activities, revisions, Attempts and bounded summaries rather than every row, file, task, tensor, metric or log event.

The architecture retains:

- no default Evidence record per row;
- no default Provenance edge per Spark task/file/row;
- distributed diagnostic references;
- bounded/paginated traversal;
- summary-first explanation with drill-down;
- reproducibility assessment from exact references/manifests rather than payload collection;
- no requirement to materialize complete source/output/Learned-State/diagnostic/telemetry data in driver memory.

Row-level lineage or exhaustive diagnostics may exist as explicitly scoped distributed data-plane material without becoming the canonical control-plane default.

---

## 17. Current synchronization interpretation

The [Current Cross-Concept Synchronization Contract](../synchronizations/current-cross-concept-synchronizations.md) controls current scope and ownership:

```text
SYNC-09  Evaluation Criterion binding
SYNC-10  Evaluation method compatibility
SYNC-11  Evaluation operational realization
SYNC-12  completed Evidence-producing Evaluation establishes Evidence
SYNC-13  Generation / Evidence completion handoff when Generation is evidence-gated
SYNC-14  Provenance recording at material transitions
SYNC-08  retired as cross-concept synchronization
SYNC-15  historical/reclassified under cross-cutting Reproducibility
```

`SYNC-13` does not include external release/use/governance decisions. Evidence remains finding authority; Generation owns applicability/sufficiency and its own completion transition; external governance remains an external-authority handoff.

Historical/current-looking references in accepted Evaluation/Evidence/Provenance documents, retained 004-G/007-I architecture, the privacy/release boundary, `core-synchronizations.md` and other pre-Phase-009 material are interpreted through the current synchronization contract and completed Phase 013 authority.

### Phase 014-E propagation note

Phase 014-E made the `SYNC-12`/`SYNC-13` scope explicit here so this detailed current architecture authority cannot be read as restoring the broader pre-014-C external-handoff interpretation.

No synchronization-design reopen is required.

---

## 18. Finding ledger

```text
A13-G-001  stale SYNC-15 / 15-rule Evidence-history references        AR-1/AR-2  AMAT-1  CLEANUP -> 013-I
A13-G-002  Evaluation zero-or-more Evidence vs successful completion  AR-3/AR-4  AMAT-1  CLARIFY / RESOLVED
A13-G-003  operational at-most-one wording vs multi-Evidence          AR-3/AR-4  AMAT-1  RESOLVED
A13-G-004  required Provenance mistaken as transition ownership       AR-3       AMAT-1  RESOLVED
A13-G-005  historical knowledge vs object-resolution collapse         AR-4/AR-5  AMAT-1  RESOLVED
A13-G-006  projection absence/global-snapshot overstatement           AR-4       AMAT-1  RESOLVED
A13-G-007  Reproducibility supportability/feasibility/disclosure      AR-3/AR-4  AMAT-1  RESOLVED
A13-G-008  external governance hidden approval state                  AR-3/AR-6  AMAT-1  RESOLVED
A13-G-009  empirical privacy Evidence -> formal guarantee/release     AR-4/AR-8  AMAT-1  RESOLVED
A13-G-010  external lineage -> canonical Provenance/Evidence          AR-3/AR-4  AMAT-1  RESOLVED
A13-G-011  disclosure redaction mutates canonical truth               AR-4/AR-5  AMAT-1  RESOLVED
```

---

## 19. Retained subject disposition

```text
Phase 004-G Evidence/history architecture           ALIGNED-WITH-CLARIFICATION
Phase 007-I Evidence/history/disclosure foundation  ALIGNED-WITH-CLARIFICATION
Evaluation concept                                  SEMANTICS ALIGNED; SYNC TAIL CLEANUP -> 013-I
Evidence concept                                    SEMANTICS ALIGNED; SYNC TAIL CLEANUP -> 013-I
Provenance concept                                  SEMANTICS ALIGNED; SYNC TAIL CLEANUP -> 013-I
Reproducibility Contract                            RETAIN AFTER 013-E CORRECTION
Privacy/Disclosure/Release Boundary                 SEMANTICS ALIGNED; SYNC CLEANUP -> 013-I
Security/Redaction architecture                     ALIGNED-WITH-CLARIFICATION
ADR-0006                                            PROVISIONAL RETAIN
ADR-0002 / ADR-0007 / ADR-0009                      PROVISIONAL RETAIN where relevant
```

Final ADR lifecycle/status and legacy corpus cleanup remain 013-I work.

---

## 20. Materiality result

```text
AMAT-2 Evaluation/Evidence/history defects   0
AMAT-3 blockers                              0
AR-9 contradictions                          0
upstream reopen                              NONE
new concepts                                 0
new synchronizations                         0
mandatory graph/SQL/history engine           0
mandatory report/UI                          0
mandatory governance product                 0
formal privacy placeholder authority         0
```

No current concept, synchronization or Phase 010 mapping correction is required.

---

## 21. Architecture invariants carried forward

1. Runtime/platform Evaluation success does not establish Evidence.
2. Evidence is established only from semantically valid Evaluation context.
3. Repeated physical work cannot duplicate/conflict one authoritative semantic finding silently.
4. One Evaluation may establish multiple independently interpretable Evidence findings.
5. Immutable Evidence semantics remain separate from current applicability.
6. Claim strength does not exceed actual method/scope/coverage/uncertainty support.
7. Negative and indeterminate findings remain legitimate Evidence.
8. Generation owns its exact Evidence-based completion transition and immutable completion basis.
9. Provenance owns typed relationships, not referenced owner state.
10. Required Provenance can constrain completion without acquiring transition ownership.
11. Direct, reconstructed, partial and unknown historical knowledge remain distinguishable.
12. Object resolution/availability and historical knowledge basis remain independent.
13. Derived query/search/graph projections remain non-authoritative.
14. Historical comparison does not invent causality or superiority.
15. Query assembly does not imply a global atomic snapshot absent such a guarantee.
16. Reproducibility is derived/contextual and has no canonical Boolean owner.
17. Historical supportability, current feasibility and actor-visible assessability remain separate.
18. Disclosure/redaction does not mutate canonical truth.
19. Existence, graph shape, counts and reverse traversal may be protected.
20. Empirical privacy Evidence is not a formal privacy guarantee.
21. Evidence is not external release/use approval.
22. External governance decisions remain external authority and do not create hidden SYNGAN approval state.
23. External lineage/metadata does not automatically become canonical Provenance/Evidence.
24. Recovery reconstruction remains owner-qualified and epistemically attributable.
25. Control-plane Evidence/history remains bounded/reference-first at enterprise scale.

---

## 22. Handoff to 013-H

013-H receives a current Evidence/history/disclosure model in which provider and deployment systems may supply qualified facts but do not own semantics.

013-H must reconcile at least:

- platform capability/support claims against actual guarantees;
- observability/telemetry as non-canonical evidence unless promoted through an owning transition;
- provider lineage/catalog integration under the external-integration boundary;
- portability without semantic weakening;
- scale/support-profile claims without universal provider assumptions;
- deployment isolation/security capabilities needed to honor current disclosure/runtime contracts;
- degraded provider capability without converting unknown/limited state into stronger semantic truth.

---

## Exit decision

```text
013-G                                      COMPLETE
Evaluation/Evidence/Provenance/history     RETAINED WITH BOUNDED CLARIFICATION
AMAT-2                                     0
AMAT-3                                     0
AR-9                                       0
upstream reopen                            NONE
R1                                         DOWNSTREAM / IN PROGRESS
013-H                                      NEXT ELIGIBLE
```

Implementation remains **NOT READY / NOT STARTED / NOT YET**.
