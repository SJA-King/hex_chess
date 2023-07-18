from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from constants import PieceNames, Players
from position import Position


@dataclass
class Piece:
    player: str = ""
    name: PieceNames = PieceNames.Piece
    # step: [str] = field(default_factory=[])  # TODO change to list(Positions)
    # step_repetition: int = 0
    # pieces_taken: [Piece] = field(default_factory=[])
    value: int = field(default=0)
    starting_position: Position = None

    def __post_init__(self):
        if not self.player:
            raise Exception(f"{self.name.value} WASNT given a player!")
        if not self.starting_position:
            raise Exception(f"{self.name.value} WASNT given a starting position!")
        self.position: Position = self.starting_position

    # @property
    # def value(self) -> int:
    #     return self._value

    def __ge__(self, other: Piece):
        return self.value > other.value

    def __le__(self, other: Piece):
        return self.value < other.value


@dataclass
class Pawn(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.Pawn, _value=1)


@dataclass
class Bishop(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.Bishop, _value=3)


@dataclass
class Knight(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.Knight, _value=3)


@dataclass
class Rook(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.Rook, _value=5)


@dataclass
class Queen(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.Queen, _value=9)


@dataclass
class King(Piece):
    def __init__(self):
        super().__init__(name=PieceNames.King, _value=99)

