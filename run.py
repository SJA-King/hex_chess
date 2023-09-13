from dataclasses import dataclass, field
from enum import Enum, auto
import math
import pygame
import random
from typing import List, Tuple

from constants import HexColours, colours
from src.classes.hexes import HexTile


def get_random_colour(min_=150, max_=255) -> Tuple[int, ...]:
    """Returns a random RGB colour with each component between min_ and max_"""
    return tuple(random.choices(list(range(min_, max_)), k=3))


def create_hexagon(colour, centre, radius: int = 50) -> HexTile:
    """Creates a hexagon tile at the specified position"""
    return HexTile(colour=colour, centre=centre, radius=radius)


def init_hexagons(screen_width: int = 0, screen_height: int = 0) -> List[HexTile]:

    length_of_middle_column = 11

    radius_of_hex = math.floor(int((screen_height / (length_of_middle_column + 1)) / 2))

    middle_x = screen_width / 2
    middle_y = screen_height / 2

    top_hex = create_hexagon(centre=(middle_x, middle_y), radius=radius_of_hex, colour=(0,0,0))

    top_y = middle_y - math.ceil(length_of_middle_column / 2) * 2*top_hex.little_r
    hexagons = []

    starting_colour = HexColours.RED
    colour = starting_colour

    for i_row in range(length_of_middle_column):
        a_hex = create_hexagon(colour=colour.rgb(), radius=top_hex.radius, centre=(middle_x, (top_y + i_row*2*top_hex.little_r)))
        colour = next(colour)
        hexagons.append(a_hex)

    col_count = 1
    for i_rows_in_column in range(length_of_middle_column-1, math.floor(length_of_middle_column / 2), -1):
        starting_colour = next(next(starting_colour))
        colour = starting_colour
        top_y += top_hex.little_r

        for i_row in range(i_rows_in_column):
            y = top_y + i_row*2*top_hex.little_r
            a_hex = create_hexagon(colour=colour.rgb(), radius=top_hex.radius, centre=(middle_x + col_count * 1.5 * radius_of_hex, y))
            hexagons.append(a_hex)
            a_hex = create_hexagon(colour=colour.rgb(), radius=top_hex.radius, centre=(middle_x - col_count * 1.5 * radius_of_hex, y))
            hexagons.append(a_hex)
            colour = next(colour)

        col_count += 1

    return hexagons


def render(screen, hexagons):
    """Renders hexagons on the screen"""
    screen.fill((0, 0, 0))
    for hexagon in hexagons:
        hexagon.render(screen)

    # # draw borders around colliding hexagons and neighbours
    # mouse_pos = pygame.mouse.get_pos()
    # colliding_hexagons = [
    #     hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    # ]
    # for hexagon in colliding_hexagons:
    #     for neighbour in hexagon.compute_neighbours(hexagons):
    #         neighbour.render_highlight(screen, border_colour=(100, 100, 100))
    #     hexagon.render_highlight(screen, border_colour=(0, 0, 0))
    pygame.display.flip()


def main():
    """Main function"""
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    hexagons = init_hexagons(screen_width=screen_width, screen_height=screen_height)
    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        # for hexagon in hexagons:
        #     hexagon.update()

        render(screen, hexagons)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()
