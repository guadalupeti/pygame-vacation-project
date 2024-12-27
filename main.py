import pygame
import sys
from character import *
from movement import *

# to-do
# modularizzar codigo de movimentação
# configurar sprites

pygame.init()

running = True

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_rect = pygame.Rect(player_pos.x, player_pos.y, 60,60)

rect = pygame.Rect(30,30,60,60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()

    

 
    dt = clock.tick(60)/1000
    playerMovement(player_rect, rect, player_pos, dt)

    screen.fill('black')

    drawCharacter(screen, player_pos) 
    drawObj(screen, rect)
    drawDebugSquare(screen, player_rect)

    pygame.display.flip()

    


pygame.quit()
sys.exit()


