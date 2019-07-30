'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard


class MedicalPage(PyWizardPage):

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
        return self.next
    def GetPrev(self):
        return self.prev

    def __DoLayout(self): #Medical Details
        title_lbl= wx.StaticText(self, label="Medical Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)
        
        heightLbl = wx.StaticText(self, -1, "Height:")
        self.height = wx.TextCtrl(self, -1, "")

        weightLbl = wx.StaticText(self, -1, "Weight:")
        self.weight = wx.TextCtrl(self, -1, "")

        allergiesLbl = wx.StaticText(self, -1, "Allergies:")
        self.allergies = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(200,100))

        otherLbl = wx.StaticText(self, -1, "Other Details:")
        self.other = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(200,100))
        
        grp1Sizer.Add(heightLbl, (1, 1))
        grp1Sizer.Add(self.height, (1, 2))
        grp1Sizer.Add(weightLbl, (1, 3))
        grp1Sizer.Add(self.weight, (1, 4))
        
        grp1Sizer.Add(allergiesLbl, (2, 1))
        grp1Sizer.Add(self.allergies, (2, 2))
        
        self.HeartTrouble = wx.CheckBox(self, label="HeartTrouble")
        grp1Sizer.Add(self.HeartTrouble, (3, 2))

        self.Diabetes = wx.CheckBox(self, label="Diabetes")
        grp1Sizer.Add(self.Diabetes, (4, 2))

        self.Epilepsy = wx.CheckBox(self, label="Epilepsy")
        grp1Sizer.Add(self.Epilepsy, (5, 2))

        self.SkinConditions = wx.CheckBox(self, label="Skin Conditions")
        grp1Sizer.Add(self.SkinConditions, (6, 2))

        self.HIV = wx.CheckBox(self, label="HIV")
        grp1Sizer.Add(self.HIV, (7, 2))

        self.Hepatits = wx.CheckBox(self, label="Hepatits")
        grp1Sizer.Add(self.Hepatits, (8, 2))

        self.Asthma = wx.CheckBox(self, label="Asthma")
        grp1Sizer.Add(self.Asthma, (9, 2))

        self.RheumaticFever = wx.CheckBox(self, label="Rheumatic Fever")
        grp1Sizer.Add(self.RheumaticFever, (10, 2))

        self.High_LowBloodPress = wx.CheckBox(self, label="High/Low Blood Press")
        grp1Sizer.Add(self.High_LowBloodPress, (3, 4))

        self.Claudication = wx.CheckBox(self, label="Claudication")
        grp1Sizer.Add(self.Claudication, (4, 4))

        self.SteroidTreatment = wx.CheckBox(self, label="Steroid Treatment")
        grp1Sizer.Add(self.SteroidTreatment, (5, 4))

        self.PeriphVascDisea = wx.CheckBox(self, label="Periph Vasc Disea")
        grp1Sizer.Add(self.PeriphVascDisea, (6, 4))
        self.VaricoseVeins = wx.CheckBox(self, label="Varicose Veins")
        grp1Sizer.Add(self.VaricoseVeins, (7, 4))
        self.ExcessiveBleading = wx.CheckBox(self, label="Excessive Bleading")
        grp1Sizer.Add(self.ExcessiveBleading, (8, 4))
        self.RheumatoidArtritis = wx.CheckBox(self, label="Rheumatoid Artritis")
        grp1Sizer.Add(self.RheumatoidArtritis, (9, 4))
        self.OsteoArtritis = wx.CheckBox(self, label="Osteo Artritis")
        grp1Sizer.Add(self.OsteoArtritis, (10, 4))
        self.Pregnancy = wx.CheckBox(self, label="Pregnancy")
        grp1Sizer.Add(self.Pregnancy, (11, 2))

        grp1Sizer.Add(otherLbl, (2, 3))
        grp1Sizer.Add(self.other, (2, 4))
        grp1Sizer.Add(self.HeartTrouble, (3, 2))

        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def OnPageChanged(self, event):
        print "EVT_WIZARD_PAGE_CHANGED"
