import pygame

class Avion:
    def _init_(self) -> None:
        self.x = 30
        self.y = 30
        self.imagen = pygame.image.load("gato.png")
    
    def moverderecha(self):
        self.x += 1
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.imagen.get_width)
    
    def moverizquierda(self):
        self.x -= 1
        Limite = 0
        self.x = max(self.x, Limite)

    
    def dibujar(self):
        pantalla = pygame.display.get_surface()
        pantalla.blit(self.imagen, (self.x, self.y))