import pygame
import objetos

pygame.init()
pantalla = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
FPS = 60
#imagen_avion = pygame.image.load("gato.png")
#avion = pygame.transform.scale(imagenes_cargadas[0],(90,150))
#avion_rect = avion.get_rect()




salir = False

avion = objetos.Avion()
#posIzda = 30
#posTop = 30

while not salir:

    clock.tick(60)
    # gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        avion.moverizquierda()
    if teclas[pygame.K_RIGHT]:
        avion.moverderecha()
    #if teclas[pygame.K_UP]:
    #    posTop -= 1
    #if teclas[pygame.K_DOWN]:
    #    posTop += 1
    # gestionar cambios
    pantalla.fill((80,80,80))

    #pantalla.blit(avion, (posIzda,posTop))
    #pygame.draw.rect(pantalla , (255,255,255), pygame.Rect(posIzda,posTop,68,68))
    avion.dibujar()
    # redibujar juego
    pygame.display.flip()

pygame.quit()