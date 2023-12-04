import pygame

class Avion:
    def __init__(self) -> None:
        
        self.x = 30
        self.y = 30
        self.imagenes_cargadas = [pygame.image.load("imagen.png"), pygame.image.load("imagen2.png")]
        self.contador = 0
    
    def moverderecha(self):
        self.x += 5
        pantalla = pygame.display.get_surface()
        tamanio_pantalla = pantalla.get_width()
        limite = tamanio_pantalla - self.imagenes_cargadas[0].get_width()
        self.x = min(self.x, limite)
    
    def moverizquierda(self):
        self.x -= 5
        Limite = 0
        self.x = max(self.x, Limite)

    
    def dibujar(self):
        pantalla = pygame.display.get_surface()
        
        self.contador = (self.contador + 1) % 40
        seleccionada = self.contador // 20
        pantalla.blit(self.imagenes_cargadas[seleccionada], (self.x, self.y))