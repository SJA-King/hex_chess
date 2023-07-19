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
        if not self.q and self.q != 0:
            raise Exception(f"Q NOT SET!")
        if not self.r and self.r != 0:
            raise Exception(f"R NOT SET!")
        if not self.s and self.s != 0:
            raise Exception(f"S NOT SET!")


class Pace(Enum):
    WALK = auto()  # move one step on a turn
    RUN = auto()  # move multiple of one type of step on a turn


@dataclass
class Step:
    vector: Position = None
    pace: Pace = None
    special: bool = False  # For En-Passant!

    def __post_init__(self):
        if not isinstance(self.pace, Pace):
            raise Exception(f"Pace must be of type {type(Pace)}")


# TODO split into pieces moves! Dont want other pieces taking other moves!
class Moves(Enum):
    BISHOP_LEFT_LEFT = Step(Position(-2, 1, 1), Pace.RUN)
    BISHOP_UP_LEFT = Step(Position(-1, -1, 2), Pace.RUN)
    BISHOP_UP_RIGHT = Step(Position(1, -2, 1), Pace.RUN)
    BISHOP_RIGHT_RIGHT = Step(Position(2, -1, -1), Pace.RUN)
    BISHOP_DOWN_RIGHT = Step(Position(1, 1, -2), Pace.RUN)
    BISHOP_DOWN_LEFT = Step(Position(-1, 2, -1), Pace.RUN)

    WHITE_PAWN_MOVE = Step(Position(0, -1, 1), Pace.WALK)
    WHITE_PAWN_FIRST_MOVE = Step(Position(0, -2, 2), Pace.WALK)
    # WHITE_PAWN_EN_PASSANT = Step(Position())
    # TODO If BLACK PAWN MOVES PASSED THIS PAWN ALLOW EN PASSANT!
    BLACK_PAWN_MOVE = Step(Position(0, 1, -1), Pace.WALK)
    BLACK_PAWN_FIRST_MOVE = Step(Position(0, 2, -2), Pace.WALK)
    # BLACK_PAWN_EN_PASSANT = Step(Position())

    KING_UP_UP = Step(Position(0, -1, 1), Pace.WALK)
    KING_LEFT_UP = Step(Position(-1, 0, 1), Pace.WALK)
    KING_LEFT_DOWN = Step(Position(-1, 1, 0), Pace.WALK)
    KING_RIGHT_UP = Step(Position(1, -1, 0), Pace.WALK)
    KING_DOWN_DOWN = Step(Position(0, 1, -1), Pace.WALK)
    KING_RIGHT_DOWN = Step(Position(1, 0, -1), Pace.WALK)

    ROOK_UP_UP = Step(Position(0, -1, 1), Pace.RUN)
    ROOK_LEFT_UP = Step(Position(-1, 0, 1), Pace.RUN)
    ROOK_LEFT_DOWN = Step(Position(-1, 1, 0), Pace.RUN)
    ROOK_RIGHT_UP = Step(Position(1, -1, 0), Pace.RUN)
    ROOK_DOWN_DOWN = Step(Position(0, 1, -1), Pace.RUN)
    ROOK_RIGHT_DOWN = Step(Position(1, 0, -1), Pace.RUN)

    QUEEN_UP_UP = Step(Position(0, -1, 1), Pace.RUN)
    QUEEN_LEFT_UP = Step(Position(-1, 0, 1), Pace.RUN)
    QUEEN_LEFT_DOWN = Step(Position(-1, 1, 0), Pace.RUN)
    QUEEN_RIGHT_UP = Step(Position(1, -1, 0), Pace.RUN)
    QUEEN_DOWN_DOWN = Step(Position(0, 1, -1), Pace.RUN)
    QUEEN_RIGHT_DOWN = Step(Position(1, 0, -1), Pace.RUN)
    QUEEN_LEFT_LEFT = Step(Position(-2, 1, 1), Pace.RUN)
    QUEEN_UP_LEFT = Step(Position(-1, -1, 2), Pace.RUN)
    QUEEN_UP_RIGHT = Step(Position(1, -2, 1), Pace.RUN)
    QUEEN_RIGHT_RIGHT = Step(Position(2, -1, -1), Pace.RUN)
    QUEEN_DOWN_RIGHT = Step(Position(1, 1, -2), Pace.RUN)
    QUEEN_DOWN_LEFT = Step(Position(-1, 2, -1), Pace.RUN)

    KNIGHT_UP_UP_LEFT = Step(Position(-1, -2, 3), Pace.WALK)
    KNIGHT_UP_UP_RIGHT = Step(Position(1, -3, 2), Pace.WALK)
    KNIGHT_RIGHT_UP_UP = Step(Position(2, -3, 1), Pace.WALK)
    KNIGHT_RIGHT_UP_RIGHT = Step(Position(3, -2, -1), Pace.WALK)
    KNIGHT_RIGHT_DOWN_RIGHT = Step(Position(3, -2, -2), Pace.WALK)
    KNIGHT_RIGHT_DOWN_DOWN = Step(Position(2, 1, -3), Pace.WALK)
    KNIGHT_DOWN_DOWN_RIGHT = Step(Position(1, 2, -3), Pace.WALK)
    KNIGHT_DOWN_DOWN_LEFT = Step(Position(-1, -2, 3), Pace.WALK)
    KNIGHT_LEFT_DOWN_DOWN = Step(Position(-2, 3, -1), Pace.WALK)
    KNIGHT_LEFT_DOWN_LEFT = Step(Position(-3, 2, 1), Pace.WALK)
    KNIGHT_LEFT_UP_LEFT = Step(Position(-3, 1, 2), Pace.WALK)
    KNIGHT_LEFT_UP_UP = Step(Position(-2, -1, 3), Pace.WALK)
