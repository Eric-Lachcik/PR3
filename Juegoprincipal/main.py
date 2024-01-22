import pygame
import elements


#Iniciamos el Juego
pygame.init()


#Tamaño de la Pantalla y posicion de la Nave
tamanio = (800, 800)
pantalla = pygame.display.set_mode(tamanio)
posicion = (355,335)
#Reloj del juego y FPS
reloj = pygame.time.Clock()
FPS = 60

#Fuente para el texto(Menu)
font = pygame.font.Font(None, 30)

#Booleano de Control
running = [True]

#Grupo de Sprites
grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_balas = pygame.sprite.Group()

grupo_sprites_todos.add(elements.Planeta(posicion))

#Bucle Principal
while running[0]:
    #Limitamos los FrameRate
    reloj.tick(FPS)
    
    #Gestionamos la Salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running[0] = False

    #Capturamos la Teclas
    teclas = pygame.key.get_pressed()
    
    
    #Pintamos la Pantalla
    pantalla.fill((80,80,80))
    grupo_sprites_todos.draw(pantalla)
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running)
    #Rdibujamos la Pantalla
    pygame.display.flip()
    pass