'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from wx.calendar import CalendarCtrl


class GeneralCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(GeneralCtrl, self).__init__(parent, style=style)
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Equipement - Details")
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
        self.purchased = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())

        
        costLbl = wx.StaticText(self, -1, "Cost:")
        self.cost = wx.TextCtrl(self, -1, text, size=(30, 23))

        nextServiceLbl = wx.StaticText(self, -1, "Next Service:")
        self.nextService = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())

        lastServiceLbl = wx.StaticText(self, -1, "Last Service:")
        self.lastService = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())
        
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

       


class OtherCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(OtherCtrl, self).__init__(parent, style=style)
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Other Equipment Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)


        serviceHistoryLbl = wx.StaticText(self, -1, "Service History:")
        #self.appointments = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300,100))
        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.serviceHistory = ServiceHistoryListCtrl(self)
        self.serviceHistory.populateList(self.rows)

        text = ""
        noteLbl = wx.StaticText(self, -1, "Notes:")
        self.other = wx.TextCtrl(self, -1, text, size=(300,100), style=wx.TE_MULTILINE)
        #td.Set(GPTable.IDX_TITLE, text, title)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        addrSizer = wx.GridBagSizer(vgap=8, hgap=8)
        
        addrSizer.Add(serviceHistoryLbl, (1, 1))
        addrSizer.Add(self.serviceHistory, (1, 2)) #wx.FIXED_MINSIZE
        
        addrSizer.Add(noteLbl, (2, 1))
        addrSizer.Add(self.other, (2, 2)) #wx.FIXED_MINSIZE

        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        
class ServiceHistoryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(ServiceHistoryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")
        self.InsertColumn(2, "Cost")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        self.SetColumnWidth(2, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[0], row[1]
            self.Append(list)
        
class EquipmentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Continuous Professional Development", size=(600, 600))
        '''
        Constructor
        '''
        self.panel = PatentEditPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        #btnSizer = wx.StdDialogButtonSizer()
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        btnSizer
        sizer.Add(self.panel, 1, wx.EXPAND)
        #okButton = wx.Button(self, wx.ID_OK, "Ok", pos=(15, 15))
        #okButton.SetDefault()
        #btnSizer.Add(okButton)
        #cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel", pos=(15, 15))
        #btnSizer.Add(cancelButton)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)
        #sizer.Add(btnSizer)
        self.SetSizer(sizer)
        #self.SetInitialSize()
        #self.Bind(wx.EVT_BUTTON, self.OnButton)
        
    #def OnButton(self, event):
        #pos = self.panel.generalCtrl.preferedPhone.Value()
        #return event
   
class PatentEditPanel(wx.Notebook):
    def __init__(self, parent):
        super(PatentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)


        self.generalCtrl = GeneralCtrl(self)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Other")


class TestApp(wx.App):
    def OnInit(self):
        equipmentEditDialog = EquipmentEditDialog()
        
        print "Opening EquipmentEditDialog"
        equipmentEditDialog.ShowModal()
        print "Closing EquipmentEditDialog"
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
