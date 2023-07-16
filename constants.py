from __future__ import annotations
from enum import Enum, auto


class Positions(Enum):
    MID_UP = auto()
    MID_DOWN = auto()
    LEFT_UP = auto()
    LEFT_DOWN = auto()
    RIGHT_UP = auto()
    RIGHT_DOWN = auto()


class HexColours(Enum):
    GREY = auto()
    BLACK = auto()
    WHITE = auto()
