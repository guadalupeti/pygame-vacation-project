import pygame
from character import Player

def getKey(player: Player, key_rect: pygame.Rect):
    player_rect = player.rect
    key_pressed = pygame.key.get_pressed()
    if player_rect.colliderect(key_rect) and key_pressed[pygame.K_e]:
        player.wKey = True

def useKey(player: Player, door_rect: pygame.Rect):
    player_rect = player.rect
    key_pressed = pygame.key.get_pressed()
    if player_rect.colliderect(door_rect) and key_pressed[pygame.K_e] and player.wKey:
        player.level += 1