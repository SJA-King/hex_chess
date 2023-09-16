from dataclasses import dataclass
import pygame

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, images_path


@dataclass
class Bishop(Piece):
    def __post_init__(self):
        self.name: PieceNames = PieceNames.Bishop
        # todo put this in Piece
        img_path = images_path / f"{self.colour.value}_bishop.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (self.hex_width*0.85, self.hex_height*0.85))

    @property
    def moves(self):
        # a bishop can do these moves as long as there is nothing in the way
        return [
            Position(2, -1, -1),
            Position(1, -2, 1),
            Position(-1,-1,2),
            Position(-2,1,1),
            Position(-1,2,-1),
            Position(1, 1, -2),
        ]

    def get_available_moves(self, the_board):
        pass
