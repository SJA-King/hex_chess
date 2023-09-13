from __future__ import annotations
from dataclasses import dataclass, field

from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames


@dataclass
class Piece:
    def __init__(self):
        self.name: PieceNames = PieceNames.Piece
        self.colour: PlayerColour = PlayerColour.NULL
        self.start: Position = Position(0, 0, 0)

    def __post_init__(self):
        self.moved: bool = False
