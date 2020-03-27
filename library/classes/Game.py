import random

import pygame

from library.classes.Apple import Apple
from library.classes.Point import Point
from library.classes.Snake import Snake, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT
from library.config import GAME_SIZE, GAME_HEIGHT, GAME_WIDTH

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (207, 207, 0)
COLOR_RED = (255, 0, 0)


class Game:

    def __init__(self):
        super().__init__()

        self.snake = Snake(Point(5.5, 5.5))
        self.snake2 = Snake(Point(9.5, 5.5))

        self.apple = self.generateApple()

    def processUserInput(self):
        firstSnakeDirectionChanged = False
        secondSnakeDirectionChanged = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not firstSnakeDirectionChanged:
                    firstSnakeDirectionChanged = self.onFirstSnakeKeyPress(event.key)
                if not secondSnakeDirectionChanged:
                    secondSnakeDirectionChanged = self.onSecondSnakeKeyPress(event.key)

    def generateApple(self):
        x = random.randint(0, GAME_WIDTH - 1) + 0.5
        y = random.randint(0, GAME_HEIGHT - 1) + 0.5
        applePoint = Point(x, y)

        for snakeBodyPoint in self.snake.bodyPoints:
            if snakeBodyPoint == applePoint:
                return self.generateApple()

        for snakeBodyPoint in self.snake2.bodyPoints:
            if snakeBodyPoint == applePoint:
                return self.generateApple()

        return Apple(applePoint)

    def onFirstSnakeKeyPress(self, key):
        newSnakeDirection = 0

        if key == pygame.K_UP:
            newSnakeDirection = DIRECTION_DOWN
        elif key == pygame.K_RIGHT:
            newSnakeDirection = DIRECTION_RIGHT
        elif key == pygame.K_DOWN:
            newSnakeDirection = DIRECTION_UP
        elif key == pygame.K_LEFT:
            newSnakeDirection = DIRECTION_LEFT

        self.snake.changeDirection(newSnakeDirection)

        return newSnakeDirection != 0

    def onSecondSnakeKeyPress(self, key):
        newSnakeDirection = 0

        if key == pygame.K_w:
            newSnakeDirection = DIRECTION_DOWN
        elif key == pygame.K_d:
            newSnakeDirection = DIRECTION_RIGHT
        elif key == pygame.K_s:
            newSnakeDirection = DIRECTION_UP
        elif key == pygame.K_a:
            newSnakeDirection = DIRECTION_LEFT

        self.snake2.changeDirection(newSnakeDirection)

        return newSnakeDirection != 0

    def update(self, screen):
        self.clearScreen(screen)

        self.snake.move()
        self.snake2.move()

        self.snake.checkForOtherSnakeCollision(self.snake2)
        self.snake2.checkForOtherSnakeCollision(self.snake)

        if self.hasSnakeAteApple(self.snake):
            self.apple = self.generateApple()
            self.snake.grow()

        if self.hasSnakeAteApple(self.snake2):
            self.apple = self.generateApple()
            self.snake2.grow()

        self.renderBeach(screen)
        self.renderApple(screen, self.apple)
        self.renderSnake(screen, self.snake)
        self.renderSnake(screen, self.snake2)

        pygame.display.flip()

    def hasSnakeAteApple(self, snake: Snake):
        return snake.bodyPoints[0] == self.apple.point

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

    def renderApple(self, screen, apple: Apple):
        self.renderSquare(screen, apple.point, color=COLOR_RED)

    def renderSnake(self, screen, snake: Snake):
        self.renderSnakeEyes(screen, snake)

        for point in snake.bodyPoints:
            self.renderSquare(screen, point, color=snake.color)

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
