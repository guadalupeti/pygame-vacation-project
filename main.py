import pygame
import sys
from character import *

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

    key = pygame.key.get_pressed()
    movement = pygame.Vector2(0,0)

    if key[pygame.K_w]:
        movement.y -= 300*dt
    if key[pygame.K_s]:
        movement.y += 300*dt
    if key[pygame.K_d]: 
        movement.x += 300*dt
    if key[pygame.K_a]:
        movement.x -= 300*dt

    new_pos = player_pos + movement

    player_rect.center = (player_pos.x + movement.x, player_pos.y)

    if not player_rect.colliderect(rect):
        player_pos.x = new_pos.x
    
    player_rect.center = (player_pos.x, player_pos.y + movement.y)
    if not player_rect.colliderect(rect):
        player_pos.y = new_pos.y
    
    
    player_rect.center = player_pos

    drawDebugSquare(screen, player_rect)

    
    screen.fill('black')
    drawCharacter(screen, player_pos) 
    drawObj(screen, rect)
    pygame.display.flip()
    dt = clock.tick(60)/1000
    


pygame.quit()
sys.exit()


