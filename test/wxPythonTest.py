# -*- coding: utf-8 -*-

import wx

app = wx.App()
window = wx.Frame(None, title="第一个GUI应用", size=(300, 200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello world", pos=(100, 50))
window.Show(True)
app.MainLoop()
