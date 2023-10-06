from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.king import King
from src.classes.position import Position
from src.classes.constants import PieceNames, info


@dataclass
class Knight(King):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Knight
        self.set_image()

    @property
    def moves(self):
        moves = [
            Position(1, -3, 2),
            Position(-1, -2, 3),
            Position(-2, -1, 3),
            Position(-3, 1, 2),
            Position(-2, 3, -1),
            Position(-3, 2, 1),
            Position(1, 2, -3),
            Position(-1, 3, -2),
            Position(2, 1, -3),
            Position(3, -1, -2),
            Position(2, -3, 1),
            Position(3, -2, 1),
            ]
        return moves
