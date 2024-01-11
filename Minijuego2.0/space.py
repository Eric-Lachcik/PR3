import pygame
import pygame_menu
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
font = pygame.font.Font(None, 30)

#booleano de control
running = [True]

posicion = (375,540)
#nave = elementos2.Nave(posicion)
#fondo = elementos2.Fondo()
##grupo de sprites
#grupo_sprites_todos = pygame.sprite.Group()
#grupo_sprites_enemigos = pygame.sprite.Group()
#grupo_sprites_balas = pygame.sprite.Group()
#
#
#grupo_sprites_todos.add(fondo)
#grupo_sprites_todos.add(nave)

#crear variable que almacena la aparicion del enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 1500




def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    frecuencia_creacion_enemigo = difficulty
    

def start_the_game():
    

    #booleano de control
    running = [True]

    global ultimo_enemigo_creado
    global reloj
    global FPS
    global frecuencia_creacion_enemigo
    global font
    
    nave = elementos2.Nave(posicion)
    #elementos2.Fondo()
    #grupo de sprites
    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_balas = pygame.sprite.Group()

    
    grupo_sprites_todos.add(elementos2.Fondo())
    grupo_sprites_todos.add(nave)

    pausado = False


    #bucle principal
    while running[0]:
        #limitamos los framerate
        reloj.tick(FPS)


        #gestionar la salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running[0] = False
        
        #capturamos las teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
           running[0] = False
        
        if teclas[pygame.K_LSHIFT]:
            pausado = not pausado

        if not pausado:
            #creamos enemigos
            momento_actual = pygame.time.get_ticks()
            if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                cordx = random.randint(0, pantalla.get_width())
                cordy = -125
                #creamos enemigos
                enemigo = elementos2.Enemigo((cordx,cordy))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual
         
            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running)

        #pintaremos
        pantalla.fill((80,80,80))
        #grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas, grupo_sprites_enemigos, running)
        grupo_sprites_todos.draw(pantalla)
        

        if pausado:
            texto = font.render("PAUSA", True, "Green")
            pantalla.blit(texto, (pantalla.get_width() / 2, pantalla.get_height() / 2))
        
        #Redibujar la pantalla  
        pygame.display.flip()
    pass
    

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Nombre')
menu.add.selector('Difficulty :', [('Hard', 200), ('Easy', 1000)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

#finalizamos el juego
pygame.quit()