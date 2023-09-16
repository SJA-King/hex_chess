from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames


@dataclass
class King(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.King
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

    def get_available_moves(self, the_board):
        pass
