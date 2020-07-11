import wx

class Painter(wx.Frame):
    def __init__(self, parent, title):
        super(Painter, self).__init__(parent, title = title,size = (500,300))
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

    def draw(self, board):
        dc = wx.PaintDC(self)