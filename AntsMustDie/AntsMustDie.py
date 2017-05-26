import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("ShemsCo - Pygame Tutorial")

Green = pygame.Color(255,0,255)

while True:
    screen.fill(Green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    pygame.display.update()
