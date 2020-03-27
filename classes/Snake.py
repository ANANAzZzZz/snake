from classes.Point import Point
from classes.config import GAME_HEIGHT, GAME_WIDTH

DIRECTION_UP = 1
DIRECTION_RIGHT = 2
DIRECTION_DOWN = 3
DIRECTION_LEFT = 4


class Snake:

    def __init__(self, externalCenterPoint: Point):
        self.bodyPoints = [
            Point(externalCenterPoint.x, externalCenterPoint.y),
            Point(externalCenterPoint.x, externalCenterPoint.y - 1),
            Point(externalCenterPoint.x, externalCenterPoint.y - 2),
            Point(externalCenterPoint.x, externalCenterPoint.y - 3),
            Point(externalCenterPoint.x, externalCenterPoint.y - 4),
            Point(externalCenterPoint.x, externalCenterPoint.y - 5)
        ]
        self.direction = DIRECTION_UP

    def changeDirection(self, wantedDirection: int):
        if wantedDirection == DIRECTION_DOWN and self.direction != DIRECTION_UP:
            self.direction = wantedDirection
        elif wantedDirection == DIRECTION_RIGHT and self.direction != DIRECTION_LEFT:
            self.direction = wantedDirection
        elif wantedDirection == DIRECTION_UP and self.direction != DIRECTION_DOWN:
            self.direction = wantedDirection
        elif wantedDirection == DIRECTION_LEFT and self.direction != DIRECTION_RIGHT:
            self.direction = wantedDirection

    def move(self):
        savedHeadPoint = Point(self.bodyPoints[0].x, self.bodyPoints[0].y)

        self.moveHead()
        self.moveBody(savedHeadPoint)

    def moveHead(self):
        movementSpeed = 1  # VALKA

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
        if self.bodyPoints[0].y >= GAME_HEIGHT:
            self.bodyPoints[0].y = 0.5
        elif self.bodyPoints[0].y == -0.5:
            self.bodyPoints[0].y = GAME_HEIGHT - 0.5
        elif self.bodyPoints[0].x >= GAME_WIDTH + 0.5:
            self.bodyPoints[0].x = 0.5
        elif self.bodyPoints[0].x == -0.5:
            self.bodyPoints[0].x = GAME_WIDTH - 0.5

    def moveBody(self, savedHeadPoint: Point):
        for pointIndex in reversed(range(2, len(self.bodyPoints))):
            self.bodyPoints[pointIndex].x = self.bodyPoints[pointIndex - 1].x
            self.bodyPoints[pointIndex].y = self.bodyPoints[pointIndex - 1].y

        self.bodyPoints[1].x = savedHeadPoint.x
        self.bodyPoints[1].y = savedHeadPoint.y
