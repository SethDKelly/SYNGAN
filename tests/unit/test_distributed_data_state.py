from __future__ import annotations

import pytest

from syngan.domain.generation_data import (
    CandidateStatus,
    GenerationDataState,
    generation_data_state_from_payload,
    generation_data_state_to_payload,
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
    sealed_subject_from_payload,
    sealed_subject_to_payload,
    topology_from_payload,
    topology_to_payload,
)
from syngan.foundation.identity import (
    AuthorityScope,
    CommitmentSnapshotId,
    LogicalId,
    ResourceKey,
    ResourceKind,
    SemanticRevisionId,
    TypedReference,
)
from syngan.foundation.representation import EncodedPayload


def semantic_reference(revision: str = "meaning-r1") -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("test"),
            kind=ResourceKind("data-meaning"),
            resource_id=LogicalId("meaning-1"),
        ),
        revision_id=SemanticRevisionId(revision),
    )


def generation_commitment() -> TypedReference:
    return TypedReference(
        key=ResourceKey(
            scope=AuthorityScope("test"),
            kind=ResourceKind("generation"),
            resource_id=LogicalId("generation-1"),
        ),
        commitment_snapshot_id=CommitmentSnapshotId("commitment-1"),
    )


def topology(*scope_ids: str, coordinated: bool = False) -> TopologyDescriptor:
    return TopologyDescriptor(
        scopes=tuple(LogicalScope(scope_id) for scope_id in scope_ids),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=semantic_reference(),
                scope_ids=tuple(scope_ids),
            ),
        ),
        hints=(
            (TopologyHint.MULTI_TABLE, TopologyHint.COMPOSITE)
            if len(scope_ids) > 1
            else (TopologyHint.SINGLE_TABLE,)
        ),
        requires_coordinated_cut=coordinated,
    )


def strong_subject(
    candidate_id: LogicalId,
    descriptor: TopologyDescriptor,
    *,
    coordination: CoordinationStrength = CoordinationStrength.INDEPENDENT,
) -> SealedPhysicalSubject:
    commitment = generation_commitment()
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
                locator=f"provider://snapshot/{candidate_id.value}/{scope_id}",
                immutable_token=f"version-{candidate_id.value}-{scope_id}",
                structural_summary=EncodedPayload.from_object({"columns": 3}),
                extent_summary=EncodedPayload.from_object({"rows": 10}),
            )
            for scope_id in descriptor.scope_ids
        ),
        strength=PhysicalSubjectStrength(
            identity=IdentityStrength.EXACT,
            read_binding=ReadBindingStrength.EXACT,
            integrity=IntegrityStrength.CLOSED_ROOT,
            retention=RetentionStrength.DECLARED,
            coordination=coordination,
        ),
        root_summary=EncodedPayload.from_object({"scope_count": len(descriptor.scopes)}),
    )


def test_topology_round_trip_preserves_exact_scope_composition() -> None:
    descriptor = TopologyDescriptor(
        scopes=(LogicalScope("entities"), LogicalScope("events")),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=semantic_reference(),
                scope_ids=("entities", "events"),
            ),
        ),
        hints=(TopologyHint.TIME_SERIES, TopologyHint.COMPOSITE),
        requires_coordinated_cut=True,
    )

    assert topology_from_payload(topology_to_payload(descriptor)) == descriptor


def test_topology_rejects_nonexact_semantic_binding() -> None:
    reference = TypedReference(key=semantic_reference().key)

    with pytest.raises(ValueError, match="exact reference"):
        SemanticBinding(
            role="data-meaning",
            reference=reference,
            scope_ids=("records",),
        )


@pytest.mark.parametrize(
    ("identity", "read_binding", "integrity"),
    [
        (
            IdentityStrength.DISTINGUISHABLE,
            ReadBindingStrength.EXACT,
            IntegrityStrength.CLOSED_ROOT,
        ),
        (
            IdentityStrength.EXACT,
            ReadBindingStrength.MUTABLE,
            IntegrityStrength.CLOSED_ROOT,
        ),
        (
            IdentityStrength.EXACT,
            ReadBindingStrength.EXACT,
            IntegrityStrength.DECLARED,
        ),
    ],
)
def test_sealed_subject_rejects_weak_physical_strength(
    identity: IdentityStrength,
    read_binding: ReadBindingStrength,
    integrity: IntegrityStrength,
) -> None:
    descriptor = topology("records")
    candidate_id = LogicalId("candidate-1")
    reference = generation_physical_subject_reference(
        generation_commitment(),
        candidate_id,
        CommitmentSnapshotId("seal-1"),
    )

    with pytest.raises(ValueError):
        SealedPhysicalSubject(
            reference=reference,
            topology=descriptor,
            scopes=(
                PhysicalScopeBinding(
                    scope_id="records",
                    locator="provider://records",
                    immutable_token="version-1",
                ),
            ),
            strength=PhysicalSubjectStrength(
                identity=identity,
                read_binding=read_binding,
                integrity=integrity,
                retention=RetentionStrength.UNKNOWN,
                coordination=CoordinationStrength.INDEPENDENT,
            ),
        )


def test_coordinated_topology_requires_coordinated_physical_cut() -> None:
    descriptor = topology("customers", "orders", coordinated=True)

    with pytest.raises(ValueError, match="coordinated"):
        strong_subject(
            LogicalId("candidate-1"),
            descriptor,
            coordination=CoordinationStrength.INDEPENDENT,
        )


def test_sealed_subject_round_trip_is_bounded_and_exact() -> None:
    descriptor = topology("customers", "orders", coordinated=True)
    subject = strong_subject(
        LogicalId("candidate-1"),
        descriptor,
        coordination=CoordinationStrength.COORDINATED,
    )

    assert sealed_subject_from_payload(sealed_subject_to_payload(subject)) == subject


def test_generation_requires_data_meaning_binding() -> None:
    descriptor = TopologyDescriptor(
        scopes=(LogicalScope("records"),),
        semantic_bindings=(),
    )

    with pytest.raises(ValueError, match="data-meaning"):
        GenerationDataState(
            generation_commitment=generation_commitment(),
            topology=descriptor,
        )



def test_generation_requires_data_meaning_revision_for_every_scope() -> None:
    commitment_binding = TypedReference(
        key=semantic_reference().key,
        commitment_snapshot_id=CommitmentSnapshotId("meaning-snapshot"),
    )
    wrong_axis = TopologyDescriptor(
        scopes=(LogicalScope("records"),),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=commitment_binding,
                scope_ids=("records",),
            ),
        ),
    )
    with pytest.raises(ValueError, match="semantic revision"):
        GenerationDataState(
            generation_commitment=generation_commitment(),
            topology=wrong_axis,
        )

    incomplete = TopologyDescriptor(
        scopes=(LogicalScope("customers"), LogicalScope("orders")),
        semantic_bindings=(
            SemanticBinding(
                role="data-meaning",
                reference=semantic_reference(),
                scope_ids=("customers",),
            ),
        ),
    )
    with pytest.raises(ValueError, match="cover every logical scope"):
        GenerationDataState(
            generation_commitment=generation_commitment(),
            topology=incomplete,
        )

def test_generation_multiple_candidates_still_allow_only_one_completed_output() -> None:
    descriptor = topology("records")
    candidate_1 = LogicalId("candidate-1")
    candidate_2 = LogicalId("candidate-2")
    subject_1 = strong_subject(candidate_1, descriptor)

    state = GenerationDataState(
        generation_commitment=generation_commitment(),
        topology=descriptor,
    )
    state = state.add_candidate(candidate_1).add_candidate(candidate_2)
    assert state.completed_output is None

    state = state.seal_candidate(candidate_1, subject_1.reference)
    assert state.candidate(candidate_1).status is CandidateStatus.SEALED
    assert state.completed_output is None
    assert state.candidate(candidate_2).status is CandidateStatus.OPEN

    state = state.promote_owner_validated_candidate(
        candidate_id=candidate_1,
        output_id=LogicalId("output-1"),
    )
    assert state.completed_output is not None
    assert state.completed_output.sealed_subject_reference == subject_1.reference
    assert state.candidate(candidate_1).status is CandidateStatus.PROMOTED

    with pytest.raises(ValueError, match="already has a completed output"):
        state.promote_owner_validated_candidate(
            candidate_id=candidate_1,
            output_id=LogicalId("output-2"),
        )


def test_generation_data_state_round_trip_preserves_promotion_basis() -> None:
    descriptor = topology("records")
    candidate_id = LogicalId("candidate-1")
    subject = strong_subject(candidate_id, descriptor)
    basis = semantic_reference("meaning-r2")

    state = GenerationDataState(
        generation_commitment=generation_commitment(),
        topology=descriptor,
    )
    state = state.add_candidate(candidate_id)
    state = state.seal_candidate(candidate_id, subject.reference)
    state = state.promote_owner_validated_candidate(
        candidate_id=candidate_id,
        output_id=LogicalId("output-1"),
        completion_basis_references=(basis,),
    )

    assert generation_data_state_from_payload(generation_data_state_to_payload(state)) == state
