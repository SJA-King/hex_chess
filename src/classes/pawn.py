from dataclasses import dataclass

from src.classes.piece import Piece
from src.classes.position import Position
from src.classes.constants import PlayerColour, PieceNames, info, die
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
            new_hex = board.positions_to_hextiles.get(new_position)
            if new_hex:
                if new_hex.piece_on_hex is None:
                    possible_moves.append(new_hex)
                else:
                    break
        info(f"Possible Moves are {possible_moves}")
        return possible_moves

    def attacking_moves(self, board, turn):
        diagonal_moves = []
        enpassant_position = None
        if self.colour == PlayerColour.WHITE:
            diagonal_moves = [Position(1, -1, 0), Position(-1, 0, 1)]
            enpassant_position = Position(0, 1, -1)
        elif self.colour == PlayerColour.BLACK:
            diagonal_moves = [Position(1, 0, -1), Position(-1, 1, 0)]
            enpassant_position = Position(0, -1, 1)
        else:
            die(f"Error - Pawn Colour not in {PlayerColour}")

        attacking_moves = []
        for move in diagonal_moves:
            new_position = self.position + move
            new_hex: HexTile = board.positions_to_hextiles.get(new_position)
            if new_hex:
                if new_hex.piece_on_hex:
                    if new_hex.piece_on_hex.colour != self.colour:
                        attacking_moves.append(new_hex)
                    else:
                        # it's the same colour
                        pass
                else:
                    # En Passant
                    new_position += enpassant_position
                    enpassant_hex = board.positions_to_hextiles.get(new_position)

                    if enpassant_hex:
                        if enpassant_hex.piece_on_hex:
                            if enpassant_hex.piece_on_hex.colour != self.colour:
                                if enpassant_hex.piece_on_hex.name == PieceNames.Pawn:
                                    if enpassant_hex.piece_on_hex.turn_moved == turn - 1:
                                        attacking_moves.append(new_hex)
                                        self.enpassant = True
                    else:
                        # there's no piece to 'attack'
                        pass
            else:
                # there is no hex
                pass

        return attacking_moves

    def valid_moves(self, board, turn):
        return self.attacking_moves(board, turn) + self.possible_moves(board)
