'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx

from wx.adv import PyWizardPage
from wx.adv import Wizard
from wx.adv import wx
from newinfo import GPInfo

    
class GP_GeneralPage(PyWizardPage):

    def __init__(self, parent, gpInfo):
        PyWizardPage.__init__(self, parent)
        self.gpInfo = gpInfo
        self.prev = self
        self.next = self
        self.__DoLayout()
        self.SetInitialSize()
        self.Bind(Wizard.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.gpInfo = GPInfo

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
        
        title_lbl= wx.StaticText(self, label="GP - Contact Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        text = ""
        titleLbl = wx.StaticText(self, -1, "Title:")
        self.title = wx.TextCtrl(self, -1, text, size=(50, 23))
          
        firstLbl = wx.StaticText(self, -1, "First Names:")
        self.first = wx.TextCtrl(self, -1, text, size=(200, 23))
        
        surnameLbl = wx.StaticText(self, -1, "Surname:")
        self.surname = wx.TextCtrl(self, -1, text, size=(100, 23))
        
        addressLbl = wx.StaticText(self, -1, "Address:")
        self.address = wx.TextCtrl(self, -1, text)
        
        townLbl = wx.StaticText(self, -1, "Town/City:")
        self.town = wx.TextCtrl(self, -1, text, size=(75, 23))
        
        postcodeLbl = wx.StaticText(self, -1, "Postcode:")
        self.postcode = wx.TextCtrl(self, -1, text)
        
        homephoneLbl = wx.StaticText(self, -1, "Home Phone:")
        self.homephone = wx.TextCtrl(self, -1, text, size=(100, 23))
         
        workphoneLbl = wx.StaticText(self, -1, "Work Phone:")
        self.workphone = wx.TextCtrl(self, -1, text, size=(100, 23))
        
        mobileLbl = wx.StaticText(self, -1, "Mobile:")
        self.mobile = wx.TextCtrl(self, -1, text, size=(100, 23))
        
        preferedPhoneLbl = wx.StaticText(self, -1, "Prefered Phone:")
        self.preferedPhone = wx.TextCtrl(self, -1, text, size=(100, 23))
        
        emailLbl = wx.StaticText(self, -1, "Email:")
        self.email = wx.TextCtrl(self, -1, text, size=(200, 23))
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(titleLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.title, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(firstLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.first, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(surnameLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.surname, 0)
        
        addrSizer.Add(addressLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.address, 0, wx.EXPAND)
        
        addrSizer.Add(townLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.town, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(postcodeLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.postcode, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(homephoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.homephone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(workphoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.workphone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(mobileLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.mobile, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(preferedPhoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.preferedPhone, 0, wx.FIXED_MINSIZE)
        
        addrSizer.Add(emailLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.email, 0, wx.FIXED_MINSIZE)
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

      

    def OnPageChanged(self, event):
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
        
    def GetPageInfo(self):
        return self.gpInfo
