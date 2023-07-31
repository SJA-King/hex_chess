from typing import Union

from pieces import Piece, King, Queen, Bishop, Knight, Pawn, Rook
from position import Position
from enum import Enum


class Player:
    name: str = ""
    pieces: list = []
    chosen_piece: Piece = None

    def __init__(self, name: str):
        self.name = name

    def make_pieces(self):
        a_pawn = Pawn("")
        # self.pieces = [Pawn(player="") for _ in range(9)]
                       # ] + [Bishop(player=self) for _ in range(3)
                       #      ] + [Knight(player=self) for _ in range(2)
                       #           ] + [Rook(player=self) for _ in range(2)
                       #                ] + [Queen(player=self) for _ in range(1)
                       #                     ] + [King(player=self) for _ in range(1)]

    def show_pieces(self):
        rundown = ""
        for index, piece in enumerate(self.pieces):
            rundown += f"\n({index}) Piece : {piece.name}, QRS : {piece.current}"

        return rundown

    def pick_piece(self):
        raise NotImplementedError

    def unpick_piece(self):
        raise NotImplementedError

    def move_picked_piece(self):
        raise NotImplementedError

    def take_with_picked_piece(self):
        raise NotImplementedError


class Players(Enum):
    WHITE = Player(name="white")
    BLACK = Player(name="black")
