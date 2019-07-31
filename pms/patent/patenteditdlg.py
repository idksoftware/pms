'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from wx.adv import DatePickerCtrl
#import  wx.calendar


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
        self.dateOfBirth = DatePickerCtrl(self, -1, wx.DateTime.Today())
        
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

class MedicalDetails():
    
    def __init__(self):
        self.height = 0
        self.weight = 0
        self.allergies = ""
        self.other = ""
        self.HeartTrouble = False
        self.Diabetes = False
        self.Epilepsy = False
        self.SkinConditions = False
        self.HIV = False
        self.Hepatits = False
        self.Asthma = False
        self.RheumaticFever = False
        self.High_LowBloodPressL = False
        self.Claudication = False
        self.SteroidTreatment = False
        self.PeriphVascDiseaDisea = False
        self.VaricoseVeins = False
        self.ExcessiveBleading = False
        self.RheumatoidArtritis = False
        self.OsteoArtritis = False
        self.Pregnancy = False
        
class InputCtrl():
    
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def getctrl(self):
        return self.ctrl

class MedicalCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(MedicalCtrl, self).__init__(parent, style=style)


        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Medical")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)



        heightLbl = wx.StaticText(self, -1, "Height:")
        #self.height = wx.TextCtrl(self, -1, "" wx.Validator)
        self.height = wx.SpinCtrl(self, -1, "", min=0, max=300, initial=200)
        
       
        

        weightLbl = wx.StaticText(self, -1, "Weight:")
        self.weight = wx.SpinCtrl(self, -1, "", min=0, max=300, initial=200)

        allergiesLbl = wx.StaticText(self, -1, "Allergies:")
        self.allergies = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(200,100))

        otherLbl = wx.StaticText(self, -1, "Other Details:")
        self.other = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(200,100))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)
        
        grp1Sizer.Add(heightLbl, (1, 1))
        #grp1Sizer.Add(self.height, (1, 2))
        grp1Sizer.Add(self.height, (1, 2))
        grp1Sizer.Add(weightLbl, (1, 3))
        grp1Sizer.Add(self.weight, (1, 4))
        
        grp1Sizer.Add(allergiesLbl, (2, 1))
        grp1Sizer.Add(self.allergies, (2, 2))
        
        grp1Sizer.Add(otherLbl, (2, 3))
        grp1Sizer.Add(self.other, (2, 4))
        
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

        

        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
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
        self.startdate = DatePickerCtrl(self, -1, wx.DateTime.Today())

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



        
        AppointmentsLbl = wx.StaticText(self, -1, "Appointment History:")
        #self.appointments = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300,100))
        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.appointments = AppointmentListCtrl(self)
        self.appointments.populateList(self.rows)

        otherLbl = wx.StaticText(self, -1, "Other Notes:")
        self.other = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(300,100))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        grp1Sizer = wx.GridBagSizer(vgap=8, hgap=8)
        
       
       
        grp1Sizer.Add(AppointmentsLbl, (1, 1))
        grp1Sizer.Add(self.appointments, (1, 2))
        
        grp1Sizer.Add(otherLbl, (2, 1))
        grp1Sizer.Add(self.other, (2, 2))
        
        mainSizer.Add(grp1Sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        
class AppointmentListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(AppointmentListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.rows = data
        for row in data:
            list = row[0], row[1]
            self.Append(list)
        
class PatentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Patent Details", size=(600, 600))
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
        self.medicalCtrl = MedicalCtrl(self)
        self.AddPage(self.medicalCtrl, "Medical")
        self.otherCtrl = OtherCtrl(self)
        self.AddPage(self.otherCtrl, "Other")
        self.historyCtrl = HistoryCtrl(self)
        self.AddPage(self.historyCtrl, "history")

class TestApp(wx.App):
    def OnInit(self):
        patentEditDialog = PatentEditDialog()
        print "Opening PatentEditDialog"
        patentEditDialog.ShowModal()
        print "Closing PatentEditDialog"
        
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
