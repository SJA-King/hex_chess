import pygame

from src.classes.board import make_hex_board
from src.classes.hexes import HexTile
from src.classes.pieces.pawn import Pawn
from src.classes.constants import HexColours, PlayerColour
from src.classes.position import Position


def render(screen, hexagons: list[HexTile]):
    """Renders hexagons on the screen"""
    screen.fill((0, 0, 0))
    for hexagon in hexagons:
        hexagon.render(screen)

    pygame.display.flip()


def main():
    """Main function"""
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    hexagons = make_hex_board(screen_width=screen_width, screen_height=screen_height)
    hexagons[0].piece_on_hex = Pawn(colour=PlayerColour.WHITE, position=Position(0, 0, 0), hex_height=int(2*hexagons[0].little_r), hex_width=int(2*hexagons[0].radius))
    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        render(screen, hexagons)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()
