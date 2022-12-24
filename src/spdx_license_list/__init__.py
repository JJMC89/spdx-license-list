"""SPDX License List as a dictionary."""
from __future__ import annotations

from typing import NamedTuple


class License(NamedTuple):
    """Data for a license."""

    id: str
    name: str
    deprecated_id: bool
    fsf_libre: bool
    osi_approved: bool


LICENSES: dict[str, License] = {}
