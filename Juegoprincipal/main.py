import pygame
import elements
import random




#Iniciamos el Juego
pygame.init()

#Tamaño de la Pantalla y posicion de la Nave
tamaño = (1920, 1080)
pantalla = pygame.display.set_mode((tamaño), pygame.FULLSCREEN)
#posicion = (960,550)
posicion = (710,480)
x = (710)
y = (480)

#Frecuencias del Enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 50

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
bala = elements.Bala((0,0),0)
grupo_sprites_todos.add(fondo, planeta, bala)


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
    if random.randint(0,1000) < frecuencia_creacion_enemigo:
        spawn = random.randint(1,4)
        if spawn == 1:
            cordx1 = random.randint(-120, 0)
            cordy1 = random.randint(0, 1080)
            enemigo = elements.Enemigo((cordx1, cordy1))
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
        elif spawn == 2:
            cordx2 = random.randint(0,1920)
            cordy2 = random.randint(-120, 0)
            enemigo = elements.Enemigo((cordx2, cordy2))
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
        elif spawn == 3:
            cordx3 = random.randint(1920,2120)
            cordy3 = random.randint(0, 1080)
            enemigo = elements.Enemigo((cordx3, cordy3))
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
        elif spawn == 4:
            cordx4 = random.randint(0,1920)
            cordy4 = random.randint(1080, 1300)
            enemigo = elements.Enemigo((cordx4, cordy4))
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
            
    #Movemos a los enemigos
    for enemigo in grupo_sprites_enemigos:
        enemigo.movimiento_enemigo(planeta)

    #Colisiones con el Planeta
    for enemigo in grupo_sprites_enemigos:
        if pygame.sprite.collide_mask(enemigo, planeta):
            grupo_sprites_enemigos.remove(enemigo)
            grupo_sprites_todos.remove(enemigo)
            running[0] = False         
 
    #Pintamos la Pantalla
    pantalla.fill((80,80,80))
    grupo_sprites_todos.draw(pantalla)
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running, x,y,pos,posicion, dis)
    #Redibujamos la Pantalla
    pygame.display.flip()
    pass