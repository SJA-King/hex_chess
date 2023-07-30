# def make_board
# def set_hex_colours
# def set_all_pieces
# def place_players_pieces
# def place_piece
from hexes import Hex

# TODO Make a list of all positions to Hexes e.g. [Position(0,-1,3): Hex]


import sys

from pieces import Pawn, Knight, Bishop, Rook, Queen, King
from position import Position, Step
from constants import HexColours


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


    def place_piece(self):
        raise NotImplementedError
        # TODO check that no other piece is on that Hex


    def validate_board(self):
        raise NotImplementedError


    def validate_board_state(self):
        raise NotImplementedError

    def export_board(self):
        raise NotImplementedError

    def import_board(self):
        raise NotImplementedError


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

    def assign_hexes_colours(self):
        # TODO may not need this
        raise NotImplementedError

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

    the_board = {"0,0,0": Hex(position=Position(0, 0, 0), colour=HexColours.GREY)}

    # TODO put this in the validate_board method
    a = Position.from_str("0,0,0")
    print(a)
    b = the_board["0,0,0"].position
    print(b)
    assert a == b

    # TODO use King's steps in future to do this - maybe?
    # TODO or have generic and King uses that
    # make ring around middle hex
    counter = 0
    # TODO make counte go up to 4!!
    while counter < 2:
        new_board = the_board.copy()
        for hex_position, hex in the_board.items():
            for vector in ["0,-1,1", "1,0,-1", "-1,1,0"]:
                a_position = Position.from_str(vector)
                new_hex_position = hex.position + a_position
                new_board[str(new_hex_position)] = Hex(colour=next(hex.colour), position=new_hex_position)

            for vector in ["0,1,-1", "1,-1,0", "-1,0,1"]:
                a_position = Position.from_str(vector)
                new_hex_position = hex.position + a_position
                new_board[str(new_hex_position)] = Hex(colour=next(next(hex.colour)), position=new_hex_position)

        the_board = new_board.copy()
        print(the_board)
        for i_position, i_hex in the_board.items():
            print(f"Position: {i_position} -> {i_hex}")
        counter += 1

    # Make '4' sequential rings, dont make NEW hexes if they exist already


if __name__ == "__main__":
    main()
