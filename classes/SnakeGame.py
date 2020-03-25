import random

from cocos.layer import Layer
from cocos.rect import Rect
from cocos.text import Label
from cocos.draw import Line
from pyglet.media.synthesis import Square

from classes.Point import Point
from classes.Snake import Snake, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT
from classes.config import DEBUG_ENABLED, SNAKE_PROPORTIONALLITY


class SnakeGame(Layer):

    is_event_handler = True

    def __init__(self):
        super().__init__()

        snakeCenterPoint = Point(
            SNAKE_PROPORTIONALLITY * 5 + SNAKE_PROPORTIONALLITY / 2,
            SNAKE_PROPORTIONALLITY * 5 + SNAKE_PROPORTIONALLITY / 2
        )

        self.snake = Snake(snakeCenterPoint)


    def on_key_press(self, key, modifiers):
        if key == 119:
            self.snake.direction = DIRECTION_UP
        elif key == 100:
            self.snake.direction = DIRECTION_RIGHT
        elif key == 115:
            self.snake.direction = DIRECTION_DOWN
        elif key == 97:
            self.snake.direction = DIRECTION_LEFT

    def initTimer(self):
        # schedule self.updateGame execution function
        self.schedule_interval(lambda x: self.updateGame(), 0.1)

    def updateGame(self):
        self.clearScreen()

        self.snake.move()

        self.renderBeach()
        self.renderSnake(self.snake.centerPoint)

    def clearScreen(self):
        for child in self.children:
            child[1].kill()

    def renderLabel(self, x, y, text):
        hello_world_label = Label(
            text,
            font_name="Times New Roman",
            font_size=7,
            anchor_x='center',
            anchor_y='center'
        )

        hello_world_label.position = x, y

        self.add(hello_world_label)

    def renderLine(self, firstPoint: Point, secondPoint: Point, color=(255, 255, 255, 255)):
        line = Line((firstPoint.x, firstPoint.y), (secondPoint.x, secondPoint.y), color)

        self.add(line)

        if DEBUG_ENABLED:
            self.renderPointLabel(firstPoint)
            self.renderPointLabel(secondPoint)

    def renderPointLabel(self, point: Point):
        offset = 15

        self.renderLabel(point.x, point.y + offset, f'{point.x}, {point.y}')

    def renderSquare(self, centerPoint: Point, width=SNAKE_PROPORTIONALLITY, color=(255, 255, 255, 255)):
        halfSquareWidth = width / 2

        bottomLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y - halfSquareWidth)
        topLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y + halfSquareWidth)
        bottomRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y - halfSquareWidth)
        topRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y + halfSquareWidth)

        self.renderLine(bottomLeftPoint, bottomRightPoint, color)
        self.renderLine(topLeftPoint, topRightPoint, color)
        self.renderLine(bottomLeftPoint, topLeftPoint, color)
        self.renderLine(bottomRightPoint, topRightPoint, color)

    def renderSnake(self, centerPoint: Point):
        greenColor = (0, 128, 0, 255)

        # Render body
        self.renderSquare(centerPoint, color=greenColor)
        self.renderSquare(Point(centerPoint.x, centerPoint.y - SNAKE_PROPORTIONALLITY), color=greenColor)
        self.renderSquare(Point(centerPoint.x, centerPoint.y - SNAKE_PROPORTIONALLITY * 2), color=greenColor)
        self.renderSquare(Point(centerPoint.x, centerPoint.y - SNAKE_PROPORTIONALLITY * 3), color=greenColor)

        # Render eyes
        eyesSpreadCoefficient = 10
        eyesSizeCoefficient = 10
        self.renderSquare(Point(centerPoint.x + SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient, centerPoint.y + SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient), SNAKE_PROPORTIONALLITY / eyesSizeCoefficient)
        self.renderSquare(Point(centerPoint.x - SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient, centerPoint.y + SNAKE_PROPORTIONALLITY / eyesSpreadCoefficient), SNAKE_PROPORTIONALLITY / eyesSizeCoefficient)

    def renderBeach(self):
        trackWidth = SNAKE_PROPORTIONALLITY
        beachColor = (200, 200, 0, 255)

        firstLineFirstPoint = Point(0, 0)
        firstLineSecondPoint = Point(0, SNAKE_PROPORTIONALLITY * 16)
        counterX = 10

        while counterX < 33:
            self.renderLine(firstLineFirstPoint, firstLineSecondPoint, beachColor)
            counterX = counterX + 1
            firstLineFirstPoint.x = firstLineFirstPoint.x + trackWidth
            firstLineSecondPoint.x = firstLineSecondPoint.x + trackWidth

        secondLineFirstPoint = Point(0, SNAKE_PROPORTIONALLITY * 16)
        secondLineSecondPoint = Point(SNAKE_PROPORTIONALLITY * 22, SNAKE_PROPORTIONALLITY * 16)

        counterY = 10

        while counterY < 40:
            self.renderLine(secondLineFirstPoint, secondLineSecondPoint, beachColor)
            counterY = counterY + 1
            secondLineFirstPoint.y = secondLineFirstPoint.y - trackWidth
            secondLineSecondPoint.y = secondLineSecondPoint.y - trackWidth

