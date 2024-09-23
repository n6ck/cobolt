from __future__ import annotations

from enum import Enum

__all__ = ("Status",)


class Status(str, Enum):
    ERROR = "error"
    PICKER = "picker"
    REDIRECT = "redirect"
    TUNNEL = "tunnel"
