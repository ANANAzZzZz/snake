import random

from cocos.layer import Layer
from cocos.text import Label
from cocos.draw import Line
from classes.Point import Point
from classes.Snake import Snake, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT
from classes.config import DEBUG_ENABLED


class SnakeGame(Layer):

    is_event_handler = True

    def __init__(self):
        super().__init__()

        snakeCenterPoint = Point(300, 300)
        self.snake = Snake(snakeCenterPoint)

    def on_key_press(self, key, modifiers):
        # up: 119
        # right: 100
        # down: 115
        # left: 97

        print(f'KEY: {key}')
        if key == 119:
            self.snake.direction = DIRECTION_UP
        elif key == 100:
            self.snake.direction = DIRECTION_RIGHT
        elif key == 115:
            self.snake.direction = DIRECTION_DOWN
        elif key == 97:
            self.snake.direction = DIRECTION_LEFT

    def initTimer(self):
        self.schedule_interval(lambda x: self.updateGame(), 0.1)

    def updateGame(self):
        self.clearScreen()

        self.snake.move()

        self.renderSnake(self.snake.centerPoint)

    def clearScreen(self):
        for child in self.children:
            child[1].kill()

    def renderLabel(self, x, y, text):
        hello_world_label = Label(
            text,
            font_name="Times New Roman",
            font_size=15,
            anchor_x='center',
            anchor_y='center'
        )

        hello_world_label.position = x, y

        self.add(hello_world_label)

    def renderLine(self, firstPoint: Point, secondPoint: Point):
        color = (255, 255, 255, 255)
        line = Line((firstPoint.x, firstPoint.y), (secondPoint.x, secondPoint.y), color)
        self.add(line)

        if DEBUG_ENABLED:
            self.renderPointLabel(firstPoint)
            self.renderPointLabel(secondPoint)

    def renderPointLabel(self, point: Point):
        offset = 15

        self.renderLabel(point.x, point.y + offset, f'{point.x}, {point.y}')

    def renderSquare(self, centerPoint: Point, width=100):
        halfSquareWidth = width / 2

        bottomLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y - halfSquareWidth)
        topLeftPoint = Point(centerPoint.x - halfSquareWidth, centerPoint.y + halfSquareWidth)
        bottomRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y - halfSquareWidth)
        topRightPoint = Point(centerPoint.x + halfSquareWidth, centerPoint.y + halfSquareWidth)

        self.renderLine(bottomLeftPoint, bottomRightPoint)
        self.renderLine(topLeftPoint, topRightPoint)
        self.renderLine(bottomLeftPoint, topLeftPoint)
        self.renderLine(bottomRightPoint, topRightPoint)

    def renderSnake(self, centerPoint: Point):
        # Render body
        self.renderSquare(centerPoint)
        self.renderSquare(Point(centerPoint.x, centerPoint.y - 100))
        self.renderSquare(Point(centerPoint.x, centerPoint.y - 200))

        # Render eyes
        self.renderSquare(Point(centerPoint.x + 20, centerPoint.y + 15), 20)
        self.renderSquare(Point(centerPoint.x - 20, centerPoint.y + 15), 20)
