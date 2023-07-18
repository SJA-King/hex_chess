from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from constants import HexColours
from .position import Position




@dataclass
class Hex:
    col: int = None
    ring: int = None
    colour: HexColours = None
    position: Position = None
    # _piece: # TODO a piece has a hex that it is on? DONT want circular imports
    # neighbours: dict[Positions, Hex] = field(default_factory={})
