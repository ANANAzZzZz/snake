from classes.Point import Point
from classes.config import SNAKE_PROPORTIONALLITY

DIRECTION_UP = 1
DIRECTION_RIGHT = 2
DIRECTION_DOWN = 3
DIRECTION_LEFT = 4


class Snake:

    def __init__(self, externalCenterPoint: Point):
        self.bodyPoints = [
            Point(externalCenterPoint.x, externalCenterPoint.y),
            Point(externalCenterPoint.x, externalCenterPoint.y - SNAKE_PROPORTIONALLITY), 
            Point(externalCenterPoint.x, externalCenterPoint.y - SNAKE_PROPORTIONALLITY * 2), 
            Point(externalCenterPoint.x, externalCenterPoint.y - SNAKE_PROPORTIONALLITY * 3)
        ]
        self.direction = DIRECTION_UP

    def move(self):
        savedHeadPoint = Point(self.bodyPoints[0].x, self.bodyPoints[0].y)

        self.moveHead()
        self.moveBody(savedHeadPoint)

    def moveHead(self):
        movementSpeed = SNAKE_PROPORTIONALLITY  # VALKA

        if self.direction == DIRECTION_UP:
            self.bodyPoints[0].y += movementSpeed
        elif self.direction == DIRECTION_RIGHT:
            self.bodyPoints[0].x += movementSpeed
        elif self.direction == DIRECTION_DOWN:
            self.bodyPoints[0].y -= movementSpeed
        else:
            self.bodyPoints[0].x -= movementSpeed

        self.teleportHead()

    def teleportHead(self):
        if self.bodyPoints[0].y >= SNAKE_PROPORTIONALLITY * 16:
            self.bodyPoints[0].y = SNAKE_PROPORTIONALLITY / 2
        elif self.bodyPoints[0].y == SNAKE_PROPORTIONALLITY * -0.5:
            self.bodyPoints[0].y = SNAKE_PROPORTIONALLITY * 16 - SNAKE_PROPORTIONALLITY / 2
        elif self.bodyPoints[0].x >= SNAKE_PROPORTIONALLITY * 21.6:
            self.bodyPoints[0].x = SNAKE_PROPORTIONALLITY - SNAKE_PROPORTIONALLITY / 2
        elif self.bodyPoints[0].x == SNAKE_PROPORTIONALLITY / 2 - SNAKE_PROPORTIONALLITY:
            self.bodyPoints[0].x = SNAKE_PROPORTIONALLITY * 21.5

    def moveBody(self, savedHeadPoint: Point):
        for pointIndex in reversed(range(2, len(self.bodyPoints))):
            self.bodyPoints[pointIndex].x = self.bodyPoints[pointIndex - 1].x
            self.bodyPoints[pointIndex].y = self.bodyPoints[pointIndex - 1].y

        self.bodyPoints[1].x = savedHeadPoint.x
        self.bodyPoints[1].y = savedHeadPoint.y
