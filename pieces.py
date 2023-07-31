from __future__ import annotations
from dataclasses import dataclass, field
from constants import PieceNames
from position import Position, Step


# TODO change back to dataclass!
class Piece:
    def __init__(self, player: str ):
        self.player: str = player
        self.name: PieceNames = PieceNames.Piece.value
        self.value: int = 0
        self.start: Position = Position(0,0,0)
        self.turn_last_moved: int = 0
        self.pieces_taken: [Piece] = None
        self.placed: bool = False
        self.moved: bool = False
        self.current: Position = self.start
        self.last: Position = self.start

    def __post_init__(self):
        if not self.player:
            raise Exception(f"{self.name.value} WASNT given a player!")
        # TODO think about checking piece after its been given to player!
        # if not self.start:
        #     raise Exception(f"{self.name.value} WASNT given a starting position!")

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


class Pawn(Piece):
    def __init__(self, player):
        super().__init__(player)

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

