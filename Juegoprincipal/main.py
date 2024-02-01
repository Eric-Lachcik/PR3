import pygame
import elements
import random




#Iniciamos el Juego
pygame.init()

#Tamaño de la Pantalla y posicion de la Nave
tamanio = (1920, 1080)
pantalla = pygame.display.set_mode((tamanio), pygame.FULLSCREEN)
posicion = (710,480)
x = (710)
y = (480)

#Frecuencias del Enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 1500

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

fondo = elements.Fondo()
planeta = elements.Planeta((posicion))
grupo_sprites_todos.add(fondo, planeta)

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
    dis = pygame.mouse.get_pressed()
    
    if teclas[pygame.K_ESCAPE]:
        running[0] = False
      
    #Aparicion  del enemigo
    momento_actual = pygame.time.get_ticks()
    if(momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
        cordx = random.randint(0, pantalla.get_width())
        cordy = -125
        #Creamos al enemigo
        enemigo = elements.Enemigo((cordx,cordy))
        grupo_sprites_todos.add(enemigo)
        grupo_sprites_enemigos.add(enemigo)
        ultimo_enemigo_creado = momento_actual
         
      
    #Pintamos la Pantalla
    pantalla.fill((80,80,80))
    grupo_sprites_todos.draw(pantalla)
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running, x,y,pos,posicion, dis)
    #Rdibujamos la Pantalla
    pygame.display.flip()
    pass