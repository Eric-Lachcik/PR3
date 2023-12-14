import pygame
import elementos2
import random


#iniciamos
pygame.init()

#pantalla
tamanyo = (800, 600)
pantalla = pygame.display.set_mode(tamanyo)

#reloj
reloj = pygame.time.Clock()
FPS = 60


#booleano de control
running = True

posicion = (275,350)
nave = elementos2.Nave(posicion)
#grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)


#crear variable que almecena la aparicion del enemigo
ultimo_enemigo_creado = 0


#bucle principal
while running:
    #limitamos los framerate
    reloj.tick(FPS)


    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #capturamos las teclas
    teclas = pygame.key.get_pressed()
    
    #creamos enemigos
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + 200):
        cordx = random.randint(0, pantalla.get_width())
        cordy = 0
        grupo_sprites.add(elementos2.Enemigo((cordx,cordy)))
        ultimo_enemigo_creado = momento_actual


    #pintaremos
    pantalla.fill((80,80,80))
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)
    
    #Redibujar la pantalla
    pygame.display.flip()

#finalizamos el juego
pygame.quit()