class Point:

    def __init__(self, externalX: float, externalY: float):
        self.x = externalX
        self.y = externalY

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
