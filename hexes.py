from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from constants import HexColours
from .position import Position


@dataclass
class Hex:
    colour: HexColours = None
    position: Position = None

    def __post_init__(self):
        if not self.colour:
            raise Exception(f"Hex {self} WASNT given a Colour!")
        if not self.position:
            raise Exception(f"Hex {self} WASNT given a Position!")
        self.piece = None

