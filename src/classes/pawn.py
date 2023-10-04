from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, images_path, info
from src.classes.hexes import HexTile


@dataclass
class Pawn(Piece):
    def __post_init__(self):
        self.name = PieceNames.Pawn
        self.set_image()

    @property
    def moves(self):
        moves = []
        if self.colour == PlayerColour.WHITE:
            moves.append(Position(0, -1, 1))
            if self.turn_moved == 0:
                moves.append(Position(0, -2, 2))

        elif self.colour == PlayerColour.BLACK:
            moves.append(Position(0, 1, -1))
            if self.turn_moved == 0:
                moves.append(Position(0, 2, -2))
        else:
            print(f"Error - Pawn Colour not in {PlayerColour}")

        return moves

    def possible_moves(self, board):
        possible_moves = []
        for move in self.moves:
            new_position = self.position + move
            new_hex = board.get_hex_from_position(new_position)
            if new_hex:
                possible_moves.append(new_hex)
        info(f"Possible Moves are {possible_moves}")
        return possible_moves

    def legal_moves(self, board):
        legal_moves = []
        for a_hex in self.possible_moves(board):
            if a_hex.piece_on_hex is None:
                legal_moves.append(a_hex)
            else:
                break

        diagonal_moves = []
        if self.colour == PlayerColour.WHITE:
            diagonal_moves = [Position(1, -1, 0), Position(-1, 0, 1)]
        elif self.colour == PlayerColour.BLACK:
            diagonal_moves = [Position(1, 0, -1), Position(-1, 1, 0)]
        else:
            print(f"Error - Pawn Colour not in {PlayerColour}")

        for move in diagonal_moves:
            new_position = self.position + move
            new_hex: HexTile = board.get_hex_from_position(new_position)
            if new_hex:
                if new_hex.piece_on_hex:
                    if new_hex.piece_on_hex.colour != self.colour:
                        legal_moves.append(new_hex)
                    else:
                        # it's the same colour
                        pass
                else:
                    # there's no piece to 'attack'
                    pass
            else:
                # there is no hex
                pass

        return legal_moves
