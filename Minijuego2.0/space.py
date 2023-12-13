import pygame
import elementos2
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

posicion = (200,200)
nave = elementos2.Nave(posicion)
#grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementos2.Nave((300,300)))
grupo_sprites.add(elementos2.Nave((400,100)))
grupo_sprites.add(elementos2.Nave((500,200)))


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
    
    #pintaremos
    pantalla.fill((80,80,80))
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)
    
    #Redibujar la pantalla
    pygame.display.flip()

#finalizamos el juego
pygame.quit()