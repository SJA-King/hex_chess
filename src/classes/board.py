import math
from typing import List

from src.classes.constants import HexColours
from src.classes.hexes import HexTile


def create_hexagon(colour, centre, radius: int = 50) -> HexTile:
    """Creates a hexagon tile at the specified position"""
    return HexTile(colour=colour, centre=centre, radius=radius)


def make_hex_board(screen_width: int = 0, screen_height: int = 0) -> List[HexTile]:

    length_of_middle_column = 11

    radius_of_hex = math.floor(int((screen_height / length_of_middle_column) / 2))

    middle_x = screen_width / 2
    middle_y = screen_height / 2 + 2*radius_of_hex  # small offset

    top_hex = create_hexagon(centre=(middle_x, middle_y), radius=radius_of_hex, colour=(0,0,0))

    top_y = middle_y - math.ceil(length_of_middle_column / 2) * 2*top_hex.little_r
    hexagons = []

    starting_colour = HexColours.RED
    colour = starting_colour

    for i_row in range(length_of_middle_column):
        a_hex = create_hexagon(colour=colour, radius=top_hex.radius, centre=(middle_x, (top_y + i_row*2*top_hex.little_r)))
        colour = next(colour)
        hexagons.append(a_hex)

    col_count = 1
    for i_rows_in_column in range(length_of_middle_column-1, math.floor(length_of_middle_column / 2), -1):
        starting_colour = next(next(starting_colour))
        colour = starting_colour
        top_y += top_hex.little_r

        for i_row in range(i_rows_in_column):
            y = top_y + i_row*2*top_hex.little_r
            a_hex = create_hexagon(colour=colour, radius=top_hex.radius, centre=(middle_x + col_count * 1.5 * radius_of_hex, y))
            hexagons.append(a_hex)
            a_hex = create_hexagon(colour=colour, radius=top_hex.radius, centre=(middle_x - col_count * 1.5 * radius_of_hex, y))
            hexagons.append(a_hex)
            colour = next(colour)

        col_count += 1

    return hexagons
