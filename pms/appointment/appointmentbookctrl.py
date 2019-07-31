'''
Created on Jan 23, 2014

@author: wzw7yn
'''
import wx
import aputils
from datetime import datetime
from datetime import timedelta
from patent.patenteditdlg import PatentEditDialog
from access.ap_pat_joined import AppointmentPatentTable


class AppointmentBookCtrl(wx.Notebook):
    def __init__(self, parent):
        super(AppointmentBookCtrl, self).__init__(parent, size=(500,300))
        self.appointmentPatentTable = AppointmentPatentTable()
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)


        self.rows = self.appointmentPatentTable.showAll()

        self.appointmentListCtrl = AppointmentListCtrl(self)

        self.appointmentListCtrl.populateList(self.rows)

        self.timeNow = datetime.now()
        time = self.timeNow + timedelta(days=1)
        dayIdx = self.timeNow.today().weekday()
        month = self.timeNow.month
        year = self.timeNow.year

        self.AddPage(self.appointmentListCtrl, "Today")
        tdate = self.timeNow + timedelta(dayIdx)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+1))
        tdate = self.timeNow + timedelta(dayIdx+1)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+2))
        tdate = self.timeNow + timedelta(dayIdx+2)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+3))
        tdate = self.timeNow + timedelta(dayIdx+3)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+4))
        tdate = self.timeNow + timedelta(dayIdx+4)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+5))
        tdate = self.timeNow + timedelta(dayIdx+5)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+6))
        tdate = self.timeNow + timedelta(dayIdx+6)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)
        
        self.AddPage(self.appointmentListCtrl, aputils.dayStr(dayIdx+7))
        tdate = self.timeNow + timedelta(dayIdx+7)
        rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(tdate))
        self.appointmentListCtrl.populateList(rows)

        self.AddPage(self.appointmentListCtrl, aputils.MonthStr(month - 1))
        self.AddPage(self.appointmentListCtrl, aputils.MonthStr(month))
        self.AddPage(self.appointmentListCtrl, aputils.MonthStr(month + 1))
        self.AddPage(self.appointmentListCtrl, str(year))
        self.AddPage(self.appointmentListCtrl, str(year+1))
        self.AddPage(self.appointmentListCtrl, "Any")

    def GetItem(self, itemId, col=0):
        return self.appointmentListCtrl.GetItem(itemId, col)

    def GetRows(self):
        return self.rows

    '''
    def dayStr(self, idx):
        day = "Mon","Tues","Wen","Thur","Fri","Sat","Sun","Mon","Tues","Wen","Thur","Fri","Sat","Sun"
        return day[idx]

    def MonthStr(self, idx):
        idx = idx - 1
        if idx > 12:
            idx = idx % 12
        if idx < 0:
            idx = 12 + idx
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
    '''

    def OnNoteBookPageChanged(self, event):
        pageIdx = self.GetSelection()
        if pageIdx < 8:
            date = self.timeNow + timedelta(days=pageIdx)

            self.rows = self.appointmentPatentTable.selectall(aputils.GetSelectDayStr(date))

        elif pageIdx < 11:
            mth = pageIdx - 8
            self.rows = self.appointmentPatentTable.selectall(aputils.GetSelectMonthStr(self.timeNow, mth))
        elif pageIdx < 13:
            year = pageIdx - 11
            date = self.timeNow + timedelta(days=pageIdx)
            self.rows = self.appointmentPatentTable.selectall(aputils.GetSelectYearStr(self.timeNow, year))
        else:
            date = self.timeNow + timedelta(days=pageIdx)
            self.rows = self.appointmentPatentTable.selectall(aputils.GetSelectAllStr())
        #self.patentListCtrl.ClearAll()

        self.appointmentListCtrl.populateList(self.rows)
        print pageIdx


class AppointmentListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(AppointmentListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(500,300))

        self.InsertColumn(0, "Date Time")
        self.InsertColumn(1, "First Name")
        self.InsertColumn(2, "Surname")
        self.InsertColumn(3, "Phone")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()
        for row in data:
            item = row[AppointmentPatentTable.IDX_TIME], row[AppointmentPatentTable.IDX_FIRST_NAME], row[AppointmentPatentTable.IDX_SURNAME], row[AppointmentPatentTable.IDX_HOME_PHONE]
            self.Append(item)


    
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
     
