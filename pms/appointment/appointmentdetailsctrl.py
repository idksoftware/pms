'''
Created on Jan 23, 2014

@author: wzw7yn
'''
import wx

from datetime import datetime
from datetime import timedelta
import aputils




import wx.lib.scrolledpanel as scrolledpanel
from access.ap_pat_joined import AppointmentPatentTable

class AppointmentTimeCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, row,  style=wx.TAB_TRAVERSAL):
        super(AppointmentTimeCtrl, self).__init__(parent, style=style)
        self.current = "Default"


        # Layout
        self.__DoLayout(row)
        self.SetInitialSize()

    def __DoLayout(self, row):
        title_lbl= wx.StaticText(self, label="Appointment Time")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)

        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        sizer = wx.GridBagSizer(vgap=8, hgap=8)

        appointmentTimeLbl = wx.StaticText(self, -1, "Appointment:")

        self.apTime = row[AppointmentPatentTable.IDX_TIME]

        timeStr = self.apTime
        self.name = wx.StaticText(self, -1, timeStr)

        sizer.Add(appointmentTimeLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        locationLbl = wx.StaticText(self, -1, "Location:")
        self.locationStr = "Redwood Home"
        self.location = wx.StaticText(self, -1, self.locationStr)

        sizer.Add(locationLbl, (3, 1))
        sizer.Add(self.location, (3, 2))

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

class PatentDetailsCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, row, style=wx.TAB_TRAVERSAL):
        super(PatentDetailsCtrl, self).__init__(parent, style=style)


        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Patent Details")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)

        nameLbl = wx.StaticText(self, -1, "Name:")

        title = 'Mr'
        first = 'Iain'
        surname = 'Ferguson'

        nameStr = title + " " + first + " " + surname
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        addressLbl = wx.StaticText(self, -1, "Address:")

        address1 = "16 St Wilfrieds Rd"
        address2 = None
        town = "Burgess Hill"
        county = "West Sussex"
        postcode = "RH158BD"
        if address2 == None:
            address1Str = address1 + " " + town
        else:
            address1Str = address1 + " " + address2 + " " + town
        self.address = wx.StaticText(self, -1, address1Str)

        self.county = wx.StaticText(self, -1, county)
        self.post = wx.StaticText(self, -1, postcode)

        sizer.Add(addressLbl, (2, 1))
        sizer.Add(self.address, (2, 2))
        sizer.Add(self.county, (3, 2))
        sizer.Add(self.post, (4, 2))



        phoneLbl = wx.StaticText(self, -1, "Phone:")
        phoneStr = "Home " + "01444-241048" " Work " + "01273-925723"
        mobileStr = "Mobile " + "+4478912786397"

        sizer.Add(phoneLbl, (6, 1))
        self.phone = wx.StaticText(self, -1, phoneStr)
        self.mobile = wx.StaticText(self, -1, mobileStr)
        sizer.Add(self.phone, (6, 2))
        sizer.Add(self.mobile, (7, 2))

        emailLbl = wx.StaticText(self, -1, "Email:")
        emailStr = "i.ferguson@idk.co.uk"
        self.email = wx.StaticText(self, -1, emailStr)
        sizer.Add(emailLbl, (8, 1))
        sizer.Add(self.email, (8, 2))


        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

class TreatmentDetailsCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, row, style=wx.TAB_TRAVERSAL):
        super(TreatmentDetailsCtrl, self).__init__(parent, style=style)
        idx = row[AppointmentPatentTable.IDX_APPOINTMENT_ID]
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Treatment")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)

        nameLbl = wx.StaticText(self, -1, "Treatment:")
        treatmentStr = "PNA"
        self.name = wx.StaticText(self, -1, treatmentStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class PaymentDetailsCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, row, style=wx.TAB_TRAVERSAL):
        super(PaymentDetailsCtrl, self).__init__(parent, style=style)
        idx = row[AppointmentPatentTable.IDX_APPOINTMENT_ID]
        # Layout
        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):
        title_lbl= wx.StaticText(self, label="Payment")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        amountLbl = wx.StaticText(self, -1, "Amount:")
        amount = wx.StaticText(self, -1, "38.50")


        addrSizer.Add(amountLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(amount, 0, wx.EXPAND)

        typeLbl = wx.StaticText(self, -1, "Type:")
        paytype = wx.StaticText(self, -1, "Cash")

        addrSizer.Add(typeLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(paytype, 0, wx.EXPAND)

        payedTodayLbl = wx.StaticText(self, -1, "Payed today:")
        self.payedToday = wx.StaticText(self, -1, "yes");

        addrSizer.Add(payedTodayLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(self.payedToday, 0, wx.EXPAND)

        invoiceRequiredLbl = wx.StaticText(self, -1, "Invoice Required:")
        self.invoiceStr = "yes";
        invoice = wx.StaticText(self, -1, self.invoiceStr);

        addrSizer.Add(invoiceRequiredLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(invoice, 0, wx.EXPAND)

        PaidbyLbl = wx.StaticText(self, -1, "Paid by:")
        Paidby = wx.StaticText(self, -1, "Patent")

        addrSizer.Add(PaidbyLbl, 0,
                    wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(Paidby, 0, wx.EXPAND)


        mainSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

class AppointmentHistoryCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent, row, style=wx.TAB_TRAVERSAL):
        super(AppointmentHistoryCtrl, self).__init__(parent, style=style)
        self.timeNow = datetime.now()
        time = self.timeNow + timedelta(days=1)
        dayIdx = self.timeNow.today().weekday()
        month = self.timeNow.month
        year = self.timeNow.year

        self.historyListCtrl = HistoryListCtrl(self)


        self.__DoLayout()
        self.SetInitialSize()

    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Prevous Patent Appointments")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.historyListCtrl, (1, 1))




        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

class HistoryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(HistoryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(400,150))

        self.InsertColumn(0, "Date/Time")
        self.InsertColumn(1, "Treatment")
        self.InsertColumn(2, "Cost")
        self.InsertColumn(3, "Paid")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()
        for row in data:
            list = row[AppointmentPatentTable.IDX_TIME], row[AppointmentPatentTable.IDX_FIRST_NAME], row[AppointmentPatentTable.IDX_SURNAME], row[AppointmentPatentTable.IDX_HOME_PHONE]
            self.Append(list)


class AppointmentDetailsCtrl(wx.Notebook):
    def __init__(self, parent, row):
        super(AppointmentDetailsCtrl, self).__init__(parent, size=(500,400))
        self.appointmentPatentTable = AppointmentPatentTable()
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)




        self.timeNow = datetime.now()
        time = self.timeNow + timedelta(days=1)
        dayIdx = self.timeNow.today().weekday()
        month = self.timeNow.month
        year = self.timeNow.year

        self.appointmentTimeCtrl = AppointmentTimeCtrl(self,row)
        self.AddPage(self.appointmentTimeCtrl, "Appointment")
        self.patentDetailsCtrl = PatentDetailsCtrl(self, row)
        self.AddPage(self.patentDetailsCtrl, "Patent")
        self.treatmentDetailsCtrl = TreatmentDetailsCtrl(self, row)
        self.AddPage(self.treatmentDetailsCtrl, "Treatment")
        self.paymentDetailsCtrl = PaymentDetailsCtrl(self, row)
        self.AddPage(self.paymentDetailsCtrl, "Payment")
        self.appointmentHistoryCtrl = AppointmentHistoryCtrl(self, row)
        self.AddPage(self.appointmentHistoryCtrl, "History")



    def OnNoteBookPageChanged(self, event):
        pass


