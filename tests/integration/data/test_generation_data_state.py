from __future__ import annotations

from pathlib import Path

import pytest

from syngan.adapters.sqlite_control_store import SQLiteControlStore
from syngan.application.generation_data_state import GenerationDataStateService
from syngan.domain.generation_data import (
    CandidateStatus,
    GenerationDataState,
    generation_physical_subject_reference,
)
from syngan.foundation.data_state import (
    CoordinationStrength,
    IdentityStrength,
    IntegrityStrength,
    LogicalScope,
    PhysicalScopeBinding,
    PhysicalSubjectStrength,
    ReadBindingStrength,
    RetentionStrength,
    SealedPhysicalSubject,
    SemanticBinding,
    TopologyDescriptor,
    TopologyHint,
    sealed_subject_to_payload,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    RecoveryFrontier,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    StateVersion,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload
from syngan.ports.control_store import CurrentStateConflict, ResolutionStatus

pytestmark = pytest.mark.integration

SCOPE = AuthorityScope("test")
FRONTIER = RecoveryFrontier(0)


def exact_reference(kind: str, resource_id: str, revision: str) -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=SCOPE,
            kind=ResourceKind(kind),
            resource_id=LogicalId(resource_id),
        ),
        revision_id=SemanticRevisionId(revision),
    )


def generation_commitment(resource_id: str = "generation-1") -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=SCOPE,
            kind=ResourceKind("generation"),
            resource_id=LogicalId(resource_id),
        ),
        commitment_snapshot_id=CommitmentSnapshotId(f"{resource_id}-commitment"),
    )


def topology() -> TopologyDescriptor:
    return TopologyDescriptor(
        scopes=(LogicalScope("customers"), LogicalScope("orders")),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=exact_reference("data-meaning", "meaning-1", "r1"),
                scope_ids=("customers", "orders"),
            ),
        ),
        hints=(TopologyHint.MULTI_TABLE,),
        requires_coordinated_cut=True,
    )


def sealed_subject(
    commitment: TypedReference,
    candidate_id: LogicalId,
    descriptor: TopologyDescriptor,
    *,
    locator_suffix: str = "v1",
) -> SealedPhysicalSubject:
    reference = generation_physical_subject_reference(
        commitment,
        candidate_id,
        CommitmentSnapshotId(f"seal-{candidate_id.value}"),
    )
    return SealedPhysicalSubject(
        reference=reference,
        topology=descriptor,
        scopes=tuple(
            PhysicalScopeBinding(
                scope_id=scope_id,
                locator=f"provider://root/{scope_id}/{locator_suffix}",
                immutable_token=f"{scope_id}-{locator_suffix}",
                structural_summary=EncodedPayload.from_object({"physical_fields": 4}),
                extent_summary=EncodedPayload.from_object({"rows": 25}),
            )
            for scope_id in descriptor.scope_ids
        ),
        strength=PhysicalSubjectStrength(
            identity=IdentityStrength.EXACT,
            read_binding=ReadBindingStrength.EXACT,
            integrity=IntegrityStrength.CLOSED_ROOT,
            retention=RetentionStrength.DECLARED,
            coordination=CoordinationStrength.COORDINATED,
        ),
        root_summary=EncodedPayload.from_object({"scope_count": 2}),
    )


def test_generation_candidate_seal_and_promotion_are_durable_metadata_only(
    tmp_path: Path,
) -> None:
    database = tmp_path / "control.sqlite"
    commitment = generation_commitment()
    descriptor = topology()
    candidate_id = LogicalId("candidate-1")
    subject = sealed_subject(commitment, candidate_id, descriptor)

    with SQLiteControlStore(database, SCOPE) as store:
        service = GenerationDataStateService(store)
        snapshot = service.initialize(
            GenerationDataState(
                generation_commitment=commitment,
                topology=descriptor,
            ),
            FRONTIER,
            LogicalId("initialize"),
        )
        assert snapshot.state_version == StateVersion(0)

        snapshot = service.register_candidate(
            commitment,
            snapshot.state_version,
            candidate_id,
            FRONTIER,
            LogicalId("register"),
        )
        assert snapshot.state.completed_output is None
        assert snapshot.state.candidate(candidate_id).status is CandidateStatus.OPEN

        snapshot = service.seal_candidate(
            commitment,
            snapshot.state_version,
            candidate_id,
            subject,
            FRONTIER,
            LogicalId("seal"),
        )
        assert snapshot.state.completed_output is None
        assert snapshot.state.candidate(candidate_id).status is CandidateStatus.SEALED

        before = store.resolve_immutable_binding(subject.reference)
        assert before.status is ResolutionStatus.RESOLVED
        assert before.record is not None
        assert before.record.payload == sealed_subject_to_payload(subject)

        snapshot = service.promote_owner_validated_candidate(
            commitment,
            snapshot.state_version,
            candidate_id,
            LogicalId("output-1"),
            (exact_reference("generation-basis", "basis-1", "r1"),),
            FRONTIER,
            LogicalId("promote"),
        )
        assert snapshot.state.completed_output is not None
        assert snapshot.state.completed_output.sealed_subject_reference == subject.reference
        assert snapshot.state.candidate(candidate_id).status is CandidateStatus.PROMOTED

        after = store.resolve_immutable_binding(subject.reference)
        assert after == before

    with SQLiteControlStore(database, SCOPE) as reopened:
        loaded = GenerationDataStateService(reopened).load(commitment)
        assert loaded.state_version == StateVersion(3)
        assert loaded.state.completed_output is not None
        assert loaded.state.completed_output.output_id == LogicalId("output-1")
        assert loaded.state.completed_output.sealed_subject_reference == subject.reference


def test_stale_generation_state_version_cannot_register_candidate(tmp_path: Path) -> None:
    commitment = generation_commitment()
    descriptor = topology()

    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = GenerationDataStateService(store)
        snapshot = service.initialize(
            GenerationDataState(commitment, descriptor),
            FRONTIER,
            LogicalId("initialize"),
        )
        service.register_candidate(
            commitment,
            snapshot.state_version,
            LogicalId("candidate-1"),
            FRONTIER,
            LogicalId("register-1"),
        )

        with pytest.raises(CurrentStateConflict):
            service.register_candidate(
                commitment,
                snapshot.state_version,
                LogicalId("candidate-2"),
                FRONTIER,
                LogicalId("register-stale"),
            )


def test_seal_rejects_subject_from_different_committed_topology(tmp_path: Path) -> None:
    commitment = generation_commitment()
    descriptor = topology()
    candidate_id = LogicalId("candidate-1")
    mismatched = TopologyDescriptor(
        scopes=(LogicalScope("customers"),),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=exact_reference("data-meaning", "meaning-1", "r1"),
                scope_ids=("customers",),
            ),
        ),
        hints=(TopologyHint.SINGLE_TABLE,),
    )
    subject = sealed_subject(commitment, candidate_id, mismatched)

    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = GenerationDataStateService(store)
        snapshot = service.initialize(
            GenerationDataState(commitment, descriptor),
            FRONTIER,
            LogicalId("initialize"),
        )
        snapshot = service.register_candidate(
            commitment,
            snapshot.state_version,
            candidate_id,
            FRONTIER,
            LogicalId("register"),
        )

        with pytest.raises(ValueError, match="topology"):
            service.seal_candidate(
                commitment,
                snapshot.state_version,
                candidate_id,
                subject,
                FRONTIER,
                LogicalId("seal"),
            )


def test_unpromoted_candidates_are_never_completed_output(tmp_path: Path) -> None:
    commitment = generation_commitment()
    descriptor = topology()
    open_candidate = LogicalId("open-candidate")
    sealed_candidate = LogicalId("sealed-candidate")

    with SQLiteControlStore(tmp_path / "control.sqlite", SCOPE) as store:
        service = GenerationDataStateService(store)
        snapshot = service.initialize(
            GenerationDataState(commitment, descriptor),
            FRONTIER,
            LogicalId("initialize"),
        )
        snapshot = service.register_candidate(
            commitment,
            snapshot.state_version,
            open_candidate,
            FRONTIER,
            LogicalId("register-open"),
        )
        snapshot = service.register_candidate(
            commitment,
            snapshot.state_version,
            sealed_candidate,
            FRONTIER,
            LogicalId("register-sealed"),
        )
        snapshot = service.seal_candidate(
            commitment,
            snapshot.state_version,
            sealed_candidate,
            sealed_subject(commitment, sealed_candidate, descriptor),
            FRONTIER,
            LogicalId("seal"),
        )

        assert snapshot.state.completed_output is None
        assert snapshot.state.candidate(open_candidate).status is CandidateStatus.OPEN
        assert snapshot.state.candidate(sealed_candidate).status is CandidateStatus.SEALED
