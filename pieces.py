from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field


class Piece:
    player: str = ""
    step: [str] = [""] # TODO change to list(Positions)
    step_repetition: int = 0
    pieces_taken: [Piece] = []
    weight: int = 0



class Pawn(Piece):
    weight = 1
