import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('midia/sprites/objects/key.png'))

        for i in range(len(self.sprites)): # loop de modificação do tamanho dos sprites
            original_size = self.sprites[i].get_size()
            new_width = int(original_size[0] * 0.1)
            new_height = int(original_size[1] * 0.1)
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (new_width, new_height))
            
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