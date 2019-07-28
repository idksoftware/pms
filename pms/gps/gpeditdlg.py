'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from access.gp import GPTable

class Attrib:

    
    def __init__(self):
        self.text = ''
        self.ctrl = None
        
    def IsChanged(self):
        if self.ctrl == None:
            return False
        if self.text != self.ctrl.GetValue():
            return True
        return False
    
    def GetText(self):
        if self.ctrl == None:
            return False
        return self.ctrl.GetValue()

    
class GPTableData:
    def __init__(self):
        self.row = list()    
        for i in range(0, 12):
            self.row.append(Attrib())
            
    def Set(self, idx, text, ctrl):
        self.row[idx].text = text
        self.row[idx].ctrl = ctrl
    
    def updateList(self):
        self.changeList = {}
        i = 0
        for item in self.row:
            if item.IsChanged():
                self.changeList[i] = item.GetText()
            i = i + 1
        return self.changeList   
        
    
class GeneralCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, td, data, style=wx.TAB_TRAVERSAL):
        super(GeneralCtrl, self).__init__(parent, style=style)
        self.current = "Default"
        # Layout
        self.__DoLayout(td, data)
        self.SetInitialSize()

    def __DoLayout(self, td, data):
        '''
         IDX_GP_ID = 0
    IDX_TITLE = 1
    IDX_FIRST_NAME = 2
    IDX_SURNAME = 3
    IDX_ADDRESS = 4
    IDX_TOWN = 5
    IDX_POST_CODE = 6
    IDX_HOME_PHONE = 7
    IDX_WORK_PHONE = 8
    IDX_MOBILE = 9
    IDX_PREFERED_PHONE = 10
    IDX_EMAIL = 11
        '''
        title_lbl= wx.StaticText(self, label="Contact Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        if data[GPTable.IDX_TITLE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_TITLE]
        titleLbl = wx.StaticText(self, -1, "Title:")
        title = wx.TextCtrl(self, -1, text, size=(50, 23))
        td.Set(GPTable.IDX_TITLE, text, title)  
        
        
        if data[GPTable.IDX_FIRST_NAME] == None:
            text = ""
        else:
            text = data[GPTable.IDX_FIRST_NAME]
        firstLbl = wx.StaticText(self, -1, "First Names:")
        first = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_FIRST_NAME, text, first)  
        
        if data[GPTable.IDX_SURNAME] == None:
            text = ""
        else:
            text = data[GPTable.IDX_SURNAME]
        surnameLbl = wx.StaticText(self, -1, "Surname:")
        surname = wx.TextCtrl(self, -1, text, size=(200, 23))
        td.Set(GPTable.IDX_SURNAME, text, surname)  
  
        if data[GPTable.IDX_ADDRESS] == None:
            text = ""
        else:
            text = data[GPTable.IDX_ADDRESS]
        addressLbl = wx.StaticText(self, -1, "Address:")
        address = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_ADDRESS, text, address)  
        #address2 = wx.TextCtrl(self, -1, "")

  
        if data[GPTable.IDX_TOWN] == None:
            text = ""
        else:
            text = data[GPTable.IDX_TOWN]
        townLbl = wx.StaticText(self, -1, "Town/City:")
        town = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_TOWN, text, town)  

  
        if data[GPTable.IDX_POST_CODE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_POST_CODE]
        postcodeLbl = wx.StaticText(self, -1, "Postcode:")
        postcode = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_POST_CODE, text, postcode)  
        
  
        if data[GPTable.IDX_HOME_PHONE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_HOME_PHONE]        
        homephoneLbl = wx.StaticText(self, -1, "Home Phone:")
        homephone = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_HOME_PHONE, text, homephone)  
       
  
        if data[GPTable.IDX_WORK_PHONE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_WORK_PHONE]        
        workphoneLbl = wx.StaticText(self, -1, "Work Phone:")
        workphone = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_WORK_PHONE, text, workphone)  
        
        if data[GPTable.IDX_MOBILE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_MOBILE]    
        mobileLbl = wx.StaticText(self, -1, "Mobile:")
        mobile = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_MOBILE, text, mobile)  
        
        if data[GPTable.IDX_PREFERED_PHONE] == None:
            text = ""
        else:
            text = data[GPTable.IDX_PREFERED_PHONE]    
        preferedPhoneLbl = wx.StaticText(self, -1, "Prefered Phone:")
        preferedPhone = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_PREFERED_PHONE, text, preferedPhone)  
        
        if data[GPTable.IDX_EMAIL] == None:
            text = ""
        else:
            text = data[GPTable.IDX_EMAIL]    
        emailLbl = wx.StaticText(self, -1, "Email:")
        email = wx.TextCtrl(self, -1, text)
        td.Set(GPTable.IDX_EMAIL, text, email)  
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(titleLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(title, 0)
        
        addrSizer.Add(firstLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(first, 0, wx.EXPAND)
        
        addrSizer.Add(surnameLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(surname, 0, wx.EXPAND)
        
        addrSizer.Add(addressLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(address, 0, wx.EXPAND)
        
        addrSizer.Add(townLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(town, 0, wx.EXPAND)
        
        addrSizer.Add(postcodeLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(postcode, 0, wx.EXPAND)
        
        addrSizer.Add(homephoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(homephone, 0, wx.EXPAND)
        
        addrSizer.Add(workphoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(workphone, 0, wx.EXPAND)
        
        addrSizer.Add(mobileLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(mobile, 0, wx.EXPAND)
        
        addrSizer.Add(preferedPhoneLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(preferedPhone, 0, wx.EXPAND)
        
        addrSizer.Add(emailLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email, 0, wx.EXPAND)
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)


class HistoryCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(HistoryCtrl, self).__init__(parent, style=style)
        #self.current = "Default"
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        

        title_lbl= wx.StaticText(self, label="History")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)
        
        firstLbl = wx.StaticText(self, -1, "First Names:")
        first = wx.TextCtrl(self, -1, "")

        surnameLbl = wx.StaticText(self, -1, "Surname:")
        surname = wx.TextCtrl(self, -1, "")

        addressLbl = wx.StaticText(self, -1, "Address:")
        address1 = wx.TextCtrl(self, -1, "")
        address2 = wx.TextCtrl(self, -1, "")

        townLbl = wx.StaticText(self, -1, "Town/City:")
        town = wx.TextCtrl(self, -1, "")

        postcodeLbl = wx.StaticText(self, -1, "Postcode:")
        postcode = wx.TextCtrl(self, -1, "")
        
        homephoneLbl = wx.StaticText(self, -1, "Home Phone:")
        homephone = wx.TextCtrl(self, -1, "")
        
        emailLbl = wx.StaticText(self, -1, "Email:")
        email = wx.TextCtrl(self, -1, "")
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(firstLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(first, 0, wx.EXPAND)
        
        addrSizer.Add(surnameLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(surname, 0, wx.EXPAND)
        
        addrSizer.Add(addressLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(address1, 0, wx.EXPAND)
        addrSizer.Add((10,10))
        addrSizer.Add(address2, 0, wx.EXPAND)
        
        addrSizer.Add(townLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(town, 0, wx.EXPAND)
        
        addrSizer.Add(postcodeLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(postcode, 0, wx.EXPAND)
        
        addrSizer.Add(homephoneLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(homephone, 0, wx.EXPAND)
        
        addrSizer.Add(emailLbl, 0,
					wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email, 0, wx.EXPAND)
        
        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class GPEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, idx):
        wx.Dialog.__init__(self, None, -1, "Patent Details", size=(700, 600))
        '''
        Constructor
        '''
        self.gpTable = GPTable() 
        self.tableData = GPTableData()
        if idx != -1:
            self.data = self.gpTable.showItem(idx)
            print self.data  
        else:
            self.data = (1, None, u'Steve', u'Dean', None, None, None, None, None, None, None, None)   
             
        self.panel = PatentEditPanel(self, self.tableData, self.data)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        okButton.SetDefault()
        btnSizer.Add(okButton)
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(15, 15))
        btnSizer.Add(cancelButton)
        sizer.Add(btnSizer)
        self.SetSizer(sizer)
        self.SetInitialSize()
       
        #self.Bind(wx.EVT_BUTTON, self.OnButton)
  
    def OnButton(self, event):
        if event == wx.ID_OK:
            self.Save()
            
    def Save(self):
        cl = self.tableData.updateList()
        if len(cl):
            self.gpTable.updatelist(1, cl)
            return True
        return False
        
    def GetUsername(self):
        self.panel.GetUsername()

    def GetPassword(self):
        self.panel.GetPasswd()

class PatentEditPanel(wx.Notebook):
    def __init__(self, parent, td, data):
        super(PatentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)
        
        self.generalCtrl = GeneralCtrl(self, td, data)
        self.AddPage(self.generalCtrl, "General")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "history")

class TestApp(wx.App):
    def OnInit(self):
        gpEditDialog = GPEditDialog(-1)
        
        print "Opening CPDEditDialog"
        gpEditDialog.ShowModal()
        print "Closing CPDEditDialog"
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()