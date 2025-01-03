import pygame
import sys
from character import *
from movement import *
from keyLogic import *
from objClasses import *

# to-do
# configurar sprites
# fazer logica das chaves
# terminar logica dos textos de ação
# fazer lógica de passagem de nivel
# terminar dicionariod de dados dos niveis

pygame.init()

running = True

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption('Exibindo texto')

player = Player(screen.get_width() / 2, screen.get_height() / 2)
key = Key(600,600)
door = Door(1280, 720)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) # criação da posição inical do personagem
player_rect = player.rect # retângulo de colisão do personagem

rect = pygame.Rect(30,30,60,60) # retângulo para testar colisão

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
 
    dt = clock.tick(60)/1000 # delta time: variável para tratar movimentação em caso de possíveis travamentos
    
    playerMovement(player_rect, rect, player_pos, dt, player)
    getKey(player, key, screen)
    useKey(player, door, screen)

    screen.fill('black')

    drawCharacterWSprites(screen, player)
    drawObj(screen, rect)
    drawDebugSquare(screen, player_rect) # quadrado de debug (o quadrado que fica em cima do personagem)
    drawDoor(screen, door)
    drawKey(screen, key)
    
    pygame.display.flip()

    
pygame.quit()
sys.exit()
