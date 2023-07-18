from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Position:
    q: int = None
    r: int = None
    s: int = None

    def __add__(self, other: Position) -> Position:
        new_q = self.q + other.q
        new_r = self.r + other.r
        new_s = self.s + other.s
        return Position(new_q, new_r, new_s)

# TODO make a step class that pieces know what they can do
# class Step:
#     pass
