from .Piece import Piece
class PawnPiece(Piece):
    def __init__(self, color, position, sprite_dict):
        name = f"pawn_{color}"
        super().__init__(color, position, name, sprite_dict)
