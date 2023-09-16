import math
from typing import List

from src.classes.constants import HexColours
from src.classes.hexes import HexTile
from src.classes.position import Position


def create_hexagon(colour, centre, radius: int = 50) -> HexTile:
    """Creates a hexagon tile at the specified position"""
    return HexTile(colour=colour, centre_xy=centre, radius=radius)


def make_hex_board(screen_width: int = 0, screen_height: int = 0) -> dict[Position, HexTile]:
    length_of_middle_column = 11

    radius_of_hex = math.floor(int((screen_height / length_of_middle_column) / 2))

    middle_x = screen_width / 2
    middle_y = screen_height / 2

    positions_to_hextiles = {}

    starting_colour = HexColours.RED
    colour = starting_colour
    centre_position = Position(0, 0, 0)
    positions_to_hextiles[centre_position] = HexTile(colour,
                                                     middle_hex_xy=(middle_x, middle_y),
                                                     position=centre_position,
                                                     radius=radius_of_hex)
    for _ in range(5):
        new_positions = positions_to_hextiles.copy()
        for hex_position, the_hex in positions_to_hextiles.items():
            for i_pos in Position(0, -1, 1), Position(1, 0, -1), Position(-1, 1, 0):
                new_hex_position = the_hex.position + i_pos
                if new_hex_position not in positions_to_hextiles:
                    new_positions[new_hex_position] = HexTile(next(the_hex.colour),
                                                                      middle_hex_xy=(middle_x, middle_y),
                                                                      position=new_hex_position,
                                                                      radius=radius_of_hex)

            for i_pos in Position(0, 1, -1), Position(1, -1, 0), Position(-1, 0, 1):
                new_hex_position = the_hex.position + i_pos
                if new_hex_position not in positions_to_hextiles:
                    new_positions[new_hex_position] = HexTile(next(next(the_hex.colour)),
                                                                      middle_hex_xy=(middle_x, middle_y),
                                                                      position=new_hex_position,
                                                                      radius=radius_of_hex)

        positions_to_hextiles = new_positions.copy()

    return positions_to_hextiles
