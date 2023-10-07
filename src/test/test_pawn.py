import pytest

from ..classes.board import Board
from ..classes.pawn import Pawn
from ..classes.position import Position
from ..classes.constants import PlayerColour


@pytest.fixture()#scope="module", autouse=True)
def make_board() -> Board:
    return Board(9, 100, 200)


def test_pawn_can_move_twice_on_first_turn(make_board):
    a_board = make_board
    a_board.make_first_hex()
    a_board.fill_board_with_hextiles()
    pawn_position = Position(0,0,0)
    a_pawn = Pawn(colour=PlayerColour.WHITE, position=pawn_position, hex_height=a_board.hex_height, hex_width=a_board.hex_width)
    a_board.positions_to_hextiles[pawn_position].piece_on_hex = a_pawn
    assert len(a_pawn.valid_moves(a_board, 0)) == 2


def test_pawn_can_move_once_on_turns_after_first():
    pass


def test_pawn_cant_move_twice_on_first_turn_as_piece_in_way():
    # check a piece on space 2 away
    # check both colours
    # check piece on space in front
    # check both colours
    pass


def test_pawn_can_take_a_piece():
    # check can take on left diag
    # check can take on right diag
    # check for both colours
    pass


def test_pawn_can_en_passant():
    # check both sides
    # check both colours
    pass


def test_pawn_gets_promoted():
    # check both colours
    pass
