from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PieceNames, info


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
            new_position = self.position + move
            new_hex = board.positions_to_hextiles.get(new_position)
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
