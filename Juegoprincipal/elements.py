from typing import Any
import pygame
from pygame.sprite import Group
import math

class Planeta(pygame.sprite.Sprite):
    #Constructor de la Nave
    def __init__(self, posicion, *args):
        super().__init__()
        #cargamos las imagenes
        self.ricardo = pygame.image.load("PlanetaF1.png")
        self.ricardo2 = pygame.transform.scale(self.ricardo, (140,140)).convert_alpha()
        self.image = self.ricardo2
        #Añadimos una mascara
        self.mask = pygame.mask.from_surface(self.image)
        #Rectangulo para la imagen
        self.rect = self.image.get_rect()
        #Actualizamos el rectangulo para que coincida con la imagen
        self.rect.topleft = posicion
        #Disparos
        self.ultimo_disparo = 0
        
        
    def update(self, *args: any, **kwargs: any):
        #Capturamos X e Y
        x = args[5]
        y = args[6]
        posicion = args[8]
        #Capturamos las teclas y el raton
        teclas = args[0]
        click_izdo, click_central, click_dcho = args[9]
        #Capturamos a Todos
        grupo_sprites_todos = args[1]
        #Capturamos las Balas
        grupo_sprites_balas = args[2]
        #Capturamos los Enemigos
        grupo_sprites_enemigos = args[3]
        #Capturamos la Pantalla
        pantalla = pygame.display.get_surface()
        #Capturamos la posicion del mouse
        pos = args[7]
        #Calculamos el angulo del planeta
        x_dist = pos[0] - x
        y_dist = -(pos[1] - y)
        angulo = math.degrees(math.atan2(y_dist, x_dist))
        #Rotacion del Planeta
        self.image = pygame.transform.rotate(self.ricardo2, angulo - 90 )
        self.rect = self.image.get_rect(center = posicion)
        #Video del movimiento de raton
        #https://www.youtube.com/watch?v=WnIycS9Gf_c
        #Gestionamos los disparos
        if click_izdo:
            #Disparar
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)
        
        
    
    def disparar(self, grupo_sprites_todos, grupo_sprites_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            bala = Bala((self.rect.x + self.image.get_width()/2, self.rect.y + self.image.get_width()/2 ))
            grupo_sprites_balas.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_disparo = momento_actual

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

class Bala(pygame.sprite.Sprite):
    
    def __init__(self, posicion) -> None:
        super().__init__()
        #Creamos el rectangulo de la bala
        self.image = pygame.Surface((5,10))
        #Añadimos color a la bala
        self.image.fill((255,0,0))    
        #Añadimos una mascara
        self.mask = pygame.mask.from_surface(self.image)
        #Añadimos el rectangulo
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect -= 5
        pos = args[7]
        x = args[5]
        y = args[6]
        x_dist = pos[0] - x
        y_dist = -(pos[1] - y)
        angulo = math.degrees(math.atan2(y_dist, x_dist))
            