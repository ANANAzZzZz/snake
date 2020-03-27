import pygame

from library.classes.Game import Game
from library.config import GAME_SIZE, GAME_WIDTH, GAME_HEIGHT

pygame.init()
screen = pygame.display.set_mode((GAME_SIZE * GAME_WIDTH, GAME_SIZE * GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
game = Game()

while True:
    game.processUserInput()
    game.update(screen)

    clock.tick(6)
