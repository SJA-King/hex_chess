from __future__ import annotations
from dataclasses import dataclass

import pygame
from abc import ABC, abstractmethod
from src.classes.position import Position
from src.classes.constants import PlayerColour,  PieceNames, images_path, info, warn


@dataclass
class Piece(ABC):
    name: PieceNames = None
    colour: PlayerColour = None
    position: Position = None
    start_position: Position = position
    last_position: Position = position
    hex_width: int = 0
    hex_height: int = 0
    img: pygame.Surface = None
    turn_moved: int = 0
    enpassant: bool = False

    def __str__(self):
        return f"{self.colour}-{self.name.value} at <{self.position}>, moved turn '{self.turn_moved}'"

    def set_image(self, hex_width: int = 0, hex_height: int = 0):
        # TODO remove hex_{height,width} as members
        img_path = images_path / f"{self.colour.value}_{self.name.value}.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (self.hex_width*0.85, self.hex_height*0.85))

    @abstractmethod
    def moves(self):
        pass

    @abstractmethod
    def possible_moves(self, board):
        pass

    def valid_moves(self, board, turn):
        # TODO add in the in_check method here
        return self.possible_moves(board)

    def attacking_moves(self, board, turn):
        attacking_moves = []
        for move in self.valid_moves(board, turn):
            if move.piece_on_hex is not None:
                attacking_moves.append(move)

        return attacking_moves

    def promote_pawn(self, board, new_hex):
        if self.name != PieceNames.Pawn:
            warn(f"A Piece ({self.name}) cant be promoted like a {PieceNames.Pawn}!")
            return
        promote = False
        if self.colour == PlayerColour.WHITE and board.is_position_at_top(new_hex.position):
            promote = True
        if self.colour == PlayerColour.BLACK and board.is_position_at_bottom(new_hex.position):
            promote = True
        if promote:
            from src.classes.queen import Queen
            board.place_piece_on_hex(new_hex.position, Queen, self.colour)
            info(f"Promoted {self.colour.value}-{PieceNames.Pawn.value} TO {PieceNames.Queen.value}")

    def move(self, board, new_hex, turn: int):
        for i_hex in board.hexagons:
            i_hex.highlight = False

        board.selected_piece = None
        if new_hex in self.valid_moves(board, turn):
            old_hex = board.get_hex_from_position(self.position)
            info(f"Move from {old_hex} to {new_hex}")

            self.last_position = self.position
            self.position = new_hex.position

            new_hex.piece_on_hex = old_hex.piece_on_hex
            if self.enpassant:
                new_position = None
                if self.colour == PlayerColour.WHITE:
                    new_position = new_hex.position + Position(0, 1, -1)
                if self.colour == PlayerColour.BLACK:
                    new_position = new_hex.position + Position(0, -1, 1)
                enpassant_hex = board.get_hex_from_position(new_position)
                enpassant_hex.piece_on_hex = None

            old_hex.piece_on_hex = None
            self.turn_moved = turn

            if self.name == PieceNames.Pawn:
                self.promote_pawn(board, new_hex)

            return True

        return False
