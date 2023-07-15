from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field


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


@dataclass
class Hex:
    col: int = None
    ring: int = None
    colour: HexColours = None
    # _piece: # TODO a piece has a hex that it is on? DONT want circular imports
    neighbours: dict[Positions, Hex] = field(default_factory={})
