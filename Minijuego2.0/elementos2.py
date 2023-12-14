from typing import Any
import pygame
from pygame.sprite import Group, Group


class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
       super().__init__()
        #cargamos la imagen
       self.manolos = [ pygame.image.load("ira2.png"), pygame.image.load("imagen2.png")]
       self.indice_manolo = 0
       self.image = self.manolos[self.indice_manolo]
       self.contador_imagen  = 0
       #creamos un rectangulo a partir de la imagen
       self.rect = self.image.get_rect()
       #actualizar rectangulo para coincidir con rectangulo
       self.rect.topleft = posicion
    #update
    def update(self, *args: any, **kwargs: any):
        #capturamps las teclas
        teclas = args[0]
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pantalla.get_width()- self.image.get_width() , self.rect.x)
        pass
        #gestionamos la animacion
        self.contador_imagen = (self.contador_imagen +1)%40
        self.indice_manolo = self.contador_imagen // 20
        self.image = self.manolos[self.indice_manolo]



class Enemigo(pygame.sprite.Sprite):
    #constructor
        def __init__(self, posicion) :
             super().__init__()
             #cargamos la imagen
             manolo = pygame.image.load("ira2.png")
             self.image = pygame.transform.rotate(manolo, 900)
             #creamos un rectangulo
             self.rect = self.image.get_rect()
             #actualizar posicion
             self.rect.topleft = posicion
        def update(self, *args: Any, **kwargs: Any):
             pantalla = pygame.display.get_surface()
             self.rect.y += 1
             self.rect.x = min(pantalla.get_width()- self.image.get_width(), self.rect.x)
              
