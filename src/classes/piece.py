from __future__ import annotations
from dataclasses import dataclass

import pygame
from src.classes.position import Position
from src.classes.constants import PlayerColour


@dataclass
class Piece:
    colour: PlayerColour = PlayerColour.NULL
    position: Position = Position(0, 0, 0)
    hex_width: int = 0
    hex_height: int = 0

    def __post_init__(self):
        self.moved: bool = False
        self.img: pygame.Surface = pygame.Surface(size=(0, 0))

    def get_available_moves(self, the_board):
        pass
