from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames, info


@dataclass
class Queen(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Queen
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
            # plus the bishop 'jumps'
            Position(2, -1, -1),
            Position(1, -2, 1),
            Position(-1, -1, 2),
            Position(-2, 1, 1),
            Position(-1, 2, -1),
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
                        if new_hex.piece_on_hex.colour != self.colour:
                            possible_moves.append(new_hex)
                        keep_going = False
                else:
                    keep_going = False
                # possible_moves.append(new_hex)
        info(f"Possible Moves are {possible_moves}")
        return possible_moves

    def legal_moves(self, board):
        legal_moves = self.possible_moves(board)
        return legal_moves
