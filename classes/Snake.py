from classes.Point import Point

DIRECTION_UP = 1
DIRECTION_RIGHT = 2
DIRECTION_DOWN = 3
DIRECTION_LEFT = 4


class Snake:

    def __init__(self, externalCenterPoint: Point):
        self.centerPoint = externalCenterPoint
        self.direction = DIRECTION_UP

    def move(self):
        movementSpeed = 100  # VALKA

        if self.direction == DIRECTION_UP:
            self.centerPoint.y += movementSpeed
        elif self.direction == DIRECTION_RIGHT:
            self.centerPoint.x += movementSpeed
        elif self.direction == DIRECTION_DOWN:
            self.centerPoint.y -= movementSpeed
        else:
            self.centerPoint.x -= movementSpeed

