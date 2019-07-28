'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.wizard import PyWizardPage
import wx.wizard
from newinfo import GPInfo


class GP_OtherPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(wx.wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.gpInfo = gpInfo
        self.Done = False;

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
        title_lbl= wx.StaticText(self, label="GP - Other")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)


        text = ""
        noteLbl = wx.StaticText(self, -1, "Notes:")
        self.other = wx.TextCtrl(self, -1, text, size=(50, 100), style=wx.TE_MULTILINE)
        #td.Set(GPTable.IDX_TITLE, text, title)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        addrSizer.Add(noteLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_TOP)
        addrSizer.Add(self.other, 0, wx.EXPAND) #wx.FIXED_MINSIZE

        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def IsDone(self):
        return self.Done


    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
        self.gpInfo.other = self.other.GetValue()
        self.Done = True

    def GetPageInfo(self):
        return self.gpInfo