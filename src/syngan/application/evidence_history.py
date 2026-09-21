"""Application coordination for Evaluation, Evidence, Provenance, and historical reads."""

from __future__ import annotations

from dataclasses import dataclass

from syngan.domain.evaluation_evidence import (
    EvidenceApplicability,
    EvidenceApplicabilityState,
    EvidenceFinding,
    EvaluationAggregate,
    EvaluationResult,
    FindingDraft,
    applicability_from_payload,
    applicability_to_payload,
    evaluation_from_payload,
    evaluation_state_key,
    evaluation_to_payload,
    evidence_applicability_key,
    evidence_from_payload,
    evidence_reference,
    evidence_to_payload,
)
from syngan.domain.provenance import (
    Assessability,
    CurrentFeasibility,
    HistoricalAssertionView,
    HistoricalKnowledgeBasis,
    HistoricalReferenceView,
    HistoricalResolution,
    ProvenanceAssertion,
    ProvenanceAssertionState,
    ProvenanceRelationship,
    ProvenanceStatus,
    ReproducibilityAssessment,
    ReproductionClass,
    provenance_from_payload,
    provenance_reference,
    provenance_state_from_payload,
    provenance_state_key,
    provenance_state_to_payload,
    provenance_to_payload,
)
from syngan.foundation.identity import (
    LogicalId,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.ports.control_store import (
    ControlStore,
    CurrentStateConflict,
    RecordNotFound,
    ResolutionStatus,
)

_SCHEMA = RepresentationSchemaVersion(1)


@dataclass(frozen=True, slots=True)
class EvaluationSnapshot:
    state: EvaluationAggregate
    state_version: StateVersion


@dataclass(frozen=True, slots=True)
class EvidenceSnapshot:
    finding: EvidenceFinding
    applicability: EvidenceApplicabilityState
    applicability_state_version: StateVersion


@dataclass(frozen=True, slots=True)
class ProvenanceSnapshot:
    assertion: ProvenanceAssertion
    state: ProvenanceAssertionState
    state_version: StateVersion


class EvidenceHistoryService:
    """Coordinate semantic findings/history without acquiring Generation or policy authority."""

    def __init__(self, store: ControlStore) -> None:
        self._store = store

    def initialize_evaluation(
        self,
        state: EvaluationAggregate,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> EvaluationSnapshot:
        committed_payload = evaluation_to_payload(state)
        self._store.put_immutable_binding(
            state.evaluation_commitment,
            _SCHEMA,
            committed_payload,
            authority_frontier,
        )
        record = self._store.create_current_state(
            key=evaluation_state_key(state.evaluation_commitment),
            schema_version=_SCHEMA,
            payload=committed_payload,
            authority_frontier=authority_frontier,
            transition_id=transition_id,
            transition_kind="evaluation-committed",
            transition_detail=EncodedPayload.from_object(
                {"evaluation_id": state.evaluation_commitment.key.resource_id.value}
            ),
        )
        return EvaluationSnapshot(
            state=evaluation_from_payload(record.payload),
            state_version=record.state_version,
        )

    def load_evaluation(self, reference: TypedReference) -> EvaluationSnapshot:
        record = self._store.get_current_state(evaluation_state_key(reference))
        if record is None:
            raise RecordNotFound("Evaluation record does not exist")
        state = evaluation_from_payload(record.payload)
        if state.evaluation_commitment != reference:
            raise ValueError("stored Evaluation does not match requested commitment")
        return EvaluationSnapshot(state=state, state_version=record.state_version)

    def activate_evaluation(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> EvaluationSnapshot:
        snapshot = self._load_expected_evaluation(reference, expected_state_version)
        return self._persist_evaluation(
            snapshot,
            snapshot.state.activate(),
            authority_frontier,
            transition_id,
            "evaluation-activated",
            EncodedPayload.from_object({}),
        )

    def complete_with_findings(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        result: EvaluationResult,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        intent_id: LogicalId,
    ) -> tuple[EvaluationSnapshot, tuple[EvidenceSnapshot, ...]]:
        snapshot = self._load_expected_evaluation(reference, expected_state_version)
        self._validate_result(snapshot.state, result)

        evidence = tuple(
            self._finding_from_draft(snapshot.state, draft) for draft in result.findings
        )
        self._store.put_coordination_intent(
            intent_id=intent_id,
            source=reference,
            intent_kind="establish-evaluation-evidence",
            payload=EncodedPayload.from_object(
                {
                    "evidence_references": [
                        item.reference.require_exact_binding()[1] for item in evidence
                    ]
                }
            ),
            authority_frontier=authority_frontier,
        )

        evidence_snapshots: list[EvidenceSnapshot] = []
        for finding in evidence:
            self._store.put_immutable_binding(
                finding.reference,
                _SCHEMA,
                evidence_to_payload(finding),
                authority_frontier,
            )
            evidence_snapshots.append(
                self._ensure_evidence_applicability(finding.reference, authority_frontier)
            )
            for assertion in self._required_finding_provenance(finding):
                self._ensure_provenance(assertion, authority_frontier)

        finding_limitations = tuple(
            limitation
            for finding in result.findings
            for limitation in finding.limitations
            if limitation not in result.limitations
        )
        completion_limitations = (*result.limitations, *finding_limitations)
        next_state = snapshot.state.complete(
            tuple(item.reference for item in evidence),
            limitations=completion_limitations,
        )
        completed = self._persist_evaluation(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "evaluation-completed",
            EncodedPayload.from_object(
                {"evidence_count": len(evidence), "limited": bool(result.limitations)}
            ),
        )
        self._store.acknowledge_coordination_intent(intent_id, authority_frontier)
        return completed, tuple(evidence_snapshots)

    def fail_evaluation(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> EvaluationSnapshot:
        snapshot = self._load_expected_evaluation(reference, expected_state_version)
        return self._persist_evaluation(
            snapshot,
            snapshot.state.fail(),
            authority_frontier,
            transition_id,
            "evaluation-failed",
            EncodedPayload.from_object({}),
        )

    def cancel_evaluation(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> EvaluationSnapshot:
        snapshot = self._load_expected_evaluation(reference, expected_state_version)
        return self._persist_evaluation(
            snapshot,
            snapshot.state.cancel(),
            authority_frontier,
            transition_id,
            "evaluation-cancelled",
            EncodedPayload.from_object({}),
        )

    def load_evidence(self, reference: TypedReference) -> EvidenceSnapshot:
        resolution = self._store.resolve_immutable_binding(reference)
        if resolution.status is not ResolutionStatus.RESOLVED or resolution.record is None:
            raise RecordNotFound("Evidence finding is not exactly resolvable")
        finding = evidence_from_payload(resolution.record.payload)
        if finding.reference != reference:
            raise ValueError("stored Evidence does not match requested reference")

        current = self._store.get_current_state(evidence_applicability_key(reference))
        if current is None:
            raise RecordNotFound("Evidence applicability record does not exist")
        applicability = applicability_from_payload(current.payload)
        if applicability.evidence_reference != reference:
            raise ValueError("stored Evidence applicability does not match finding")
        return EvidenceSnapshot(
            finding=finding,
            applicability=applicability,
            applicability_state_version=current.state_version,
        )

    def change_evidence_applicability(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        status: EvidenceApplicability,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        *,
        reasons: tuple[str, ...] = (),
        replacement_references: tuple[TypedReference, ...] = (),
    ) -> EvidenceSnapshot:
        snapshot = self.load_evidence(reference)
        if snapshot.applicability_state_version != expected_state_version:
            raise CurrentStateConflict("Evidence applicability state version is stale")
        next_state = snapshot.applicability.with_status(
            status,
            reasons=reasons,
            replacement_references=replacement_references,
        )
        record = self._store.compare_and_swap_current_state(
            key=evidence_applicability_key(reference),
            expected_state_version=expected_state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=applicability_to_payload(next_state),
            transition_id=transition_id,
            transition_kind="evidence-applicability-changed",
            transition_detail=EncodedPayload.from_object({"status": status.value}),
        )
        return EvidenceSnapshot(
            finding=snapshot.finding,
            applicability=applicability_from_payload(record.payload),
            applicability_state_version=record.state_version,
        )

    def resolve_applicable_evidence(
        self,
        references: tuple[TypedReference, ...],
    ) -> tuple[EvidenceFinding, ...]:
        findings: list[EvidenceFinding] = []
        for reference in references:
            snapshot = self.load_evidence(reference)
            if snapshot.applicability.status is not EvidenceApplicability.APPLICABLE:
                raise ValueError(
                    f"Evidence {reference.key.resource_id.value!r} is not currently applicable"
                )
            findings.append(snapshot.finding)
        return tuple(findings)

    def record_generation_evidence_use(
        self,
        generation_reference: TypedReference,
        evidence_references: tuple[TypedReference, ...],
        assertion_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> ProvenanceSnapshot:
        generation_reference.require_exact_binding()
        self.resolve_applicable_evidence(evidence_references)
        assertion = ProvenanceAssertion(
            reference=provenance_reference(generation_reference, assertion_id),
            relationship=ProvenanceRelationship.USED_FOR_COMPLETION,
            subject_references=(generation_reference,),
            object_references=evidence_references,
            basis=HistoricalKnowledgeBasis.DIRECT,
            qualifiers=EncodedPayload.from_object({"owner": "generation"}),
        )
        return self._ensure_provenance(assertion, authority_frontier)

    def record_provenance(
        self,
        assertion: ProvenanceAssertion,
        authority_frontier: RecoveryFrontier,
    ) -> ProvenanceSnapshot:
        return self._ensure_provenance(assertion, authority_frontier)

    def load_provenance(self, reference: TypedReference) -> ProvenanceSnapshot:
        resolution = self._store.resolve_immutable_binding(reference)
        if resolution.status is not ResolutionStatus.RESOLVED or resolution.record is None:
            raise RecordNotFound("Provenance assertion is not exactly resolvable")
        assertion = provenance_from_payload(resolution.record.payload)
        current = self._store.get_current_state(provenance_state_key(reference))
        if current is None:
            raise RecordNotFound("Provenance assertion state does not exist")
        state = provenance_state_from_payload(current.payload)
        return ProvenanceSnapshot(assertion, state, current.state_version)

    def change_provenance_status(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
        status: ProvenanceStatus,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        *,
        reasons: tuple[str, ...] = (),
        replacement_reference: TypedReference | None = None,
    ) -> ProvenanceSnapshot:
        snapshot = self.load_provenance(reference)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict("Provenance assertion state version is stale")
        next_state = snapshot.state.with_status(
            status,
            reasons=reasons,
            replacement_reference=replacement_reference,
        )
        record = self._store.compare_and_swap_current_state(
            key=provenance_state_key(reference),
            expected_state_version=expected_state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=provenance_state_to_payload(next_state),
            transition_id=transition_id,
            transition_kind="provenance-status-changed",
            transition_detail=EncodedPayload.from_object({"status": status.value}),
        )
        return ProvenanceSnapshot(
            snapshot.assertion,
            provenance_state_from_payload(record.payload),
            record.state_version,
        )

    def compose_assertion(self, reference: TypedReference) -> HistoricalAssertionView:
        snapshot = self.load_provenance(reference)
        basis = snapshot.assertion.basis
        subjects = tuple(
            self.resolve_historical_reference(item, basis)
            for item in snapshot.assertion.subject_references
        )
        objects = tuple(
            self.resolve_historical_reference(item, basis)
            for item in snapshot.assertion.object_references
        )
        return HistoricalAssertionView(snapshot.assertion, snapshot.state, subjects, objects)

    def resolve_historical_reference(
        self,
        reference: TypedReference,
        knowledge_basis: HistoricalKnowledgeBasis,
    ) -> HistoricalReferenceView:
        reference.require_exact_binding()
        if knowledge_basis is HistoricalKnowledgeBasis.UNKNOWN:
            return HistoricalReferenceView(
                reference,
                knowledge_basis,
                HistoricalResolution.UNKNOWN,
            )
        resolution = self._store.resolve_immutable_binding(reference)
        if resolution.status is ResolutionStatus.RESOLVED and resolution.record is not None:
            return HistoricalReferenceView(
                reference,
                knowledge_basis,
                HistoricalResolution.RESOLVED,
                resolution.record.payload,
            )
        if resolution.status is ResolutionStatus.UNAVAILABLE:
            return HistoricalReferenceView(
                reference,
                knowledge_basis,
                HistoricalResolution.KNOWN_UNAVAILABLE,
            )
        return HistoricalReferenceView(
            reference,
            knowledge_basis,
            HistoricalResolution.UNKNOWN,
        )

    def compare_evidence(
        self,
        left_reference: TypedReference,
        right_reference: TypedReference,
    ) -> EncodedPayload:
        left = self.load_evidence(left_reference)
        right = self.load_evidence(right_reference)
        fields = {
            "criterion": left.finding.criterion_reference != right.finding.criterion_reference,
            "subject": left.finding.subject_reference != right.finding.subject_reference,
            "method": left.finding.method_reference != right.finding.method_reference,
            "disposition": left.finding.disposition != right.finding.disposition,
            "result": left.finding.result != right.finding.result,
            "scope": left.finding.logical_scope != right.finding.logical_scope,
            "claim_strength": left.finding.claim_strength != right.finding.claim_strength,
            "limitations": left.finding.limitations != right.finding.limitations,
            "applicability": left.applicability.status != right.applicability.status,
        }
        return EncodedPayload.from_object({"differences": fields})

    def assess_reproducibility(
        self,
        target_reference: TypedReference,
        intended_class: ReproductionClass,
        material_references: tuple[TypedReference, ...],
        *,
        historical_conditions_preserved: bool | None,
        environment_eligible: bool | None,
        assessability: Assessability = Assessability.INDETERMINATE,
    ) -> ReproducibilityAssessment:
        target_reference.require_exact_binding()
        views = tuple(
            self.resolve_historical_reference(reference, HistoricalKnowledgeBasis.DIRECT)
            for reference in material_references
        )
        reasons: list[str] = []

        if historical_conditions_preserved is True:
            supportability = intended_class
        else:
            supportability = ReproductionClass.NOT_REPRODUCIBLE
            reasons.append("historical reproduction conditions are incomplete or unproven")

        if environment_eligible is False:
            feasibility = CurrentFeasibility.INFEASIBLE
            reasons.append("current environment is ineligible")
        elif any(
            view.resolution is HistoricalResolution.KNOWN_UNAVAILABLE for view in views
        ):
            feasibility = CurrentFeasibility.INFEASIBLE
            reasons.append("required material is currently unavailable")
        elif environment_eligible is None or any(
            view.resolution
            in {
                HistoricalResolution.UNKNOWN,
                HistoricalResolution.INVALID,
                HistoricalResolution.WITHHELD,
            }
            for view in views
        ):
            feasibility = CurrentFeasibility.INDETERMINATE
            reasons.append("current material/runtime feasibility is not fully established")
        else:
            feasibility = CurrentFeasibility.FEASIBLE

        return ReproducibilityAssessment(
            target_reference=target_reference,
            historical_supportability=supportability,
            current_feasibility=feasibility,
            assessability=assessability,
            reasons=tuple(reasons),
        )

    def _load_expected_evaluation(
        self,
        reference: TypedReference,
        expected_state_version: StateVersion,
    ) -> EvaluationSnapshot:
        snapshot = self.load_evaluation(reference)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict("Evaluation state version is stale")
        return snapshot

    def _persist_evaluation(
        self,
        snapshot: EvaluationSnapshot,
        next_state: EvaluationAggregate,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        detail: EncodedPayload,
    ) -> EvaluationSnapshot:
        record = self._store.compare_and_swap_current_state(
            key=evaluation_state_key(snapshot.state.evaluation_commitment),
            expected_state_version=snapshot.state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=evaluation_to_payload(next_state),
            transition_id=transition_id,
            transition_kind=transition_kind,
            transition_detail=detail,
        )
        return EvaluationSnapshot(
            evaluation_from_payload(record.payload),
            record.state_version,
        )

    def _validate_result(
        self,
        state: EvaluationAggregate,
        result: EvaluationResult,
    ) -> None:
        if result.evaluation_commitment != state.evaluation_commitment:
            raise ValueError("Evaluation result commitment does not match")
        if result.criterion_references != state.criterion_references:
            raise ValueError("Evaluation result Criteria do not match commitment")
        if result.subject_reference != state.subject_reference:
            raise ValueError("Evaluation result subject does not match commitment")
        if result.method_reference != state.method_reference:
            raise ValueError("Evaluation result method does not match commitment")
        if not result.assumptions_valid or not result.interpretable:
            raise ValueError("Evaluation result is not semantically interpretable")
        if not result.findings:
            raise ValueError("completed Evidence-producing Evaluation requires findings")
        for finding in result.findings:
            if finding.criterion_reference not in state.criterion_references:
                raise ValueError("finding answers an unbound Criterion")
            if any(
                reference not in state.baseline_references
                for reference in finding.baseline_references
            ):
                raise ValueError("finding uses an unbound baseline reference")

    def _finding_from_draft(
        self,
        evaluation: EvaluationAggregate,
        draft: FindingDraft,
    ) -> EvidenceFinding:
        return EvidenceFinding(
            reference=evidence_reference(evaluation.evaluation_commitment, draft.slot),
            producing_evaluation=evaluation.evaluation_commitment,
            criterion_reference=draft.criterion_reference,
            subject_reference=evaluation.subject_reference,
            method_reference=evaluation.method_reference,
            slot=draft.slot,
            disposition=draft.disposition,
            result=draft.result,
            logical_scope=draft.logical_scope,
            claim_strength=draft.claim_strength,
            uncertainty=draft.uncertainty,
            limitations=draft.limitations,
            baseline_references=draft.baseline_references,
        )

    def _ensure_evidence_applicability(
        self,
        reference: TypedReference,
        authority_frontier: RecoveryFrontier,
    ) -> EvidenceSnapshot:
        current = self._store.get_current_state(evidence_applicability_key(reference))
        finding_resolution = self._store.resolve_immutable_binding(reference)
        if finding_resolution.record is None:
            raise RecordNotFound("Evidence finding was not established")
        finding = evidence_from_payload(finding_resolution.record.payload)
        if current is None:
            initial = EvidenceApplicabilityState(reference)
            transition_id = LogicalId(f"app-{reference.key.resource_id.value}")
            current = self._store.create_current_state(
                key=evidence_applicability_key(reference),
                schema_version=_SCHEMA,
                payload=applicability_to_payload(initial),
                authority_frontier=authority_frontier,
                transition_id=transition_id,
                transition_kind="evidence-established",
                transition_detail=EncodedPayload.from_object({}),
            )
        applicability = applicability_from_payload(current.payload)
        if applicability.evidence_reference != reference:
            raise CurrentStateConflict("Evidence applicability identity conflicts")
        return EvidenceSnapshot(finding, applicability, current.state_version)

    def _required_finding_provenance(
        self,
        finding: EvidenceFinding,
    ) -> tuple[ProvenanceAssertion, ...]:
        roles = (
            (
                "producer",
                ProvenanceRelationship.PRODUCED_BY,
                (finding.producing_evaluation,),
            ),
            (
                "criterion",
                ProvenanceRelationship.ANSWERS_CRITERION,
                (finding.criterion_reference,),
            ),
            (
                "subject",
                ProvenanceRelationship.EVALUATED_SUBJECT,
                (finding.subject_reference,),
            ),
        )
        assertions: list[ProvenanceAssertion] = []
        for suffix, relationship, objects in roles:
            assertion_id = LogicalId(f"{finding.reference.key.resource_id.value}-{suffix}")
            assertions.append(
                ProvenanceAssertion(
                    reference=provenance_reference(finding.reference, assertion_id),
                    relationship=relationship,
                    subject_references=(finding.reference,),
                    object_references=objects,
                    basis=HistoricalKnowledgeBasis.DIRECT,
                    qualifiers=EncodedPayload.from_object({"evidence_slot": finding.slot}),
                )
            )
        return tuple(assertions)

    def _ensure_provenance(
        self,
        assertion: ProvenanceAssertion,
        authority_frontier: RecoveryFrontier,
    ) -> ProvenanceSnapshot:
        self._store.put_immutable_binding(
            assertion.reference,
            _SCHEMA,
            provenance_to_payload(assertion),
            authority_frontier,
        )
        current = self._store.get_current_state(provenance_state_key(assertion.reference))
        if current is None:
            initial = ProvenanceAssertionState(assertion.reference)
            transition_id = LogicalId(f"prov-{assertion.reference.key.resource_id.value}")
            current = self._store.create_current_state(
                key=provenance_state_key(assertion.reference),
                schema_version=_SCHEMA,
                payload=provenance_state_to_payload(initial),
                authority_frontier=authority_frontier,
                transition_id=transition_id,
                transition_kind="provenance-established",
                transition_detail=EncodedPayload.from_object(
                    {"relationship": assertion.relationship.value}
                ),
            )
        state = provenance_state_from_payload(current.payload)
        if state.assertion_reference != assertion.reference:
            raise CurrentStateConflict("Provenance status identity conflicts")
        return ProvenanceSnapshot(assertion, state, current.state_version)
