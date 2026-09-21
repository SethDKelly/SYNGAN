"""Optional runtime/platform telemetry port."""

from __future__ import annotations

from typing import Protocol

from syngan.foundation.observability import TelemetryEvent


class TelemetryUnavailable(RuntimeError):
    pass


class TelemetrySink(Protocol):
    def emit(self, event: TelemetryEvent) -> None: ...
