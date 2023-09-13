from __future__ import annotations
from enum import Enum, auto


colours = {
    "RED": (255, 150, 150),
    "BLUE": (152, 232, 242),
    "GREEN": (180, 248, 221)
}


# def get_next_colour(colour: str) -> str:
#     if colour == "RED":
#         return "BLUE"
#     if colour == "BLUE":
#         return "GREEN"
#     if colour == "GREEN":
#         return "RED"


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

# TODO make this a test
# q = HexColours.GREY
# print(next(q))
# print(next(q))
# print(next(q))




class PieceNames(Enum):
    Piece = None
    Pawn = "Pawn"
    Knight = "Knight"
    Bishop = "Bishop"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"
