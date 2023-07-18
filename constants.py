from __future__ import annotations
from enum import Enum, auto


class HexColours(Enum):
    GREY = auto()
    BLACK = auto()
    WHITE = auto()


class Players(Enum):
    WHITE = "White"
    BLACK = "Black"


class PieceNames(Enum):
    Piece = "Piece"
    Pawn = "Pawn"
    Knight = "Knight"
    Bishop = "Bishop"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"