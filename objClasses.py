import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('midia/sprites/objects/key.png'))
        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.taken = False

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('midia/sprites/objects/door.png'))
        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]