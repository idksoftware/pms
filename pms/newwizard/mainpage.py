'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard

class MainPage(PyWizardPage):

    def __init__(self, parent):
        PyWizardPage.__init__(self, parent)
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, next):
        self.next = next
        return self.next
    def GetNext(self):
        if self.appointmentRadio.GetValue() == True:
            self.next = self.options[0]
        elif self.patentRadio.GetValue() == True:
            self.next = self.options[1]
        elif self.gpRadio.GetValue() == True:
            self.next = self.options[2]
        elif self.cpdRadio.GetValue() == True:
            self.next = self.options[3]
        elif self.equRadio.GetValue() == True:
            self.next = self.options[4]
        return self.next
    def GetPrev(self):
        return self.prev

    def SetOptions(self, options={}):
        self.options = options

    def __DoLayout(self):
        sizer = wx.GridBagSizer(vgap=4, hgap=4)

        title_lbl = wx.StaticText(self, label="New Item Wizard")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        current_lbl = wx.StaticText(self, label="Where do you want to create the mirror")
        sizer.Add(current_lbl, (3, 1))

        self.appointmentRadio = wx.RadioButton(self, -1, "Appointment - Creates a new patent appointment");
        self.patentRadio = wx.RadioButton(self, -1, "Patent - Creates a new patent record");
        self.gpRadio = wx.RadioButton(self, -1, "GP - Creates a new GP Record");
        self.cpdRadio = wx.RadioButton(self, -1, "CPD - Creates a new CPD Record");
        self.equRadio = wx.RadioButton(self, -1, "Equipment - Creates a new equipment record");
        sizer.Add(self.appointmentRadio, (4 , 2))
        sizer.Add(self.patentRadio, (6 , 2))
        sizer.Add(self.gpRadio, (8 , 2))
        sizer.Add(self.cpdRadio, (10 , 2))
        sizer.Add(self.equRadio, (12 , 2))

        sizer.Add(title_lbl, (1 , 1))
        self.SetSizer(sizer)

    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
