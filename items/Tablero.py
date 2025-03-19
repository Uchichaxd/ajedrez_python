from pieces.Pawn import PawnPiece
from pieces.Rook import RookPiece
from pieces.Bishop import BishopPiece
from pieces.Queen import QueenPiece
from pieces.King import KingPiece
from pieces.Knight import KnightPiece
from pieces.Piece import Piece
class Tablero:
    def __init__(self, sprite_dict):
        self.piezas = [[None for _ in range(8)] for _ in range(8)]
        self.sprite_dict = sprite_dict
        self.inicializar_piezas()

    def inicializar_piezas(self):
        # Piezas negras (fila 0 y 1)
        self.piezas[0][0] = Piece('black', (0, 0), 'rook_black', self.sprite_dict)
        self.piezas[0][1] = Piece('black', (0, 1), 'knight_black', self.sprite_dict)
        self.piezas[0][2] = Piece('black', (0, 2), 'bishop_black', self.sprite_dict)
        self.piezas[0][3] = Piece('black', (0, 3), 'queen_black', self.sprite_dict)
        self.piezas[0][4] = Piece('black', (0, 4), 'king_black', self.sprite_dict)
        self.piezas[0][5] = Piece('black', (0, 5), 'bishop_black', self.sprite_dict)
        self.piezas[0][6] = Piece('black', (0, 6), 'knight_black', self.sprite_dict)
        self.piezas[0][7] = Piece('black', (0, 7), 'rook_black', self.sprite_dict)

        # Peones negros (fila 1)
        for col in range(8):
            self.piezas[1][col] = Piece('black', (1, col), 'pawn_black', self.sprite_dict)

        # Peones blancos (fila 6)
        for col in range(8):
            self.piezas[6][col] = Piece('white', (6, col), 'pawn_white', self.sprite_dict)

        # Piezas blancas (fila 7)
        self.piezas[7][0] = Piece('white', (7, 0), 'rook_white', self.sprite_dict)
        self.piezas[7][1] = Piece('white', (7, 1), 'knight_white', self.sprite_dict)
        self.piezas[7][2] = Piece('white', (7, 2), 'bishop_white', self.sprite_dict)
        self.piezas[7][3] = Piece('white', (7, 3), 'queen_white', self.sprite_dict)
        self.piezas[7][4] = Piece('white', (7, 4), 'king_white', self.sprite_dict)
        self.piezas[7][5] = Piece('white', (7, 5), 'bishop_white', self.sprite_dict)
        self.piezas[7][6] = Piece('white', (7, 6), 'knight_white', self.sprite_dict)
        self.piezas[7][7] = Piece('white', (7, 7), 'rook_white', self.sprite_dict)

    def obtener_pieza(self, position):
        fila, columna = position
        return self.piezas[fila][columna]
