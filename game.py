# def make_board
# def set_hex_colours
# def set_all_pieces
# def place_players_pieces
# def place_piece
from hexes import Hex
from player import Player

# TODO Make a list of all positions to Hexes e.g. [Position(0,-1,3): Hex]


import sys

from pieces import Pawn, Knight, Bishop, Rook, Queen, King
from position import Position, Step
from constants import HexColours
from player import Players, Player


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
        self.board: dict = None
        self.white: Player = Players.WHITE.value
        self.black: Player = Players.BLACK.value

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

    # todo use this to make the hexagons
    def make_board(self):
        """ Create a central Hex, then make 5 rings of Hexes around it """
        self.board = {"0,0,0": Hex(position=Position(0, 0, 0), colour=HexColours.GREY)}
        for _ in range(5):
            new_board = self.board.copy()
            for hex_position, a_hex in self.board.items():
                for vector in ["0,-1,1", "1,0,-1", "-1,1,0"]:
                    a_position = Position.from_str(vector)
                    new_hex_position = a_hex.position + a_position
                    new_board[str(new_hex_position)] = Hex(colour=next(a_hex.colour), position=new_hex_position)

                for vector in ["0,1,-1", "1,-1,0", "-1,0,1"]:
                    a_position = Position.from_str(vector)
                    new_hex_position = a_hex.position + a_position
                    new_board[str(new_hex_position)] = Hex(colour=next(next(a_hex.colour)), position=new_hex_position)

            self.board = new_board.copy()

    def show_board(self):
        for i_position, i_hex in self.board.items():
            info(f"Position: {i_position} -> {i_hex}")


    # TODO add validate pieces on board, at start, during etc

    def promote_pawn(self):
        raise NotImplementedError


def main():
    print("Want to Play Hex Chess?!")
    # king = King(player="Simon", start=Position(0,0,0))
    # print(king)
    # queen = Queen()
    # rook = Rook()
    # bishop = Bishop()
    # knight = Knight()
    # pawn = Pawn(player="Simon", start=Position(0,0,0))
    # print(pawn)

    game = Game()
    game.make_board()
    game.black.make_pieces()
    game.white.make_pieces()
    print(game.black.show_pieces())
    print(game.white.show_pieces())

    # TODO use King's steps in future to do this - maybe?
    # TODO or have generic and King uses that
    # make ring around middle hex




if __name__ == "__main__":
    main()
