from __future__ import annotations

from functools import lru_cache

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
        x, y = self.centre
        half_radius = self.radius / 2
        return [
            (x - self.radius, y),
            (x - half_radius, y + self.minimal_radius),
            (x + half_radius, y + self.minimal_radius),
            (x + self.radius, y),
            (x + half_radius, y - self.minimal_radius),
            (x - half_radius, y - self.minimal_radius),
        ]

    def render(self, screen) -> None:
        """Renders the hexagon on the screen"""
        pygame.draw.polygon(screen, self.highlight_colour, self.vertices)

    @lru_cache
    def compute_neighbours(self, hexagons: List[HexTile]) -> List[HexTile]:
        """Returns hexagons whose centres are two minimal radiuses away from self.centre"""
        return [hexagon for hexagon in hexagons if self.is_neighbour(hexagon)]

    def collide_with_point(self, point: Tuple[float, float]) -> bool:
        """Returns True if distance from centre to point is less than horizontal_length"""
        return math.dist(point, self.centre) < self.minimal_radius

    def is_neighbour(self, hexagon: HexTile) -> bool:
        """Returns True if hexagon centre is approximately
        2 minimal radiuses away from own centre
        """
        distance = math.dist(hexagon.centre, self.centre)
        return math.isclose(distance, 2 * self.minimal_radius, rel_tol=0.05)

    def render_highlight(self, screen, border_colour) -> None:
        """Draws a border around the hexagon with the specified colour"""
        self.highlight_tick = self.max_highlight_ticks
        # pygame.draw.polygon(screen, self.highlight_colour, self.vertices)
        pygame.draw.aalines(screen, border_colour, closed=True, points=self.vertices)
