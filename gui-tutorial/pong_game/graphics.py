import wx
import sys


class Painter(wx.Frame):
    def __init__(self, parent, title, game):
        super(Painter, self).__init__(parent, title=title, size=(500, 300))
        self.game = game
        self.init_ui()

    def init_ui(self):
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        startItem = fileMenu.Append(wx.ID_DEFAULT, 'Start', 'Start game')
        endItem = fileMenu.Append(wx.ID_EXECUTE, 'End', 'End game')
        quitItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit, quitItem)
        self.Bind(wx.EVT_MENU, self.on_start, startItem)
        self.Bind(wx.EVT_MENU, self.on_end, endItem)
        self.Show(True)

    def on_quit(self, e):
        print("Good Bye")
        self.Close()

    def on_start(self, e):
        print("Game started")
        self.game.start()

    def on_end(self, e):
        print("Game ended")
        self.game.stop()

    def on_paint(self, e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("brown")
        dc.SetBackground(brush)
        dc.Clear()
        bat =self.game.board.bat
        dc.DrawRectangle(bat.x, bat.x, bat.WIDTH, bat.HEIGHT)
        ball = self.game.board.ball
        dc.DrawCircle(ball.x, ball.y, ball.RADIUS)
