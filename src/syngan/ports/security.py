"""Ports for current external security, trust, secret, and audit authorities."""

from __future__ import annotations

from typing import Protocol

from syngan.foundation.security import (
    AuthorizationDecision,
    AuthorizationRequest,
    SecretMaterial,
    SecretRef,
    SecurityAuditEvent,
)


class AuthorizationAuthority(Protocol):
    def authorize(self, request: AuthorizationRequest) -> AuthorizationDecision: ...


class SecretBroker(Protocol):
    def resolve(self, secret_ref: SecretRef) -> SecretMaterial: ...


class SecurityAuditSink(Protocol):
    def emit(self, event: SecurityAuditEvent) -> None: ...
