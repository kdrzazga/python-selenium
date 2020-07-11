import wx

class Painter(wx.Frame):
    def __init__(self, parent, title, board):
        super(Painter, self).__init__(parent, title = title,size = (500,300))
        self.bat = board.bat
        self.ball = board.ball
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show(True)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("brown")
        dc.SetBackground(brush)
        dc.Clear()
        dc.DrawRectangle(self.bat.x, self.bat.x, self.bat.WIDTH, self.bat.HEIGHT)
