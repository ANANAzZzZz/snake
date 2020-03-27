import pygame
from classes.Game import Game
from classes.config import GAME_SIZE, GAME_HEIGHT, GAME_WIDTH

pygame.init()
screen = pygame.display.set_mode((GAME_SIZE * GAME_WIDTH, GAME_SIZE * GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
game = Game()

while True:
    game.processUserInput()
    game.update(screen)

    clock.tick(6)
