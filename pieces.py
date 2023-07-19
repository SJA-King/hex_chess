from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from constants import PieceNames, Players
from position import Position, Step


@dataclass
class Piece:
    player: str = ""
    name: PieceNames = PieceNames.Piece.value
    value: int = field(default=0)
    start: Position = None

    def __init__(self):
        self.last_moved: int = 0
        self.pieces_taken: [Piece] = None
        self.moved: bool = False
        self.current: Position = self.start
        self.last: Position = self.start

    def __post_init__(self):
        if not self.player:
            raise Exception(f"{self.name.value} WASNT given a player!")
        if not self.start:
            raise Exception(f"{self.name.value} WASNT given a starting position!")

    def __ge__(self, other: Piece):
        return self.value > other.value

    def __le__(self, other: Piece):
        return self.value < other.value

    # TODO make test
    def move_to(self, step: Step, turn: int) -> None:
        self.last = self.current
        self.current += step.vector
        self.last_moved = turn

    def take(self):
        raise NotImplementedError

    def possible_moves(self):
        raise NotImplementedError


@dataclass
class Pawn(Piece):

    def __post_init__(self):
        self.name = PieceNames.Pawn.value
        self.value = 1
        super(Pawn, self).__post_init__()

    # TODO - think about this - it may go in Game
    def promote(self, piece: Piece):
        raise NotImplementedError


@dataclass
class Bishop(Piece):
    def __post_init__(self):
        self.name = PieceNames.Bishop.value
        self.value = 3


@dataclass
class Knight(Piece):
    def __post_init__(self):
        self.name = PieceNames.Knight.value
        self.value = 3


@dataclass
class Rook(Piece):
    def __post_init__(self):
        self.name = PieceNames.Rook.value
        self.value = 5


@dataclass
class Queen(Piece):
    def __post_init__(self):
        self.name = PieceNames.Queen.value
        self.value = 9


@dataclass
class King(Piece):
    def __post_init__(self):
        self.name = PieceNames.King.value
        self.value = 99
        super(King, self).__post_init__()

