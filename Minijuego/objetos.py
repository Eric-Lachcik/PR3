import pygame
import math
class Avion:
    def __init__(self) -> None:
        
        self.x = 285
        self.y = 425
        self.imagenes_cargadas = [pygame.image.load("imagen.png"), pygame.image.load("imagen2.png")]
        self.contador = 0
    
    def moverderecha(self):
        self.x += 7
        pantalla = pygame.display.get_surface()
        tamanio_pantalla = pantalla.get_width()
        limite = tamanio_pantalla - self.imagenes_cargadas[0].get_width()
        self.x = min(self.x, limite)
    
    def moverizquierda(self):
        self.x -= 7
        Limite = 0
        self.x = max(self.x, Limite)

    
    def dibujar(self):
        pantalla = pygame.display.get_surface()
        
        self.contador = (self.contador + 1) % 40
        seleccionada = self.contador // 20
        pantalla.blit(self.imagenes_cargadas[seleccionada], (self.x, self.y))


class Fondo:
    def __init__(self) -> None:
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #cargamos la pantalla
        imagen = pygame.image.load("fondopri.png")
        self.fondo = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        #scroll
        self.scroll = 0
        #cuantas piezas
        self.piezas = math.ceil(pantalla.get_height() / self.fondo.get_height())+1

    def dibujar(self):
        #aumentar scroll
        self.scroll += 1
        #localizar pantalla
        pantalla = pygame.display.get_surface()
        #resetear scroll
        if self.scroll > self.fondo.get_height():
            self.scroll = 0
        #dibujamos el fondo
        for i in range(0, self.piezas):
            pantalla.blit(self.fondo, (0, -self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))