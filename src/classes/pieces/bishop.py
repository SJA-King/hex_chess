from dataclasses import dataclass
import pygame

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, images_path


@dataclass
class Bishop(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Bishop
        self.set_image()

    @property
    def moves(self):
        # a bishop can do these moves as long as there is nothing in the way
        return [
            Position(2, -1, -1),
            Position(1, -2, 1),
            Position(-1,-1,2),
            Position(-2,1,1),
            Position(-1,2,-1),
            Position(1, 1, -2),
        ]

    def get_possible_moves(self, board):
        possible_moves = []
        return possible_moves

    def get_legal_moves(self, board):
        legal_moves = []
        return legal_moves
