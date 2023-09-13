from __future__ import annotations
from enum import Enum, auto


class HexColours(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

    def __next__(self):
        """ Provide the next colour in a sequence."""
        new_value = self.value + 1
        if new_value > 3:
            new_value = 1
        return HexColours(new_value)

    def rgb(self):
        colour_to_rgb = {
            1: (255, 150, 150),
            2: (152, 232, 242),
            3: (180, 248, 221)
        }
        return colour_to_rgb[self.value]

    def rgb_highlight(self):
        colour_to_rgb = {  # todo put proper colours in here
            1: (255, 0, 0),
            2: (0, 232, 0),
            3: (0, 0, 221)
        }
        return colour_to_rgb[self.value]


class PieceNames(Enum):
    Piece = None
    Pawn = "Pawn"
    Knight = "Knight"
    Bishop = "Bishop"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"


class PlayerColour(Enum):
    NULL = auto()
    WHITE = auto()
    BLACK = auto()
