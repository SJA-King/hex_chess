from __future__ import annotations

from dataclasses import dataclass
import math
import pygame
from typing import List, Tuple
from src.classes.constants import HexColours
from src.classes.piece import Piece
from src.classes.position import Position


@dataclass
class HexTile:
    colour: HexColours = None
    centre_xy: Tuple[float, float] = None
    middle_hex_xy: Tuple[float, float] = None
    position: Position = None
    radius: int = None
    piece_on_hex: Piece = None
    highlight: bool = False

    def __post_init__(self):
        self.vertices = self.compute_vertices()

    @property
    def little_r(self) -> float:
        """
        The horizontal length of the hexagon https://en.wikipedia.org/wiki/Hexagon#Parameters
        """
        return self.radius * math.cos(math.radians(30))

    # def get_xy_position(position: Position = None, radius: int = None, little_r: int = None):
    # # if we deal with q,r,s through and only when we place things convert to x and y this becomes a lot easier
    # # we need to set the middle_x, and middle_y though so we can convert the Position to the scalar values
    # a = Position(0, 1, -1)  # x + 0, y + 2r (go down)
    # b = Position(0, -1, 1)  # x + 0, y - 2r (go up)
    # c = Position(-1, 0, 1)  # x - 3/2R, y - r (go left up)
    # d = Position(-1, 1, 0)  # x - 3/2R, y + r (go left down)
    # e = Position(1, 0, -1)  # x + 3/2R, y + r (go right down)
    # f = Position(1, -1, 0)  # x + 3/2R, y - r (go right up)

    @property
    def x(self):
        mid_x, _ = self.middle_hex_xy
        return mid_x + self.position.q * (3 / 2) * self.radius

    @property
    def y(self):
        _, mid_y = self.middle_hex_xy
        return mid_y + (self.position.r - self.position.s) * self.little_r

    def compute_vertices(self) -> List[Tuple[float, float]]:
        """
        Returns a list of the hexagon's vertices as x, y tuples
        """
        return [
            (self.x - self.radius, self.y),
            (self.x - self.radius / 2, self.y + self.little_r),
            (self.x + self.radius / 2, self.y + self.little_r),
            (self.x + self.radius, self.y),
            (self.x + self.radius / 2, self.y - self.little_r),
            (self.x - self.radius / 2, self.y - self.little_r),
        ]

    def render(self, screen) -> None:
        """Renders the hexagon on the screen"""
        if self.highlight:
            pygame.draw.polygon(screen, self.colour.rgb_highlight(), self.vertices)
        else:
            pygame.draw.polygon(screen, self.colour.rgb(), self.vertices)

        if self.piece_on_hex is not None:
            center_hex = self.piece_on_hex.img.get_rect()
            center_hex.center = (self.x, self.y) # self.centre_xy
            screen.blit(self.piece_on_hex.img, center_hex.topleft)
