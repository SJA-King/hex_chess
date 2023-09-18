import math
from typing import List, Union

from src.classes.constants import HexColours
from src.classes.hexes import HexTile
from src.classes.position import Position
from src.classes.piece import Piece


class Board:

    def __init__(self, middle_column_length: int = 11,
                 screen_width: int = 0,
                 screen_height: int = 0):
        self.mid_col_length = middle_column_length
        if screen_height == 0 or screen_width == 0:
            raise Exception(f"Screen Size is Non-existent")
        self.middle_x = screen_width / 2
        self.middle_y = screen_height / 2
        self.radius_of_hex = math.floor(int((screen_height / self.mid_col_length) / 2))
        self.positions_to_hextiles: dict[Position, HexTile] = {}
        self.hex_height = 0
        self.hex_width = 0

    def create_hexagon(self, colour, position: Position) -> HexTile:
        """Creates a hexagon tile at the specified position"""
        return HexTile(colour, middle_hex_xy=(self.middle_x, self.middle_y), position=position, radius=self.radius_of_hex)

    def fill_board_with_hextiles(self) -> None:
        colour = HexColours.RED
        centre_position = Position(0, 0, 0)
        self.positions_to_hextiles[centre_position] = self.create_hexagon(colour, centre_position)

        for _ in range(5):
            new_positions = self.positions_to_hextiles.copy()
            for hex_position, the_hex in self.positions_to_hextiles.items():
                for i_pos in Position(0, -1, 1), Position(1, 0, -1), Position(-1, 1, 0):
                    new_hex_position = the_hex.position + i_pos
                    if new_hex_position not in self.positions_to_hextiles:
                        new_positions[new_hex_position] = self.create_hexagon(next(the_hex.colour), new_hex_position)

                for i_pos in Position(0, 1, -1), Position(1, -1, 0), Position(-1, 0, 1):
                    new_hex_position = the_hex.position + i_pos
                    if new_hex_position not in self.positions_to_hextiles:
                        new_positions[new_hex_position] = self.create_hexagon(next(next(the_hex.colour)), new_hex_position)

            self.positions_to_hextiles = new_positions.copy()

    def get_hex_from_position(self, position: Position) -> Union[HexTile, None]:
        if position not in self.positions_to_hextiles:
            # TODO add warning here
            return None
        return self.positions_to_hextiles[position]

    def cache_hex_dimensions(self):
        self.hex_height = int(2 * self.positions_to_hextiles[Position(0, 0, 0)].little_r)
        self.hex_width = int(2 * self.positions_to_hextiles[Position(0, 0, 0)].radius)

    def place_piece_on_hex(self, position: Position, piece, colour) -> None:
        self.positions_to_hextiles[position].piece_on_hex = piece(colour=colour, position=position, hex_height=self.hex_height, hex_width=self.hex_width)

        # Pawn(colour=PlayerColour.BLACK,
        #      position=Position(0, -1, 1),
        #      hex_height=hex_height,
        #      hex_width=hex_width)
