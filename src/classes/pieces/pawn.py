from dataclasses import dataclass
from pathlib import Path

import pygame

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, images_path


@dataclass
class Pawn(Piece):
    def __post_init__(self):
        self.name = PieceNames.Pawn

        img_path = images_path / f"{self.colour.WHITE.value}_pawn.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (self.hex_width*0.85, self.hex_height*0.85))

    @property
    def possible_moves(self):
        moves = []
        if self.colour == PlayerColour.WHITE:
            moves.append(Position(0, -1, 1))
            if not self.moved:
                moves.append(Position(0, -2, 2))

        elif self.colour == PlayerColour.BLACK:
            moves.append(Position(0, 1, -1))
            if not self.moved:
                moves.append(Position(0, 2, -2))
        else:
            print(f"Error - Pawn Colour not in {PlayerColour}")

        return moves

    def get_available_moves(self, the_board):
        pass