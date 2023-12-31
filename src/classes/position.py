from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Position:
    q: int = None
    r: int = None
    s: int = None

    def __init__(self, q, r, s):
        # TODO add check these are ints!
        # TODO fix un-needed constructor class - put logic in post-init
        self.q = int(q)
        self.r = int(r)
        self.s = int(s)

    def __add__(self, other: Position) -> Position:
        new_q = self.q + other.q
        new_r = self.r + other.r
        new_s = self.s + other.s
        return Position(new_q, new_r, new_s)

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __str__(self):
        return f"{self.q},{self.r},{self.s}"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_str(cls, qrs_str: str, delimitor: str = ",") -> Position:
        assert len(delimitor) == 1
        q, r, s = qrs_str.split(delimitor)
        return cls(q, r, s)

    def __post_init__(self):
        if not self.q and self.q != 0:
            raise Exception(f"Q NOT SET!")
        if not self.r and self.r != 0:
            raise Exception(f"R NOT SET!")
        if not self.s and self.s != 0:
            raise Exception(f"S NOT SET!")

    def __hash__(self):
        return hash(str(self))



class Pace(Enum):
    WALK = auto()  # move one step on a turn
    RUN = auto()  # move multiple of one type of step on a turn


@dataclass
class Step:
    vector: Position = Position(0, 0, 0)
    pace: Pace = Pace.WALK
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


