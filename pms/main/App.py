'''
Created on Jun 27, 2013

@author: wzw7yn

import -

'''
import os
import platform
import wx
import wx.aui as aui
from mainpane import MainPane
from newwizard.wizard import NewWizard
from access.database import Database
from utils.configreader import ConfigReader
#from _winreg import *

from toolbar import EasyToolBar
#from PartitionTreeCtrl import PartitionBrowserPanel
from main.menu import MainMenu

class MyApp(wx.App):
    def OnInit(self):

        self.frame = MyFrame()
        #self.frame.SetBackgroundColour(wx.BLUE)
        #self.flame.SetTitle("Image Archive client")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    ID_IMPORT = wx.NewId()
    ID_EXPORT = wx.NewId()

    def __init__(self):
        super(MyFrame, self).__init__(None, wx.ID_ANY)

        auiFlags = aui.AUI_MGR_DEFAULT
        if wx.Platform == '__WXGTK__' and aui.AUI_MGR_DEFAULT & aui.AUI_MGR_TRANSPARENT_HINT:
            auiFlags = aui.AUI_MGR_TRANSPARENT_HINT
            auiFlags = aui.AUI_MGR_VENETIAN_BLINDS_HINT

        self._mgr = aui.AuiManager(flags=auiFlags)

        #self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        #top = wx.Panel(self, wx.ID_ANY)
        self.center = MainPane(self)
        # left = PartitionBrowserPanel(self)
        #left = ExplorerPane(self)
        #right = wx.Panel(self, wx.ID_ANY)
        #topInfo = aui.AuiPaneInfo().Name("Top Pane").Caption("The Center Pane").Bottom()
        centerInfo = aui.AuiPaneInfo().Name("Center Pane").Caption("Image View").Center()
        #rightInfo = aui.AuiPaneInfo().Name("Right Pane").Caption("Image Details").Right()
        #leftInfo = aui.AuiPaneInfo().Name("Left Pane").Caption("Explorer").Left()
        #self._mgr.AddPane(top, topInfo)
        self._mgr.AddPane(self.center, centerInfo)
        #self._mgr.AddPane(right, rightInfo)
        #self._mgr.AddPane(left, leftInfo)
        self.statusBar = self.CreateStatusBar(5)
        self.statusBar.SetStatusText("Test text")
        #floatingInfo = aui.AuiPaneInfo().Name("Center Pane").Caption("The Center Pane").Centre()
        #floating = wx.Panel(self, wx.ID_ANY)

        # Create application icon
        self._mgr.Update()
        self.Show()
        self.Bind(wx.EVT_CLOSE, self.OnAuiBaseClose)


        img_path = os.path.abspath("./success_36x36.png")
        icon = wx.Icon(img_path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        #self.SetBackgroundColour(wx.CYAN)
        self.SetLabel("test")
        #self.SetTitle("Image Archive Client")
        self.SetTitle("Podiatry Management system")
        #create main menu

        self.mainmenu_bar = MainMenu()
        self.SetMenuBar(self.mainmenu_bar)

        self.Bind(wx.EVT_MENU, self.OnMenu)

        # toolbar
        #toolb = EasyToolBar(self)
        #toolb.AddEasyToolBar(wx.ID_CUT)
        #toolb.AddEasyToolBar(wx.ID_COPY)
        #toolb.AddEasyToolBar(wx.ID_PASTE)
        #toolb.Realize()
        #self.SetToolBar(toolb)
       
        #test1 = wx.TextCtrl(self, -1, 'Pane 1 - simple text', wx.DefaultPosition, wx.Size(150, 150),
        #                    wx.NO_BORDER | wx.TE_MULTILINE)
        # test2 = wx.TextCtrl(self, -1, 'Pane 1 - simple text', wx.DefaultPosition, wx.Size(20, 150),
        #                    wx.NO_BORDER | wx.TE_MULTILINE)
        # test3 = wx.TextCtrl(self, -1, 'Pane 1 - simple text', wx.DefaultPosition, wx.Size(20, 150),
        #                    wx.NO_BORDER | wx.TE_MULTILINE)

        #self.Bind(wx.EVT_TOOL, self.OnToolBar)
        #self._mgr.AddPane(IAPanal(self), wx.LEFT, "Pane 1")
        #self._mgr.AddPane(test2, wx.BOTTOM, "Pane 2")
        #self._mgr.AddPane(test3, wx.CENTER, "Pane 3")

        self._mgr.Update()

    def OnToolBar(self, event):
        print "ToolBarItem Clicked", event.GetId()
        event.Skip()

    def OnAuiBaseClose(self, event):
        appName = wx.GetApp().GetAppName()
        assert appName, "No App Name Set"


    def OnMenu(self, event):
        evt_id = event.GetId()
        print evt_id
        if evt_id == wx.ID_NEW:

            self.OnNew()
        elif evt_id == wx.ID_OPEN:
            self.OnNew()
        elif evt_id == wx.ID_CLOSE:
            self.OnNew()
        elif evt_id == wx.ID_SAVE:
            self.OnNew()
        elif evt_id == wx.ID_SAVEAS:
            pass
        elif evt_id == wx.ID_PREFERENCES:
            self.OnNew()
        elif evt_id == wx.ID_EXIT:
            self.Quit()


    def OnNew(self):
        print "New"
        page = self.center.GetCurrentPage()
        print page.pageName
        wizard = NewWizard(self)
        wizard.Create()
        wizard.Run()
        
    def AddPane(self, pane, auiInfo):
        self._mgr.AddPane(pane, auiInfo)
        self._mgr.Update()

    def LoadDefaultPerspective(self):
        appName = wx.GetApp().GetAppName()
        assert appName, "No App Name Set"
        config = wx.Config(appName)
        perspective = config.Read("perspective")
        if perspective:
            self._mgr.LoadPerspective(perspective)
    def Quit(self):
        self._mgr.UnInit()
        self.Destroy()

class IAPanel(wx.Panel):
    def __init__(self, *args, **keys):
        wx.Panel.__init__(self, *args, **keys)
        self.test1 = wx.TextCtrl(self, wx.ID_ANY, 'Pane 1 - simple text')

if __name__=="__main__":
    #str=os.path.curdir
    #new
    if os.name == 'posix':
        print os.environ['PWD']
    print platform.system()
    cfg = ConfigReader()
    cfg.read("config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    # end new
    app=MyApp(False)
    app.MainLoop()
