# def make_board
# def set_hex_colours
# def set_all_pieces
# def place_players_pieces
# def place_piece
from .hexes import Hex

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


# TODO make a singleton!
class Game:
    def __init__(self):
        self.board = None


    def hex_at_position(self, position: Position):
        raise NotImplementedError

    def piece_on_hex(self, a_hex: Hex):
        raise NotImplementedError

    def piece_at_position(self, position: Position):
        raise NotImplementedError


    def make_board(self):
        raise NotImplementedError

    # TODO Need to check board is expected size - add a validate board

    # TODO add validate pieces on board, at start, during etc


    def promote_pawn(self):
        raise NotImplementedError



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
