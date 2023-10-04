from __future__ import annotations
from dataclasses import dataclass

import pygame
from abc import ABC, abstractmethod
from src.classes.position import Position
from src.classes.constants import PlayerColour,  PieceNames, images_path, info


@dataclass
class Piece(ABC):
    name: PieceNames = None
    colour: PlayerColour = None
    position: Position = None
    hex_width: int = 0
    hex_height: int = 0
    img: pygame.Surface = None
    moved: bool = None

    def __post_init__(self):
        self.moved = False

    def __str__(self):
        return f"{self.name} : {self.colour} : {self.position} : Moved={self.moved}"

    def set_image(self, hex_width: int = 0, hex_height: int = 0):
        # TODO remove hex_{height,width} as memebers
        img_path = images_path / f"{self.colour.value}_{self.name.value}.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (self.hex_width*0.85, self.hex_height*0.85))

    @abstractmethod
    def moves(self):
        pass

    @abstractmethod
    def possible_moves(self, board):
        pass

    @abstractmethod
    def legal_moves(self, board):
        pass

    def promote_pawn(self, board, new_hex):
        promote = False
        if self.colour == PlayerColour.WHITE and board.is_position_at_top(new_hex.position):
            promote = True
        if self.colour == PlayerColour.BLACK and board.is_position_at_bottom(new_hex.position):
            promote = True
        if promote:
            from src.classes.queen import Queen
            board.place_piece_on_hex(new_hex.position, Queen, self.colour)
            info(f"Promoted {self.colour.value}-{PieceNames.Pawn.value} TO {PieceNames.Queen.value}")

    def move(self, board, new_hex):
        for i_hex in board.hexagons:
            i_hex.highlight = False

        board.selected_piece = None
        if new_hex in self.legal_moves(board):
            old_hex = board.get_hex_from_position(self.position)
            info(f"Move from {old_hex} to {new_hex}")
            self.position = new_hex.position
            new_hex.piece_on_hex = old_hex.piece_on_hex
            old_hex.piece_on_hex = None
            self.moved = True

            if self.name == PieceNames.Pawn:
                self.promote_pawn(board, new_hex)

            return True

        return False
