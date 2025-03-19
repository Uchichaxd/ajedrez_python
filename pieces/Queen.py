from .Piece import Piece
class QueenPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"queen_{color}"
        super().__init__(color, position, name, sprite_dict)
