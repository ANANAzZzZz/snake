import random

import pygame
from classes.Point import Point
from classes.Snake import Snake, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT
from classes.config import SNAKE_PROPORTIONALLITY

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (207, 207, 0)


class Game:

    def __init__(self):
        super().__init__()

        snakeCenterPoint = Point(
            SNAKE_PROPORTIONALLITY * 5 + SNAKE_PROPORTIONALLITY / 2,
            SNAKE_PROPORTIONALLITY * 5 + SNAKE_PROPORTIONALLITY / 2
        )

        self.snake = Snake(snakeCenterPoint)

    def onKeyPress(self, key):
        if key == pygame.K_UP:
            self.snake.direction = DIRECTION_DOWN
        elif key == pygame.K_RIGHT:
            self.snake.direction = DIRECTION_RIGHT
        elif key == pygame.K_DOWN:
            self.snake.direction = DIRECTION_UP
        elif key == pygame.K_LEFT:
            self.snake.direction = DIRECTION_LEFT

    def update(self, screen):
        self.clearScreen(screen)

        self.snake.move()
        self.renderBeach(screen)
        self.renderSnake(screen, self.snake)

        pygame.display.flip()

    def clearScreen(self, screen):
        screen.fill(COLOR_WHITE)

    def renderLine(self, screen, firstPoint: Point, secondPoint: Point, color=(255, 255, 255)):
        pygame.draw.line(screen, color, [firstPoint.x, firstPoint.y], [secondPoint.x, secondPoint.y], 5)

    def renderSquare(self, screen, centerPoint: Point, width=SNAKE_PROPORTIONALLITY, color=(255, 255, 255)):
        halfSquareWidth = width / 2

        bottomLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y - halfSquareWidth)
        topLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y + halfSquareWidth)
        bottomRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y - halfSquareWidth)
        topRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y + halfSquareWidth)

        self.renderLine(screen, bottomLeftPoint, bottomRightPoint, color)
        self.renderLine(screen, topLeftPoint, topRightPoint, color)
        self.renderLine(screen, bottomLeftPoint, topLeftPoint, color)
        self.renderLine(screen, bottomRightPoint, topRightPoint, color)

    def renderSnake(self, screen, snake: Snake):
        # Render body
        for point in snake.bodyPoints:
            self.renderSquare(screen, point, color=COLOR_GREEN)

        # Render eyes
        eyesSpreadCoefficient = 6
        eyesSizeCoefficient = 10
        self.renderSquare(screen, Point(snake.bodyPoints[0].x + SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient, snake.bodyPoints[0].y - SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient), SNAKE_PROPORTIONALLITY / eyesSizeCoefficient, COLOR_BLACK)
        self.renderSquare(screen, Point(snake.bodyPoints[0].x - SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient, snake.bodyPoints[0].y - SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient), SNAKE_PROPORTIONALLITY / eyesSizeCoefficient, COLOR_BLACK)

    def renderBeach(self, screen):
        trackWidth = SNAKE_PROPORTIONALLITY

        firstLineFirstPoint = Point(0, 0)
        firstLineSecondPoint = Point(0, SNAKE_PROPORTIONALLITY * 16)
        counterX = 10

        while counterX < 33:
            self.renderLine(screen, firstLineFirstPoint, firstLineSecondPoint, COLOR_YELLOW)
            counterX = counterX + 1
            firstLineFirstPoint.x = firstLineFirstPoint.x + trackWidth
            firstLineSecondPoint.x = firstLineSecondPoint.x + trackWidth

        secondLineFirstPoint = Point(0, SNAKE_PROPORTIONALLITY * 16)
        secondLineSecondPoint = Point(SNAKE_PROPORTIONALLITY * 22, SNAKE_PROPORTIONALLITY * 16)

        counterY = 10

        while counterY < 40:
            self.renderLine(screen, secondLineFirstPoint, secondLineSecondPoint, COLOR_YELLOW)
            counterY = counterY + 1
            secondLineFirstPoint.y = secondLineFirstPoint.y - trackWidth
            secondLineSecondPoint.y = secondLineSecondPoint.y - trackWidth
