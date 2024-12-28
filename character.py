import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('midia/sprites/player/bono1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        
    def update(self):
        self.image = self.sprites[int(self.current_sprite)]
    
        
def drawCharacter(screen: pygame.display, player_pos: pygame.Vector2):
    pygame.draw.circle(screen, "red", player_pos, 40)

def drawCharacterWSprites(screen: pygame.display, player: Player):
    movingSprites = pygame.sprite.Group()
    movingSprites.add(player)
    movingSprites.draw(screen)
    
def drawObj(screen: pygame.display, rect: pygame.Rect):
    pygame.draw.rect(screen, 'blue', rect)

def drawDebugSquare(screen :pygame.display, player_rect: pygame.Rect):
    pygame.draw.rect(screen, 'green', player_rect, 2)   
    
    