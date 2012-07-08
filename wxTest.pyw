#!/usr/bin/env python
import wx
from PIL import Image, ImageFile, ImageDraw, ImageFont
import os

def PilImageToWxImage( myPilImage ):
    myWxImage = wx.EmptyImage( myPilImage.size[0], myPilImage.size[1] )
    myWxImage.SetData( myPilImage.convert( 'RGB' ).tostring() )
    return myWxImage

def WxImageToWxBitmap( myWxImage ) :
    return myWxImage.ConvertToBitmap()

def PilImageToWxBitmap( myPilImage ) :
    return WxImageToWxBitmap( PilImageToWxImage( myPilImage ) )


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(600,400))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

    def OnPaint(self, event):
        image = wx.Image('Photo.jpg')
        bm = wx.BitmapFromImage(image)
        bg = wx.PaintDC(self)
        bg.DrawBitmap(PilImageToWxBitmap(PILimage), 0, 0)

    def OnClose(self, event):
        self.Destroy()


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = Frame("Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.

PILimage = Image.new("RGB", (600, 100), (255,255,255))
draw = ImageDraw.Draw(PILimage)
defaultFont = ImageFont.truetype("arial.ttf", 14)
font = ImageFont.truetype("ArnoPro-BoldSmText.otf", 20)

draw.text((10, 30), "The quick brown fox jumps over the lazy dog", font=font, fill="#000")
draw.text((10, 0), "The quick brown fox jumps over the lazy dog", font=defaultFont, fill="#000")

app.MainLoop()