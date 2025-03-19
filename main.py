import pygame
from items.Tablero import Tablero
from pieces.spritesheetLoader import load_pieces_from_spritesheet
pygame.init()
sizeBox = 80
sizeBoard = 8 * sizeBox
screen = pygame.display.set_mode((sizeBoard, sizeBoard))
pygame.display.set_caption("Chess")

def drawBoard(Screen):
    for row in range(8):
        for column in range(8):
            color = (255, 255, 255) if (row + column) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(Screen, color, (column * sizeBox, row * sizeBox, sizeBox, sizeBox))

def drawPieces(Screen, board):
    for fila in range(8):
        for columna in range(8):
            pieza = board.obtener_pieza((fila, columna))
            if pieza:
                Screen.blit(pieza.image, (columna * sizeBox, fila * sizeBox))


# Cargar todas las piezas desde el spritesheet
sprite_dict = load_pieces_from_spritesheet("assets/Chess-Pieces/16x16_chess_piece_2.png")

# Inicializar el tablero con las piezas
board = Tablero(sprite_dict)

# Bucle principal
while True:
    drawBoard(screen)  # Dibuja el tablero
    drawPieces(screen, board)  # Dibuja las piezas
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            