from typing import Any
import pygame
from pygame.sprite import Group


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
       self.ultimo_disparo = 0
    #update
    def update(self, *args: any, **kwargs: any):
        #capturamps las teclas
        teclas = args[0]
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        #Gestionamos las teclas
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
    
    def disparar(self, grupo_sprites):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            bala = Bala((self.rect.x + self.image.get_width() /2, self.rect.y))
            grupo_sprites.add(bala)
            self.ultimo_disparo = momento_actual
         



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
             self.rect.y += 1
             #capturamos la pantalla
             pantalla = pygame.display.get_surface()
             self.rect.x = min(pantalla.get_width()- self.image.get_width(), self.rect.x)
             if(self.rect.y > pantalla.get_height()):
                  self.kill()


class Fondo(pygame.sprite.Sprite):
        def __init__(self) -> None:
             super().__init__()
             #cargamos la imagen
             manolo = pygame.image.load("fondopri.png")
             #capturamos la pantalla
             pantalla = pygame.display.get_surface()
             self.image = pygame.transform.scale(manolo, (pantalla.get_width(), pantalla.get_height()))
             #creamos un rectangulo
             self.rect = self.image.get_rect()
             #actualizar posicion
             self.rect.topleft = (0,0)

class Bala(pygame.sprite.Sprite):
        def __init__(self, posicion ) -> None:
             super().__init__()
             #creamos el rectangulo
             self.image = pygame.Surface((5,10))
             self.image.fill((255,0,0))
             self.rect = self.image.get_rect()
             self.rect.center = posicion

        def update(self, *args: Any, **kwargs: Any) -> None:
             self.rect.y -= 5
        
              
