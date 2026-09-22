---
type: Knowledge Bundle
title: SYNGAN Current Knowledge
status: active
---

# SYNGAN Current Knowledge

## Purpose

Route humans and agents to the smallest current owner. Historical design, phase, audit, and
implementation evidence is preserved under [Documentation History](history/index.md) and is not
current authority.

## Start here

1. [Current Repository Status](authority/current-repository-status.md)
2. [Problem & Purpose](problem/index.md)
3. [Concepts](concepts/index.md)
4. [Dependence / Application Family](dependence/index.md)
5. [Current Cross-Concept Synchronizations](synchronizations/current-cross-concept-synchronizations.md)
6. [Experience](experience/index.md) and [Mapping](mapping/index.md)
7. [Architecture](architecture/index.md)
8. [Cross-Cutting Authority](authority/index.md)
9. [Current Implementation & Support Scope](implementation/current-support-scope.md)
10. [Completed Phase 017 / Phase 018 Handoff](phases/017/index.md)
11. [Completed Phase 016 Hardening](phases/016/index.md)

Use [Backlog](backlog/index.md) only for non-authoritative future work and [History](history/index.md)
only for rationale, provenance, supersession analysis, or reconstruction.

## Authority order

~~~text
methodology / cross-cutting authority
  > problem / accepted concepts
  > dependence / application family
  > current synchronization contract
  > experience / mapping
  > current architecture topic owners
  > implementation governance / current support scope
  > completed Phase 016 hardening / readiness authority
  > completed Phase 017 program authorities / current handoff
  > code / tests / provider evidence
  > backlog

history is provenance, not a competing current authority plane
~~~

Canonical ownership is defined by [Canonical Knowledge Ownership Map](authority/canonical-knowledge-ownership-map.md).
Stable logical routing is governed by [Stable Reference, Deterministic Resolution & Drift Control](authority/stable-reference-resolution-drift-control.md).
Human-directed agent work is governed by [Agent Authority, Human-Directed Scope, Change Classes, Security & Trust Boundaries](authority/agent-authority-human-directed-scope-security-trust.md).

## Current state

See [Current Repository Status](authority/current-repository-status.md).

~~~text
Jackson concept design              COMPLETE FOR CURRENT PRODUCT SCOPE
Phase 013 architecture              COMPLETE
Phase 014 whole-design/readiness    COMPLETE
Phase 015 implementation foundation COMPLETE
Phase 016                           COMPLETE
Phase 017                           COMPLETE
017-A..017-I                        COMPLETE
Phase 017 exit                      PASS WITH CARRY-FORWARD

repository implementation readiness READY FOR EXPLICIT START GATE / 100 OF 100
Phase 018                           NEXT ELIGIBLE / NOT AUTHORIZED

product implementation execution   NOT AUTHORIZED
product/provider/runtime delivery   NOT AUTHORIZED
~~~

## Current-history boundary

Current knowledge lives in the subject-owner directories linked above.

Completed phase work, discovery/probe records, prior architecture generations, validation/
consolidation evidence, and completed implementation slices are preserved under docs/history/.

Historical wording such as active, current, canonical, next, MUST, or SHALL is stage-local unless a
current owner re-adopts it.

## OKF note

The authored docs tree is SYNGAN's current knowledge/authority surface. The generated knowledge tree
is a deterministic OKF v0.2 compatibility projection governed by the
[OKF v0.2 Producer Profile](authority/okf-v0.2-producer-profile.md).
