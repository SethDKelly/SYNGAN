"""Durable Execution/Attempt operational coordination."""

from __future__ import annotations

from dataclasses import dataclass

from syngan.domain.execution import (
    AdmissionDecision,
    AdmissionFacts,
    AdmissionStatus,
    AttemptStatus,
    CheckpointDescriptor,
    ExecutionAggregate,
    ProviderObservation,
    checkpoint_from_payload,
    checkpoint_to_payload,
    execution_from_payload,
    execution_state_key,
    execution_to_payload,
    runtime_plan_reference,
)
from syngan.foundation.identity import (
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    RepresentationSchemaVersion,
    ResourceKey,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload, JsonObject, JsonValue, encode_reference
from syngan.foundation.runtime import RuntimeRealizationPlan
from syngan.ports.control_store import (
    ControlStore,
    CoordinationIntentRecord,
    CurrentStateConflict,
    RecordNotFound,
    ResolutionStatus,
)
from syngan.ports.recovery_authority import RecoveryAuthority

_SCHEMA = RepresentationSchemaVersion(1)


@dataclass(frozen=True, slots=True)
class ExecutionSnapshot:
    state: ExecutionAggregate
    state_version: StateVersion


def _pair_list(values: tuple[tuple[str, str], ...]) -> list[JsonValue]:
    return [{"name": name, "identity": identity} for name, identity in values]


def runtime_plan_to_payload(plan: RuntimeRealizationPlan) -> EncodedPayload:
    payload: JsonObject = {
        "activity_reference": encode_reference(plan.activity_reference),
        "strategy_reference": encode_reference(plan.strategy_reference),
        "binding_id": plan.binding_id,
        "build_identity": plan.build_identity,
        "dependency_profile": plan.dependency_profile.value,
        "closure_identity": plan.closure_identity,
        "exact_dependency_identities": _pair_list(plan.exact_dependency_identities),
        "exact_role_environment_identities": _pair_list(plan.exact_role_environment_identities),
        "runtime_roles": list(plan.runtime_roles),
        "learned_state_reference": (
            encode_reference(plan.learned_state_reference)
            if plan.learned_state_reference is not None
            else None
        ),
        "direct_input_references": [
            encode_reference(reference) for reference in plan.direct_input_references
        ],
        "limitations": list(plan.limitations),
    }
    return EncodedPayload.from_object(payload)


class ExecutionService:
    """Persist operational truth without acquiring semantic-result ownership."""

    def __init__(
        self,
        store: ControlStore,
        recovery_authority: RecoveryAuthority,
    ) -> None:
        self._store = store
        self._recovery_authority = recovery_authority

    def initialize_execution(
        self,
        state: ExecutionAggregate,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        self._require_global_continuity(state.authority_frontier)
        key = execution_state_key(state.execution_reference)

        existing = self._store.get_current_state(key)
        if existing is not None:
            if self._transition_exists(key, transition_id, "execution-initialized"):
                return self.load(state.execution_reference)
            raise CurrentStateConflict("Execution state already exists")

        record = self._store.create_current_state(
            key=key,
            schema_version=_SCHEMA,
            payload=execution_to_payload(state),
            authority_frontier=state.authority_frontier,
            transition_id=transition_id,
            transition_kind="execution-initialized",
            transition_detail=EncodedPayload.from_object(
                {"activity_reference": encode_reference(state.activity_reference)}
            ),
        )
        return ExecutionSnapshot(
            state=execution_from_payload(record.payload),
            state_version=record.state_version,
        )

    def load(self, execution_reference: TypedReference) -> ExecutionSnapshot:
        record = self._store.get_current_state(execution_state_key(execution_reference))
        if record is None:
            raise RecordNotFound("Execution state does not exist")
        state = execution_from_payload(record.payload)
        if state.execution_reference != execution_reference:
            raise ValueError("stored Execution does not match requested reference")
        return ExecutionSnapshot(state=state, state_version=record.state_version)

    def assess_admission(
        self,
        execution_reference: TypedReference,
        facts: AdmissionFacts,
    ) -> AdmissionDecision:
        snapshot = self.load(execution_reference)
        return self._assess_admission(snapshot.state, facts)

    def prepare_attempt(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        plan: RuntimeRealizationPlan,
        plan_snapshot_id: CommitmentSnapshotId,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        *,
        resume_checkpoint_reference: TypedReference | None = None,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "attempt-prepared",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "attempt-prepared",
        ):
            return snapshot

        self._require_global_continuity(authority_frontier)
        if snapshot.state.authority_frontier != authority_frontier:
            raise ValueError("Execution has not adopted the current recovery frontier")
        if plan.activity_reference != snapshot.state.activity_reference:
            raise ValueError("runtime plan targets a different committed activity")

        plan_reference = runtime_plan_reference(
            execution_reference,
            attempt_id,
            plan_snapshot_id,
        )
        plan_payload = runtime_plan_to_payload(plan)

        if resume_checkpoint_reference is not None:
            self._require_resume_compatibility(
                execution_reference,
                resume_checkpoint_reference,
                plan_payload,
            )

        self._store.put_immutable_binding(
            reference=plan_reference,
            schema_version=_SCHEMA,
            payload=plan_payload,
            authority_frontier=authority_frontier,
        )
        next_state = snapshot.state.prepare_attempt(
            attempt_id=attempt_id,
            runtime_plan_reference=plan_reference,
            authority_frontier=authority_frontier,
            resume_checkpoint_reference=resume_checkpoint_reference,
        )
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "attempt-prepared",
            EncodedPayload.from_object(
                {
                    "attempt_id": attempt_id.value,
                    "runtime_plan_reference": encode_reference(plan_reference),
                    "resume_checkpoint_reference": (
                        encode_reference(resume_checkpoint_reference)
                        if resume_checkpoint_reference is not None
                        else None
                    ),
                }
            ),
        )

    def activate_attempt(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        facts: AdmissionFacts,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "attempt-activated",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "attempt-activated",
        ):
            return snapshot

        decision = self._assess_admission(snapshot.state, facts)
        if decision.status is not AdmissionStatus.ADMITTED:
            raise ValueError(
                f"Attempt admission is {decision.status.value}: {', '.join(decision.reasons)}"
            )
        next_state = snapshot.state.activate_attempt(attempt_id, authority_frontier)
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "attempt-activated",
            EncodedPayload.from_object({"attempt_id": attempt_id.value}),
        )

    def prepare_provider_submission(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        submission_intent_id: LogicalId,
        authority_frontier: RecoveryFrontier,
    ) -> tuple[ExecutionSnapshot, CoordinationIntentRecord]:
        snapshot = self.load(execution_reference)
        key = execution_state_key(execution_reference)
        payload = EncodedPayload.from_object({"attempt_id": attempt_id.value})

        intent = self._store.put_coordination_intent(
            intent_id=submission_intent_id,
            source=execution_reference,
            intent_kind="provider-submission",
            payload=payload,
            authority_frontier=authority_frontier,
        )

        if self._transition_exists(
            key,
            submission_intent_id,
            "provider-submission-prepared",
        ):
            return self.load(execution_reference), intent
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict(
                f"expected Execution version {expected_state_version.value}, "
                f"found {snapshot.state_version.value}"
            )

        next_state = snapshot.state.register_submission_intent(
            attempt_id,
            submission_intent_id,
            authority_frontier,
        )
        result = self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            submission_intent_id,
            "provider-submission-prepared",
            payload,
        )
        return result, intent

    def record_provider_observation(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        observation: ProviderObservation,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        *,
        correlation: str | None = None,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "provider-observation-recorded",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "provider-observation-recorded",
        ):
            return snapshot

        next_state = snapshot.state.record_provider_observation(
            attempt_id=attempt_id,
            observation=observation,
            authority_frontier=authority_frontier,
            correlation=correlation,
        )
        result = self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "provider-observation-recorded",
            EncodedPayload.from_object(
                {
                    "attempt_id": attempt_id.value,
                    "observation": observation.value,
                    "correlation": correlation,
                }
            ),
        )

        attempt = result.state.attempt(attempt_id)
        if attempt.submission_intent_id is not None and (
            correlation is not None or observation is not ProviderObservation.UNKNOWN
        ):
            self._store.acknowledge_coordination_intent(
                attempt.submission_intent_id,
                authority_frontier,
            )
        return result

    def commit_checkpoint(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        checkpoint: CheckpointDescriptor,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "checkpoint-committed",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "checkpoint-committed",
        ):
            return snapshot

        if checkpoint.execution_reference != execution_reference:
            raise ValueError("checkpoint targets a different Execution")
        attempt = snapshot.state.attempt(checkpoint.attempt_id)
        if attempt.epoch != checkpoint.attempt_epoch:
            raise ValueError("checkpoint Attempt epoch does not match")
        if attempt.runtime_plan_reference != checkpoint.runtime_plan_reference:
            raise ValueError("checkpoint runtime plan does not match Attempt")
        if checkpoint.authority_frontier != authority_frontier:
            raise ValueError("checkpoint was not produced under current recovery authority")

        self._store.put_immutable_binding(
            reference=checkpoint.reference,
            schema_version=_SCHEMA,
            payload=checkpoint_to_payload(checkpoint),
            authority_frontier=authority_frontier,
        )
        next_state = snapshot.state.attach_checkpoint(
            attempt_id=checkpoint.attempt_id,
            checkpoint_reference=checkpoint.reference,
            authority_frontier=authority_frontier,
        )
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "checkpoint-committed",
            EncodedPayload.from_object(
                {
                    "attempt_id": checkpoint.attempt_id.value,
                    "checkpoint_reference": encode_reference(checkpoint.reference),
                }
            ),
        )

    def record_attempt_outcome(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        outcome: AttemptStatus,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "attempt-outcome-recorded",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "attempt-outcome-recorded",
        ):
            return snapshot

        next_state = snapshot.state.record_attempt_outcome(
            attempt_id,
            outcome,
            authority_frontier,
        )
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "attempt-outcome-recorded",
            EncodedPayload.from_object({"attempt_id": attempt_id.value, "outcome": outcome.value}),
        )

    def fence_indeterminate_attempt(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        attempt_id: LogicalId,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "indeterminate-attempt-fenced",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "indeterminate-attempt-fenced",
        ):
            return snapshot

        next_state = snapshot.state.fence_indeterminate_attempt(
            attempt_id,
            authority_frontier,
        )
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "indeterminate-attempt-fenced",
            EncodedPayload.from_object({"attempt_id": attempt_id.value}),
        )

    def request_cancellation(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "cancellation-requested",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "cancellation-requested",
        ):
            return snapshot
        next_state = snapshot.state.request_cancellation(authority_frontier)
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "cancellation-requested",
            EncodedPayload.from_object({}),
        )

    def confirm_cancelled(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "execution-cancelled",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "execution-cancelled",
        ):
            return snapshot
        next_state = snapshot.state.confirm_cancelled(authority_frontier)
        return self._persist_transition(
            snapshot,
            next_state,
            authority_frontier,
            transition_id,
            "execution-cancelled",
            EncodedPayload.from_object({}),
        )

    def begin_regressive_recovery(self) -> RecoveryFrontier:
        store_frontier = self._store.current_recovery_frontier()
        recovery_frontier = self._recovery_authority.current_frontier()
        observed = RecoveryFrontier(max(store_frontier.value, recovery_frontier.value))
        fresh = self._recovery_authority.advance_after(observed)
        self._store.advance_recovery_frontier(store_frontier, fresh)
        return fresh

    def reconcile_execution_after_recovery(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        fresh_frontier: RecoveryFrontier,
        transition_id: LogicalId,
    ) -> ExecutionSnapshot:
        self._require_global_continuity(fresh_frontier)
        snapshot = self._load_expected_or_replayed(
            execution_reference,
            expected_state_version,
            transition_id,
            "execution-recovered",
        )
        if self._transition_exists(
            execution_state_key(execution_reference),
            transition_id,
            "execution-recovered",
        ):
            return snapshot

        next_state = snapshot.state.adopt_recovery_frontier(fresh_frontier)
        return self._persist_transition(
            snapshot,
            next_state,
            fresh_frontier,
            transition_id,
            "execution-recovered",
            EncodedPayload.from_object({"fresh_frontier": fresh_frontier.value}),
        )

    def resolve_checkpoint(
        self,
        checkpoint_reference: TypedReference,
    ) -> CheckpointDescriptor:
        resolution = self._store.resolve_immutable_binding(checkpoint_reference)
        if resolution.status is not ResolutionStatus.RESOLVED or resolution.record is None:
            raise RecordNotFound("checkpoint is not exactly resolvable")
        checkpoint = checkpoint_from_payload(resolution.record.payload)
        if checkpoint.reference != checkpoint_reference:
            raise ValueError("resolved checkpoint identity does not match reference")
        return checkpoint

    def _require_resume_compatibility(
        self,
        execution_reference: TypedReference,
        checkpoint_reference: TypedReference,
        new_plan_payload: EncodedPayload,
    ) -> None:
        checkpoint = self.resolve_checkpoint(checkpoint_reference)
        if checkpoint.execution_reference != execution_reference:
            raise ValueError("checkpoint belongs to a different Execution")
        prior_plan = self._store.resolve_immutable_binding(checkpoint.runtime_plan_reference)
        if prior_plan.status is not ResolutionStatus.RESOLVED or prior_plan.record is None:
            raise RecordNotFound("checkpoint runtime plan is not exactly resolvable")
        if prior_plan.record.payload != new_plan_payload:
            raise ValueError("checkpoint runtime plan is not exactly compatible with retry plan")

    def _assess_admission(
        self,
        state: ExecutionAggregate,
        facts: AdmissionFacts,
    ) -> AdmissionDecision:
        store_frontier = self._store.current_recovery_frontier()
        authority_frontier = self._recovery_authority.current_frontier()
        if store_frontier != authority_frontier or state.authority_frontier != store_frontier:
            return AdmissionDecision(
                AdmissionStatus.RECONCILIATION_REQUIRED,
                ("recovery continuity is not current",),
            )
        if state.terminal or state.cancellation_requested:
            return AdmissionDecision(
                AdmissionStatus.CANCELLED_OR_TERMINAL,
                ("Execution is cancelled or terminal",),
            )
        if state.current_attempt_id is not None:
            return AdmissionDecision(
                AdmissionStatus.BLOCKED,
                ("Execution already has a current Attempt",),
            )

        checks = (
            ("current authorization unavailable", facts.current_authorization),
            ("runtime closure is not current", facts.runtime_closure_current),
            ("required references are not resolvable", facts.references_resolvable),
        )
        for reason, value in checks:
            if value is False:
                return AdmissionDecision(AdmissionStatus.BLOCKED, (reason,))
        if facts.provider_guarantees_sufficient is False:
            return AdmissionDecision(
                AdmissionStatus.INCOMPATIBLE,
                ("required provider/deployment guarantee is unavailable",),
            )
        if facts.capacity_available is False:
            return AdmissionDecision(
                AdmissionStatus.QUEUED,
                ("temporary resource capacity is unavailable",),
            )
        values = (
            facts.current_authorization,
            facts.runtime_closure_current,
            facts.references_resolvable,
            facts.provider_guarantees_sufficient,
            facts.capacity_available,
        )
        if any(value is None for value in values):
            return AdmissionDecision(
                AdmissionStatus.INDETERMINATE,
                ("one or more current admission facts are unknown",),
            )
        return AdmissionDecision(AdmissionStatus.ADMITTED)

    def _require_global_continuity(self, frontier: RecoveryFrontier) -> None:
        store_frontier = self._store.current_recovery_frontier()
        authority_frontier = self._recovery_authority.current_frontier()
        if frontier != store_frontier or frontier != authority_frontier:
            raise ValueError("control-store and recovery-authority frontiers are not aligned")

    def _load_expected_or_replayed(
        self,
        execution_reference: TypedReference,
        expected_state_version: StateVersion,
        transition_id: LogicalId,
        transition_kind: str,
    ) -> ExecutionSnapshot:
        key = execution_state_key(execution_reference)
        if self._transition_exists(key, transition_id, transition_kind):
            return self.load(execution_reference)
        snapshot = self.load(execution_reference)
        if snapshot.state_version != expected_state_version:
            raise CurrentStateConflict(
                f"expected Execution version {expected_state_version.value}, "
                f"found {snapshot.state_version.value}"
            )
        return snapshot

    def _transition_exists(
        self,
        key: ResourceKey,
        transition_id: LogicalId,
        transition_kind: str,
    ) -> bool:
        for record in self._store.list_transition_history(key):
            if record.transition_id == transition_id:
                if record.transition_kind != transition_kind:
                    raise CurrentStateConflict(
                        "transition identity was reused for a different operation"
                    )
                return True
        return False

    def _persist_transition(
        self,
        snapshot: ExecutionSnapshot,
        next_state: ExecutionAggregate,
        authority_frontier: RecoveryFrontier,
        transition_id: LogicalId,
        transition_kind: str,
        detail: EncodedPayload,
    ) -> ExecutionSnapshot:
        key = execution_state_key(snapshot.state.execution_reference)
        record = self._store.compare_and_swap_current_state(
            key=key,
            expected_state_version=snapshot.state_version,
            authority_frontier=authority_frontier,
            schema_version=_SCHEMA,
            payload=execution_to_payload(next_state),
            transition_id=transition_id,
            transition_kind=transition_kind,
            transition_detail=detail,
        )
        return ExecutionSnapshot(
            state=execution_from_payload(record.payload),
            state_version=record.state_version,
        )
