from .Piece import Piece

class BishopPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"bishop_{color}"
        super().__init__(color, position, name, sprite_dict)
