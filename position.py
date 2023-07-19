from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Position:
    q: int = None
    r: int = None
    s: int = None

    def __add__(self, other: Position) -> Position:
        new_q = self.q + other.q
        new_r = self.r + other.r
        new_s = self.s + other.s
        # TODO dont check out of bounds here!
        # assert 5 > new_q > -5
        # assert 5 > new_r > -5
        # assert 5 > new_s > -5
        return Position(new_q, new_r, new_s)

    def __post_init__(self):
        if not self.q:
            raise Exception(f"Q NOT SET!")
        if not self.r:
            raise Exception(f"R NOT SET!")
        if not self.s:
            raise Exception(f"S NOT SET!")

@dataclass
class Step:
    position_modifier: Position = None
    pace: int = 1
    special: bool = False  # For En-Passant!

    def __post_init__(self):
        if self.pace != 1 or self.pace != 99:
            raise Exception(f"Pace should be once or many was - {self.pace}")

# TODO split into pieces moves! Dont want other pieces taking other moves!
class Moves(Enum):
    BISHOP_LEFT_LEFT = Step(Position(-2, 1, 1), 99)
    BISHOP_UP_LEFT = Step(Position(-1, -1, 2), 99)
    BISHOP_UP_RIGHT = Step(Position(1, -2, 1), 99)
    BISHOP_RIGHT_RIGHT = Step(Position(2, -1, -1), 99)
    BISHOP_DOWN_RIGHT = Step(Position(1, 1, -2), 99)
    BISHOP_DOWN_LEFT = Step(Position(-1, 2, -1), 99)

    WHITE_PAWN_MOVE = Step(Position(0, -1, 1))
    WHITE_PAWN_FIRST_MOVE = Step(Position(0, -2, 2))
    # WHITE_PAWN_EN_PASSANT = Step(Position())
    # TODO If BLACK PAWN MOVES PASSED THIS PAWN ALLOW EN PASSANT!
    BLACK_PAWN_MOVE = Step(Position(0, 1, -1))
    BLACK_PAWN_FIRST_MOVE = Step(Position(0, 2, -2))
    # BLACK_PAWN_EN_PASSANT = Step(Position())

    KING_UP_UP = Step(Position(0, -1, 1))
    KING_LEFT_UP = Step(Position(-1, 0, 1))
    KING_LEFT_DOWN = Step(Position(-1, 1, 0))
    KING_RIGHT_UP = Step(Position(1, -1, 0))
    KING_DOWN_DOWN = Step(Position(0, 1, -1))
    KING_RIGHT_DOWN = Step(Position(1, 0, -1))

    ROOK_UP_UP = Step(Position(0, -1, 1), 99)
    ROOK_LEFT_UP = Step(Position(-1, 0, 1), 99)
    ROOK_LEFT_DOWN = Step(Position(-1, 1, 0), 99)
    ROOK_RIGHT_UP = Step(Position(1, -1, 0), 99)
    ROOK_DOWN_DOWN = Step(Position(0, 1, -1), 99)
    ROOK_RIGHT_DOWN = Step(Position(1, 0, -1), 99)

    QUEEN_UP_UP = Step(Position(0, -1, 1), 99)
    QUEEN_LEFT_UP = Step(Position(-1, 0, 1), 99)
    QUEEN_LEFT_DOWN = Step(Position(-1, 1, 0), 99)
    QUEEN_RIGHT_UP = Step(Position(1, -1, 0), 99)
    QUEEN_DOWN_DOWN = Step(Position(0, 1, -1), 99)
    QUEEN_RIGHT_DOWN = Step(Position(1, 0, -1), 99)
    QUEEN_LEFT_LEFT = Step(Position(-2, 1, 1), 99)
    QUEEN_UP_LEFT = Step(Position(-1, -1, 2), 99)
    QUEEN_UP_RIGHT = Step(Position(1, -2, 1), 99)
    QUEEN_RIGHT_RIGHT = Step(Position(2, -1, -1), 99)
    QUEEN_DOWN_RIGHT = Step(Position(1, 1, -2), 99)
    QUEEN_DOWN_LEFT = Step(Position(-1, 2, -1), 99)

    KNIGHT_UP_UP_LEFT = Step(Position(-1, -2, 3))
    KNIGHT_UP_UP_RIGHT = Step(Position(1, -3, 2))
    KNIGHT_RIGHT_UP_UP = Step(Position(2, -3, 1))
    KNIGHT_RIGHT_UP_RIGHT = Step(Position(3, -2, -1))
    KNIGHT_RIGHT_DOWN_RIGHT = Step(Position(3, -2, -2))
    KNIGHT_RIGHT_DOWN_DOWN = Step(Position(2, 1, -3))
    KNIGHT_DOWN_DOWN_RIGHT = Step(Position(1, 2, -3))
    KNIGHT_DOWN_DOWN_LEFT = Step(Position(-1, -2, 3))
    KNIGHT_LEFT_DOWN_DOWN = Step(Position(-2, 3, -1))
    KNIGHT_LEFT_DOWN_LEFT = Step(Position(-3, 2, 1))
    KNIGHT_LEFT_UP_LEFT = Step(Position(-3, 1, 2))
    KNIGHT_LEFT_UP_UP = Step(Position(-2, -1, 3))
