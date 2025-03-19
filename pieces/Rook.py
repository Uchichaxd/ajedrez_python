from .Piece import Piece

class RookPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"rook_{color}"
        super().__init__(color, position, name, sprite_dict)

        