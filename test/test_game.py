import pytest

from ..game import Game

#
# @pytest.fixture(scope="module", autouse=True)
# def make_game():
#     game = Game()
#     game.make_board()
#     return game


def test_make_board():
    test_game = Game()
    test_game.make_board()

    assert len(test_game.board) == 91
    assert test_game.board["0,-5,5"]


