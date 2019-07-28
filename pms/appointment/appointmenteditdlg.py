'''
Created on Jan 8, 2014

@author: wzw7yn
'''
import wx
import wx.lib.scrolledpanel as scrolledpanel
from wx.calendar import CalendarCtrl
from access.ap_pat_joined import AppointmentPatentTable
from appointmentpickerdlg import AppointmentPickerDialog





class AppointmentEditDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Patent Details", size=(500, 450))
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

class PatentEditPanel(wx.Panel):
    def __init__(self, parent):
        super(PatentEditPanel, self).__init__(parent, style=wx.LB_BOTTOM)
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Appointment Time")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)

        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        sizer = wx.GridBagSizer(vgap=8, hgap=8)

        appointmentTimeLbl = wx.StaticText(self, -1, "Appointment:")
        timeLbl = wx.StaticText(self, -1, ":")
        #self.apTime = row[AppointmentPatentTable.IDX_TIME]

        text = ""
        self.date = wx.DatePickerCtrl(self, -1, wx.DateTime.Today())
        sizer.Add(appointmentTimeLbl, (1, 1))
        
        
        timeSizer = wx.BoxSizer(wx.HORIZONTAL)
        timeSizer.Add(self.date)
        timeSizer.AddSpacer(20)
        self.hour = wx.SpinCtrl(self, -1, "", size=(40,25), min=0, max=23, initial=9)
        hourLbl = wx.StaticText(self, -1, " hour ")
        self.min = wx.SpinCtrl(self, -1, "", size=(40,25), min=0, max=59, initial=30)
        minLbl = wx.StaticText(self, -1, " min")
        
        timeSizer.Add(self.hour)
        timeSizer.Add(hourLbl)
        timeSizer.Add(self.min)
        timeSizer.Add(minLbl)
        
        sizer.Add(timeLbl, (1, 1))
        sizer.Add(timeSizer, (1, 2))  
        self.lookupTimeSlotButton = wx.Button(self, -1, "Look Time Slot", size=(100, 23))
        sizer.Add(self.lookupTimeSlotButton, (2, 3))   

        locationLbl = wx.StaticText(self, -1, "Location:")
        locationCatList = [ 'Clinic', 'Home', 'Other' ]
        self.location = wx.ComboBox(self, -1, "", (10, 30), (200, 23), locationCatList, wx.CB_DROPDOWN)
        self.locationAddButton = wx.Button(self, -1, "Look up", size=(100, 23))

        sizer.Add(locationLbl, (3, 1))
        sizer.Add(self.location, (3, 2))
        sizer.Add(self.locationAddButton, (3,3))

        addressLbl = wx.StaticText(self, -1, "Address:")

        address1 = "211 Redwood Rd"
        address2 = None
        town = "Burgess Hill"
        county = "West Sussex"
        postcode = "RH346HG"
        if address2 == None:
            address1Str = address1 + " " + town
        else:
            address1Str = address1 + " " + address2 + " " + town
        self.address = wx.StaticText(self, -1, address1Str)

        self.county = wx.StaticText(self, -1, county)
        self.post = wx.StaticText(self, -1, postcode)

        sizer.Add(addressLbl, (4, 1))
        sizer.Add(self.address, (4, 2))
        sizer.Add(self.county, (5, 2))
        sizer.Add(self.post, (6, 2))



        phoneLbl = wx.StaticText(self, -1, "Phone:")
        phoneStr = "Home " + "01444-241048" " Work " + "01273-925723"
        mobileStr = "Mobile " + "+4478912786397"

        sizer.Add(phoneLbl, (7, 1))
        self.phone = wx.StaticText(self, -1, phoneStr)
        self.mobile = wx.StaticText(self, -1, mobileStr)
        sizer.Add(self.phone, (7, 2))
        sizer.Add(self.mobile, (8, 2))

        emailLbl = wx.StaticText(self, -1, "Email:")
        emailStr = "i.ferguson@idk.co.uk"
        self.email = wx.StaticText(self, -1, emailStr)
        sizer.Add(emailLbl, (9, 1))
        sizer.Add(self.email, (9, 2))

        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        self.locationAddButton.Bind(wx.EVT_BUTTON, self.OnLocationButton)
        self.lookupTimeSlotButton.Bind(wx.EVT_BUTTON, self.OnLookupTimeSlotButton)

    def OnLookupTimeSlotButton(self, event):
        appointmentPickerDialog = AppointmentPickerDialog()
        print "Opening AppointmentPickerDialog"
        appointmentPickerDialog.ShowModal()
        print "Closing AppointmentPickerDialog"
        
    def OnLocationButton(self, event):
        lookupDialog = LookupDialog(self.location.Value, -1)
        print "Opening LookupDialog"
        lookupDialog.ShowModal()
        print "Closing LookupDialog"
       


class LookupDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, loctype, row):
        wx.Dialog.__init__(self, None, -1, "Appointment Details", size=(1000, 600))
        '''
        Constructor
        '''
        if loctype == 'Clinic':
            self.panel = LookupClinicPanel(self, row)
        elif loctype == 'Home':
            self.panel = LookupHomePanel(self, row)
        else:
            self.panel = LookupOtherPanel(self, row)
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



class LookupClinicPanel(wx.Panel):
    def __init__(self, parent, row):
        super(LookupClinicPanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(500, 400))
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()
        


    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Lookup Clinic")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)

        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.rows = [
                ("2013 12 23", "PNA"),
                ("2013 06 02", "Check-up"),
                ]

        self.clinicListCtrl = ClinicListCtrl(self)
        self.clinicListCtrl.populateList(self.rows)

        #mainSizer = wx.BoxSizer(wx.VERTICAL)
        
class ClinicListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(ClinicListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(300,100))

        self.InsertColumn(0, "Date")
        self.InsertColumn(1, "Title")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 180)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        for row in data:
            list = row[0], row[1]
            self.Append(list)
        
class LookupHomePanel(wx.Panel):
    def __init__(self, parent, row):
        super(LookupHomePanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(500, 400))
        #self.appointmentDetailsCtrl = AppointmentDetailsCtrl(self, row)
        # Layout
        self.__DoLayout(row)
        self.SetInitialSize()
        self.row = row


    def __DoLayout(self, row):
        title_lbl= wx.StaticText(self, label="Lookup Home")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)

        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

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
        
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

        
class LookupOtherPanel(wx.Panel):
    def __init__(self, parent, row):
        super(LookupOtherPanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(500, 400))
        #self.appointmentDetailsCtrl = AppointmentDetailsCtrl(self, row)
        # Layout
        self.__DoLayout(row)
        self.SetInitialSize()
        self.row = row


    def __DoLayout(self, row):
        title_lbl= wx.StaticText(self, label="Lookup Other")
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
        
        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class TestApp(wx.App):
    def OnInit(self):
        appointmentEditDialog = AppointmentEditDialog()
        print "Opening AppointmentEditDialog"
        appointmentEditDialog.ShowModal()
        print "Closing AppointmentEditDialog"
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()
