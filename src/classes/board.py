import math
from typing import List, Union

from src.classes.hexes import HexTile
from src.classes.pieces.pawn import Pawn
from src.classes.pieces.bishop import Bishop
from src.classes.pieces.king import King
from src.classes.pieces.queen import Queen
from src.classes.pieces.rook import Rook
from src.classes.pieces.knight import Knight
from src.classes.constants import HexColours, PlayerColour
from src.classes.position import Position


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
        self.positions_to_xy: dict[Position, (float, float)] = {}
        self.hex_height = 0
        self.hex_width = 0

    def create_hexagon(self, colour, position: Position) -> HexTile:
        """Creates a hexagon tile at the specified position"""
        new_hex_tile = HexTile(colour, middle_hex_xy=(self.middle_x, self.middle_y), position=position, radius=self.radius_of_hex)
        self.positions_to_xy[position] = (new_hex_tile.x, new_hex_tile.y)
        return new_hex_tile

    def fill_board_with_hextiles(self) -> None:
        colour = HexColours.RED
        centre_position = Position(0, 0, 0)
        self.positions_to_hextiles[centre_position] = self.create_hexagon(colour, centre_position)
        self.hex_height = int(2 * self.positions_to_hextiles[centre_position].little_r)
        self.hex_width = int(2 * self.positions_to_hextiles[centre_position].radius)

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

    @property
    def hexagons(self):
        return list(self.positions_to_hextiles.values())

    def get_hex_from_position(self, position: Position) -> Union[HexTile, None]:
        if position not in self.positions_to_hextiles:
            # TODO add warning here
            return None
        return self.positions_to_hextiles[position]

    def get_hex_from_xy(self, x: int, y: int) -> HexTile:
        closest_position = Position(0, 0, 0)
        x_difference = None
        y_difference = None
        for position, xy in self.positions_to_xy.items():
            if x_difference is None and y_difference is None:
                x_difference = abs(xy[0] - x)
                y_difference = abs(xy[1] - y)
                closest_position = position
            else:
                if abs(xy[0] - x) < x_difference and abs(xy[1] - y) < y_difference:
                    x_difference = abs(xy[0] - x)
                    y_difference = abs(xy[1] - y)
                    closest_position = position

        return self.get_hex_from_position(closest_position)

    def place_piece_on_hex(self, position: Position, piece, colour) -> None:
        self.positions_to_hextiles[position].piece_on_hex = piece(colour=colour, position=position, hex_height=self.hex_height, hex_width=self.hex_width)

    def place_white_piece_on_hex(self, position: Position, piece) -> None:
        self.place_piece_on_hex(position=position, piece=piece, colour=PlayerColour.WHITE)

    def place_black_piece_on_hex(self, position: Position, piece) -> None:
        self.place_piece_on_hex(position=position, piece=piece, colour=PlayerColour.BLACK)

    def place_black_starting_pieces(self):
        self.place_black_pawns()

        for i_rs in range(3, 6):
            self.place_black_piece_on_hex(position=Position(0, -i_rs, i_rs), piece=Bishop)

        self.place_black_piece_on_hex(position=Position(1, -5, 4), piece=King)
        self.place_black_piece_on_hex(position=Position(2, -5, 3), piece=Knight)
        self.place_black_piece_on_hex(position=Position(-2, -3, 5), piece=Knight)
        self.place_black_piece_on_hex(position=Position(-1, -4, 5), piece=Queen)
        self.place_black_piece_on_hex(position=Position(3, -5, 2), piece=Rook)
        self.place_black_piece_on_hex(position=Position(-3, -2, 5), piece=Rook)

    def place_black_pawns(self):
        self.place_black_piece_on_hex(position=Position(0, -1, 1), piece=Pawn)
        for i_q in range(1, 5):
            a_position = Position(-i_q, -1, 1 + i_q)
            self.place_black_piece_on_hex(position=a_position, piece=Pawn)
            a_position = Position(i_q, -1 - i_q, 1)
            self.place_black_piece_on_hex(position=a_position, piece=Pawn)

    def place_white_starting_pieces(self):
        self.place_white_pawns()

        for i_rs in range(3, 6):
            self.place_white_piece_on_hex(position=Position(0, i_rs, -i_rs), piece=Bishop)

        self.place_white_piece_on_hex(position=Position(1, 4, -5), piece=King)
        self.place_white_piece_on_hex(position=Position(2, 3, -5), piece=Knight)
        self.place_white_piece_on_hex(position=Position(-2, 5, -3), piece=Knight)
        self.place_white_piece_on_hex(position=Position(-1, 5, -4), piece=Queen)
        self.place_white_piece_on_hex(position=Position(3,2,-5), piece=Rook)
        self.place_white_piece_on_hex(position=Position(-3,5,-2), piece=Rook)

    def place_white_pawns(self):
        self.place_white_piece_on_hex(position=Position(0, 1, -1), piece=Pawn)
        for i_q in range(1, 5):
            a_position = Position(i_q, 1, -1 - i_q)
            self.place_white_piece_on_hex(position=a_position, piece=Pawn)
            a_position = Position(-i_q, 1 + i_q, -1)
            self.place_white_piece_on_hex(position=a_position, piece=Pawn)

    def handle_click(self, mouse_x: int, mouse_y: int) -> HexTile:
        mouse_x = (mouse_x // 10) * 10
        mouse_y = (mouse_y // 10) * 10
        clicked_hex = self.get_hex_from_xy(mouse_x, mouse_y)
        return clicked_hex