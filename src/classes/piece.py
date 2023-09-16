from __future__ import annotations
from dataclasses import dataclass

import pygame
from abc import ABC, abstractmethod
from src.classes.position import Position
from src.classes.constants import PlayerColour,  PieceNames, images_path


@dataclass
class Piece(ABC):
    name: PieceNames = None
    colour: PlayerColour = None
    position: Position = None
    hex_width: int = 0
    hex_height: int = 0
    img: pygame.Surface = None

    def __post_init__(self):
        self.moved: bool = False
        # self.img: pygame.Surface = pygame.Surface(size=(0, 0))

    @abstractmethod
    def get_available_moves(self, the_board):
        pass

    def set_image(self):
        img_path = images_path / f"{self.colour.value}_{self.name.value}.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (self.hex_width*0.85, self.hex_height*0.85))
