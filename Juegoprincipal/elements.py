from typing import Any
import pygame
from pygame.sprite import  Group


class Planeta(pygame.sprite.Sprite):
    #Constructor de la Nave
    def __init__(self, posicion):
        super().__init__()
        #cargamos las imagenes
        self.ricardo = pygame.image.load("PlanetaF1.png")
        self.ricardo2 = pygame.transform.scale(self.ricardo, (140,140))
        self.image = self.ricardo2
        self.mask = pygame.mask.from_surface(self.image)
        #Rectangulo para la imagen
        self.rect = self.image.get_rect()
        #Actualizamos el rectangulo para que coincida con la imagen
        self.rect.topleft = posicion
    
    def update(self, *args: any, **kwargs: any):
        #Capturamos las teclas
        teclas = args[0]
        #Capturamos a Todos
        grupo_sprites_todos = args[1]
        #Capturamos las Balas
        grupo_sprites_balas = args[2]
        #Capturamos la Pantalla
        pantalla = pygame.display.get_surface()
        #Gestionamos las teclas para la rotación de Planeta
        
        return 

class Fondo(pygame.sprite.Sprite):
    
    def __init__(self,) -> None:
        super().__init__()
        #Cargamos la imagen del Fondo
        paco = pygame.image.load("fondoF.png")
        #Capturamos la Pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(paco,(pantalla.get_width(), pantalla.get_height()))
        #Creamos un Rectangulo
        self.rect = self.image.get_rect()
        #Actualizamos su posición
        self.rect.topleft = (0,0)
        