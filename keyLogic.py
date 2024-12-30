import pygame
from character import Player
from objClasses import *

def getKey(player: Player, key: Key):
    key_rect = key.rect
    player_rect = player.rect
    key_pressed = pygame.key.get_pressed()
    if player_rect.colliderect(key_rect) and key_pressed[pygame.K_e]:
        player.wKey = True
        key.taken = True

def useKey(player: Player, door_rect: pygame.Rect):
    player_rect = player.rect
    key_pressed = pygame.key.get_pressed()
    if player_rect.colliderect(door_rect) and key_pressed[pygame.K_e] and player.wKey:
        player.level += 1