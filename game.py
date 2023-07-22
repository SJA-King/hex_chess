# def make_board
# def set_hex_colours
# def set_all_pieces
# def place_players_pieces
# def place_piece

# TODO Make a list of all positions to Hexes e.g. [Position(0,-1,3): Hex]


import sys

from pieces import Pawn, Knight, Bishop, Rook, Queen, King
from position import Position, Step


def info(msg: str):
    print(f"{msg}", file=sys.stderr, flush=True)


def warn(msg: str):
    print(f"warning: {msg}", file=sys.stderr, flush=True)


def die(msg: str):
    print(f"error: {msg}", file=sys.stderr, flush=True)
    sys.exit(1)


def make_board():
    raise NotImplementedError


class Game:
    def __init__(self):


    def hex_at_position(self, position: Position):



def main():
    print("Want to Play Hex Chess?!")
    king = King(player="Simon", start=Position(0,0,0))
    print(king)
    queen = Queen()
    rook = Rook()
    bishop = Bishop()
    knight = Knight()
    pawn = Pawn(player="Simon", start=Position(0,0,0))
    print(pawn)


if __name__ == "__main__":
    main()
