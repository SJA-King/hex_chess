from __future__ import annotations

from dataclasses import dataclass
import math
import pygame
from typing import List, Tuple
from src.classes.constants import HexColours
from src.classes.piece import Piece


@dataclass
class HexTile:
    colour: HexColours = None
    centre: Tuple[float, float] = None
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

    def compute_vertices(self) -> List[Tuple[float, float]]:
        """
        Returns a list of the hexagon's vertices as x, y tuples
        """
        x, y = self.centre
        return [
            (x - self.radius, y),
            (x - self.radius / 2, y + self.little_r),
            (x + self.radius / 2, y + self.little_r),
            (x + self.radius, y),
            (x + self.radius / 2, y - self.little_r),
            (x - self.radius / 2, y - self.little_r),
        ]

    def render(self, screen) -> None:
        """Renders the hexagon on the screen"""
        if self.highlight:
            pygame.draw.polygon(screen, self.colour.rgb_highlight(), self.vertices)
        else:
            pygame.draw.polygon(screen, self.colour.rgb(), self.vertices)
