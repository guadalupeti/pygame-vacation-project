import pygame

def drawCharacter(screen: pygame.display, player_pos: pygame.Vector2):
    pygame.draw.circle(screen, "red", player_pos, 40)
    
def drawObj(screen: pygame.display, rect: pygame.Rect):
    pygame.draw.rect(screen, 'blue', rect)

def drawDebugSquare(screen :pygame.display, player_rect: pygame.Rect):
    pygame.draw.rect(screen, 'green', player_rect, 2)