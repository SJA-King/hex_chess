from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from constants import Positions


@dataclass
class Piece:
    player: str = ""
    # step: [str] = field(default_factory=[])  # TODO change to list(Positions)
    # step_repetition: int = 0
    # pieces_taken: [Piece] = field(default_factory=[])
    _value: int = field(default=0)

    @property
    def value(self) -> int:
        return self._value

    def __ge__(self, other: Piece):
        return self.value > other.value

    def __le__(self, other: Piece):
        return self.value < other.value


@dataclass
class Pawn(Piece):
    def __init__(self):
        super().__init__(_value=1)


@dataclass
class Bishop(Piece):
    def __init__(self):
        super().__init__(_value=3)


@dataclass
class Knight(Piece):
    def __init__(self):
        super().__init__(_value=3)


@dataclass
class Rook(Piece):
    def __init__(self):
        super().__init__(_value=5)


@dataclass
class Queen(Piece):
    def __init__(self):
        super().__init__(_value=9)


@dataclass
class King(Piece):
    def __init__(self):
        super().__init__(_value=99)

