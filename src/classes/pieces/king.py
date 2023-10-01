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

    def possible_moves(self, board):
        possible_moves = []
        return possible_moves

    def legal_moves(self, board):
        legal_moves = []
        return legal_moves