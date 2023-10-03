from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames, info


@dataclass
class Knight(Piece):
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

    def possible_moves(self, board):
        possible_moves = []
        for move in self.moves:
            new_position = self.position + move
            new_hex = board.get_hex_from_position(new_position)
            if new_hex:
                if new_hex.piece_on_hex:
                    if new_hex.piece_on_hex.colour != self.colour:
                        possible_moves.append(new_hex)
                    else:
                        # it's the same colour
                        pass
                else:
                    possible_moves.append(new_hex)
            else:
                # there is no hex
                pass
        info(f"Possible Moves are {possible_moves}")
        return possible_moves

    def legal_moves(self, board):
        legal_moves = self.possible_moves(board)
        return legal_moves
