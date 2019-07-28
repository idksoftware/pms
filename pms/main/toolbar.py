'''
Created on Jul 8, 2013

@author: wzw7yn
'''
import wx

ART_MAP = { wx.ID_CUT : wx.ART_CUT,
            wx.ID_COPY : wx.ART_COPY,
            wx.ID_PASTE : wx.ART_PASTE,
            }

class EasyToolBar(wx.ToolBar):
    def AddEasyToolBar(self, id, shortHelp="", longhelp=""):
        assert id in ART_MAP, "Unknown ID"
        art_id = ART_MAP.get(id)
        bmp = wx.ArtProvider.GetBitmap(art_id, wx.ART_TOOLBAR)
        self.AddSimpleTool(id, bmp, shortHelp, longhelp)
        
class ToolBarFrame(wx.Frame):
    '''
    classdocs
    '''
    def __init__(self, *args, **kwargs):
        super(ToolBarFrame, self).__init__(*args, **kwargs)
        '''
        Constructor
        '''
        toolb = EasyToolBar(self)
        toolb.AddEasyToolBar(wx.ID_CUT)
        toolb.AddEasyToolBar(wx.ID_COPY)
        toolb.AddEasyToolBar(wx.ID_PASTE)
        toolb.Realize()
        self.SetToolBar(toolb)
        
        self.Bind(wx.EVT_TOOL, self.OnToolBar)
        
    def OnToolBar(self, event):
        print "ToolBarItem Clicked", event.GetId()
        
        