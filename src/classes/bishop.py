from dataclasses import dataclass

from src.classes.queen import Queen
from src.classes.position import Position
from src.classes.constants import PieceNames


@dataclass
class Bishop(Queen):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Bishop
        self.set_image()

    @property
    def moves(self):
        return [
            Position(2, -1, -1),
            Position(1, -2, 1),
            Position(-1, -1, 2),
            Position(-2, 1, 1),
            Position(-1, 2, -1),
            Position(1, 1, -2),
        ]
