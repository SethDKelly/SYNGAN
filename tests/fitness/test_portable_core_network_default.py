from __future__ import annotations

import socket

import pytest
import pytest_socket


def test_socket_creation_is_denied_in_portable_core_profile() -> None:
    with pytest.raises(pytest_socket.SocketBlockedError):
        socket.socket()
