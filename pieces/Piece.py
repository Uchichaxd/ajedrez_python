#Clase abstracta para las piezas
class Piece:
    def __init__(self, color, position, name, sprite_dict):
        self.color = color
        self.position = position
        self.name = name
        self.image = sprite_dict[name]  # Obtiene la imagen desde el diccionario

    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (y * 80, x * 80))  # Dibuja la pieza

    def movimientos_posibles(self, tablero):
        # Lógica para calcular los movimientos posibles
        pass