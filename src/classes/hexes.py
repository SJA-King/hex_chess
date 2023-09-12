from __future__ import annotations

from constants import HexColours
from position import Position

from dataclasses import dataclass, field
from enum import Enum, auto
import math
import pygame
import random
from typing import List, Tuple



@dataclass
class HexTile:
    # colour: HexColours = None
    colour: Tuple[int, ...] = None
    centre: Tuple[float, float] = None
    radius: int = None
    highlight_offset: int = 3
    max_highlight_ticks: int = 15

    def __post_init__(self):
        # if not self.colour:
        #     raise Exception(f"Hex {self} WASNT given a Colour!")
        # if not self.position:
        #     raise Exception(f"Hex {self} WASNT given a Position!")
        self.piece = None
        self.vertices = self.compute_vertices()
        self.highlight_tick = 0

    def update(self):
        """Updates tile highlights"""
        if self.highlight_tick > 0:
            self.highlight_tick -= 1

    # @property
    # def centre(self) -> Tuple[float, float]:
    #     """Centre of the hexagon"""
    #     x, y = self.position
    #     return x, y + self.radius

    @property
    def minimal_radius(self) -> float:
        """Horizontal length of the hexagon"""
        # https://en.wikipedia.org/wiki/Hexagon#Parameters
        return self.radius * math.cos(math.radians(30))

    @property
    def highlight_colour(self) -> Tuple[int, ...]:
        """Colour of the hexagon tile when rendering highlight"""
        offset = 10
        brighten = lambda x, y: x + y if x + y < 255 else 255
        return tuple(brighten(x, offset) for x in self.colour)

    def compute_vertices(self) -> List[Tuple[float, float]]:
        """
        Returns a list of the hexagon's vertices as x, y tuples
        """
        # pylint: disable=invalid-name
        x, y = self.centre
        half_radius = self.radius / 2
        # minimal_radius = self.minimal_radius
        return [
            (x - self.radius, y),
            (x - half_radius, y + self.minimal_radius),
            (x + half_radius, y + self.minimal_radius),
            (x + self.radius, y),
            (x + half_radius, y - self.minimal_radius),
            (x - half_radius, y - self.minimal_radius),
        ]

    # (x, y),
    # (x - half_radius, y + minimal_radius),
    # (x, y + 2 * minimal_radius),
    # (x + self.radius, y + 2 * minimal_radius),
    # (x + 3 * half_radius, y + minimal_radius),
    # (x + self.radius, y),

    def render(self, screen) -> None:
        """Renders the hexagon on the screen"""
        pygame.draw.polygon(screen, self.highlight_colour, self.vertices)
