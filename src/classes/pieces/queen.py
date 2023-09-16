from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames


@dataclass
class Queen(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Queen
        self.set_image()

    @property
    def moves(self):
        return []

    def get_available_moves(self, the_board):
        pass