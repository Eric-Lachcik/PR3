import pygame
import elements



#Iniciamos el Juego
pygame.init()

#Tamaño de la Pantalla y posicion de la Nave
tamanio = (1920, 1080)
pantalla = pygame.display.set_mode((tamanio), pygame.FULLSCREEN)
posicion = (650,380)
x = (650)
y = (380)

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

#Añadimos las cosas a los sprites
grupo_sprites_todos.add(elements.Fondo())
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
    #Capturamos la posicion del Mouse
    pos = pygame.mouse.get_pos()
    
    if teclas[pygame.K_ESCAPE]:
        running[0] = False
      
    #Pintamos la Pantalla
    pantalla.fill((80,80,80))
    grupo_sprites_todos.draw(pantalla)
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running, x,y,pos)
    #Rdibujamos la Pantalla
    pygame.display.flip()
    pass