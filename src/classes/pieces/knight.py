from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames


@dataclass
class Knight(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Knight
        self.set_image()

    @property
    def moves(self):
        return []

    def get_possible_moves(self, board):
        possible_moves = []
        return possible_moves

    def get_legal_moves(self, board):
        legal_moves = []
        return legal_moves
