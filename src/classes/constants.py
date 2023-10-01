from __future__ import annotations
from enum import Enum, auto
from pathlib import Path
import sys


classes_path = Path(__file__).parent
src_path = classes_path.parent
images_path = src_path / "images"


def info(msg: str):
    print(f"INFO = {msg}", file=sys.stderr, flush=True)


def warn(msg: str):
    print(f"WARNING = {msg}", file=sys.stderr, flush=True)


def die(msg: str):
    print(f"ERROR = {msg}", file=sys.stderr, flush=True)
    sys.exit(1)


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

    def __str__(self):
        if self.value == 1:
            return "Red"
        if self.value == 2:
            return "Blue"
        if self.value == 3:
            return "Green"

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
            2: (0, 0, 221),
            3: (0, 232, 0),
        }
        return colour_to_rgb[self.value]


class PieceNames(Enum):
    Pawn = "Pawn"
    Knight = "Knight"
    Bishop = "Bishop"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"


class PlayerColour(Enum):
    NULL = ""
    WHITE = "w"  # todo change to white/black etc
    BLACK = "b"
