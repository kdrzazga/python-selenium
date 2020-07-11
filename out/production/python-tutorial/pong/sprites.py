from pong import Velocity


class Ball:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.velocity = Velocity(5, 1.57)

class Bat:
    def __init__(self, x):
        self.x = x;
        self.y = 100
