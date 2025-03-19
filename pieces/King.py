from .Piece import Piece

class KingPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"king_{color}"
        super().__init__(color, position, name, sprite_dict)
