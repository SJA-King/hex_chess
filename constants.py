from __future__ import annotations
from enum import Enum, auto


class HexColours(Enum):
    GREY = 1
    WHITE = 2
    BLACK = 3

    def __next__(self):
        """ Provide the next colour in a sequence."""
        new_value = self.value + 1
        if new_value > 3:
            new_value = 1
        return HexColours(new_value)

# TODO make this a test
# q = HexColours.GREY
# print(next(q))
# print(next(q))
# print(next(q))

class Player(Enum):
    WHITE = "White"
    BLACK = "Black"


class PieceNames(Enum):
    Piece = None
    Pawn = "Pawn"
    Knight = "Knight"
    Bishop = "Bishop"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"
