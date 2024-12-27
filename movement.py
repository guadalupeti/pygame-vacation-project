import pygame

def playerMovement(player_rect, rect, player_pos, dt):
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