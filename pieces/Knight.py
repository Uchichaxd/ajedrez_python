from .Piece import Piece

class KnightPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"knight_{color}"
        super().__init__(color, position, name, sprite_dict)
