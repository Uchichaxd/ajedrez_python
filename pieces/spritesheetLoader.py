import pygame

def load_pieces_from_spritesheet(path, size=16):
    """
    Carga las piezas desde el spritesheet.

    :param path: Ruta del spritesheet.
    :param size: Tamaño individual de cada pieza (16x16).
    :return: Diccionario con las piezas asignadas por nombre.
    """
    spritesheet = pygame.image.load(path).convert_alpha()

    # Diccionario para asociar las piezas con sus sprites
    pieces = {}

    # Mapeo de nombres a coordenadas (fila, columna)
    piezas = {
        "pawn_white": (4, 0), "knight_white": (4, 1), "rook_white": (4, 2),
        "bishop_white": (4, 3), "queen_white": (4, 4), "king_white": (4, 5),

        "pawn_black": (6, 0), "knight_black": (6, 1), "rook_black": (6, 2),
        "bishop_black": (6, 3), "queen_black": (6, 4), "king_black": (6, 5)
    }

    # Extrae cada pieza del spritesheet
    for name, (row, col) in piezas.items():
        # Obtiene la subimagen del spritesheet
        piece_sprite = spritesheet.subsurface(
            pygame.Rect(col * size, row * size, size, size)
        )
        
        # Escala la imagen al tamaño del tablero (80x80)
        piece_sprite = pygame.transform.scale(piece_sprite, (80, 80))
        pieces[name] = piece_sprite

    return pieces
