from __future__ import annotations
from dataclasses import dataclass, field

from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames


@dataclass
class Piece:
    name: PieceNames = PieceNames.Piece
    colour: PlayerColour = PlayerColour.NULL
    position: Position = Position(0, 0, 0)

    def __post_init__(self):
        self.moved: bool = False

    def get_available_moves(self, the_board):
        pass