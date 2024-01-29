# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import annotations

import typing

from cryptography.hazmat.bindings._rust import x509 as rust_x509
from cryptography.x509.general_name import DNSName, IPAddress

__all__ = [
    "Store",
    "Subject",
    "ServerVerifier",
    "PolicyBuilder",
    "VerificationError",
]

Store = rust_x509.Store
Subject = typing.Union[DNSName, IPAddress]
ServerVerifier = rust_x509.ServerVerifier
# PolicyBuilder = rust_x509.PolicyBuilder
VerificationError = rust_x509.VerificationError


def PolicyBuilder() -> rust_x509.PolicyBuilder:  # noqa: N802
    raise RuntimeError(
        "Downstream does not support unstable X.509 path verification in "
        "c10s / RHEL 10, see https://issues.redhat.com/browse/RHEL-23012"
    )
