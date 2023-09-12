from dataclasses import dataclass, field
from enum import Enum, auto
import math
import pygame
import random
from typing import List, Tuple

from src.classes.hexes import HexTile


def get_random_colour(min_=150, max_=255) -> Tuple[int, ...]:
    """Returns a random RGB colour with each component between min_ and max_"""
    return tuple(random.choices(list(range(min_, max_)), k=3))


def create_hexagon(centre, radius: int = 50) -> HexTile:
    """Creates a hexagon tile at the specified position"""
    return HexTile(colour=get_random_colour(), centre=centre, radius=radius)


# def init_hexagons(num_x=2, num_y=2) -> List[HexTile]:
#     """Creates a hexaogonal tile map of size num_x * num_y"""
#     leftmost_hexagon = create_hexagon(position=(50, 0))
#     hexagons = [leftmost_hexagon]
#     y = leftmost_hexagon.minimal_radius*2
#     step = leftmost_hexagon.minimal_radius*2
#     x = leftmost_hexagon.minimal_radius
#     for i in range(5):
#         hexagons.append(create_hexagon((x + i*step + step, y)))
#     y = y - (leftmost_hexagon.radius + (leftmost_hexagon.radius / 2))
#     x = leftmost_hexagon.minimal_radius * 2
#     for i in range(5):
#         hexagons.append(create_hexagon((x + i*step + step, y)))
#     y = y - (leftmost_hexagon.radius + (leftmost_hexagon.radius / 2))
#     x = leftmost_hexagon.minimal_radius * 3
#     for i in range(5):
#         hexagons.append(create_hexagon((x + i * step + step, y)))
#
#     return hexagons

import math
def init_hexagons(screen_width: int = 0, screen_height: int = 0) -> List[HexTile]:

    length_of_middle_column = 5#11

    radius_of_hex = math.floor(int((screen_width / (length_of_middle_column + 1)) / 2))# + (screen_height / 2*length_of_middle_row)) / 2
    print(radius_of_hex)
    # radius_of_hex = 50

    middle_x = screen_width / 2
    print(middle_x)
    middle_y = screen_height / 2#) - radius_of_hex
    print(middle_y)

    # top_y = math.floor(length_of_middle_column /2 ) * 2

    top_hex = create_hexagon(centre=(middle_x, middle_y), radius=radius_of_hex)

    top_y = math.floor(length_of_middle_column / 2) * 2*top_hex.minimal_radius
    hexagons = []

    for i in range(-math.floor(length_of_middle_column / 2), math.ceil(length_of_middle_column / 2)):
        hexagons.append(create_hexagon(radius=top_hex.radius, centre=(middle_x, (middle_y + i*2*top_hex.minimal_radius))))

    col_count = 1
    for j in range(length_of_middle_column-1, math.floor(length_of_middle_column / 2), -1):
        print(j)
        # do right side
        for i in range(-math.floor(j / 2), math.ceil(j / 2)):
            y = (middle_y + i * 2 * top_hex.minimal_radius + top_hex.minimal_radius)
            hexagons.append(
                create_hexagon(radius=top_hex.radius, centre=(middle_x + col_count*1.5*radius_of_hex, y)))
            hexagons.append(
                create_hexagon(radius=top_hex.radius, centre=(middle_x - col_count * 1.5 * radius_of_hex, y)))

        col_count += 1


    #hexagons.append(create_hexagon(radius=top_hex.radius, centre=(middle_x, (middle_y + radius_of_hex))))
    #hexagons.append(create_hexagon(radius=top_hex.radius, centre=(middle_x + 1.5*radius_of_hex, (middle_y + radius_of_hex + top_hex.minimal_radius))))
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
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    hexagons = init_hexagons(screen_width=screen_width, screen_height=screen_height)
    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        for hexagon in hexagons:
            hexagon.update()

        render(screen, hexagons)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()
