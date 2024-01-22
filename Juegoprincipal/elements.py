from typing import Any
import pygame
from pygame.sprite import  Group


class Planeta(pygame.sprite.Sprite):
    #Constructor de la Nave
    def __init__(self, posicion):
        super().__init__()
        #cargamos las imagenes
        self.ricardo = pygame.image.load("PlanetaF1.png")
        self.ricardo2 = pygame.transform.scale(self.ricardo, (100,100))
        self.image = self.ricardo2
        self.mask = pygame.mask.from_surface(self.image)
        #Rectangulo para la imagen
        self.rect = self.image.get_rect()
        #Actualizamos el rectangulo para que coincida con la imagen
        self.rect.topleft = posicion

class Fondo(pygame.sprite.Sprite):
    
    def __init__(self,) -> None:
        super().__init__()
        #Cargamos la imagen del Fondo
        