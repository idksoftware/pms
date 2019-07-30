'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard
from wx.adv import DatePickerCtrl
from equipment.serviceproviderdlg import ServiceProviderDialog

class Eqp_GeneralPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.gpInfo = gpInfo
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        #self.gpInfo = GPInfo

    def SetPrev(self, prev):
        self.prev = prev
        return self.prev

    def SetNext(self, nxt):
        self.next = nxt
        return self.next
    def GetNext(self):
        return self.next
    def GetPrev(self):
        return self.prev


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Equipment - Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        text = ""
        typeLbl = wx.StaticText(self, -1, "Type:")

        typeList = [ 'Autoclave', 'Ultra Sound' ]
        self.type = wx.ComboBox(self, -1, "", (10, 30), (130, 23), typeList, wx.CB_DROPDOWN)

        makeModelLbl = wx.StaticText(self, -1, "Make/Model:")
        self.makeModel = wx.TextCtrl(self, -1, text, size=(200, 23))
        
        serialNoLbl = wx.StaticText(self, -1, "Serial No:")
        self.serialNo = wx.TextCtrl(self, -1, text, size=(200, 23))
        
        purchasedLbl = wx.StaticText(self, -1, "Purchased:")
        self.purchased = DatePickerCtrl(self, -1, wx.DateTime.Today())

        
        costLbl = wx.StaticText(self, -1, "Cost:")
        self.cost = wx.TextCtrl(self, -1, text, size=(30, 23))

        nextServiceLbl = wx.StaticText(self, -1, "Next Service:")
        self.nextService = DatePickerCtrl(self, -1, wx.DateTime.Today())

        lastServiceLbl = wx.StaticText(self, -1, "Last Service:")
        self.lastService = DatePickerCtrl(self, -1, wx.DateTime.Today())
        
        intervalList = [ '3 Months', '6 Months', 'Year', '2 Years', '5 years' ]
        serviceIntervalLbl = wx.StaticText(self, -1, "Service Interval:")
        self.serviceInterval = wx.ComboBox(self, -1, "", (10, 30), (130, 23), intervalList, wx.CB_DROPDOWN)

        spList = [ 'GEC Equipment', 'H&I Services' ]
        serviceProviderLbl = wx.StaticText(self, -1, "Service Provider:")
        self.serviceProvider = wx.ComboBox(self, -1, "", (10, 30), (200, 23), spList, wx.CB_DROPDOWN)
        spAddButton = wx.Button(self, -1, "Add", size=(50, 23))
        


        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(typeLbl, (1, 1))
        grpSizer.Add(self.type, (1, 2))
        
        grpSizer.Add(makeModelLbl, (2, 1))
        grpSizer.Add(self.makeModel, (2, 2))
        
        grpSizer.Add(serialNoLbl, (3, 1))
        grpSizer.Add(self.serialNo, (3, 2))
        
        grpSizer.Add(purchasedLbl, (4, 1))
        grpSizer.Add(self.purchased, (4, 2))
        
        grpSizer.Add(costLbl, (4, 3))
        grpSizer.Add(self.cost, (4, 4))
        
        grpSizer.Add(nextServiceLbl, (5, 1))
        grpSizer.Add(self.nextService, (5, 2))
        
        grpSizer.Add(lastServiceLbl, (5, 3))
        grpSizer.Add(self.lastService, (5, 4))


        grpSizer.Add(serviceIntervalLbl, (6, 1))
        grpSizer.Add(self.serviceInterval, (6, 2))

        grpSizer.Add(serviceProviderLbl, (7, 1))
        grpSizer.Add(self.serviceProvider, (7, 2))
        grpSizer.Add(spAddButton, (7, 3))

    
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_BUTTON, self.OnNew, spAddButton)
        
    def OnNew(self, event):
        serviceProviderDialog = ServiceProviderDialog()
        serviceProviderDialog.ShowModal()

    def OnPageChanged(self, event):
        '''
        self.gpInfo.title = self.title.GetValue()
        self.gpInfo.first = self.first.GetValue()
        self.gpInfo.surname = self.surname.GetValue()
        self.gpInfo.address = self.address.GetValue()
        self.gpInfo.town = self.town.GetValue()
        self.gpInfo.postcode = self.postcode.GetValue()
        self.gpInfo.homephone = self.homephone.GetValue()
        self.gpInfo.workphone = self.workphone.GetValue()
        self.gpInfo.mobile = self.mobile.GetValue()
        self.gpInfo.preferedPhone = self.preferedPhone.GetValue()
        self.gpInfo.email = self.email.GetValue()
        '''
        pass
    def GetPageInfo(self):
        '''
        return self.gpInfo
        '''
        pass