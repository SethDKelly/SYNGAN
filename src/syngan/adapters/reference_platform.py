"""Provider-neutral reference platform adapter for capability-contract verification.

This adapter is intentionally not a Spark, Databricks, cloud, or enterprise-scale
implementation. It exists only to prove the portable capability-provider contract.
"""

from __future__ import annotations

from dataclasses import dataclass

from syngan.foundation.platform import (
    CapabilityAssertion,
    PlatformQualificationContext,
)


@dataclass(frozen=True, slots=True)
class StaticPlatformCapabilityProvider:
    context: PlatformQualificationContext
    assertions: tuple[CapabilityAssertion, ...]

    def __post_init__(self) -> None:
        if any(assertion.context != self.context for assertion in self.assertions):
            raise ValueError("reference provider assertions must share one exact context")

    def describe_capabilities(
        self,
        context: PlatformQualificationContext,
    ) -> tuple[CapabilityAssertion, ...]:
        if context != self.context:
            return ()
        return self.assertions
