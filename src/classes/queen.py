from dataclasses import dataclass

from src.classes.king import King
from src.classes.constants import PieceNames, info


@dataclass
class Queen(King):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Queen
        self.set_image()

    def possible_moves(self, board):
        possible_moves = []
        for move in self.moves:
            keep_going = True
            new_position = self.position
            while keep_going:
                new_position += move
                new_hex = board.positions_to_hextiles.get(new_position)
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
