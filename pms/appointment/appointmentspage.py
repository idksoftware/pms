'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from datetime import datetime
from datetime import timedelta
from wx.adv import CalendarCtrl

from appointmentdlg import AppointmentDialog

import wx.lib.scrolledpanel as scrolledpanel
from access.ap_pat_joined import AppointmentPatentTable
from appointmentbookctrl import AppointmentBookCtrl

class AppointmentsCtrl(scrolledpanel.ScrolledPanel):
    pageName = "AppointmentsPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(AppointmentsCtrl, self).__init__(parent, style=style)
        self.appointmentBookCtrl = AppointmentBookCtrl(self)


        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Appointments")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)

        appointmentTimeLbl = wx.StaticText(self, -1, "Appointment:")

        self.apTime = '23 01 2014 12.30'

        timeStr = self.apTime
        self.name = wx.StaticText(self, -1, timeStr)

        sizer.Add(appointmentTimeLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        locationLbl = wx.StaticText(self, -1, "Location:")
        locationStr = "Redwood Home"
        self.location = wx.StaticText(self, -1, locationStr)

        sizer.Add(locationLbl, (2, 1))
        sizer.Add(self.location, (2, 2))

        nameLbl = wx.StaticText(self, -1, "Name:")

        title = 'Mr'
        first = 'Iain'
        surname = 'Ferguson'

        nameStr = title + " " + first + " " + surname
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (3, 1))
        sizer.Add(self.name, (3, 2))

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




        btnszr = wx.StdDialogButtonSizer()
        self.editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        
        
        self.editbtn.SetDefault()
        sizer.Add(self.editbtn, (9, 3))
        sizer.Add(openbtn, (9, 4))
       
        btnszr.Realize()

        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.appointmentBookCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_BUTTON, self.OnClicked, self.editbtn)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = self.appointmentBookCtrl.selected_row
        #self.selected_row = event.GetIndex()
        row = self.rows[self.selected_row]
        
        print "Opening AppointmentDialog"
        appointmentDialog = AppointmentDialog(row)
        print "Closing AppointmentDialog"
       
        appointmentDialog.ShowModal()

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
        val = list()
        for column in range(1,3):
            item = self.appointmentBookCtrl.GetItem(self.selected_row, column)
            val.append(item.GetText())
        frame = self.GetTopLevelParent()
        frame.PushStatusText(" ".join(val))
        self.rows = self.appointmentBookCtrl.GetRows()
        row = self.rows[self.selected_row]
        self.AddressUpdate(row)


    def DBStr(self,data):
        if data == None:
            return ""
        return data


    def AddressUpdate(self, row):


        title = self.DBStr(row[AppointmentPatentTable.IDX_TITLE])
        first = self.DBStr(row[AppointmentPatentTable.IDX_FIRST_NAME])
        surname = self.DBStr(row[AppointmentPatentTable.IDX_SURNAME])
        nameStr = ""
        if title == "":
            nameStr = first + " " + surname
        else:
            nameStr = title + " " + first + " " + surname
        self.name.SetLabel(nameStr)

        address = self.DBStr(row[AppointmentPatentTable.IDX_ADDRESS])
        town = self.DBStr(row[AppointmentPatentTable.IDX_TOWN])

        address1Str = address + " " + town
        self.address.SetLabel(address1Str)

        county = "West Sussex"
        postcode = self.DBStr(row[AppointmentPatentTable.IDX_POST_CODE])

        self.county.SetLabel(county)
        self.post.SetLabel(postcode)

        Home = self.DBStr(row[AppointmentPatentTable.IDX_HOME_PHONE])
        Work = self.DBStr(row[AppointmentPatentTable.IDX_WORK_PHONE])
        Mobile = self.DBStr(row[AppointmentPatentTable.IDX_MOBILE])

        phoneStr = "Home " + Home + " Work " + Work

        if Mobile == None:
            mobileStr = "Mobile " + Mobile
        else:
            mobileStr = ""

        self.phone.SetLabel(phoneStr)
        self.mobile.SetLabel(mobileStr)

        email = self.DBStr(row[AppointmentPatentTable.IDX_EMAIL])
        if email != None:
            self.email.SetLabel(email)
        else:
            self.email.SetLabel("")
            
class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.appointmentsCtrl = AppointmentsCtrl(self)
        self.AddPage(self.appointmentsCtrl, "Appointment")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
