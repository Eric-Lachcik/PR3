import pygame

pygame.init()
pantalla = pygame.display.set.mode((800,800))

salir = False

posIzda = 30
posTop = 30

while not salir:
    # gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    
    teclas = pygame.key.get.pressed()
    if teclas(pygame.K_LEFT):
        posIzda = 1
    if teclas(pygame.K_RIGHT):
        posIzda = 1
    if teclas(pygame.K_TOP):
        posTop = 1
    if teclas(pygame.K_DOWN):
        posTop = 1
    # gestionar cambios
    pantalla.fill((80,80,80))

    pygame.draw.rect(pantalla , (80,80,80), pygame.Rect(posIzda,posTop,68,68))

    # redibujar juego
    pygame.display.flip()

pygame.quit()