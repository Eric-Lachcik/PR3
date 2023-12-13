import pygame
from pygame.sprite import Group


class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
       super().__init__()
        #cargamos la imagen
       self.image = pygame.image.load("ira2.png")
       #creamos un rectangulo a partir de la imagen
       self.rect = self.image.get_rect()
       #actualizar rectangulo para coincidir con rectangulo
       self.rect.topleft = posicion
    #update
    def update(self, *args: any, **kwargs: any):
        teclas = args[0]
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += 2
        pass

