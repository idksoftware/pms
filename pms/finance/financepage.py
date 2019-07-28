'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from datetime import datetime
from datetime import timedelta

#from patenteditdlg import PatentEditDialog

import wx.lib.scrolledpanel as scrolledpanel
#from access.patent import PatentTable

class FinanceCtrl(scrolledpanel.ScrolledPanel):
    pageName = "PaymentsPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(FinanceCtrl, self).__init__(parent, style=style)
        self.financeBookCtrl = FinanceBookCtrl(self)

        #patentTable = PatentTable()
        #self.rows = patentTable.showAll()
        #self.backupsListCtrl.populateList(self.rows)
        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Finance")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)





        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.financeBookCtrl, (1, 1))

        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        ##self.rows[self.selected_row]
        from paymentdlg import PaymentEditDialog
        paymentEditDialog = PaymentEditDialog()
        paymentEditDialog.ShowModal()

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()


class FinanceBookCtrl(wx.Notebook):

    def __init__(self, parent):
        super(FinanceBookCtrl, self).__init__(parent, size=(500,700), style=wx.NB_BOTTOM)

        self.rows = None
        self.financeDetailPageCtrl = FinanceDetailPageCtrl(self)
        self.financeSummaryPageCtrl = FinanceSummaryPageCtrl(self)
        self.AddPage(self.financeDetailPageCtrl, "Details")
        self.AddPage(self.financeSummaryPageCtrl, "Summary")

class FinanceDetailPageCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent):
        super(FinanceDetailPageCtrl, self).__init__(parent, size=(400,300))

        self.rows = [
                ("2013 12 23", "John Steadman", "28.50", "Cash"),
                ("2013 06 02", "Joe Smith", "28.50", "Cash"),
                ("2013 01 22", "Nigel Johnson", "29.50", "Cheque"),
                ("2012 11 10", "Mike Morrison", "38.50", "Cash")
                ]

        self.financeDetailsBookCtrl = FinanceDetailsBookCtrl(self)
        #self.financeDetailListCtrl.populateList(self.rows)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        nameLbl = wx.StaticText(self, -1, "Patent:")

        title = 'Mr'
        first = 'Iain'
        surname = 'Ferguson'

        nameStr = title + " " + first + " " + surname
        self.name = wx.StaticText(self, -1, nameStr)

        appointmentLbl = wx.StaticText(self, -1, "Apointment:")
        appointmentStr = "12 01 23 12:30"
        appointmentVal = wx.StaticText(self, -1, appointmentStr)

        amountLbl = wx.StaticText(self, -1, "Amount:")
        amountStr = "38.50"
        addressVal = wx.StaticText(self, -1, amountStr)

        typeLbl = wx.StaticText(self, -1, "Type:")
        typeStr = "Cash"
        typeVal = wx.StaticText(self, -1, typeStr)

        paidLbl = wx.StaticText(self, -1, "Paid:")
        paidStr = "Yes"
        paidVal = wx.StaticText(self, -1, paidStr)

        paidDateLbl = wx.StaticText(self, -1, "Date:")
        paidDateStr = "12 02 2014"
        paidDateVal = wx.StaticText(self, -1, paidDateStr)

        invoiceLbl = wx.StaticText(self, -1, "Invoice:")
        invoiceStr = "Yes"
        invoiceVal = wx.StaticText(self, -1, invoiceStr)

        invoiceDateLbl = wx.StaticText(self, -1, "Sent:")
        invoiceDateStr = "12 02 2014"
        invoiceDateVal = wx.StaticText(self, -1, invoiceDateStr)

        paidByLbl = wx.StaticText(self, -1, "Paid By:")
        paidByStr = "Patent"
        paidByVal = wx.StaticText(self, -1, paidByStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        sizer.Add(appointmentLbl, (2, 1))
        sizer.Add(appointmentVal, (2, 2))

        sizer.Add(amountLbl, (3, 1))
        sizer.Add(addressVal, (3, 2))

        sizer.Add(typeLbl, (4, 1))
        sizer.Add(typeVal, (4, 2))

        sizer.Add(paidLbl, (5, 1))
        sizer.Add(paidVal, (5, 2))

        sizer.Add(paidDateLbl, (5, 3))
        sizer.Add(paidDateVal, (5, 4))

        sizer.Add(invoiceLbl, (6, 1))
        sizer.Add(invoiceVal, (6, 2))

        sizer.Add(invoiceDateLbl, (6, 3))
        sizer.Add(invoiceDateVal, (6, 4))

        sizer.Add(paidByLbl, (7, 1))
        sizer.Add(paidByVal, (7, 2))


        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.financeDetailsBookCtrl, (1, 1))

        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)




        #self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)

        #self.AddPage(self.financeListCtrl, "A")
class FinanceDetailsBookCtrl(wx.Notebook):

    def __init__(self, parent):
        super(FinanceDetailsBookCtrl, self).__init__(parent, size=(450,300))

        self.rows = [
                ("2013 12 23", "John Steadman", "28.50", "Cash"),
                ("2013 06 02", "Joe Smith", "28.50", "Cash"),
                ("2013 01 22", "Nigel Johnson", "29.50", "Cheque"),
                ("2012 11 10", "Mike Morrison", "38.50", "Cash")
                ]

        self.financeDetailListCtrl = FinanceDetailListCtrl(self)
        self.financeDetailListCtrl.populateList(self.rows)
        #self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)
        self.timeNow = datetime.now()
        time = self.timeNow + timedelta(days=1)
        dayIdx = self.timeNow.today().weekday()
        month = self.timeNow.month
        year = self.timeNow.year


        self.AddPage(self.financeDetailListCtrl, "Today")
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+1))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+2))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+3))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+4))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+5))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+6))
        self.AddPage(self.financeDetailListCtrl, self.dayStr(dayIdx+7))

        self.AddPage(self.financeDetailListCtrl, self.MonthStr(month - 1))
        self.AddPage(self.financeDetailListCtrl, self.MonthStr(month))
        self.AddPage(self.financeDetailListCtrl, self.MonthStr(month + 1))
        self.AddPage(self.financeDetailListCtrl, str(year))
        self.AddPage(self.financeDetailListCtrl, str(year+1))
        self.AddPage(self.financeDetailListCtrl, "Any")



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



class FinanceDetailListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(FinanceDetailListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(400,300))

        self.InsertColumn(0, "Patent")
        self.InsertColumn(1, "Appointment")
        self.InsertColumn(2, "Amount")
        self.InsertColumn(3, "Type")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        #self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()
        for row in data:
            list = row[0], row[1], row[2], row[3]
            self.Append(list)

class FinanceSummaryPageCtrl(scrolledpanel.ScrolledPanel):

    def __init__(self, parent):
        super(FinanceSummaryPageCtrl, self).__init__(parent, size=(500,300))

        self.financeSummaryBookCtrl = FinanceSummaryBookCtrl(self)
        #self.financeDetailListCtrl.populateList(self.rows)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        startdateLbl = wx.StaticText(self, -1, "Start Date:")
        startdateStr = "11 12 2013"
        startdateVal = wx.StaticText(self, -1, startdateStr)

        enddateLbl = wx.StaticText(self, -1, "End Date:")
        enddateStr = "12 01 2013"
        enddateVal = wx.StaticText(self, -1, enddateStr)

        amountLbl = wx.StaticText(self, -1, "Total Amount:")
        amountStr = "6573.92"
        amountVal = wx.StaticText(self, -1, amountStr)

        cashLbl = wx.StaticText(self, -1, "Cash:")
        cashStr = "1289.90"
        cashVal = wx.StaticText(self, -1, cashStr)

        chequesLbl = wx.StaticText(self, -1, "Cheques:")
        chequesStr = "2456.67"
        chequesVal = wx.StaticText(self, -1, chequesStr)

        bankLbl = wx.StaticText(self, -1, "Inter Bank:")
        bankStr = "735.90"
        bankVal = wx.StaticText(self, -1, bankStr)

        unpaidLbl = wx.StaticText(self, -1, "Un-Paid:")
        unpaidStr = "73.90"
        unpaidVal = wx.StaticText(self, -1, unpaidStr)


        sizer.Add(startdateLbl, (1, 1))
        sizer.Add(startdateVal, (1, 2))

        sizer.Add(enddateLbl, (2, 1))
        sizer.Add(enddateVal, (2, 2))

        sizer.Add(amountLbl, (3, 1))
        sizer.Add(amountVal, (3, 2))

        sizer.Add(cashLbl, (4, 1))
        sizer.Add(cashVal, (4, 2))

        sizer.Add(chequesLbl, (5, 1))
        sizer.Add(chequesVal, (5, 2))

        sizer.Add(bankLbl, (6, 1))
        sizer.Add(bankVal, (6, 2))

        #   sizer.Add(bankLbl, (7, 1))
        #   sizer.Add(bankVal, (7, 2))

        sizer.Add(unpaidLbl, (8, 1))
        sizer.Add(unpaidVal, (8, 2))



        listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        listSizer.Add(self.financeSummaryBookCtrl, (1, 1))

        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)


class FinanceSummaryBookCtrl(wx.Notebook):

    def __init__(self, parent):
        super(FinanceSummaryBookCtrl, self).__init__(parent, size=(500,300))

        self.rows = None
        self.financeSummaryListCtrl = FinanceSummaryListCtrl(self)
        self.financeSummaryListCtrl.populateList(self.rows)
        #self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNoteBookPageChanged)

        self.AddPage(self.financeSummaryListCtrl, "Day")


class FinanceSummaryListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        super(FinanceSummaryListCtrl, self).__init__(parent, style=wx.LC_REPORT, size=(450,300))

        self.InsertColumn(0, "Period")
        self.InsertColumn(1, "Type")
        self.InsertColumn(2, "Volume Set Label")
        self.InsertColumn(3, "Location")

        self.SetColumnWidth(0, 120)
        self.SetColumnWidth(1, 50)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def populateList(self, data):
        self.DeleteAllItems()

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        row = self.rows[self.selected_row]
        
        from paymentdlg import PaymentEditDialog
        paymentEditDialog = PaymentEditDialog(row)
        
        print "Opening PaymentEditDialog"
        paymentEditDialog.ShowModal()
        print "Closing PaymentEditDialog"

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

class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.financeCtrl = FinanceCtrl(self)
        self.AddPage(self.financeCtrl, "Finance")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
