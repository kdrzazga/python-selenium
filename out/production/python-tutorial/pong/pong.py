import wx

#TODO Finish this
from pong.graphics import Painter
from pong.sprites import Bat, Ball


class Game:
    def start(self):
        self.TITLE = "PONG"
        self.board = Board()
        self.painter = Painter(None, self.TITLE)

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