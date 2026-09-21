"""Small self-contained source-derived text reference runtime.

This adapter exists to prove the supported local/no-network text path. It is deliberately
bounded and is not an enterprise-scale or fidelity reference implementation.
"""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass

from syngan.foundation.identity import TypedReference
from syngan.foundation.representation import EncodedPayload
from syngan.foundation.runtime import (
    DependencyProfile,
    ImplementationBinding,
)


@dataclass(frozen=True, slots=True)
class SourceDerivedTextState:
    weighted_values: tuple[tuple[str, int], ...]
    observed_count: int
    truncated: bool

    def __post_init__(self) -> None:
        if not self.weighted_values:
            raise ValueError("source-derived text state requires at least one retained value")
        if self.observed_count < 1:
            raise ValueError("observed_count must be positive")
        if any(weight < 1 for _, weight in self.weighted_values):
            raise ValueError("source-derived text weights must be positive")


def reference_source_derived_binding(
    strategy_reference: TypedReference,
) -> ImplementationBinding:
    """Return the bounded built-in binding for the portable source-derived text path."""

    return ImplementationBinding(
        binding_id="builtin.source-derived-text.v1",
        strategy_reference=strategy_reference,
        build_identity="syngan.source-derived-text.stdlib.v1",
        dependency_profile=DependencyProfile.SELF_CONTAINED,
        required_roles=("local-worker",),
        dependency_requirements=(),
        limitations=(
            "bounded-distinct-value-summary",
            "source-derived-only",
            "not-enterprise-scale-qualified",
        ),
        source_derived_text_capable=True,
    )


def learn_source_derived_text(
    values: tuple[str, ...],
    *,
    max_distinct_values: int = 256,
) -> SourceDerivedTextState:
    if max_distinct_values < 1:
        raise ValueError("max_distinct_values must be positive")
    if not values:
        raise ValueError("source-derived text learning requires at least one value")

    counts = Counter(values)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    retained = tuple(ordered[:max_distinct_values])
    return SourceDerivedTextState(
        weighted_values=retained,
        observed_count=len(values),
        truncated=len(ordered) > len(retained),
    )


def generate_source_derived_text(
    state: SourceDerivedTextState,
    *,
    count: int,
    seed: int,
) -> tuple[str, ...]:
    if count < 0:
        raise ValueError("generation count must be non-negative")
    values = [value for value, _ in state.weighted_values]
    weights = [weight for _, weight in state.weighted_values]
    rng = random.Random(seed)
    return tuple(rng.choices(values, weights=weights, k=count))


def generate_source_derived_text_direct(
    values: tuple[str, ...],
    *,
    count: int,
    seed: int,
    max_distinct_values: int = 256,
) -> tuple[str, ...]:
    """Generate through a transient source-derived summary without creating Learned State."""

    state = learn_source_derived_text(
        values,
        max_distinct_values=max_distinct_values,
    )
    return generate_source_derived_text(state, count=count, seed=seed)


def source_derived_text_state_to_payload(state: SourceDerivedTextState) -> EncodedPayload:
    return EncodedPayload.from_object(
        {
            "weighted_values": [
                {"value": value, "weight": weight} for value, weight in state.weighted_values
            ],
            "observed_count": state.observed_count,
            "truncated": state.truncated,
        }
    )


def source_derived_text_state_from_payload(payload: EncodedPayload) -> SourceDerivedTextState:
    value = payload.as_object()
    weighted = value.get("weighted_values")
    observed = value.get("observed_count")
    truncated = value.get("truncated")
    if not isinstance(weighted, list):
        raise ValueError("weighted_values must be a list")
    if not isinstance(observed, int) or isinstance(observed, bool):
        raise ValueError("observed_count must be an integer")
    if not isinstance(truncated, bool):
        raise ValueError("truncated must be boolean")

    parsed: list[tuple[str, int]] = []
    for item in weighted:
        if not isinstance(item, dict):
            raise ValueError("weighted text entry must be an object")
        text = item.get("value")
        weight = item.get("weight")
        if not isinstance(text, str):
            raise ValueError("weighted text value must be a string")
        if not isinstance(weight, int) or isinstance(weight, bool):
            raise ValueError("weighted text weight must be an integer")
        parsed.append((text, weight))

    return SourceDerivedTextState(
        weighted_values=tuple(parsed),
        observed_count=observed,
        truncated=truncated,
    )
