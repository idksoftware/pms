'''
Created on Jan 22, 2014

@author: wzw7yn
'''
import wx
import os

from datetime import datetime
from datetime import timedelta
import calendar

from patenteditdlg import PatentEditDialog

import wx.lib.scrolledpanel as scrolledpanel
from access.ap_pat_joined import AppointmentPatentTable

class CurrentPatentCtrl(scrolledpanel.ScrolledPanel):
    pageName = "CurrentPatentPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(CurrentPatentCtrl, self).__init__(parent, style=style)
        self.currentPatentDetailsCtrl = CurrentPatentDetailsCtrl(self)


        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Current Patent")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        
        

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)


        sizer = wx.GridBagSizer(vgap=2, hgap=2)

        appointmentTimeLbl = wx.StaticText(self, -1, "Appointment:")

        self.apTime = '23 01 2014           12.30'

        timeStr = self.apTime
        self.name = wx.StaticText(self, -1, timeStr)

        sizer.Add(appointmentTimeLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        nameLbl = wx.StaticText(self, -1, "Name:")

        title = 'Mr'
        first = 'Iain'
        surname = 'Ferguson'

        nameStr = title + " " + first + " " + surname
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (2, 1))
        sizer.Add(self.name, (2, 2))

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

        sizer.Add(addressLbl, (3, 1))
        sizer.Add(self.address, (3, 2))
        sizer.Add(self.county, (4, 2))
        sizer.Add(self.post, (5, 2))



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




        btnszr = wx.StdDialogButtonSizer()
       
        paymentbtn = wx.Button(self, wx.ID_OK, "Payment", pos=(15, 15))
        changebtn = wx.Button(self, wx.ID_OK, "Change", pos=(15, 15))
        prevbtn = wx.Button(self, wx.ID_OK, "<<", pos=(15, 15))
        nextbtn = wx.Button(self, wx.ID_OK, ">>", pos=(15, 15))
        
        paymentbtn.SetDefault()
        
        sizer.Add(paymentbtn, (10, 5))
        sizer.Add(changebtn, (9, 5))
        sizer.Add(prevbtn, (9, 3))
        sizer.Add(nextbtn, (9, 4))
        
        btnszr.Realize()
        
        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.currentPatentDetailsCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)
       
        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.rows[self.selected_row]
        patentEditDialog = PatentEditDialog()
        
        print "Opening PatentEditDialog"
        patentEditDialog.ShowModal()
        print "Closing PatentEditDialog"
        
    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
        val = list()
        for column in range(1,3):
            item = self.currentPatentDetailsCtrl.GetItem(self.selected_row, column)
            val.append(item.GetText())
        frame = self.GetTopLevelParent()
        frame.PushStatusText(" ".join(val))
        self.rows = self.currentPatentDetailsCtrl.GetRows()
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

class CurrentPatentDetailsCtrl(wx.Notebook):
    def __init__(self, parent):
        super(CurrentPatentDetailsCtrl, self).__init__(parent, size=(1000,300))
    
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)
        self.backupsListCtrl = BackupListCtrl(self)
        self.appointmentPatentTable = AppointmentPatentTable()
        self.rows = self.appointmentPatentTable.showAll()
        self.backupsListCtrl.populateList(self.rows)
        self.timeNow = datetime.now()
        time = self.timeNow + timedelta(days=1)
        dayIdx = self.timeNow.today().weekday()
        month = self.timeNow.month
        year = self.timeNow.year

        self.AddPage(self.backupsListCtrl, "Today")
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+1))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+2))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+3))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+4))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+5))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+6))
        self.AddPage(self.backupsListCtrl, self.dayStr(dayIdx+7))

        self.AddPage(self.backupsListCtrl, self.MonthStr(month - 1))
        self.AddPage(self.backupsListCtrl, self.MonthStr(month))
        self.AddPage(self.backupsListCtrl, self.MonthStr(month + 1))
        self.AddPage(self.backupsListCtrl, str(year))
        self.AddPage(self.backupsListCtrl, str(year+1))
        self.AddPage(self.backupsListCtrl, "Any")

    def GetItem(self, itemId, col=0):
        return self.backupsListCtrl.GetItem(itemId, col)

    def GetRows(self):
        return self.rows

    def dayStr(self, idx):
        day = "Mon","Tues","Wen","Thur","Fri","Sat","Sun","Mon","Tues","Wen","Thur","Fri","Sat","Sun"
        return day[idx]

    def MonthStr(self, idx):
        
        if idx > 12:
            idx = idx % 12
        if idx < 0:
            idx = 12 + idx 
        idx = idx - 1
        month = ( "Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")
        return month[idx]

    def GetSelectDayStr(self, date):
        day = date.day
        month = date.month
        year = date.year
        start = datetime(year, month, day, 01, 01, 00)
        end = datetime(year, month, day, 23, 01, 00)
        startStr = start.strftime("%d-%m-%Y %H:%M")
        endStr = end.strftime("%d-%m-%Y %H:%M")
        return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"

    def lastDayOfMonth(self,dt):
        next_month = (dt.month % 12) + 1
        end_date = datetime(dt.year, next_month, 1)
        end_date = end_date - timedelta(days=1)
        return end_date

    def lastDayOfYear(self,dt):
        next_year = (dt.year + 1)
        end_date = datetime(next_year, 1, 1)
        end_date = end_date - timedelta(days=1)
        return end_date

    def GetSelectMonthStr(self, date, mth):
        
        day = date.day
        if mth < 13:
            month = date.month + mth
            year = date.year
        else:
            month = date.month + mth % 12
            year = date.year + mth / 12
        start = datetime(year, month, 1, 00, 01, 00)
        end = self.lastDayOfMonth(start)
        startStr = start.strftime("%d-%m-%Y %H:%M")
        endStr = end.strftime("%d-%m-%Y %H:%M")
        return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"
        #return "select * from patent where surname like " + whereStr[idx] + " order by time;"

    def GetSelectYearStr(self, date):
     
        year = date.year
        start = datetime(year, 1, 1, 01, 01, 00)
        end = self.lastDayOfYear(start)
        startStr = start.strftime("%d-%m-%Y %H:%M")
        endStr = end.strftime("%d-%m-%Y %H:%M")
        return "select * from appointment, patent where time between \'"+ startStr + "\' and \'" + endStr + "\' and Appointment.patent_id = patent.patent_id;"
        #return "select * from patent where surname like " + whereStr[idx] + " order by time;"

    def GetSelectAllStr(self):

        return "select * from appointment, patent where Appointment.patent_id = patent.patent_id;"


    def OnNoteBookPageChanged(self, event):
        pageIdx = self.GetSelection()
        if pageIdx < 8:
            date = self.timeNow + timedelta(days=pageIdx)
            self.rows = self.appointmentPatentTable.selectall(self.GetSelectDayStr(date))
        elif pageIdx < 11:
            mth = pageIdx - 8
            self.rows = self.appointmentPatentTable.selectall(self.GetSelectMonthStr(self.timeNow, mth))
        elif pageIdx < 13:
            year = pageIdx - 11
            date = self.timeNow + timedelta(days=pageIdx)
            self.rows = self.appointmentPatentTable.selectall(self.GetSelectYearStr(self.timeNow, year))
        else:
            date = self.timeNow + timedelta(days=pageIdx)
            self.rows = self.appointmentPatentTable.selectall(self.GetSelectAllStr())
        #self.patentListCtrl.ClearAll()
        self.backupsListCtrl.populateList(self.rows)
        print pageIdx

class BackupListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(BackupListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(700,300))

        self.InsertColumn(0, "Date Time")
        self.InsertColumn(1, "First Name")
        self.InsertColumn(2, "Surname")
        self.InsertColumn(3, "Phone")

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


    '''
    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        self.rows[self.selected_row]
        patentEditDialog = PatentEditDialog()
        patentEditDialog.ShowModal()

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
        val = list()
        for column in range(1,3):
            item = self.GetItem(self.selected_row, column)
            val.append(item.GetText())
        frame = self.GetTopLevelParent()
        frame.PushStatusText(" ".join(val))
     '''

class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.currentPatentCtrl = CurrentPatentCtrl(self)
        self.AddPage(self.currentPatentCtrl, "Current Patent")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
