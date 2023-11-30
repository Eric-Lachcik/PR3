import pygame

pygame.init()
pantalla = pygame.display.set_mode((800,800))

imagen_avion = pygame.image.load("cosa.png")
avion = pygame.transform.scale(imagen_avion,(90,150))
avion_rect = avion.get_rect()




salir = False


posIzda = 30
posTop = 30

while not salir:
    # gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posIzda -= 1
    if teclas[pygame.K_RIGHT]:
        posIzda += 1
    if teclas[pygame.K_UP]:
        posTop -= 1
    if teclas[pygame.K_DOWN]:
        posTop += 1
    # gestionar cambios
    pantalla.fill((80,80,80))

    pantalla.blit(avion, (posIzda,posTop))
    #pygame.draw.rect(pantalla , (255,255,255), pygame.Rect(posIzda,posTop,68,68))

    # redibujar juego
    pygame.display.flip()

pygame.quit()