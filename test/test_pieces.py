import pytest
from ..pieces import Pawn, Piece, King, Queen, Knight, Rook, Bishop


@pytest.mark.parametrize("piece1, piece2", [
    [King(), Queen()],
    [Queen(), Rook()],
    [Rook(), Knight()],
    [Bishop(), Pawn()],
    [Knight(), Pawn()],
])
def test_pieces_values(piece1: Piece, piece2: Piece):

    assert piece1.value > piece2.value, f"Piece2={piece2} has HIGHER value than Piece1={piece1}"
