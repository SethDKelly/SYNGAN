---
type: Documentation Audit
title: 016-A — Full Documentation Corpus Inventory, Duplication / Supersession / Current-Owner Audit
status: complete
---

# 016-A — Full Documentation Corpus Inventory, Duplication / Supersession / Current-Owner Audit

## Objective

Establish a complete repository documentation inventory and a conservative disposition hypothesis before any physical topology normalization.

016-A answers:

- what documentation exists;
- where current authority and historical phase work are physically mixed;
- where multiple documents appear to own or restate the same subject;
- which areas already have strong current-owner/index discipline;
- which files are obvious history candidates;
- which files require semantic-owner adjudication before relocation;
- what 016-B must preserve while normalizing topology.

016-A does **not** move or delete documentation.

## Inventory evidence

Machine-readable inventory:

- [016-A Documentation Corpus Inventory](016-A-documentation-corpus-inventory.json)

The inventory is a path-level audit snapshot generated from the main-branch Git tree after the Phase 016 start gate.

Its classifications are **disposition hypotheses**, not authority changes.

## Corpus size

At the 016-A inventory baseline:

~~~text
Markdown documents under docs/          349
Markdown bytes                          5,111,504

docs/phases/ documents                  154
docs/phases/ bytes                      1,530,137

initial history candidates              245
history-candidate bytes                 3,162,856

current-owner candidates                 67
current-routing candidates               12
current/supersession review               9
current-rationale review                 10
synchronization history/summary review    4
~~~

Before the three Phase 016 start-gate documents were created, the repository contained 346 Markdown documents and 152 phase documents. The small delta is Phase 016 itself.

Approximately 44% of the Markdown files are phase work records, and the initial classifier identifies roughly 70% of the corpus as likely historical/work-record material.

This does not mean 70% of documentation is useless. It means most of the corpus should not compete with current semantic owners during ordinary implementation retrieval.

## Top-level inventory

| Area | Files | Bytes | 016-A interpretation |
|---|---:|---:|---|
| architecture | 29 | 824,710 | current topic owners mixed with multiple architecture-phase generations |
| authority | 43 | 640,158 | durable cross-cutting authority mixed with phase/audit completion evidence |
| backlog | 1 | 7,586 | current non-authoritative planning |
| concepts | 18 | 391,679 | 11 accepted concept owners plus normalization/audit/consolidation records |
| decisions | 11 | 77,112 | ADR rationale; retain pending supersession review |
| dependence | 5 | 86,896 | compact current semantic ownership |
| discovery | 23 | 303,268 | predominantly design-history/discovery evidence |
| experience | 11 | 222,101 | current experience owners mixed with phase consolidation summaries |
| implementation | 28 | 537,979 | current governance mixed with historical Phase 005/006/007 plans and completed Phase 015 authorities |
| mapping | 8 | 217,540 | current mapping authority, large but well-bounded |
| phases | 154 | 1,530,137 | work/progression evidence; strong history candidate |
| problem | 6 | 61,640 | compact current problem authority |
| synchronizations | 6 | 151,826 | one explicit current contract plus prior refinement/consolidation material |
| terminology | 5 | 50,300 | current terminology/reference candidates |
| root index | 1 | 8,572 | authored discovery root, currently overloaded |

## Provisional current-owner map

The following are strong **current-owner families** for 016-B to preserve:

~~~text
docs/problem/                 problem / actors / outcomes / scale envelope
docs/concepts/               eleven concept owners
docs/dependence/             inclusion dependence / valid subsets
docs/synchronizations/
  current-cross-concept-synchronizations.md
                              current synchronization owner
docs/experience/             actor/programmatic experience contracts
docs/mapping/                semantic/interaction mapping
docs/architecture/           non-phase architecture topic owners
docs/authority/              non-phase cross-cutting policy/contract owners
docs/terminology/            terminology/reference ownership
docs/decisions/ADR-*         accepted architecture rationale, subject to supersession review
docs/implementation/
  implementation-authority-delivery-governance-toolchain-repository-enforcement.md
                              implementation-governance candidate
docs/backlog/                non-authoritative future-work ledger
~~~

This is not yet a canonical ownership inventory. 016-B must make ownership explicit before moving ambiguous files.

## High-confidence history candidates

### Phase records

All docs/phases/001 through completed docs/phases/015 are work/progression evidence rather than the preferred current semantic lookup plane.

Phase 016 remains current while active and later becomes history at its own exit.

### Discovery corpus

docs/discovery/ records concept discovery, hypotheses, probes, revalidation and adversarial design work. The accepted current meanings have been promoted into problem/concept/dependence/synchronization/experience/authority/architecture owners.

The directory is therefore a high-confidence design-history candidate, subject to conservation checks.

### Phase-prefixed architecture

Architecture currently contains accepted topic owners alongside:

- Phase 004 architecture;
- Phase 006 reconciliation;
- Phase 007 architecture/implementation-reentry records;
- Phase 013 reconciliation groups and consolidated evidence.

The current topic owners should survive. Prior phase realizations/reconciliation evidence should become provenance unless a specific proposition is found to exist nowhere else.

### Phase/audit authority

docs/authority/ mixes durable policies with Phase 006/007/009/010/011/012/013/014 records and design-quality audit artifacts.

The durable rule should stay current; the audit proving how it was accepted should normally become history.

### Completed implementation phase records

Historical Phase 005/006/007 implementation planning and completed Phase 015 slice authorities are critical provenance/evidence but should not all remain first-line current implementation routing indefinitely.

016-B must preserve the final support/implementation posture while separating completed delivery evidence from live implementation governance.

## Duplication / overlap register

### DUP-01 — phase-status and completion posture

Current state is repeated across:

- AGENTS.md;
- docs/index.md;
- Jackson completion/hold documents;
- Phase 014/015 indexes and exit records;
- Phase 015 implementation authorities;
- post-Phase-015 reconciliation.

This repetition has already produced stale-state cleanup work in prior phases.

**016-B target:** one small current status owner plus derived/routing summaries that reference it.

### DUP-02 — architecture generations

The same architecture subject families appear in:

~~~text
Phase 004 initial architecture
Phase 006 reconciliation
Phase 007 architecture foundation / re-entry
Phase 013 architecture reconciliation
non-phase current architecture topic owners
ADRs
~~~

Examples include identity/persistence/history, distributed data/promotion, Strategy/runtime, Execution/recovery, Evidence/history, security/no-egress and deployment/portability.

**Risk:** search order can surface a historically valid but superseded architecture formulation.

**016-B target:** current architecture topic owner + ADR rationale + history; no competing current phase-generation authority.

### DUP-03 — implementation planning generations

Implementation subject families appear in:

~~~text
non-phase implementation plans
Phase 005 planning
Phase 006 planning reconciliation
Phase 007 implementation locks/bootstrap
Phase 015 completed implementation authorities
current code/tests/C0-C9 evidence
~~~

**Risk:** an agent can mistake a detailed historical plan for current implementation authority because it is more concrete than the current owner.

**016-B target:** current implementation governance/package routing separated from historical plans and completed-slice evidence.

### DUP-04 — concept discovery / validation vs concept owners

Eleven concept-specific owner documents coexist with:

- lifecycle normalization;
- independence/genericity/familiarity review;
- operational-principle normalization;
- state/identity/history normalization;
- catalog/perimeter rediscovery audit;
- Phase 008 individual-concept consolidation;
- the full discovery corpus.

These are valuable evidence but are not all independent current definitions.

**016-B target:** exactly one current concept owner per accepted concept; validation/consolidation material becomes provenance.

### DUP-05 — synchronization generations

The explicit current synchronization owner coexists with:

- core synchronizations;
- trigger/ownership normalization;
- composition economy/synergy/integrity;
- application-family revalidation.

**016-B target:** one current synchronization contract, with other material retained only where it supplies rationale not promoted into current owners.

### DUP-06 — experience consolidation

Current experience-topic documents coexist with Phase 003 and Phase 006 consolidated experience contracts.

**016-B target:** current experience-topic owners plus historical consolidation provenance.

### DUP-07 — completion / readiness audit chain

Phase 011/012/013/014/015 completion and reconciliation artifacts remain readily discoverable beside current owners.

Their role is valid but predominantly evidentiary.

**016-B target:** preserve auditability without requiring agents to traverse completion chronology for current truth.

## Concision and progressive-disclosure findings

### NAV-01 — root agent context is too broad

Root AGENTS.md is approximately 8K characters and its current Start with section names **25 documents**.

The byte size itself is not excessive, but requiring or implying 25 startup reads is inconsistent with bounded progressive disclosure.

**Required direction:** AGENTS.md should contain durable operating rules and a small route to current status/discovery, not a preloaded corpus.

### NAV-02 — root documentation index is overloaded

docs/index.md is a valid discovery root, but its Current governing authority section directly enumerates Phase 014 and Phase 015 detail records alongside current semantic owners.

This conflates:

- current semantic discovery;
- methodology/current-status routing;
- completed-phase evidence navigation.

**Required direction:** reduce the root to first-level current routes and move chronology/provenance into history indexes.

### NAV-03 — section indexing is generally strong

Most multi-document semantic areas already have index.md files.

This is a positive foundation: 016-B should simplify and rebind existing indexes rather than invent a new navigation system everywhere.

## OKF/profile audit

### OKF-01 — current model conflates canonical corpus and OKF bundle

Current documentation governance declares the entire docs/ tree to be the OKF 0.2 knowledge bundle.

That forces current owners, phase records, historical audits, implementation plans and navigation artifacts into one knowledge plane.

The stronger comparison pattern is:

~~~text
repository-native canonical docs     authored current authority
history                              authored provenance only
knowledge/                           generated OKF compatibility projection
~~~

016-C will decide the exact SYNGAN profile after 016-B establishes clean ownership/topology.

### OKF-02 — status vocabulary is internally inconsistent

Documentation governance currently recommends frontmatter statuses:

~~~text
draft
proposed
active
deprecated
superseded
archived
~~~

Existing current/phase documents also use values such as:

~~~text
complete
complete-current
~~~

This is a concrete profile-drift issue.

**016-B/016-C target:** distinguish phase-progress state from durable knowledge lifecycle metadata instead of overloading status.

### OKF-03 — no deterministic full-corpus OKF validation path

The repository currently has OKF-oriented governance but no DMTZ-style generated projection, full structure/resource validator, or dedicated OKF conformance CI.

GOV-001 already records strict external OKF normalization as open/non-blocking.

**016-C target:** resolve this explicitly rather than continuing implicit compliance claims.

## Agentic-readiness findings

### AGT-01 — authority model exists, operating model is incomplete

SYNGAN already has:

- root AGENTS.md;
- documentation authority hierarchy;
- smallest-owner reopen discipline;
- C0-C9 product verification;
- explicit no-auto-next-phase controls.

It does not yet have a complete shared agentic-development foundation for:

- A1/A2/A3/A4 action classes;
- deterministic context discovery;
- context budgets;
- tool-neutral skills;
- tool-adapter inheritance rules;
- agentic change classes;
- repository secret/sensitive-data rules for coding agents;
- agentic conformance/negative controls.

### AGT-02 — product verification and agentic conformance must remain separate

C0-C9 are strong product/architecture verification lanes.

They should not be overloaded with:

- routing drift;
- generated OKF mismatch;
- context-budget violations;
- agent-tool configuration problems;
- current-vs-history topology errors.

016-G should establish a separate agentic/documentation conformance workflow.

## Findings requiring 016-B action

| ID | Finding | Severity | P16 class | 016-A disposition |
|---|---|---|---|---|
| A-01 | current truth and phase/history physically intermixed | high | P16-1 | confirmed |
| A-02 | 245 initial history candidates remain under active docs surface | high | P16-1 | confirmed |
| A-03 | architecture has multiple phase-generation layers beside current topic owners | high | P16-1 | confirmed |
| A-04 | implementation plans/authorities span several historical generations | high | P16-1 | confirmed |
| A-05 | current status/completion posture is repeatedly copied | medium | P16-1 | confirmed |
| A-06 | AGENTS.md startup path is too broad (25 documents) | medium | P16-2 later | confirmed |
| A-07 | root index mixes current discovery with completion chronology | medium | P16-1 | confirmed |
| A-08 | synchronization/concept/experience validation evidence competes with current owners | medium | P16-1 | confirmed |
| A-09 | OKF lifecycle/status vocabulary is inconsistent | medium | P16-1/2 | confirmed |
| A-10 | strict external OKF conformance is not yet deterministically proven | medium | P16-2 | carry to 016-C |
| A-11 | no canonical ownership inventory exists | high | P16-1/2 | carry to 016-B |
| A-12 | no physical docs/history/ boundary exists | high | P16-1 | carry to 016-B |
| A-13 | section indexes are broadly present and reusable | positive | P16-0 | preserve |
| A-14 | no P16-3/P16-4 semantic/design contradiction found | positive | — | no reopen |

## 016-B migration constraints

016-B must not treat 016-A's classifier as automatic move authority.

Before moving a file it must answer:

1. What current proposition(s), if any, does the file uniquely own?
2. If it is history, where is the promoted current owner?
3. Which inbound current links must be rebound?
4. Is the file needed as ADR/current rationale rather than phase history?
5. Will moving it change an accepted stable/reference path that agents or code depend on?
6. Is a redirect/index entry needed for human provenance discovery?
7. Does the move preserve Git-level and repository-level auditability?
8. Does the move reduce, rather than create, dual current authority?

## Proposed normalization waves for 016-B

~~~text
Wave 1  establish canonical ownership inventory + docs/history topology
Wave 2  move completed phase records and discovery work
Wave 3  move phase-prefixed authority/architecture/experience/implementation evidence
Wave 4  adjudicate non-phase overlap clusters and old implementation plans
Wave 5  reduce root/current indexes to progressive-disclosure routes
Wave 6  validate conservation, links, ownership uniqueness and current-status routing
~~~

No wave may delete historical evidence merely because it is verbose.

## 016-A completion decision

~~~text
full Markdown path inventory             COMPLETE
machine-readable corpus manifest         COMPLETE
current-owner disposition hypothesis     COMPLETE
duplication/overlap register             COMPLETE
progressive-disclosure audit             COMPLETE
initial OKF/profile audit                COMPLETE
agentic-readiness topology audit         COMPLETE
P16-3 semantic findings                  0
P16-4 product-scope findings             0
upstream reopen                          NONE
~~~

016-A is complete.

## Handoff

**016-B — Current Knowledge vs History Topology Normalization, Canonical Ownership Map & Progressive Disclosure** is next eligible but remains **NOT AUTHORIZED** until separately proceeded.

016-B should use this audit and the machine-readable inventory as its starting evidence.
