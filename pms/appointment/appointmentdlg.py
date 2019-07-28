'''
Created on Jan 23, 2014

@author: wzw7yn
'''
import wx


from access.ap_pat_joined import AppointmentPatentTable
from appointmentdetailsctrl import AppointmentDetailsCtrl




class AppointmentDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, row):
        wx.Dialog.__init__(self, None, -1, "Appointment Details", size=(1000, 600))
        '''
        Constructor
        '''
        self.panel = AppointmentPanel(self, row)

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



class AppointmentPanel(wx.Panel):
    def __init__(self, parent, row):
        super(AppointmentPanel, self).__init__(parent, style=wx.LB_BOTTOM, size=(1000, 600))
        self.appointmentDetailsCtrl = AppointmentDetailsCtrl(self, row)
        # Layout
        self.__DoLayout(row)
        self.SetInitialSize()
        self.row = row


    def __DoLayout(self, row):


        mainSizer = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)

        appointmentTimeLbl = wx.StaticText(self, -1, "Date/Time:")
        self.apTime = row[AppointmentPatentTable.IDX_TIME]
        self.time = wx.StaticText(self, -1, self.apTime)

        sizer.Add(appointmentTimeLbl, (1, 1))
        sizer.Add(self.time, (1, 2))

        nameLbl = wx.StaticText(self, -1, "Name:")

        title = row[AppointmentPatentTable.IDX_TITLE]
        first = row[AppointmentPatentTable.IDX_FIRST_NAME]
        surname = row[AppointmentPatentTable.IDX_SURNAME]

        nameStr = self.GetNameStr(title,first,surname)
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (2, 1))
        sizer.Add(self.name, (2, 2))

        locationLbl = wx.StaticText(self, -1, "Location:")
        self.locationStr = "Redwood Home"
        self.location = wx.StaticText(self, -1, self.locationStr)

        sizer.Add(locationLbl, (3, 1))
        sizer.Add(self.location, (3, 2))

        treatmentLbl = wx.StaticText(self, -1, "Treatment:")
        self.treatmentStr = "PNA"
        self.treatment = wx.StaticText(self, -1, self.treatmentStr)

        sizer.Add(treatmentLbl, (4, 1))
        sizer.Add(self.treatment, (4, 2))

        duationLbl = wx.StaticText(self, -1, "Appox Duation:")
        self.duationStr = "45 min"
        self.duation = wx.StaticText(self, -1, self.duationStr)

        sizer.Add(duationLbl, (5, 1))
        sizer.Add(self.duation, (5, 2))

        costLbl = wx.StaticText(self, -1, "Cost:")
        self.costStr = "250.00 pounds"
        self.cost = wx.StaticText(self, -1, self.costStr)

        sizer.Add(costLbl, (6, 1))
        sizer.Add(self.cost, (6, 2))

        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        #openbtn = wx.Button(self, wx.ID_OPEN)


        editbtn.SetDefault()
        btnszr.Add(editbtn)
        #btnszr.Add(openbtn)

        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.appointmentDetailsCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)

        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(btnszr, 0, wx.ALIGN_RIGHT, 12)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_BUTTON, self.OnEdit, editbtn)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def GetNameStr(self,title,first,surname):
        if title == None:
            if first == None:
                if surname == None:
                    return None
                else:
                    return surname
            else:
                return first + " " + surname
        else:
            return title + " " + first + " " + surname


    def OnEdit(self, event):
        page = self.appointmentDetailsCtrl.GetSelection()
        if page == 0:
            print "Appointments page"
            from appointmenteditdlg import AppointmentEditDialog
            appointmentEditDialog = AppointmentEditDialog()
            print "Opening AppointmentEditDialog"
            appointmentEditDialog.ShowModal()
            print "Closing AppointmentEditDialog"
        elif page == 1:
            print "Patents page"
            from patent.patenteditdlg import PatentEditDialog
            patentEditDialog = PatentEditDialog()
            print "Opening PatentEditDialog"
            patentEditDialog.ShowModal()
            print "Closing PatentEditDialog"
        elif page == 2:
            print "Treatment page"
            from patent.treatmenteditdlg import TreatmentEditDialog
            treatmentEditDialog = TreatmentEditDialog()
            print "Opening TreatmentEditDialog"
            treatmentEditDialog.ShowModal()
            print "Closing TreatmentEditDialog"
        elif page == 3:
            print "Payment page"
            from patent.paymenteditdlg import PaymentEditDialog
            paymentEditDialog = PaymentEditDialog()
            print "Opening PaymentEditDialog"
            paymentEditDialog.ShowModal()
            print "Closing PaymentEditDialog"
        elif page == 4:
            print "History page"
            from appointmenthistoryeditdlg import AppointmentHistoryDialog
            appointmentHistoryDialog = AppointmentHistoryDialog(self.row)
            print "Opening AppointmentHistoryDialog"
            appointmentHistoryDialog.ShowModal()
            print "Closing AppointmentHistoryDialog"
        print "Edit button"


class TestApp(wx.App):
    def OnInit(self):
        patentEditDialog = AppointmentDialog()
        print "Opening AppointmentDialog"
        patentEditDialog.ShowModal()
        print "Closing AppointmentDialog"
        return True

from access.database import Database
from utils.configreader import ConfigReader

if __name__=="__main__":
    cfg = ConfigReader()
    cfg.read("config.xml")
    Database.Open(cfg.GetPath(), cfg.GetUsername(), cfg.GetPassword())
    app = TestApp(False)
    app.MainLoop()