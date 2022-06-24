import pygame, random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
cell_size = 40
cell_number = 20

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()




screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)




