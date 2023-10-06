from dataclasses import dataclass

from src.classes.queen import Queen
from src.classes.position import Position
from src.classes.constants import PieceNames


@dataclass
class Rook(Queen):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Rook
        self.set_image()

    @property
    def moves(self):
        return [
            Position(0, -1, 1),
            Position(-1, 0, 1),
            Position(-1, 1, 0),
            Position(1, -1, 0),
            Position(0, 1, -1),
            Position(1, 0, -1),
        ]
