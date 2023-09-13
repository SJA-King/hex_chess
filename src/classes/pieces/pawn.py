from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames


@dataclass
class Pawn(Piece):
    def __post_init__(self):
        self.name = PieceNames.Pawn

    @property
    def possible_moves(self):
        moves = []
        if self.colour == PlayerColour.WHITE:
            moves.append(Position(0, -1, 1))
            if not self.moved:
                moves.append(Position(0, -2, 2))

        elif self.colour == PlayerColour.BLACK:
            moves.append(Position(0, 1, -1))
            if not self.moved:
                moves.append(Position(0, 2, -2))
        else:
            print(f"Error - Pawn Colour not in {PlayerColour}")

        return moves
