import sys

import pygame

from src.classes.board import Board
from src.classes.hexes import HexTile


def render(screen, board: Board):#hexagons: list[HexTile]):
    """Renders hexagons on the screen"""
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.update()



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

    the_board = Board(middle_column_length=11, screen_width=screen_width, screen_height=screen_height)
    the_board.make_first_hex()
    the_board.fill_board_with_hextiles()
    the_board.place_black_starting_pieces()
    the_board.place_white_starting_pieces()

    terminated = False
    while not terminated:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked
                if event.button == 1:
                    a_hex = the_board.handle_click(mouse_x, mouse_y)
                    print(a_hex)

        render(screen, the_board)


if __name__ == "__main__":
    main()
