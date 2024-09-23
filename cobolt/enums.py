from __future__ import annotations

from enum import Enum, auto

__all__ = ("Status",)


class Status(Enum):
    ERROR = auto()
    PICKER = auto()
    REDIRECT = auto()
    TUNNEL = auto()
