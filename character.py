import pygame
from objClasses import *

class Player(pygame.sprite.Sprite): # Classe de definição dos sprites
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('midia/sprites/player/bono0.png'))

        for i in range(len(self.sprites)): # loop de modificação do tamanho dos sprites
            original_size = self.sprites[i].get_size()
            new_width = int(original_size[0] * 0.1)
            new_height = int(original_size[1] * 0.1)
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (new_width, new_height))

        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.direction = 1 # 0 - esquerda / 1 - direita
        self.wKey = False
        self.level = 1
        
    def update(self):
        self.image = self.sprites[int(self.current_sprite)]

        match self.direction:
            case 0:
                self.image = pygame.transform.flip(self.image, True, False)
            case 1:
                self.image = pygame.transform.flip(self.image, False, False)

def drawCharacterWSprites(screen: pygame.display, player: Player):
    movingSprites = pygame.sprite.Group()
    movingSprites.add(player)
    movingSprites.draw(screen)
    movingSprites.update()
    
def drawObj(screen: pygame.display, rect: pygame.Rect):
    pygame.draw.rect(screen, 'blue', rect)

def drawDebugSquare(screen :pygame.display, player_rect: pygame.Rect):
    pygame.draw.rect(screen, 'green', player_rect, 2)   

def drawKey(screen: pygame.display, key: Key):
    movingSprites = pygame.sprite.Group()
    movingSprites.add(key)
    movingSprites.draw(screen)
    movingSprites.update()

def drawDoor(screen: pygame.display, door: Door):
    movingSprites = pygame.sprite.Group()
    movingSprites.add(door)
    movingSprites.draw(screen)
    movingSprites.update()
    
    