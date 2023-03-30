import math
import threading
import time
import wx
from pong_game.graphics import Painter


class Velocity:
    def __init__(self, value, angle):
        self.value = value
        self.angle = angle


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS=5
        self.velocity = Velocity(5, 0.77)

    def move(self):
        self.x = self.x + self.velocity.value* math.cos(self.velocity.angle)
        self.y = self.y + self.velocity.value* math.sin(self.velocity.angle)


class Bat:
    def __init__(self, x):
        self.x = x
        self.y = 100
        self.WIDTH = 30
        self.HEIGHT = 7


class Game:
    def worker(self):
        while 1 == 1:
            if self.running == 1:
                print(".")
            time.sleep(0.2)

    def __init__(self):
        self.TITLE = "PONG"
        self.board = Board()
        self.painter = Painter(None, self.TITLE, self)
        self.counter = 0
        self.running = 0
        self.t = threading.Thread(target=self.worker)
        self.t.start()

    def stop(self):
        self.running = 0

    def start(self):
        self.running = 1

    def update(self):
        self.board.ball.move()

class Board:
    def __init__(self):
        self.WIDTH = 300
        self.HEIGHT = 500
        init_x = 30
        self.bat = Bat(init_x)
        self.ball = Ball(init_x, self.bat.y)


pong = wx.App()
game = Game()
# game.run()
pong.MainLoop()
