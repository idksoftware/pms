'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard



class App_TimePage(PyWizardPage):

    def __init__(self, parent):
        PyWizardPage.__init__(self, parent)
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.Done = False

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, next):
        self.next = next
        return self.next
    def GetNext(self):
        return self.next
    def GetPrev(self):
        return self.prev

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Appointments - Time")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        
        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        

    
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        
    def IsDone(self):
        return self.Done


    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
        self.Done = True