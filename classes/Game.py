import random

import pygame
from classes.Point import Point
from classes.Snake import Snake, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT
from classes.config import GAME_SIZE, GAME_HEIGHT, GAME_WIDTH

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (207, 207, 0)


class Game:

    def __init__(self):
        super().__init__()

        snakeCenterPoint = Point(5.5, 5.5)

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

    def renderLine(self, screen, firstPoint: Point, secondPoint: Point, color=COLOR_WHITE):
        startPosition = [
            firstPoint.x * GAME_SIZE,
            firstPoint.y * GAME_SIZE
        ]
        endPosition = [
            secondPoint.x * GAME_SIZE,
            secondPoint.y * GAME_SIZE
        ]

        pygame.draw.line(screen, color, startPosition, endPosition, 5)

    def renderSquare(self, screen, centerPoint: Point, width=1.0, color=COLOR_WHITE):
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
        self.renderSnakeEyes(screen, snake)

        for point in snake.bodyPoints:
            self.renderSquare(screen, point, color=COLOR_GREEN)

    def renderSnakeEyes(self, screen, snake):
        eyesSpreadCoefficient = 0.2
        eyesSizeCoefficient = 0.1

        leftEyePoint = Point(
            snake.bodyPoints[0].x + eyesSpreadCoefficient,
            snake.bodyPoints[0].y - eyesSpreadCoefficient
        )
        rightEyePoint = Point(
            snake.bodyPoints[0].x - eyesSpreadCoefficient,
            snake.bodyPoints[0].y - eyesSpreadCoefficient
        )

        self.renderSquare(screen, leftEyePoint, eyesSizeCoefficient, COLOR_BLACK)
        self.renderSquare(screen, rightEyePoint, eyesSizeCoefficient, COLOR_BLACK)

    def renderBeach(self, screen):
        trackWidth = 1

        firstLineFirstPoint = Point(0, 0)
        firstLineSecondPoint = Point(0, GAME_HEIGHT)
        counterX = 0

        while counterX < GAME_WIDTH + 1:
            self.renderLine(screen, firstLineFirstPoint, firstLineSecondPoint, COLOR_YELLOW)
            counterX = counterX + 1
            firstLineFirstPoint.x = firstLineFirstPoint.x + trackWidth
            firstLineSecondPoint.x = firstLineSecondPoint.x + trackWidth

        secondLineFirstPoint = Point(0, GAME_HEIGHT)
        secondLineSecondPoint = Point(GAME_WIDTH, GAME_HEIGHT)

        counterY = 0

        while counterY < GAME_HEIGHT + 1:
            self.renderLine(screen, secondLineFirstPoint, secondLineSecondPoint, COLOR_YELLOW)
            counterY = counterY + 1
            secondLineFirstPoint.y = secondLineFirstPoint.y - trackWidth
            secondLineSecondPoint.y = secondLineSecondPoint.y - trackWidth
