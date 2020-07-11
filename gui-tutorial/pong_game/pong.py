import threading
import wx

#TODO Finish this
from pong_game.graphics import Painter

class Velocity:
    def __init__(self, value, angle):
        self.value = value
        self.angle = angle

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = Velocity(5, 1.57)

class Bat:
    def __init__(self, x):
        self.x = x
        self.y = 100
        self.WIDTH = 30
        self.HEIGHT = 7


class Game(threading.Thread):
    def start(self):
        self.TITLE = "PONG"
        self.board = Board()
        self.painter = Painter(None, self.TITLE, self.board)

class Board:
    def __init__(self):
       self.WIDTH = 300
       self.HEIGHT = 500
       initX = 30
       self.bat = Bat(initX)
       self.ball = Ball(initX, self.bat.y)

pong = wx.App()
Game().start()
pong.MainLoop()