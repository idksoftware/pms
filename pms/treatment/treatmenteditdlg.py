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
        title_lbl= wx.StaticText(self, label="Treatment Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        nameLbl = wx.StaticText(self, -1, "Name:")

        nameStr = 'Prelimary Assessment'
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        discriptionLbl = wx.StaticText(self, -1, "Discription:")
        
        discriptionStr = 'Inital assessment of the patent'
        self.discription = wx.StaticText(self, -1, discriptionStr)

        sizer.Add(discriptionLbl, (2, 1))
        sizer.Add(self.discription, (2, 2))
        
        amountLbl = wx.StaticText(self, -1, "Amount:")
        amountStr = '38.50'
        sizer.Add(amountLbl, (5, 1))
        self.amount = wx.StaticText(self, -1, amountStr)
        sizer.Add(self.amount, (5, 2))
        



        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        editbtn.SetDefault()
        sizer.Add(editbtn, (8, 3))
        sizer.Add(openbtn, (8, 4))

        btnszr.Realize()

        #listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        #listSizer.Add(self.backupsListCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        #mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)




class OtherCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(OtherCtrl, self).__init__(parent, style=style)

        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Other Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)



        statusLbl = wx.StaticText(self, -1, "Status:")
        testList = [ 'One', 'Two', 'Three' ]
        self.status = wx.ComboBox(self, -1, "", (10, 30), wx.DefaultSize, testList, wx.CB_DROPDOWN)
        statusAddButton = wx.Button(self, -1, "Add", size=(50, 23))
        #okButton.SetDefault()




        startdateLbl = wx.StaticText(self, -1, "Start date:")
        #self.startdate = CalendarCtrl(self, -1, wx.DateTime.Today(), style=)
        self.startdate = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())

        insuranceInformationLbl = wx.StaticText(self, -1, "Insurance Information:")
        self.insuranceInformation = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(200,100))

        referralSourceLbl = wx.StaticText(self, -1, "Referral Source:")
        testList = [ 'One', 'Two', 'Three' ]
        self.referralSource = wx.ComboBox(self, -1, "", (10, 30), (200, 23), testList, wx.CB_DROPDOWN)
        referralSourceAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        categoryLbl = wx.StaticText(self, -1, "Category:")
        testList = [ 'One', 'Two', 'Three' ]
        self.category = wx.ComboBox(self, -1, "", (10, 30), (200, 23), testList, wx.CB_DROPDOWN)
        categoryAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        clinicLbl = wx.StaticText(self, -1, "Clinic Attended:")
        testList = [ 'One', 'Two', 'Three' ]
        self.clinic = wx.ComboBox(self, -1, "", (10, 30), (200, 23), testList, wx.CB_DROPDOWN)
        clinicAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)

        grp1Sizer.Add(statusLbl, (1, 1))
        grp1Sizer.Add(self.status, (1, 2))
        grp1Sizer.Add(statusAddButton, (1,3))

        grp1Sizer.Add(startdateLbl, (2, 1))
        grp1Sizer.Add(self.startdate, (2, 2))

        grp1Sizer.Add(insuranceInformationLbl, (3, 1))
        grp1Sizer.Add(self.insuranceInformation, (3, 2))

        grp1Sizer.Add(referralSourceLbl, (4, 1))
        grp1Sizer.Add(self.referralSource, (4, 2))
        grp1Sizer.Add(referralSourceAddButton, (4,3))

        grp1Sizer.Add(categoryLbl, (5, 1))
        grp1Sizer.Add(self.category, (5, 2))
        grp1Sizer.Add(categoryAddButton, (5,3))

        grp1Sizer.Add(clinicLbl, (6, 1))
        grp1Sizer.Add(self.clinic, (6, 2))
        grp1Sizer.Add(clinicAddButton, (6,3))

        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class TreatmentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Treatment Details", size=(600, 600))
        '''
        Constructor
        '''
        self.panel = TreatmentEditPanel(self)

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

class TreatmentEditPanel(wx.Notebook):
    def __init__(self, parent):
        super(TreatmentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        self.generalCtrl = GeneralCtrl(self)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Other")

class TestApp(wx.App):
    def OnInit(self):
        treatmentEditDialog = TreatmentEditDialog()
        print "Opening TreatmentEditDialog"
        treatmentEditDialog.ShowModal()
        print "Closing TreatmentEditDialog"
        
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
