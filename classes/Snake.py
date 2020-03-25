from classes.Point import Point
from classes.config import SNAKE_PROPORTIONALLITY

DIRECTION_UP = 1
DIRECTION_RIGHT = 2
DIRECTION_DOWN = 3
DIRECTION_LEFT = 4


class Snake:

    def __init__(self, externalCenterPoint: Point):
        self.centerPoint = externalCenterPoint
        self.direction = DIRECTION_UP

    def move(self):
        movementSpeed = SNAKE_PROPORTIONALLITY  # VALKA

        if self.direction == DIRECTION_UP:
            self.centerPoint.y += movementSpeed
        elif self.direction == DIRECTION_RIGHT:
            self.centerPoint.x += movementSpeed
        elif self.direction == DIRECTION_DOWN:
            self.centerPoint.y -= movementSpeed
        else:
            self.centerPoint.x -= movementSpeed

        self.teleport()

    def teleport(self):
        if self.centerPoint.y >= SNAKE_PROPORTIONALLITY * 16:
            self.centerPoint.y = SNAKE_PROPORTIONALLITY / 2
        elif self.centerPoint.y == SNAKE_PROPORTIONALLITY * -0.5:
            self.centerPoint.y = SNAKE_PROPORTIONALLITY * 16 - SNAKE_PROPORTIONALLITY / 2
        elif self.centerPoint.x >= SNAKE_PROPORTIONALLITY * 21.6:
            self.centerPoint.x = SNAKE_PROPORTIONALLITY - SNAKE_PROPORTIONALLITY / 2
        elif self.centerPoint.x == SNAKE_PROPORTIONALLITY / 2 - SNAKE_PROPORTIONALLITY:
            self.centerPoint.x = SNAKE_PROPORTIONALLITY * 21.5
