import math
from typing import List, Union, Type

import pygame.surface

from src.classes.hexes import HexTile
from src.classes.piece import Piece
from src.classes.pawn import Pawn
from src.classes.bishop import Bishop
from src.classes.king import King
from src.classes.queen import Queen
from src.classes.rook import Rook
from src.classes.knight import Knight
from src.classes.constants import HexColours, PlayerColour, info, warn, die
from src.classes.position import Position


class Board:

    def __init__(self, middle_column_length: int = 11, screen_width: int = 0, screen_height: int = 0):
        self.mid_col_length = middle_column_length
        if screen_height == 0 or screen_width == 0:
            die("Screen Size is Non-existent")
        self.middle_x = screen_width / 2
        self.middle_y = screen_height / 2
        self.radius_of_hex = math.floor(int((screen_height / self.mid_col_length) / 2))
        self.positions_to_hextiles: dict[Position, HexTile] = {}
        self.positions_at_top = []
        self.positions_at_bottom = []
        self.xy_to_positions: dict[(float, float), Position] = {}
        self.hex_height: int = 0
        self.hex_width: int = 0
        self.turn: PlayerColour = PlayerColour.WHITE
        self.selected_piece: Union[Piece, None] = None
        self.set_hex_info = False
        self.board_size: int = 5
        self.turn_number: int = 1

    def create_hexagon(self, colour: HexColours, position: Position) -> HexTile:
        """Creates a hexagon tile at the specified position"""
        new_hex_tile = HexTile(colour,
                               middle_hex_xy=(self.middle_x, self.middle_y),
                               position=position,
                               radius=self.radius_of_hex)
        self.xy_to_positions[(new_hex_tile.x, new_hex_tile.y)] = position
        return new_hex_tile

    def make_first_hex(self):
        """ Create the First Hex (generally the middle one)"""
        if self.set_hex_info:
            die("Trying to Set First Hex Again!")
        centre_position = Position(0, 0, 0)
        first_hex = self.create_hexagon(colour=HexColours.RED, position=centre_position)
        self.positions_to_hextiles[centre_position] = first_hex
        self.hex_height = int(2 * first_hex.little_r)
        self.hex_width = int(2 * first_hex.radius)
        self.set_hex_info = True

    def fill_board_with_hextiles(self) -> None:
        """ Using the first hex as a template, compute the surronding hexes for the outgoing rings of hexes to make a board """
        for _ in range(self.board_size):
            new_positions = self.positions_to_hextiles.copy()
            for hex_position, the_hex in self.positions_to_hextiles.items():
                for i_pos in Position(0, -1, 1), Position(1, 0, -1), Position(-1, 1, 0):
                    new_hex_position = the_hex.position + i_pos
                    if new_hex_position not in self.positions_to_hextiles:
                        new_positions[new_hex_position] = self.create_hexagon(next(the_hex.colour), new_hex_position)

                for i_pos in Position(0, 1, -1), Position(1, -1, 0), Position(-1, 0, 1):
                    new_hex_position = the_hex.position + i_pos
                    if new_hex_position not in self.positions_to_hextiles:
                        new_positions[new_hex_position] = self.create_hexagon(next(next(the_hex.colour)),
                                                                              new_hex_position)

            self.positions_to_hextiles = new_positions.copy()

    def is_position_at_top(self, position: Position) -> bool:
        """ Check if a position (representing a HexTile) is at the TOP of the board """
        if position.s == self.board_size or position.r == -self.board_size:
            info(f"position: {position} at TOP!")
            return True
        return False

    def is_position_at_bottom(self, position: Position) -> bool:
        """ Check if a position (representing a HexTile) is at the BOTTOM of the board """
        if position.s == -self.board_size or position.r == self.board_size:
            info(f"position: {position} at BOTTOM!")
            return True
        return False

    @property
    def hexagons(self) -> list[HexTile]:
        """ Provide a list of all HexTiles that make up this board"""
        return list(self.positions_to_hextiles.values())

    def get_hex_from_xy(self, x: int, y: int) -> Union[HexTile, None]:
        """ Calculate from an x, y coord pair what HexTile 'likely' contains said pair"""
        x_difference = None
        y_difference = None
        closest_x = None
        closest_y = None
        for i_hex in self.positions_to_hextiles.values():
            if x_difference is None or x_difference > abs(i_hex.x - x):
                x_difference = abs(i_hex.x - x)
                closest_x = i_hex.x

            if y_difference is None or y_difference > abs(i_hex.y - y):
                y_difference = abs(i_hex.y - y)
                closest_y = i_hex.y

        if (closest_x, closest_y) in self.xy_to_positions:
            closest_position = self.xy_to_positions[(closest_x, closest_y)]
            return self.positions_to_hextiles.get(closest_position)
        else:
            # TODO need to fix when we click too close to edge of Hex
            return None

    def place_piece_on_hex(self, position: Position, piece, colour: PlayerColour) -> None:
        """ Place a piece_on_hex of any Piece Type on a HexTile at position"""
        self.positions_to_hextiles[position].piece_on_hex = piece(colour=colour,
                                                                  position=position,
                                                                  hex_height=self.hex_height,
                                                                  hex_width=self.hex_width)

    def place_white_piece_on_hex(self, position: Position, piece: Type[Piece]) -> None:
        """ Place a White piece on a HexTile at position"""
        self.place_piece_on_hex(position=position, piece=piece, colour=PlayerColour.WHITE)

    def place_black_piece_on_hex(self, position: Position, piece: Type[Piece]) -> None:
        """ Place a Black piece on a HexTile at position"""
        self.place_piece_on_hex(position=position, piece=piece, colour=PlayerColour.BLACK)

    def place_black_starting_pieces(self) -> None:
        """ Place all the Black Pieces in their starting locations"""
        self.place_black_piece_on_hex(position=Position(0, -1, 1), piece=Pawn)
        for i_q in range(1, 5):
            self.place_black_piece_on_hex(position=Position(-i_q, -1, 1 + i_q), piece=Pawn)
            self.place_black_piece_on_hex(position=Position(i_q, -1 - i_q, 1), piece=Pawn)

        for i_rs in range(3, 6):
            self.place_black_piece_on_hex(position=Position(0, -i_rs, i_rs), piece=Bishop)

        for position, piece in [[Position(1, -5, 4), King],
                                [Position(2, -5, 3), Knight], [Position(-2, -3, 5), Knight],
                                [Position(-1, -4, 5), Queen],
                                [Position(3, -5, 2), Rook], [Position(-3, -2, 5), Rook]]:
            self.place_black_piece_on_hex(position=position, piece=piece)

    def place_white_starting_pieces(self) -> None:
        """ Place all the White Pieces in their starting locations"""
        self.place_white_piece_on_hex(position=Position(0, 1, -1), piece=Pawn)
        for i_q in range(1, 5):
            self.place_white_piece_on_hex(position=Position(i_q, 1, -1 - i_q), piece=Pawn)
            self.place_white_piece_on_hex(position=Position(-i_q, 1 + i_q, -1), piece=Pawn)

        for i_rs in range(3, 6):
            self.place_white_piece_on_hex(position=Position(0, i_rs, -i_rs), piece=Bishop)

        for position, piece in [[Position(1, 4, -5), King],
                                [Position(2, 3, -5), Knight], [Position(-2, 5, -3), Knight],
                                [Position(-1, 5, -4), Queen],
                                [Position(3, 2, -5), Rook], [Position(-3, 5, -2), Rook]]:
            self.place_white_piece_on_hex(position=position, piece=piece)

    def handle_click(self, mouse_x: int, mouse_y: int) -> Union[HexTile, None]:
        """ For a click on the board work out what can be done with it """
        clicked_hex = self.get_hex_from_xy(mouse_x, mouse_y)
        info(f"Clicked Hex {clicked_hex}")
        if not clicked_hex:
            return None
        if self.selected_piece is None:
            if clicked_hex.piece_on_hex is not None:
                if clicked_hex.piece_on_hex.colour == self.turn:
                    self.selected_piece = clicked_hex.piece_on_hex

        elif self.selected_piece.move(self, clicked_hex, self.turn_number):
            info(f"Player-{self.turn.value}, Turn {self.turn_number}")
            self.turn = PlayerColour.WHITE if self.turn == PlayerColour.BLACK else PlayerColour.BLACK
            self.turn_number += 1

        elif clicked_hex.piece_on_hex is not None:
            if clicked_hex.piece_on_hex.colour == self.turn:
                self.selected_piece = clicked_hex.piece_on_hex
        return clicked_hex

    def in_check(self) -> bool:
        """ Work out if the current Players' King is in check"""
        return False

    def render(self, screen: pygame.surface.Surface) -> None:
        """Renders hexagons on the screen"""
        if self.selected_piece is not None:
            self.positions_to_hextiles.get(self.selected_piece.position).highlight = True
            for a_hex in self.selected_piece.valid_moves(self, self.turn_number):
                a_hex.highlight = True
        for hexagon in self.hexagons:
            hexagon.render(screen)
