import pygame

from src.classes.board import Board
from src.classes.hexes import HexTile
from src.classes.pieces.pawn import Pawn
from src.classes.pieces.bishop import Bishop
from src.classes.pieces.king import King
from src.classes.pieces.queen import Queen
from src.classes.pieces.rook import Rook
from src.classes.pieces.knight import Knight
from src.classes.constants import HexColours, PlayerColour
from src.classes.position import Position


def render(screen, hexagons: list[HexTile]):
    """Renders hexagons on the screen"""
    screen.fill((0, 0, 0))
    for hexagon in hexagons:
        hexagon.render(screen)

    pygame.display.flip()


def get_qrs_position(x: int = None, y: int = None):
    pass

# todo put this method in the HexTile class



# def test_get_xy_position():
#     radius = 6
#     little_r = 5
#     middle_x = 10
#     middle_y = 10
#
#     x, y = get_xy_position(Position(2, -1, -1), radius, little_r)
#
#     x += middle_x
#     y += middle_y
#     assert x == 28
#     assert y == 10
#
#     x,y = get_xy_position(Position(2, -4, 2), radius, little_r)
#     x += middle_x
#     y += middle_y
#     assert x == 28
#     assert y == -20


# below is wrong as you could have 4, 2, 2
# def gen_unique_positions():
#     positions = []
#     for q in range(-2, 3):
#         for r in range(-2, 3):
#             for s in range(-2, 3):
#                 if s == r:
#                     continue
#                 if s == q:
#                     continue
#                 if r == q:
#                     continue
#                 positions.append(Position(q, r, s))
#
#     return positions


# def test_get_unique_positions():
#     pass


def main():
    """Main function"""
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    the_board = Board(middle_column_length=11, screen_width=screen_width, screen_height=screen_height)
    the_board.fill_board_with_hextiles()
    # hexagons = make_hex_board(screen_width=screen_width, screen_height=screen_height)
    hexagons = the_board.positions_to_hextiles
    the_board.cache_hex_dimensions()
    # hex_height = int(2*hexagons[Position(0,-1,1)].little_r)
    # hex_width = int(2*hexagons[Position(0,-1,1)].radius)
    # hexagons[Position(0,-1,1)].piece_on_hex = Pawn(colour=PlayerColour.BLACK,
    #                                                position=Position(0,-1,1),
    #                                                hex_height=hex_height,
    #                                                hex_width=hex_width)
    the_board.place_black_starting_pieces()
    the_board.place_white_starting_pieces()

    for i_rs in range(3, 6):
        hexagons[Position(0, -i_rs, i_rs)].piece_on_hex = Bishop(colour=PlayerColour.BLACK,
                                                         position=Position(0, -i_rs, i_rs),
                                                         hex_height=the_board.hex_height,
                                                         hex_width=the_board.hex_width)
    # for i_q in range(1, 5):
        hexagons[Position(0, i_rs, -i_rs)].piece_on_hex = Bishop(colour=PlayerColour.WHITE,
                                                         position=Position(0, i_rs, -i_rs),
                                                         hex_height=the_board.hex_height,
                                                         hex_width=the_board.hex_width)
    hexagons[Position(1, -5, 4)].piece_on_hex = King(colour=PlayerColour.BLACK,
                                                             position=Position(1, -5, 4),
                                                             hex_height=the_board.hex_height,
                                                             hex_width=the_board.hex_width)
    hexagons[Position(1, 4, -5)].piece_on_hex = King(colour=PlayerColour.WHITE,
                                                             position=Position(1, 4, -5),
                                                             hex_height=the_board.hex_height,
                                                             hex_width=the_board.hex_width)
    hexagons[Position(-1, -4, 5)].piece_on_hex = Queen(colour=PlayerColour.BLACK,
                                                     position=Position(-1, -4, 5),
                                                     hex_height=the_board.hex_height,
                                                     hex_width=the_board.hex_width)
    hexagons[Position(-1, 5, -4)].piece_on_hex = Queen(colour=PlayerColour.WHITE,
                                                     position=Position(-1, 5, -4),
                                                     hex_height=the_board.hex_height,
                                                     hex_width=the_board.hex_width)
    hexagons[Position(3,-5,2)].piece_on_hex = Rook(colour=PlayerColour.BLACK,
                                                       position=Position(3,-5,2),
                                                       hex_height=the_board.hex_height,
                                                       hex_width=the_board.hex_width)
    hexagons[Position(-3,-2,5)].piece_on_hex = Rook(colour=PlayerColour.BLACK,
                                                      position=Position(-3,-2,5),
                                                      hex_height=the_board.hex_height,
                                                      hex_width=the_board.hex_width)
    hexagons[Position(3,2,-5)].piece_on_hex = Rook(colour=PlayerColour.WHITE,
                                                       position=Position(3,2,-5),
                                                       hex_height=the_board.hex_height,
                                                       hex_width=the_board.hex_width)
    hexagons[Position(-3,5,-2)].piece_on_hex = Rook(colour=PlayerColour.WHITE,
                                                      position=Position(-3,5,-2),
                                                      hex_height=the_board.hex_height,
                                                      hex_width=the_board.hex_width)
    hexagons[Position(2, -5, 3)].piece_on_hex = Knight(colour=PlayerColour.BLACK,
                                                     position=Position(2, -5, 3),
                                                     hex_height=the_board.hex_height,
                                                     hex_width=the_board.hex_width)
    hexagons[Position(-2, -3, 5)].piece_on_hex = Knight(colour=PlayerColour.BLACK,
                                                      position=Position(-2, -3, 5),
                                                      hex_height=the_board.hex_height,
                                                      hex_width=the_board.hex_width)
    hexagons[Position(2, 3, -5)].piece_on_hex = Knight(colour=PlayerColour.WHITE,
                                                     position=Position(2, 3, -5),
                                                     hex_height=the_board.hex_height,
                                                     hex_width=the_board.hex_width)
    hexagons[Position(-2, 5, -3)].piece_on_hex = Knight(colour=PlayerColour.WHITE,
                                                      position=Position(-2, 5, -3),
                                                      hex_height=the_board.hex_height,
                                                      hex_width=the_board.hex_width)
    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        render(screen, list(hexagons.values()))
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()
