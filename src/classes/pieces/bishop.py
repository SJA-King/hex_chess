from dataclasses import dataclass
import pygame

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, images_path, info


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

    def possible_moves(self, board):
        possible_moves = []
        for move in self.moves:
            keep_going = True
            new_position = self.position
            while keep_going:
                new_position += move
                new_hex = board.get_hex_from_position(new_position)
                if new_hex:
                    if new_hex.piece_on_hex is None:
                        possible_moves.append(new_hex)
                    else:
                        keep_going = False
                else:
                    keep_going = False
                # possible_moves.append(new_hex)
        info(f"Possible Moves are {possible_moves}")
        return possible_moves

    def legal_moves(self, board):
        legal_moves = self.possible_moves(board)
        return legal_moves
