import pygame
from classes.Game import Game
from classes.config import GAME_SIZE, GAME_HEIGHT, GAME_WIDTH

pygame.init()
screen = pygame.display.set_mode((GAME_SIZE * GAME_WIDTH, GAME_SIZE * GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

done = False
clock = pygame.time.Clock()
game = Game()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game.onKeyPress(event.key)
        elif event.type == pygame.QUIT:
            done = True

    game.update(screen)

    clock.tick(6)
