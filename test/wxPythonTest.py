# -*- coding: utf-8 -*-

import wx

app = wx.App()
window = wx.Frame(None, -1, "install test")
btn = wx.Button(window, label="Button")
window.Show()
app.MainLoop()
