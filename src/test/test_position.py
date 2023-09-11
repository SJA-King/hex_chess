import pytest
from ..position import Position
from ..hexes import Hex, HexColours


def test_add_sum():
    x = Position(1, 2, 3)
    y = Position(4, 5, 6)
    z = x + y
    assert z.q == 5
    assert z.r == 7
    assert z.s == 9


def test_add_to_self():
    x = Position(1, 2, 3)
    y = Position(4, 5, 6)
    x += y
    assert x.q == 5
    assert x.r == 7
    assert x.s == 9


def test_positions_equal():
    x = Position(1, 2, 3)
    y = Position(1, 2, 3)
    assert x == y


def test_positions_not_equal():
    x = Position(1, 2, 3)
    y = Position(4, 5, 6)
    assert x != y


def test_position_from_str():
    test_str = "1,2,3"
    test_position = Position.from_str(position_as_str=test_str)
    assert test_position.q == 1
    assert test_position.r == 2
    assert test_position.s == 3


def test_position_from_str_as_key():
    test_qrs = "0,0,0"
    test_board = {test_qrs: Hex(position=Position(0, 0, 0), colour=HexColours.GREY)}

    assert Position.from_str(test_qrs) == test_board[test_qrs].position

    test_board = {test_qrs: Hex(position=Position.from_str(test_qrs), colour=HexColours.GREY)}

    assert Position.from_str(test_qrs) == test_board[test_qrs].position






# test negatives
# add limit for q,r,s - e.g. -4 and +4 - check for each q,r,s etc
# check for multiple adds
# check for mixed adds e.g. +1, 0, -1