import pytest
from ..pieces import Pawn, Piece, King, Queen, Knight, Rook, Bishop
from ..constants import Players
from ..position import Position

x = Position(1,1,1)
king = King(player=Players.WHITE, starting_position=x)
queen = Queen(Players.BLACK, x)

@pytest.mark.parametrize("piece1, piece2", [
    [, Queen()],
    [Queen(), Rook()],
    [Rook(), Knight()],
    [Bishop(), Pawn()],
    [Knight(), Pawn()],
])
def test_pieces_values(piece1: Piece, piece2: Piece):

    assert piece1.value > piece2.value, f"Piece2={piece2} has HIGHER value than Piece1={piece1}"
