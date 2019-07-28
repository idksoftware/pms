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
        title_lbl= wx.StaticText(self, label="Contact Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        text = ""
        titleLbl = wx.StaticText(self, -1, "Title:")

        titleList = [ 'Mr', 'Miss', 'Dr', 'Sir', 'Madam' ]
        self.title = wx.ComboBox(self, -1, "", (10, 30), (90, 23), titleList, wx.CB_DROPDOWN)

        firstLbl = wx.StaticText(self, -1, "First Names:")
        self.first = wx.TextCtrl(self, -1, text, size=(100, 23))

        surnameLbl = wx.StaticText(self, -1, "Surname:")
        self.surname = wx.TextCtrl(self, -1, text, size=(200, 23))

        addressLbl = wx.StaticText(self, -1, "Address:")
        self.address = wx.TextCtrl(self, -1, text, style=wx.TE_MULTILINE, size=(200,50))

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
        testList = [ 'Home', 'Work', 'Mobile' ]
        self.preferedPhone = wx.ComboBox(self, -1, "", (10, 30), (90, 23), testList, wx.CB_DROPDOWN)

        emailLbl = wx.StaticText(self, -1, "Email:")
        self.email = wx.TextCtrl(self, -1, text, size=(200, 23))

        genderLbl = wx.StaticText(self, -1, "Gender:")
        genderList = [ 'Male', 'Female']
        self.gender = wx.RadioBox(self, -1, "", (10, 10), wx.DefaultSize, genderList, 2, wx.RA_SPECIFY_COLS | wx.NO_BORDER)

        NI_NumberLbl = wx.StaticText(self, -1, "NI Number:")
        self.niNumber = wx.TextCtrl(self, -1, text, size=(100, 23))

        dateOfBirthLbl = wx.StaticText(self, -1, "Date of Birth:")
        self.dateOfBirth = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())

        gpLbl = wx.StaticText(self, -1, "General Practioner:")
        testList = [ 'None', 'Dr Smith', 'Dr Johnson', 'Dr King' ]
        self.gp = wx.ComboBox(self, -1, "", (10, 30), wx.DefaultSize, testList, wx.CB_DROPDOWN)
        gpAddButton = wx.Button(self, -1, "Add", size=(50, 23))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)



        grpSizer.Add(titleLbl, (1, 1))
        grpSizer.Add(self.title, (1, 2))

        grpSizer.Add(firstLbl, (2, 1))
        grpSizer.Add(self.first, (2, 2))

        grpSizer.Add(surnameLbl, (3, 1))
        grpSizer.Add(self.surname, (3, 2))

        grpSizer.Add(addressLbl, (4, 1))
        grpSizer.Add(self.address, (4, 2))

        grpSizer.Add(townLbl, (5, 1))
        grpSizer.Add(self.town, (5, 2))

        grpSizer.Add(postcodeLbl, (5, 3))
        grpSizer.Add(self.postcode, (5, 4))

        grpSizer.Add(homephoneLbl, (6, 1))
        grpSizer.Add(self.homephone, (6, 2))

        grpSizer.Add(workphoneLbl, (6, 3))
        grpSizer.Add(self.workphone, (6, 4))

        grpSizer.Add(mobileLbl, (7, 1))
        grpSizer.Add(self.mobile, (7, 2))

        grpSizer.Add(preferedPhoneLbl, (7, 3))
        grpSizer.Add(self.preferedPhone, (7, 4))

        grpSizer.Add(emailLbl, (8, 1))
        grpSizer.Add(self.email, (8, 2))

        grpSizer.Add(genderLbl, (9, 1))
        grpSizer.Add(self.gender, (9, 2))

        grpSizer.Add(NI_NumberLbl, (10, 1))
        grpSizer.Add(self.niNumber, (10, 2))

        grpSizer.Add(dateOfBirthLbl, (11, 1))
        grpSizer.Add(self.dateOfBirth, (11, 2))

        grpSizer.Add(gpLbl, (12, 1))
        grpSizer.Add(self.gp, (12, 2))
        grpSizer.Add(gpAddButton, (12, 3))

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)




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

class PaymentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Payment Details", size=(600, 600))
        '''
        Constructor
        '''
        self.panel = PaymentEditPanel(self)

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

class PaymentEditPanel(wx.Notebook):
    def __init__(self, parent):
        super(PaymentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        self.generalCtrl = GeneralCtrl(self)
        self.AddPage(self.generalCtrl, "General")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Other")

class TestApp(wx.App):
    def OnInit(self):
        paymentEditDialog = PaymentEditDialog()
        
        print "Opening PaymentEditDialog"
        paymentEditDialog.ShowModal()
        print "Closing PaymentEditDialog"
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
