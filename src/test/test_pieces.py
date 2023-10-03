import pytest
from ..classes.piece import Piece
from ..classes.position import Position

# a_king = King(player=Players.WHITE, start=Position(1, 1, 1))
# a_queen = Queen(player=Players.WHITE, start=Position(1, 1, 1))
# a_bishop = Bishop(player=Players.WHITE, start=Position(1, 1, 1))
# a_rook = Rook(player=Players.WHITE, start=Position(1, 1, 1))
# a_pawn = Pawn(player=Players.WHITE, start=Position(1, 1, 1))
# a_knight = Knight(player=Players.WHITE, start=Position(1, 1, 1))
#
#
# @pytest.mark.parametrize("piece1, piece2", [
#     [a_king, a_queen],
#     [a_queen, a_rook],
#     [a_rook, a_knight],
#     [a_bishop, a_pawn],
#     [a_knight, a_pawn],
# ])
# def test_pieces_values(piece1: Piece, piece2: Piece):
#     assert piece1.value > piece2.value, f"Piece2={piece2} has HIGHER value than Piece1={piece1}"

# TODO test piece creation
# TODO test no player results in exception
# TODO test no start position results in exception
